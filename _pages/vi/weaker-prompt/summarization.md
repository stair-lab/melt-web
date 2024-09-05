---
layout: default
permalink: /leaderboard/vi/weaker-prompt/summarization
---
# Weak-Prompt Summarization Leaderboard
{% assign lang = 'vi' %} 

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
  <thead>
    <tr>
      <th rowspan="2" class="text-center align-middle">
        <b>Models</b>
      </th>
      {% for dataset in site.data.leaderboard[lang].weaker_prompt.summarization %}
      <th colspan="8" class="text-center">
        <b>{{ dataset[0] }}</b>
      </th>
      {% endfor %}
    </tr>
    <tr>
      {% for dataset in site.data.leaderboard[lang].weaker_prompt.summarization %}
      <th class="text-center"><b>R1↑</b></th>
      <th class="text-center"><b>R2↑</b></th>
      <th class="text-center"><b>RL↑</b></th>
      <th class="text-center"><b>SC↑</b></th>
      <th class="text-center"><b>BS↑</b></th>
      <th class="text-center"><b>Cv↑</b></th>
      <th class="text-center"><b>De↑</b></th>
      <th class="text-center"><b>Cp↑</b></th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for model in site.data.leaderboard[lang].models.models %}
    <tr>
      <td class="text-center">
        <b>{{ model }}</b> 
      </td>
      {% for dataset in site.data.leaderboard[lang].weaker_prompt.summarization %}
        {% assign R1_best = 0 %} 
        {% assign R2_best = 0 %}
        {% assign RL_best = 0 %} 
        {% assign SC_best = -1 %}
        {% assign BS_best = 0 %}
        {% assign Cv_best = 0 %}
        {% assign De_best = 0 %}
        {% assign Cp_best = 0 %}
        {% for m in site.data.leaderboard[lang].models.models %}
          {% if dataset[1][m].R1 and dataset[1][m].R1 > R1_best %}
            {% assign R1_best = dataset[1][m].R1 %}
          {% endif %}
          {% if dataset[1][m].R2 and dataset[1][m].R2 > R2_best %}
            {% assign R2_best = dataset[1][m].R2 %}
          {% endif %}
          {% if dataset[1][m].RL and dataset[1][m].RL > RL_best %}
            {% assign RL_best = dataset[1][m].RL %}
          {% endif %}
          {% if dataset[1][m].SC and dataset[1][m].SC > SC_best %}
            {% assign SC_best = dataset[1][m].SC %}
          {% endif %}
          {% if dataset[1][m].BS and dataset[1][m].BS > BS_best %}
            {% assign BS_best = dataset[1][m].BS %}
          {% endif %}
          {% if dataset[1][m].Cv and dataset[1][m].Cv > Cv_best %}
            {% assign Cv_best = dataset[1][m].Cv %}
          {% endif %}
          {% if dataset[1][m].De and dataset[1][m].De > De_best %}
            {% assign De_best = dataset[1][m].De %}
          {% endif %}
          {% if dataset[1][m].Cp and dataset[1][m].Cp > Cp_best %}
            {% assign Cp_best = dataset[1][m].Cp %}
          {% endif %}
        {% endfor %}
        <td class="text-center" {% if dataset[1][model].R1 == R1_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].R1 %}
          {{ dataset[1][model].R1 | round: 2 }} ± {{ dataset[1][model].R1_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].R2 == R2_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].R2 %}
          {{ dataset[1][model].R2 | round: 2 }} ± {{ dataset[1][model].R2_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].RL == RL_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].RL %}
          {{ dataset[1][model].RL | round: 2 }} ± {{ dataset[1][model].RL_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].SC == SC_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].SC %}
          {{ dataset[1][model].SC | round: 2 }} ± {{ dataset[1][model].SC_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].BS == BS_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].BS %}
          {{ dataset[1][model].BS | round: 2 }} ± {{ dataset[1][model].BS_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].Cv == Cv_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].Cv %}
          {{ dataset[1][model].Cv | round: 2 }} ± {{ dataset[1][model].Cv_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].De == De_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].De %}
          {{ dataset[1][model].De | round: 2 }} ± {{ dataset[1][model].De_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
        <td class="text-center" {% if dataset[1][model].Cp == Cp_best %}style="background-color: cyan;"{% endif %}>
          {% if dataset[1][model].Cp %}
          {{ dataset[1][model].Cp | round: 2 }} ± {{ dataset[1][model].Cp_std | round: 2 }}
          {% else %}
          -
          {% endif %}
        </td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
</table>