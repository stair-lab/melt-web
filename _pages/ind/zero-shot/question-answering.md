---
layout: default
permalink: /leaderboard/ind/zero-shot/question-answering
---
# Zero-Shot Question Answering Leaderboard
{% assign lang = 'ind' %}

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
  <thead>
    <tr>
      <th rowspan="2" class="text-center align-middle">
        <b>Models</b>
      </th>
      {% for dataset in site.data.leaderboard[lang].zero_shot.question_answering %}
      <th colspan="2" class="text-center">
        <b>{{ dataset[0] }}</b>
      </th>
      {% endfor %}
    </tr>
    <tr>
      {% for dataset in site.data.leaderboard[lang].zero_shot.question_answering %}
      <th class="text-center"><b>EM↑</b></th>
      <th class="text-center"><b>F1↑</b></th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for model in site.data.leaderboard[lang].models.models %}
    <tr>
      <td class="text-center">
        <b>{{ model }}</b>
      </td>
      {% for dataset in site.data.leaderboard[lang].zero_shot.question_answering %}
        {% assign EM_best = 0 %}
        {% assign F1_best = 0 %}
        {% for m in site.data.leaderboard[lang].models.models %}
          {% if dataset[1][m].EM and dataset[1][m].EM > EM_best %}
            {% assign EM_best = dataset[1][m].EM %}
          {% endif %}
          {% if dataset[1][m].F1 and dataset[1][m].F1 > F1_best %}
            {% assign F1_best = dataset[1][m].F1 %}
          {% endif %}
        {% endfor %}
        <td class="text-center" {% if dataset[1][model].EM == EM_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].EM %}
          {{ dataset[1][model].EM | round: 2 }} ± {{ dataset[1][model].EM_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].F1 == F1_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].F1 %}
          {{ dataset[1][model].F1 | round: 2 }} ± {{ dataset[1][model].F1_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>