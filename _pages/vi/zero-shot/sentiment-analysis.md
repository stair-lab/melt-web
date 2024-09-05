---
layout: default
permalink: /leaderboard/vi/zero-shot/sentiment-analysis
---
# Zero-Shot Sentiment Analysis Leaderboard
{% assign lang = 'vi' %}

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
  <thead>
    <tr>
      <th rowspan="2" class="text-center align-middle">
        <b>Models</b>
      </th>
      {% for dataset in site.data.leaderboard[lang].zero_shot.sentiment_analysis %}
      <th colspan="5" class="text-center">
        <b>{{ dataset[0] }}</b>
      </th>
      {% endfor %}
    </tr>
    <tr>
      {% for dataset in site.data.leaderboard[lang].zero_shot.sentiment_analysis %}
      <th class="text-center"><b>AC↑</b></th>
      <th class="text-center"><b>F1↑</b></th>
      <th class="text-center"><b>AR↑</b></th>
      <th class="text-center"><b>ECE↓</b></th>
      <th class="text-center"><b>A@10↑</b></th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for model in site.data.leaderboard[lang].models.models %}
    <tr>
      <td class="text-center">
        <b>{{ model }}</b>
      </td>
      {% for dataset in site.data.leaderboard[lang].zero_shot.sentiment_analysis %}
        {% assign AC_best = 0 %}
        {% assign F1_best = 0 %}
        {% assign AR_best = 0 %}
        {% assign ECE_best = 1 %} 
        {% assign A10_best = 0 %}
        {% for m in site.data.leaderboard[lang].models.models %}
          {% if dataset[1][m].AC and dataset[1][m].AC > AC_best %}
            {% assign AC_best = dataset[1][m].AC %}
          {% endif %}
          {% if dataset[1][m].F1 and dataset[1][m].F1 > F1_best %}
            {% assign F1_best = dataset[1][m].F1 %}
          {% endif %}
          {% if dataset[1][m].AR and dataset[1][m].AR > AR_best %}
            {% assign AR_best = dataset[1][m].AR %}
          {% endif %}
          {% if dataset[1][m].ECE and dataset[1][m].ECE < ECE_best %}
            {% assign ECE_best = dataset[1][m].ECE %}
          {% endif %}
          {% if dataset[1][m]["A@10"] and dataset[1][m]["A@10"] > A10_best %}
            {% assign A10_best = dataset[1][m]["A@10"] %}
          {% endif %}
        {% endfor %}
        <td class="text-center" {% if dataset[1][model].AC == AC_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].AC %}
          {{ dataset[1][model].AC | round: 2 }} ± {{ dataset[1][model].AC_std | round: 2 }}
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
        <td class="text-center" {% if dataset[1][model].AR == AR_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].AR %}
          {{ dataset[1][model].AR | round: 2 }} ± {{ dataset[1][model].AR_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].ECE == ECE_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].ECE %}
          {{ dataset[1][model].ECE | round: 2 }} ± {{ dataset[1][model].ECE_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model]["A@10"] == A10_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["A@10"] %}
          {{ dataset[1][model]["A@10"] | round: 2 }} ± {{ dataset[1][model]["A@10_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>