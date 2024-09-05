---
layout: default
permalink: /leaderboard/kr/few-shot/language-modeling
---
# Few-Shot Language Modeling Leaderboard
{% assign lang = 'kr' %}

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
  <thead>
    <tr>
      <th rowspan="2" class="text-center align-middle">
        <b>Models</b>
      </th>
      {% for dataset in site.data.leaderboard[lang].few_shot.language_modeling %}
      <th colspan="6" class="text-center">
        <b>{{ dataset[0] }}</b>
      </th>
      {% endfor %}
    </tr>
    <tr>
      {% for dataset in site.data.leaderboard[lang].few_shot.language_modeling %}
      <th class="text-center"><b>EM↑</b></th>
      <th class="text-center"><b>CER↓</b></th>
      <th class="text-center"><b>WER↓</b></th>
      <th class="text-center"><b>CED↓</b></th>
      <th class="text-center"><b>WED↓</b></th>
      <th class="text-center"><b>PLX↓</b></th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for model in site.data.leaderboard[lang].models.models %}
    <tr>
      <td class="text-center">
        <b>{{ model }}</b>
      </td>
      {% for dataset in site.data.leaderboard[lang].few_shot.language_modeling %}
        {% assign EM_best = 0 %}
        {% assign CER_best = 1 %}
        {% assign WER_best = 1 %}
        {% assign CED_best = 10000 %} 
        {% assign WED_best = 10000 %}
        {% assign PLX_best = 10000 %}
        {% for m in site.data.leaderboard[lang].models.models %}
          {% if dataset[1][m].EM and dataset[1][m].EM > EM_best %}
            {% assign EM_best = dataset[1][m].EM %}
          {% endif %}
          {% if dataset[1][m].CER and dataset[1][m].CER < CER_best %}
            {% assign CER_best = dataset[1][m].CER %}
          {% endif %}
          {% if dataset[1][m].WER and dataset[1][m].WER < WER_best %}
            {% assign WER_best = dataset[1][m].WER %}
          {% endif %}
          {% if dataset[1][m].CED and dataset[1][m].CED < CED_best %}
            {% assign CED_best = dataset[1][m].CED %}
          {% endif %}
          {% if dataset[1][m].WED and dataset[1][m].WED < WED_best %}
            {% assign WED_best = dataset[1][m].WED %}
          {% endif %}
          {% if dataset[1][m].PLX and dataset[1][m].PLX < PLX_best %}
            {% assign PLX_best = dataset[1][m].PLX %}
          {% endif %}
        {% endfor %}
        <td class="text-center" {% if dataset[1][model].EM == EM_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].EM %}
          {{ dataset[1][model].EM | round: 2 }} ± {{ dataset[1][model].EM_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].CER == CER_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].CER %}
          {{ dataset[1][model].CER | round: 2 }} ± {{ dataset[1][model].CER_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].WER == WER_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].WER %}
          {{ dataset[1][model].WER | round: 2 }} ± {{ dataset[1][model].WER_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].CED == CED_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].CED %}
          {{ dataset[1][model].CED | round: 2 }} ± {{ dataset[1][model].CED_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].WED == WED_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].WED %}
          {{ dataset[1][model].WED | round: 2 }} ± {{ dataset[1][model].WED_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].PLX == PLX_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].PLX %}
          {{ dataset[1][model].PLX | round: 2 }} ± {{ dataset[1][model].PLX_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>