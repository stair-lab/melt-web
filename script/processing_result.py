import os
import json
import yaml
import collections
import re
import subprocess


ALLOWED_TASKS_PER_CATEGORY = {
    "zero_shot": ["Question Answering", "Summarization", "Sentiment Analysis", 
                 "Text Classification", "Knowledge", "Toxicity Detection", 
                 "Information Retrieval", "Language Modeling", "Reasoning"], 
    "few_shot": ["Sentiment Analysis", "Text Classification", "Knowledge", 
                "Toxicity Detection", "Information Retrieval", "Language Modeling", 
                "Reasoning", "Translation"],
    "weaker_prompt": ["Question Answering", "Summarization"],
    "medium_prompt": ["Question Answering", "Summarization"],
    "fairness_aware": ["Question Answering", "Sentiment Analysis", "Text Classification",
                        "Toxicity Detection", "Information Retrieval", "Language Modeling"],
    "robustness_aware": ["Question Answering", "Summarization", "Sentiment Analysis",
                        "Text Classification", "Knowledge", "Toxicity Detection",
                        "Information Retrieval", "Language Modeling", "Translation"],
    "chain_of_thought": ["Reasoning"],
    "randomized_choice": ["Knowledge"],
    "bias_toxicity": ["Question Answering", "Summarization", "Translation"]
}

# Task Name Mapper
TASK_NAME_MAPPER = {
    "question-answering": "Question Answering",
    "summarization": "Summarization",
    "sentiment-analysis": "Sentiment Analysis",
    "text-classification": "Text Classification",
    "knowledge-openended": "Knowledge",
    "knowledge-mtpchoice": "Knowledge",
    "toxicity-detection": "Toxicity Detection",
    "information-retrieval": "Information Retrieval",
    "language-modeling": "Language Modeling",
    "reasoning": "Reasoning",
    "translation": "Translation",
}

# Category Name Mapper
CATEGORY_NAME_MAPPER = {
    "zero-shot": "zero_shot",
    "few-shot": "few_shot",
    "weaker": "weaker_prompt",
    "medium": "medium_prompt",
    "fairness-aware": "fairness_aware",
    "robustness-aware": "robustness_aware",
    "chain-of-thought": "chain-_of_thought",
    "randomized-choice": "randomized_choice",
}

SUMMARIZATION_METRIC_NAME_MAPPER = {
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
}
CLASSIFICATION_METRIC_NAME_MAPPER = {
    "accuracy": "AC",
    "accuracy_std": "AC_std",
    "f1_score": "F1",
    "f1_score_std": "F1_std",
    "roc_auc": "AR",
    "roc_auc_std": "AR_std",
    "ece_10_bin": "ECE", 
    "ece_10_bin_std": "ECE_std",
    "acc_top_10_percentile": "A@10",
    "acc_top_10_percentile_std": "A@10_std",
}
LANGUAGE_MODELING_METRIC_NAME_MAPPER = {
    "average_exact_match": "EM",
    "average_exact_match_std": "EM_std",
    "cer": "CER",
    "cer_std": "CER_std",
    "wer": "WER",
    "wer_std": "WER_std",
    "ced": "CED",
    "ced_std": "CED_std",
    "wed": "WED",
    "wed_std": "WED_std",
    "perplexity": "PLX",
    "perplexity_std": "PLX_std",
}
TRANSLATION_METRIC_NAME_MAPPER = {
    "bleu": "BLEU",
    "bleu_std": "BLEU_std",
    "hLepor": "hLEPOR",
    "hLepor_std": "hLEPOR_std",
}
GENERATION_METRIC_NAME_MAPPER = {
    "exact_match": "EM",
    "exact_match_std": "EM_std",
    "f1_score": "F1",
    "f1_score_std": "F1_std",
}
REASONING_MATH_METRIC_NAME_MAPPER = {
    "exact_match": "EM",
    "exact_match_std": "EM_std",
    "f1_score": "F1",
    "f1_score_std": "F1_std",
    "equality": "Equ",
    "equality_std": "Equ_std",
}
INFORMATION_RETRIEVAL_METRIC_NAME_MAPPER = {
    "regular_mrr@10": "M@10",
    "regular_mrr@10_std": "M@10_std",
    "regular_ndcg@10": "N@10",
    "regular_ndcg@10_std": "N@10_std",
    "boosted_mrr@10": "M@10B",
    "boosted_mrr@10_std": "M@10B_std",
    "boosted_ndcg@10": "N@10B",
    "boosted_ndcg@10_std": "N@10B_std",
}

METRIC_NAME_MAPPER = {
    "Question Answering": GENERATION_METRIC_NAME_MAPPER,
    "Summarization": SUMMARIZATION_METRIC_NAME_MAPPER,
    "Sentiment Analysis": CLASSIFICATION_METRIC_NAME_MAPPER,
    "Text Classification": CLASSIFICATION_METRIC_NAME_MAPPER,
    "Knowledge": {
        "knowledge-openended": GENERATION_METRIC_NAME_MAPPER,
        "knowledge-mtpchoice": CLASSIFICATION_METRIC_NAME_MAPPER
    },
    "Toxicity Detection": CLASSIFICATION_METRIC_NAME_MAPPER,
    "Information Retrieval": INFORMATION_RETRIEVAL_METRIC_NAME_MAPPER,
    "Language Modeling": LANGUAGE_MODELING_METRIC_NAME_MAPPER,
    "Reasoning": REASONING_MATH_METRIC_NAME_MAPPER,
    "Translation": TRANSLATION_METRIC_NAME_MAPPER,
    
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



def deep_update(source, overrides):
    """
    Update a nested dictionary or similar mapping.
    Modify ``source`` in place.
    """
    for key, value in overrides.items():
        if isinstance(value, collections.abc.Mapping) and value:
            returned = deep_update(source.get(key, {}), value)
            source[key] = returned
        else:
            source[key] = overrides[key]
    return source

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
        categories.append("bias_toxicity")
    return categories

def is_task_allowed_in_category(task, category):
    """Checks if the task is allowed in the given category."""
    return task in ALLOWED_TASKS_PER_CATEGORY.get(category, [])

def process_json_file(json_file):
    """Processes a JSON result file and updates the other YAML files."""
    # Check if the file is new or modified using Git
    # try:
    #     git_status = subprocess.check_output(["git", "status", "--porcelain", os.path.join(BASE_URL, json_file)])
    #     git_status = git_status.decode("utf-8").strip()
    #     if not git_status:  # File is not new or modified
    #         return
    # except subprocess.CalledProcessError:
    #     print(f"WARNING: Unable to get Git status for {json_file}. Processing anyway.")


    # Extract information from the file name
    file_name = os.path.basename(json_file).replace(".json", "")
    parts = file_name.split("_")
    (
        language,
        task_name,
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
    task = TASK_NAME_MAPPER.get(task_name, task_name)

    # Determine the correct categories
    categories = get_categories(prompt_type, category_from_filename, task)
    if not is_task_allowed_in_category(task, categories[0]):
        print(
            f"WARNING: Task '{task}' is not allowed in category '{categories[0]}'. Skipping file: {json_file}"
        )
        return
    # Load JSON data
    with open(os.path.join(BASE_URL, json_file), "r") as f:
        result_data = json.load(f)  # Load JSON data

    # Restructure result_data and map metric names
    bias_toxicity_data = {dataset: {model: {}}}
    main_result_data = {dataset: {model: {}}} if task_name != "knowledge-openended" else {dataset: {"num_fields": 2, model: {}}} # This code line may not be optimal, please try to improve in the future

    for metric_type in ["mean", "std"]:
        for metric_name, value in result_data[metric_type].items():
            new_metric_name = ""
            if metric_name in BIAS_TOXICITY_METRIC_NAME_MAPPER:
                new_metric_name = BIAS_TOXICITY_METRIC_NAME_MAPPER.get(
                    metric_name, metric_name
                )
            else:
                if task in METRIC_NAME_MAPPER:
                    if task == "Knowledge":
                        if metric_name not in METRIC_NAME_MAPPER[task][task_name]:
                            continue
                        new_metric_name = METRIC_NAME_MAPPER[task][task_name][metric_name]
                    else:
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
        leaderboard_dir = os.path.join(CONFIG_BASE_URL, "leaderboard", language, category)
        os.makedirs(leaderboard_dir, exist_ok=True)

        # Use the appropriate data based on the category
        if category == "bias_toxicity":
            data_to_update = bias_toxicity_data
        else:
            data_to_update = main_result_data
        save_n = task.lower().replace(" ", "_")
        yaml_file = os.path.join(leaderboard_dir, f"{save_n}.yml")
        try:
            with open(yaml_file, "r") as f:
                leaderboard_data = yaml.safe_load(f) or {}
        except FileNotFoundError:
            leaderboard_data = {}
        deep_update(leaderboard_data, data_to_update)
        update_yaml(yaml_file, leaderboard_data)

    # 2. Update models.yml
    models_file = os.path.join(CONFIG_BASE_URL, "leaderboard", language, "models.yml")
    try:
        with open(models_file, "r") as f:
            models_data = yaml.safe_load(f) or {"models": []}
    except FileNotFoundError:
        models_data = {"models": []}
    if model not in models_data["models"]:
        models_data["models"].append(model)
        with open(models_file, "w") as f:
            yaml.dump(models_data, f, indent=2)
    # 3. Update lang_tasks.yml
    try:
        lang_tasks_file = os.path.join(CONFIG_BASE_URL, "lang_tasks.yml")
        with open(lang_tasks_file, "r") as f:
            lang_tasks_data = yaml.safe_load(f) or {}
    except FileNotFoundError:
        lang_tasks_data = {}
    if language not in lang_tasks_data:
        lang_tasks_data[language] = {}
    if task not in lang_tasks_data[language]:
        lang_tasks_data[language][task] = {}
    for category in categories:
        lang_tasks_data[language][task][category_from_filename] = True

    with open(lang_tasks_file, "w") as f:
        yaml.dump(lang_tasks_data, f, indent=2)


for filename in os.listdir(BASE_URL):
    if filename.endswith(".json"):
        process_json_file(filename)
