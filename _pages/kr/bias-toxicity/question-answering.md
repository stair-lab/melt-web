---
layout: default
permalink: /leaderboard/kr/bias-toxicity/question-answering
---
# Bias-Toxicity Question Answering Leaderboard
{% assign lang = 'kr' %}

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
  <thead>
    <tr>
      <th rowspan="2" class="text-center align-middle">
        <b>Models</b>
      </th>
      {% for dataset in site.data.leaderboard[lang].bias_toxicity.question_answering %}
      <th colspan="5" class="text-center">
        <b>{{ dataset[0] }}</b>
      </th>
      {% endfor %}
    </tr>
    <tr>
      {% for dataset in site.data.leaderboard[lang].bias_toxicity.question_answering %}
      <th class="text-center"><b>DRR↓</b></th>
      <th class="text-center"><b>DRG↓</b></th>
      <th class="text-center"><b>SAR↓</b></th>
      <th class="text-center"><b>SAG↓</b></th>
      <th class="text-center"><b>Tox↓</b></th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for model in site.data.leaderboard[lang].models.models %}
    <tr>
      <td class="text-center">
        <b>{{ model }}</b> 
      </td>
      {% for dataset in site.data.leaderboard[lang].bias_toxicity.question_answering %}
        {% assign DRR_min = 1 %} 
        {% assign DRG_min = 1 %}
        {% assign SAR_min = 1 %}
        {% assign SAG_min = 1 %}
        {% assign Tox_min = 1 %} 
        {% for m in site.data.leaderboard[lang].models.models %}
          {% if dataset[1][m].DRR and dataset[1][m].DRR < DRR_min %}
            {% assign DRR_min = dataset[1][m].DRR %}
          {% endif %}
          {% if dataset[1][m].DRG and dataset[1][m].DRG < DRG_min %}
            {% assign DRG_min = dataset[1][m].DRG %}
          {% endif %}
          {% if dataset[1][m].SAR and dataset[1][m].SAR < SAR_min %}
            {% assign SAR_min = dataset[1][m].SAR %}
          {% endif %}
          {% if dataset[1][m].SAG and dataset[1][m].SAG < SAG_min %}
            {% assign SAG_min = dataset[1][m].SAG %}
          {% endif %}
          {% if dataset[1][m].Tox and dataset[1][m].Tox < Tox_min %}
            {% assign Tox_min = dataset[1][m].Tox %}
          {% endif %}
        {% endfor %}
      <td class="text-center" {% if dataset[1][model].DRR == DRR_min %}style="background-color: cyan;"{% endif %}>
        {% if dataset[1][model].DRR %}
        {{ dataset[1][model].DRR | round: 2 }} ± {{ dataset[1][model].DRR_std | round: 2 }}
        {% else %}
        -
        {% endif %}
      </td>
      <td class="text-center" {% if dataset[1][model].DRG == DRG_min %}style="background-color: cyan;"{% endif %}>
        {% if dataset[1][model].DRG %}
        {{ dataset[1][model].DRG | round: 2 }} ± {{ dataset[1][model].DRG_std | round: 2 }}
        {% else %}
        -
        {% endif %}
      </td>
      <td class="text-center" {% if dataset[1][model].SAR == SAR_min %}style="background-color: cyan;"{% endif %}>
        {% if dataset[1][model].SAR %}
        {{ dataset[1][model].SAR | round: 2 }} ± {{ dataset[1][model].SAR_std | round: 2 }}
        {% else %}
        -
        {% endif %}
      </td>
      <td class="text-center" {% if dataset[1][model].SAG == SAG_min %}style="background-color: cyan;"{% endif %}>
        {% if dataset[1][model].SAG %}
        {{ dataset[1][model].SAG | round: 2 }} ± {{ dataset[1][model].SAG_std | round: 2 }}
        {% else %}
        -
        {% endif %}
      </td>
      <td class="text-center" {% if dataset[1][model].Tox == Tox_min %}style="background-color: cyan;"{% endif %}>
        {% if dataset[1][model].Tox %}
        {{ dataset[1][model].Tox | round: 2 }} ± {{ dataset[1][model].Tox_std | round: 2 }}
        {% else %}
        -
        {% endif %}
      </td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>