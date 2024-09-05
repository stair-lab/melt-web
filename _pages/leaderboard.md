---
layout: default
permalink: /leaderboard/
---

<select class="form-control" name="lang" id="lang">
  <option value="vi" selected>Vietnamese</option>
  <option value="ind">Indonesian</option>
  <option value="kr">Korean</option>
</select>

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
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable1_zeroshot.png" class="img-fluid" alt="Zero-shot">   
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
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable7_fewshot.png" class="img-fluid" alt="Few-shot">   
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
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable9_weakprompt.png" class="img-fluid" alt="Weaker Prompt">   
        </div> 
    </div>
    <div class="tab-pane fade" id="fairness-aware" role="tabpanel" aria-labelledby="fairness-aware-tab">
        <h3>Fairness Aware</h3>
        <p>
            Fairness aware evaluation is a measure of how well a model can deal with fairness issues such as race and gender.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable2_fairness.png" class="img-fluid" alt="Fairness Aware">   
        </div> 
    </div>
    <div class="tab-pane fade" id="robustness-aware" role="tabpanel" aria-labelledby="robustness-aware-tab">
        <h3>Robustness Aware</h3>
        <p>
            Robustness aware evaluation is a measure of how well a model can deal with robustness issues such as adversarial attacks.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable10_typo.png" class="img-fluid" alt="Robustness Aware">   
        </div> 
    </div>
    <div class="tab-pane fade" id="chain-of-thought" role="tabpanel" aria-labelledby="chain-of-thought-tab">
        <h3>Chain-of-Thought</h3>
        <p>
            Chain-of-Thought evaluation is a measure of how well a model can perform on a task that requires a chain-of-thought.
        </p>
        <div class="row w-25">
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable_chainofthought.png" class="img-fluid" alt="Chain-of-Thought">   
        </div> 
    </div>
    <div class="tab-pane fade" id="randomized-choice" role="tabpanel" aria-labelledby="randomized-choice-tab">
        <h3>Randomized Choice</h3>
        <p>
            Randomized Choice evaluation is a measure of how well a model can perform on a multiple choice task with randomized choices.
        </p>
        <div class="row w-25">
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable_randomzedchoice.png" class="img-fluid" alt="Randomized Choice">   
        </div> 
    </div>
    <div class="tab-pane fade" id="bias-toxicity" role="tabpanel" aria-labelledby="bias-toxicity-tab">
        <h3>Bias & Toxicity</h3>
        <p>
            Bias & Toxicity evaluation is a measure of how well a model can deal with bias and toxicity issues.
        </p>
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable3_biastoxic_DRG.png" class="img-fluid" alt="Bias">   
        </div> 
        <div class="row w-100">
            <img src="{{ site.baseurl }}/assets/images/vi/generaltable3_biastoxic_Toxicity.png" class="img-fluid" alt="Toxicity">   
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
      <th><b>Medium Prompt</b></th>
      <th><b>Fairness Aware</b></th>
      <th><b>Robustness Aware</b></th>
      <th><b>Chain-of-Thought</b></th>
      <th><b>Randomized Choice</b></th>
      <th><b>Bias & Toxicity</b></th>
    </tr>
  </thead>
  <tbody>
    {% assign tasks = site.data.lang_tasks.vi %}
    {% for task_name in tasks %}
      <tr class="text-center">
        <td>{{ task_name[0] }}</td> 
        {% for category in site.data.categories %}
          <td>
              <a href="#" 
                 data-baseurl="{{ site.baseurl }}"
                 data-category="{{ category }}"
                 data-task="{{ task_name[0] | slugify }}"
                 class="dynamic-link"
              ></a>
          </td>
        {% endfor %}
      </tr>
    {% endfor %}
  </tbody>
</table>

<script>
    const langSelect = document.getElementById('lang');
    const imageElements = document.querySelectorAll('.tab-content img'); // Select all images within tab content
    const dynamicLinks = document.querySelectorAll('.dynamic-link');
    const allLangTasks = {{ site.data.lang_tasks | jsonify | safe }}
    
    function slugifyTaskNames(langData) {
        for (const taskName in langData) {
            const slugifiedTaskName = taskName.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]+/g, '');
            if (taskName !== slugifiedTaskName) {
                langData[slugifiedTaskName] = langData[taskName];
                delete langData[taskName];
        }
        }
        return langData;
    }
    for (const langCode in allLangTasks) {
        allLangTasks[langCode] = slugifyTaskNames(allLangTasks[langCode]);
    }
    function updateLinks() {
        const selectedLang = langSelect.value;
        const langTasks = allLangTasks[selectedLang];

        imageElements.forEach(img => {
            const currentSrc = img.getAttribute('src');
            const newSrc = currentSrc.replace(/\/assets\/images\/\w+\//, `/assets/images/${selectedLang}/`);
            img.setAttribute('src', newSrc);
        });
        

        // console.log(langTasks)
        dynamicLinks.forEach(link => {
            const baseUrl = link.dataset.baseurl;
            const category = link.dataset.category;
            const task = link.dataset.task;
           
            // Get the tasks data for the selected language
            // Check if the language and task exist in the data
            if (langTasks && langTasks[task] && langTasks[task][category]) { 
                link.href = `${baseUrl}/leaderboard/${selectedLang}/${category}/${task}`;
                link.textContent = 'View';
            } else {
                // Language or task not found, display "-"
                link.href = '#'; 
                link.textContent = '-'; 
                link.classList.add('disabled');
            }
        });
    }

    langSelect.addEventListener('change', updateLinks);
    updateLinks(); 
</script>