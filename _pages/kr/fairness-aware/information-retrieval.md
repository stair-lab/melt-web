---
layout: default
permalink: /leaderboard/kr/fairness-aware/information-retrieval
---
# Fairness-Aware Information Retrieval Leaderboard
{% assign lang = 'kr' %}

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
  <thead>
    <tr>
      <th rowspan="2" class="text-center align-middle">
        <b>Models</b>
      </th>
      {% for dataset in site.data.leaderboard[lang].fairness_aware.information_retrieval %}
      <th colspan="4" class="text-center">
        <b>{{ dataset[0] }}</b>
      </th>
      {% endfor %}
    </tr>
    <tr>
      {% for dataset in site.data.leaderboard[lang].fairness_aware.information_retrieval %}
      <th class="text-center"><b>M@10↑</b></th>
      <th class="text-center"><b>M@10B↑</b></th>
      <th class="text-center"><b>N@10↑</b></th>
      <th class="text-center"><b>N@10B↑</b></th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for model in site.data.leaderboard[lang].models.models %}
    <tr>
      <td class="text-center">
        <b>{{ model }}</b> 
      </td>
      {% for dataset in site.data.leaderboard[lang].fairness_aware.information_retrieval %}
        {% assign M10_best = 0 %} 
        {% assign M10B_best = 0 %}
        {% assign N10_best = 0 %} 
        {% assign N10B_best = 0 %}
        {% for m in site.data.leaderboard[lang].models.models %}
          {% if dataset[1][m]["M@10"] and dataset[1][m]["M@10"] > M10_best %}
            {% assign M10_best = dataset[1][m]["M@10"] %}
          {% endif %}
          {% if dataset[1][m]["M@10B"] and dataset[1][m]["M@10B"] > M10B_best %}
            {% assign M10B_best = dataset[1][m]["M@10B"] %}
          {% endif %}
          {% if dataset[1][m]["N@10"] and dataset[1][m]["N@10"] > N10_best %}
            {% assign N10_best = dataset[1][m]["N@10"] %}
          {% endif %}
          {% if dataset[1][m]["N@10B"] and dataset[1][m]["N@10B"] > N10B_best %}
            {% assign N10B_best = dataset[1][m]["N@10B"] %}
          {% endif %}
        {% endfor %}
        <td class="text-center" {% if dataset[1][model]["M@10"] == M10_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["M@10"] %}
          {{ dataset[1][model]["M@10"] | round: 2 }} ± {{ dataset[1][model]["M@10_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model]["M@10B"] == M10B_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["M@10B"] %}
          {{ dataset[1][model]["M@10B"] | round: 2 }} ± {{ dataset[1][model]["M@10B_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model]["N@10"] == N10_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["N@10"] %}
          {{ dataset[1][model]["N@10"] | round: 2 }} ± {{ dataset[1][model]["N@10_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model]["N@10B"] == N10B_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["N@10B"] %}
          {{ dataset[1][model]["N@10B"] | round: 2 }} ± {{ dataset[1][model]["N@10B_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>