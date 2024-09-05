---
layout: default
permalink: /leaderboard/vi/few-shot/translation
---
# Few-Shot Translation Leaderboard
{% assign lang = 'vi' %}

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
  <thead>
    <tr>
      <th rowspan="2" class="text-center align-middle">
        <b>Models</b>
      </th>
      {% for dataset in site.data.leaderboard[lang].few_shot.translation %}
      <th colspan="4" class="text-center">
        <b>{{ dataset[0] }}</b>
      </th>
      {% endfor %}
    </tr>
    <tr>
      {% for dataset in site.data.leaderboard[lang].few_shot.translation %}
      <th class="text-center"><b>BLEU envi↑</b></th>
      <th class="text-center"><b>BLEU vien↑</b></th>
      <th class="text-center"><b>hLEPOR envi↑</b></th>
      <th class="text-center"><b>hLEPOR vien↑</b></th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for model in site.data.leaderboard[lang].models.models %}
    <tr>
      <td class="text-center">
        <b>{{ model }}</b>
      </td>
      {% for dataset in site.data.leaderboard[lang].few_shot.translation %}
        {% assign bleu_envi_best = 0 %}
        {% assign bleu_vien_best = 0 %}
        {% assign hlepor_envi_best = 0 %}
        {% assign hlepor_vien_best = 0 %}
        {% for m in site.data.leaderboard[lang].models.models %}
          {% if dataset[1][m]["BLEU envi"] and dataset[1][m]["BLEU envi"] > bleu_envi_best %}
            {% assign bleu_envi_best = dataset[1][m]["BLEU envi"] %}
          {% endif %}
          {% if dataset[1][m]["BLEU vien"] and dataset[1][m]["BLEU vien"] > bleu_vien_best %}
            {% assign bleu_vien_best = dataset[1][m]["BLEU vien"] %}
          {% endif %}
          {% if dataset[1][m]["hLEPOR envi"] and dataset[1][m]["hLEPOR envi"] > hlepor_envi_best %}
            {% assign hlepor_envi_best = dataset[1][m]["hLEPOR envi"] %}
          {% endif %}
          {% if dataset[1][m]["hLEPOR vien"] and dataset[1][m]["hLEPOR vien"] > hlepor_vien_best %}
            {% assign hlepor_vien_best = dataset[1][m]["hLEPOR vien"] %}
          {% endif %}
        {% endfor %}
        <td class="text-center" {% if dataset[1][model]["BLEU envi"] == bleu_envi_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["BLEU envi"] %}
          {{ dataset[1][model]["BLEU envi"] | round: 2 }} ± {{ dataset[1][model]["BLEU envi_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model]["BLEU vien"] == bleu_vien_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["BLEU vien"] %}
          {{ dataset[1][model]["BLEU vien"] | round: 2 }} ± {{ dataset[1][model]["BLEU vien_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model]["hLEPOR envi"] == hlepor_envi_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["hLEPOR envi"] %}
          {{ dataset[1][model]["hLEPOR envi"] | round: 2 }} ± {{ dataset[1][model]["hLEPOR envi_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model]["hLEPOR vien"] == hlepor_vien_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model]["hLEPOR vien"] %}
          {{ dataset[1][model]["hLEPOR vien"] | round: 2 }} ± {{ dataset[1][model]["hLEPOR vien_std"] | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>