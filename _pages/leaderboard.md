---
layout: default
permalink: /leaderboard/
---

## Overall Rankings
🌟Welcome to our leaderboard!🌟 Below, you will find the current rankings of the models we have evaluated. The leaderboard is based on the overall score of the models. The overall scores for each scenario are calculated as the average of the scores across all datasets in that scenario.

<ul class="nav nav-pills nav-fill nav-tabs" role="tablist">
    <li class="nav-item" role="presentation">
        <a class="nav-link active" id="zeroshot-tab" data-toggle="tab" data-target="#zero-shot" type="button" role="tab" aria-controls="zero-shot" aria-selected="true">
            Zero-shot
        </a>
    </li>
    <li class="nav-item" role="presentation">
        <a class="nav-link" id="fewshot-tab" data-toggle="tab" data-target="#few-shot" type="button" role="tab" aria-selected="false" aria-controls="few-shot">
            Few-shot
        </a>
    </li>
    <li class="nav-item" role="presentation">
        <a class="nav-link" id="weaker-prompt-tab" data-toggle="tab" data-target="#weaker-prompt" role="button" role="tab" aria-selected="false" aria-controls="weaker-prompt">
            Weaker Prompt
        </a>
    </li>
    <li class="nav-item" role="presentation">
        <a class="nav-link"  id="fairness-aware-tab" data-toggle="tab" data-target="#fairness-aware" role="button" role="tab" aria-selected="false" aria-controls="fairness-aware">
            Faireness
        </a>
    </li>
    <li class="nav-item" role="presentation">
        <a class="nav-link" id="robustness-aware-tab" data-toggle="tab" data-target="#robustness-aware" role="button" role="tab" aria-selected="false" aria-controls="robustness-aware">
            Robustness
        </a>
    </li>
    <li class="nav-item" role="presentation">
        <a class="nav-link" id="chain-of-thought-tab" data-toggle="tab" data-target="#chain-of-thought" role="button" role="tab" aria-selected="false" aria-controls="chain-of-thought">
            CoT
        </a>
    </li>
    <li class="nav-item" role="presentation">
        <a class="nav-link" id="randomized-choice-tab" data-toggle="tab" data-target="#randomized-choice" role="button" role="tab" aria-selected="false" aria-controls="randomized-choice">
            Ran. Choices
        </a>
    </li>
    <li class="nav-item" role="presentation">
        <a class="nav-link" id="bias-toxicity-tab" data-toggle="tab" data-target="#bias-toxicity" role="button" role="tab" aria-selected="false" aria-controls="bias-toxicity">
            Bias & Toxicity
        </a>
    </li>
</ul>
<div class="tab-content">
    <div class="tab-pane fade show active" id="zero-shot" role="tabpanel" aria-labelledby="zeroshot-tab">
        <h3>Zero-shot</h3>
        <p>
            Zero-shot evaluation is a measure of how well a model can perform on a task without any training data. 
            The model is given a prompt and asked to generate a response. 
            The model is not given any examples of the task it is being asked to perform.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable1_zeroshot.png" class="img-fluid" alt="Zero-shot">   
        </div> 
    </div>
    <div class="tab-pane fade" id="few-shot" role="tabpanel" aria-labelledby="fewshot-tab">
        <h3>Few-shot</h3>
        <p>
            Few-shot evaluation is a measure of how well a model can perform on a task with very few examples. 
            The model is given a prompt and asked to generate a response. 
            The model is given a few examples of the task it is being asked to perform.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable7_fewshot.png" class="img-fluid" alt="Few-shot">   
        </div> 
    </div>
    <div class="tab-pane fade" id="weaker-prompt" role="tabpanel" aria-labelledby="weaker-prompt-tab">
        <h3>Weaker Prompt</h3>
        <p>
            Weaker prompt evaluation is a measure of how well a model can perform on a task with a weaker prompt. 
            The model is given a prompt and asked to generate a response. 
            The model is given a weaker prompt of the task it is being asked to perform.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable9_weakprompt.png" class="img-fluid" alt="Weaker Prompt">   
        </div> 
    </div>
    <div class="tab-pane fade" id="fairness-aware" role="tabpanel" aria-labelledby="fairness-aware-tab">
        <h3>Fairness Aware</h3>
        <p>
            Fairness aware evaluation is a measure of how well a model can deal with fairness issues such as race and gender.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable2_fairness.png" class="img-fluid" alt="Fairness Aware">   
        </div> 
    </div>
    <div class="tab-pane fade" id="robustness-aware" role="tabpanel" aria-labelledby="robustness-aware-tab">
        <h3>Robustness Aware</h3>
        <p>
            Robustness aware evaluation is a measure of how well a model can deal with robustness issues such as adversarial attacks.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable10_typo.png" class="img-fluid" alt="Robustness Aware">   
        </div> 
    </div>
    <div class="tab-pane fade" id="chain-of-thought" role="tabpanel" aria-labelledby="chain-of-thought-tab">
        <h3>Chain-of-Thought</h3>
        <p>
            Chain-of-Thought evaluation is a measure of how well a model can perform on a task that requires a chain-of-thought.
        </p>
        <div class="row w-25">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable_chainofthought.png" class="img-fluid" alt="Chain-of-Thought">   
        </div> 
    </div>
    <div class="tab-pane fade" id="randomized-choice" role="tabpanel" aria-labelledby="randomized-choice-tab">
        <h3>Randomized Choice</h3>
        <p>
            Randomized Choice evaluation is a measure of how well a model can perform on a multiple choice task with randomized choices.
        </p>
        <div class="row w-25">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable_randomzedchoice.png" class="img-fluid" alt="Randomized Choice">   
        </div> 
    </div>
    <div class="tab-pane fade" id="bias-toxicity" role="tabpanel" aria-labelledby="bias-toxicity-tab">
        <h3>Bias & Toxicity</h3>
        <p>
            Bias & Toxicity evaluation is a measure of how well a model can deal with bias and toxicity issues.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable3_biastoxic_DRG.png" class="img-fluid" alt="Bias">   
        </div> 
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/overall/generaltable3_biastoxic_Toxicity.png" class="img-fluid" alt="Toxicity">   
        </div> 
    </div>
</div>
<br>

## Detailed Evaluation Results
<p>
Below are our detail evaluation results, please choose the task and scenario to view the results.
</p>

<table class="table table-striped table-bordered table-sm w-100" cellspacing="0">
    <thead>
        <tr class="text-center">
            <th class="text-center align-middle"><b>Models</b></th>
            <th><b>Zero-shot</b></th>
            <th><b>Few-shot</b></th>
            <th><b>Weaker Prompt</b></th>
            <th><b>Fairness Aware</b></th>
            <th><b>Robustness Aware</b></th>
            <th><b>Chain-of-Thought</b></th>
            <th><b>Randomized Choice</b></th>
            <th><b>Bias & Toxicity</b></th>
        </tr>
    </thead>
    <tbody>
        <tr class="text-center">
            <td>
                Question-Answering
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/question-answering">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/weaker-prompt/question-answering">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/fairness-aware/question-answering">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/robustness-aware/question-answering">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/bias-toxicity/question-answering">View</a>
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Summarization
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/summarization">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/weaker-prompt/summarization">View</a>
            </td>   
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/robustness-aware/summarization">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/bias-toxicity/summarization">View</a>
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Sentiment Analysis
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/sentiment-analysis">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/few-shot/sentiment-analysis">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/fairness-aware/sentiment-analysis">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/robustness-aware/sentiment-analysis">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Text Classification
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/text-classification">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/few-shot/text-classification">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/fairness-aware/text-classification">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/robustness-aware/text-classification">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Knowledge
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/knowledge">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/few-shot/knowledge">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/robustness-aware/knowledge">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/randomized-choice/knowledge">View</a>
            </td>
            <td>
                -
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Toxicity Detection
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/toxicity-detection">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/few-shot/toxicity-detection">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/fairness-aware/toxicity-detection">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/robustness-aware/toxicity-detection">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Information Retrieval
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/information-retrieval">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/few-shot/information-retrieval">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/fairness-aware/information-retrieval">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/robustness-aware/information-retrieval">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Language Modeling
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/language-modeling">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/few-shot/language-modeling">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/fairness-aware/language-modeling">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Reasoning
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/zero-shot/reasoning">View</a>
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/few-shot/reasoning">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/chain-of-thought/reasoning">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
        </tr>
        <tr class="text-center">
            <td>
                Translation
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/few-shot/translation">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/robustness-aware/translation">View</a>
            </td>
            <td>
                -
            </td>
            <td>
                -
            </td>
            <td>
                <a href="{{ site.baseurl }}/leaderboard/bias-toxicity/translation">View</a>
            </td>
        </tr>
    </tbody>
</table>