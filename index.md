---
layout: default
---

<div class="row" >
  <div class="col-md-12 mb-5">
    <h2>What We Do</h2>
    <hr />
    <p>
    <div markdown="1">
The recent emergence of multilingual large language models (LLMs) is revolutionizing natural language processing, bridging communication gaps across diverse cultures and languages. However, to truly harness the potential of these models, it's crucial to understand their strengths and limitations across a wide range of languages and tasks. MELT is designed with this in mind, offering a comprehensive approach to evaluate LLMs in various linguistic contexts. Recognizing that proficiency in one language or task does not guarantee similar performance elsewhere, MELT enables users to pinpoint specific areas for improvement, fostering the development of robust and reliable multilingual language technologies.

MELT includes ten carefully selected evaluation scenarios, each targeting a key aspect of LLM capability:

1. **Summarization:** Evaluates the model's ability to condense large texts while retaining essential information.
2. **Question-Answering:** Assesses comprehension and accurate extraction of answers from provided contexts.
3. **Knowledge:** Tests the model's ability to recall and apply information across different domains.
4. **Sentiment Analysis:** Measures the ability to detect and classify emotional tones in text.
5. **Text Classification:** Evaluates accuracy in categorizing text into predefined labels.
6. **Toxic Detection:** Identifies the model's capacity to flag harmful or biased language.
7. **Language Modeling:** Tests fluency and coherence in generating contextually appropriate text.
8. **Reasoning:** Measures logical deduction and understanding of complex relationships.
9. **Math:** Assesses competency in solving mathematical problems in text form.
10. **Information Retrieval:** Tests effectiveness in searching, retrieving, and synthesizing relevant information.

MELT also includes tools to ensure the ethical deployment of LLMs:

- **Bias Assessment:** Identifies and mitigates potential biases in model outputs.
- **Toxicity Assessment:** Measures and controls the generation of harmful or offensive language.
- **Fairness Evaluation:** Ensures equitable performance across demographic groups and languages.
- **Robustness Analysis:** Examines resilience to noisy inputs and adversarial attacks, ensuring reliable performance in real-world scenarios.

MELT offers a holistic evaluation framework that not only assesses performance but also emphasizes ethical considerations, making it an essential tool for developing multilingual language models that are both effective and responsible. MELT currently supports the following languages and tasks:

</div>  
  </p>

    <!-- Create tables -->
    <div class="row">
      <div class="col-md-3">
        <table class="table table-bordered table-md w-100" cellspacing="0">
          <thead>
            <tr>
              <th class="text-center bg-secondary text-white">Model</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <ul>
                  <li>GPT-4</li>
                  <li>GPT-3.5</li>
                  <li>Gemini</li>
                  <li><a href="https://huggingface.co/meta-llama/Llama-2-70b-chat-hf">LLaMa-70B</a></li>
                  <li><a href="https://huggingface.co/meta-llama/Llama-2-13b-chat-hf">LLaMa-13B</a></li>
                  <li><a href="https://huggingface.co/meta-llama/Llama-2-7b-chat-hf">LLaMa-7B</a></li>
                  <li><a href="https://huggingface.co/ura-hcmut/ura-llama-70b">URA-LLaMa-70B</a></li>
                  <li><a href="https://huggingface.co/ura-hcmut/ura-llama-13b">URA-LLaMa-13B</a></li>
                  <li><a href="https://huggingface.co/ura-hcmut/ura-llama-7b">URA-LLaMa-7B</a></li>
                  <li><a href="https://huggingface.co/ura-hcmut/MixSUra">MixSUra</a></li>
                  <li><a href="https://huggingface.co/ura-hcmut/GemSUra-7B">GemSUra-7B</a></li>
                  <li><a href="https://huggingface.co/ura-hcmut/GemSUra-2B">GemSUra-2B</a></li>
                  <li><a href="https://huggingface.co/vilm/vietcuna-7b-v3">Vietcuna-7B</a></li>
                  <li><a href="https://huggingface.co/Viet-Mistral/Vistral-7B-Chat">Vistral</a></li>
                </ul>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="col-md-9">
        <table class="table table-bordered table-md w-100" cellspacing="0">
          <thead>
            <tr>
              <th class="text-center bg-secondary text-white">Task</th>
              <th class="text-center bg-secondary text-white">Dataset</th>
              <th class="text-center bg-secondary text-white">Metric</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td rowspan="2">Question Answering</td>
              <td><a href="https://huggingface.co/datasets/juletxara/xquad_xtreme">XQuaD</a></td>
              <td rowspan="2">Exact Match, F1 Score</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/mlqa">MLQA</a></td>
            </tr>
            <tr>
              <td rowspan="2">Text Summarization</td>
              <td><a href="https://huggingface.co/datasets/Yuhthe/vietnews">VietNews</a></td>
              <td rowspan="2">ROUGE-1, ROUGE-2, ROUGE-L, <br>SummaC, BERTScore, Coverage, <br>Density, Compression</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/GEM/wiki_lingua">WikiLingua</a></td>
            </tr>
            <tr>
              <td rowspan="2">Sentiment Analysis</td>
              <td><a href="https://vlsp.org.vn/resources-vlsp2016">VLSP 2016</a></td>
              <td rowspan="2">Accuracy, F1 Score, AUC ROC, <br>Expected Calibration Error at top-10, <br>Accuracy at 10% coverage</td>
            </tr>
            <tr>
              <td><a href="https://nlp.uit.edu.vn/datasets">UiT-VSFC</a></td>
            </tr>
            <tr>
              <td rowspan="2">Text Classification</td>
              <td><a href="https://nlp.uit.edu.vn/datasets">UiT-VSMEC</a></td>
              <td rowspan="2">Accuracy, F1 Score, AUC ROC, <br>Expected Calibration Error at top-10, <br>Accuracy at 10% coverage</td>
            </tr>
            <tr>
              <td><a href="https://github.com/VinAIResearch/JointIDSF">PhoATIS</a></td>
            </tr>
            <tr>
              <td rowspan="2">Knowledge</td>
              <td>ZaloE2E</td>
              <td>Exact Match, F1 Score</td>
            </tr>
            <tr>
              <td><a href="https://nlp.uit.edu.vn/datasets">ViMMRC</a></td>
              <td>Accuracy, F1 Score, AUC ROC, <br>Expected Calibration Error at top-10, <br>Accuracy at 10% coverage</td>
            </tr>
            <tr>
              <td rowspan="2">Toxicity Detection</td>
              <td><a href="https://nlp.uit.edu.vn/datasets">UiT-ViCTSD</a></td>
              <td rowspan="2">Accuracy, F1 Score, AUC ROC, <br>Expected Calibration Error at top-10, <br>Accuracy at 10% coverage</td>
            </tr>
            <tr>
              <td><a href="https://nlp.uit.edu.vn/datasets">UiT-ViHSD</a></td>
            </tr>
            <tr>
              <td rowspan="2">Information Retrieval</td>
              <td><a href="https://huggingface.co/datasets/unicamp-dl/mmarco">mMARCO</a></td>
              <td rowspan="2">Mean Reciprocal Rank in top-10, <br>Boosted Mean Reciprocal Rank in top-10, <br>Normalized Discounted Cumulative Gain in top-10, <br>Boosted Normalized Discounted Cumulative Gain in top-10</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/unicamp-dl/mrobust">mRobust04</a></td>
            </tr>
            <tr>
              <td rowspan="2">Language Modeling</td>
              <td>MLQA-MLM</td>
              <td rowspan="2">Exact Match, Character Error Rate, <br>Word Error Rate, Character Edit Distance, <br>Word Edit Distance, Perplexity</td>
            </tr>
            <tr>
              <td><a href="https://github.com/VSEC2021/VSEC">VSEC</a></td>
            </tr>
            <tr>
              <td rowspan="3">Reasoning</td>
              <td><a href="https://huggingface.co/datasets/ura-hcmut/synthetic_reasoning_natural">Synthetic Reasoning - <br>Natural Language</a></td>
              <td rowspan="3">Exact Match, F1 Score, Equivalent</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/ura-hcmut/synthetic_reasoning">Synthetic Reasoning - <br>Abstract Symbol</a></td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/ura-hcmut/MATH_Level_1">MATH</a></td>
            </tr>
            <tr>
              <td rowspan="2">Machine Translation</td>
              <td><a href="https://github.com/VinAIResearch/PhoMT">PhoMT</a></td>
              <td rowspan="2">Bilingual Evaluation Understudy, hLEPOR</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/Helsinki-NLP/opus-100">OPUS100</a></td>
            </tr>
            <tr>
              <td rowspan="6">Bias & Toxicity <br> in generation</td>
              <td><a href="https://huggingface.co/datasets/juletxara/xquad_xtreme">XQuaD</a></td>
              <td rowspan="6">Demographic Representations of Races, <br>Demographic Representations of Genders, <br> Stereotypical Associations of Races, <br>Stereotypical Associations of genders, <br> Toxicity score</td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/mlqa">MLQA</a></td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/Yuhthe/vietnews">VietNews</a></td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/GEM/wiki_lingua">WikiLingua</a></td>
            </tr>
            <tr>
              <td><a href="https://github.com/VinAIResearch/PhoMT">PhoMT</a></td>
            </tr>
            <tr>
              <td><a href="https://huggingface.co/datasets/Helsinki-NLP/opus-100">OPUS100</a></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
      
    <!-- Action button -->
    <div class="row">
      <div class="col-md-12">
        <a class="btn btn-primary btn-lg float-right" href="{{ site.baseurl }}/leaderboard">View LeaderBoard &raquo;</a>
      </div>
    </div>

  </div>
</div>
<!-- /.row -->

<div class="row">
  <div class="col-md-12 mb-2">
    <h2>Who We Are</h2>
    <hr />
  </div>
  <div class="col-md-3 mb-5">
    <div class="card border-0 shadow h-100">
      <img class="card-img-top" src="{{ site.baseurl }}/assets/images/sttruong.png" alt="" />
      <div class="card-body">
        <h4 class="card-title">Sang T. Truong</h4>
        <p class="card-text">
          Stanford University
        </p>
      </div>
      <div class="card-footer">
        <a href="#" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>

  <div class="col-md-3 mb-5">
    <div class="card border-0 shadow h-100">
      <img class="card-img-top" src="{{ site.baseurl }}/assets/images/nqduc.jpg" alt="" />
      <div class="card-body">
        <h4 class="card-title">Duc Q. Nguyen</h4>
        <p class="card-text">
          Ho Chi Minh City University of Technology - VNU-HCM
        </p>
      </div>
      <div class="card-footer">
        <a href="https://martinakaduc.github.io/" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>

  <div class="col-md-3 mb-5">
    <div class="card border-0 shadow h-100">
      <img class="card-img-top" src="{{ site.baseurl }}/assets/images/ndvtoan.jpg" alt="" />
      <div class="card-body">
        <h4 class="card-title">Toan Nguyen</h4>
        <p class="card-text">
          Ho Chi Minh City University of Technology - VNU-HCM
        </p>
      </div>
      <div class="card-footer">
        <a href="#" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>

  <div class="col-md-3 mb-5">
    <div class="card border-0 shadow h-100">
      <img class="card-img-top" src="{{ site.baseurl }}/assets/images/lddong.jpg" alt="" />
      <div class="card-body">
        <h4 class="card-title">Dong D. Le</h4>
        <p class="card-text">
          Ho Chi Minh City University of Technology - VNU-HCM
        </p>
      </div>
      <div class="card-footer">
        <a href="http://ledong0110.github.io" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>

  <div class="col-md-3 mb-5">
    <div class="card border-0 shadow h-100">
      <img class="card-img-top" src="{{ site.baseurl }}/assets/images/nhintruong.png" alt="" />
      <div class="card-body">
        <h4 class="card-title">Nhi N. Truong</h4>
        <p class="card-text">
          Ho Chi Minh City University of Technology - VNU-HCM
        </p>
      </div>
      <div class="card-footer">
        <a href="https://nhintruong.github.io" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>

  <div class="col-md-3 mb-5">
    <div class="card border-0 shadow h-100">
      <img class="card-img-top" src="{{ site.baseurl }}/assets/images/qttho.jpg" alt="" />
      <div class="card-body">
        <h4 class="card-title">Prof. Tho T. Quan</h4>
        <p class="card-text">
          Ho Chi Minh City University of Technology - VNU-HCM
        </p>
      </div>
      <div class="card-footer">
        <a href="http://www.cse.hcmut.edu.vn/qttho/doku.php?id=start" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>

  <div class="col-md-3 mb-5">
    <div class="card border-0 shadow h-100">
      <img class="card-img-top" src="{{ site.baseurl }}/assets/images/skoyejo.jpg" alt="" />
      <div class="card-body">
        <h4 class="card-title">Prof. Sanmi Koyejo</h4>
        <p class="card-text">
          Stanford University
        </p>
      </div>
      <div class="card-footer">
        <a href="https://cs.stanford.edu/~sanmi/" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>
</div>
<!-- /.row -->