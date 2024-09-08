import os
import json
import yaml
import re

# Task Name Mapper
TASK_NAME_MAPPER = {
    "question_answering": "Question Answering",
    "summarization": "Summarization",
    "sentiment_analysis": "Sentiment Analysis",
    "text_classification": "Text Classification",
    "knowledge": "Knowledge",
    "toxicity_detection": "Toxicity Detection",
    "information_retrieval": "Information Retrieval",
    "language_modeling": "Language Modeling",
    "reasoning": "Reasoning",
    "translation": "Translation",
}

# Category Name Mapper
CATEGORY_NAME_MAPPER = {
    "zero-shot": "zero-shot",
    "few-shot": "few-shot",
    "weaker": "weaker-prompt",
    "medium": "medium-prompt",
    "fairness-aware": "fairness-aware",
    "robustness-aware": "robustness-aware",
    "chain-of-thought": "chain-of-thought",
    "randomized-choice": "randomized-choice",
}

METRIC_NAME_MAPPER = {
    "Summarization": {
        "rouge1": "R1",
        "rouge1_std": "R1_std",
        "rouge2": "R2",
        "rouge2_std": "R2_std",
        "rougeL": "RL",
        "rougeL_std": "RL_std",
        "SummaC": "SC",
        "SummaC_std": "SC_std",
        "BERTScore-F1": "BS",
        "BERTScore-F1_std": "BS_std",
        "coverage": "Cv",
        "coverage_std": "Cv_std",
        "density": "De",
        "density_std": "De_std",
        "compression": "Cp",
        "compression_std": "Cp_std",
    },
    # ... Other tasks mapping
}

BIAS_TOXICITY_METRIC_NAME_MAPPER = {
    "race_profession_demographic": "DRR",
    "race_profession_demographic_std": "DRR_std",
    "gender_profession_demographic": "DRG",
    "gender_profession_demographic_std": "DRG_std",
    "race_profession_stereotypical": "SAR",
    "race_profession_stereotypical_std": "SAR_std",
    "gender_profession_stereotypical": "SAG",
    "gender_profession_stereotypical_std": "SAG_std",
    "toxicity": "Tox",
    "toxicity_std": "Tox_std",
}

# Base URL for result files and configuration files
BASE_URL = "results"
CONFIG_BASE_URL = "_data"


def update_yaml(file_path, new_data):
    """Updates a YAML file with new data."""
    try:
        with open(file_path, "r") as f:
            existing_data = yaml.safe_load(f) or {}
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(new_data)

    with open(file_path, "w") as f:
        yaml.dump(existing_data, f, indent=2)


def get_categories(prompt_type, category_from_filename, task):
    """Determines the correct categories."""
    if prompt_type == "weaker" or prompt_type == "medium":
        category_from_filename = prompt_type
    categories = [
        CATEGORY_NAME_MAPPER.get(category_from_filename, category_from_filename)
    ]
    if (
        prompt_type == "normal"
        and category_from_filename == "zero-shot"
        and task in ["Summarization", "Question Answering", "Translation"]
    ):
        categories.append("bias-toxicity")
    return categories


def process_json_file(json_file):
    """Processes a JSON result file and updates the other YAML files."""

    # Extract information from the file name
    file_name = os.path.basename(json_file).replace(".json", "")
    parts = file_name.split("_")
    (
        language,
        task,
        dataset,
        model,
        prompt_type,
        category_from_filename,
        num_shots,
        pt,
        seed,
    ) = (
        parts[0],
        parts[1],
        parts[2],
        parts[3],
        parts[4],
        parts[5],
        parts[6],
        parts[7],
        parts[8],
    )

    # Map task name to the standard format
    task = TASK_NAME_MAPPER.get(task, task)

    # Determine the correct categories
    categories = get_categories(prompt_type, category_from_filename, task)

    # Load JSON data
    with open(os.path.join(BASE_URL, json_file), "r") as f:
        result_data = json.load(f)  # Load JSON data

    # Restructure result_data and map metric names
    bias_toxicity_data = {dataset: {model: {}}}
    main_result_data = {dataset: {model: {}}}

    for metric_type in ["mean", "std"]:
        for metric_name, value in result_data[metric_type].items():
            new_metric_name = ""
            if metric_name in BIAS_TOXICITY_METRIC_NAME_MAPPER:
                new_metric_name = BIAS_TOXICITY_METRIC_NAME_MAPPER.get(
                    metric_name, metric_name
                )
            else:
                if task in METRIC_NAME_MAPPER:
                    if metric_name not in METRIC_NAME_MAPPER[task]:
                        continue
                    new_metric_name = METRIC_NAME_MAPPER[task][metric_name]
                else:
                    raise ValueError("Not Found")

            # Check if the metric is a bias-toxicity metric
            if new_metric_name in BIAS_TOXICITY_METRIC_NAME_MAPPER.values():
                bias_toxicity_data[dataset][model][new_metric_name] = (
                    value if str(value) != "nan" else None
                )
            else:
                main_result_data[dataset][model][new_metric_name] = (
                    value if str(value) != "nan" else None
                )

    # 1. Update leaderboard YAML file(s)
    for category in categories:
        leaderboard_dir = os.path.join("leaderboard", language, category)
        os.makedirs(leaderboard_dir, exist_ok=True)

        # Use the appropriate data based on the category
        if category == "bias-toxicity":
            data_to_update = bias_toxicity_data
        else:
            data_to_update = main_result_data

        yaml_file = os.path.join(leaderboard_dir, f"{task.lower()}.yml")
        try:
            with open(yaml_file, "r") as f:
                leaderboard_data = yaml.safe_load(f) or {}
        except FileNotFoundError:
            leaderboard_data = {}

        leaderboard_data.update(data_to_update)
        update_yaml(yaml_file, leaderboard_data)

    # 2. Update models.yml
    models_file = os.path.join(CONFIG_BASE_URL, "leaderboard", language, "models.yml")
    with open(models_file, "r") as f:
        models_data = yaml.safe_load(f)
    if model not in models_data["models"]:
        models_data["models"].append(model)
        with open(models_file, "w") as f:
            yaml.dump(models_data, f, indent=2)
    # 3. Update lang_tasks.yml
    lang_tasks_file = os.path.join(CONFIG_BASE_URL, "lang_tasks.yml")
    with open(lang_tasks_file, "r") as f:
        lang_tasks_data = yaml.safe_load(f)

    if language not in lang_tasks_data:
        lang_tasks_data[language] = {}
    if task not in lang_tasks_data[language]:
        lang_tasks_data[language][task] = {}
    for category in categories:
        lang_tasks_data[language][task][category] = True

    with open(lang_tasks_file, "w") as f:
        yaml.dump(lang_tasks_data, f, indent=2)


for filename in os.listdir(BASE_URL):
    if filename.endswith(".json"):
        process_json_file(filename)
