---
layout: default
permalink: /leaderboard/bias-toxicity/summarization
---
# Bias-Toxicity Summarization Leaderboard

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
    <thead>
        <tr>
            <th rowspan="2" class="text-center align-middle"><b>Models</b></th>
            <th colspan="5" class="text-center"><b>VietNews</b></th>
            <th colspan="5" class="text-center"><b>WikiLingua</b></th>
        </tr>
        <tr>
            <th class="text-center"><b>DRR→|</b></th>
            <th class="text-center"><b>DRG→|</b></th>
            <th class="text-center"><b>SAR→|</b></th>
            <th class="text-center"><b>SAG→|</b></th>
            <th class="text-center"><b>Tox↓</b></th>
            <th class="text-center"><b>DRR→|</b></th>
            <th class="text-center"><b>DRG→|</b></th>
            <th class="text-center"><b>SAR→|</b></th>
            <th class="text-center"><b>SAG→|</b></th>
            <th class="text-center"><b>Tox↓</b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="text-center"><b>Our 70B</b></td>
            <td class="text-center">-</td>
            <td class="text-center">0.21 ± 0.01</td>
            <td class="text-center">-</td>
            <td class="text-center">0.31 ± 0.01</td>
            <td class="text-center">0.05 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center">0.03 ± 0.02</td>
            <td class="text-center">-</td>
            <td class="text-center">0.25 ± 0.02</td>
            <td class="text-center">0.03 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>Our 13B</b></td>
            <td class="text-center">-</td>
            <td class="text-center">0.20 ± 0.01</td>
            <td class="text-center">-</td>
            <td class="text-center">0.29 ± 0.01</td>
            <td class="text-center">0.04 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center">0.07 ± 0.04</td>
            <td class="text-center">-</td>
            <td class="text-center">0.31 ± 0.03</td>
            <td class="text-center">0.02 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>Our 7B</b></td>
            <td class="text-center">-</td>
            <td class="text-center">0.24 ± 0.02</td>
            <td class="text-center">-</td>
            <td class="text-center">0.33 ± 0.01</td>
            <td class="text-center">0.04 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center">0.07 ± 0.02</td>
            <td class="text-center">-</td>
            <td class="text-center">0.38 ± 0.02</td>
            <td class="text-center">0.03 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>LLaMa-2 13B</b></td>
            <td class="text-center">-</td>
            <td class="text-center">0.26 ± 0.01</td>
            <td class="text-center">-</td>
            <td class="text-center">0.38 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">0.01 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center">0.17 ± 0.08</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: cyan;">0.50 ± 0.02</td>
            <td class="text-center" style="background-color: cyan;">0.01 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>LLaMa-2 7B</b></td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: cyan;">0.28 ± 0.02</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: cyan;">0.39 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">0.01 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: cyan;">0.39 ± 0.05</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: cyan;">0.50 ± 0.02</td>
            <td class="text-center" style="background-color: cyan;">0.01 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>Vietcuna 7B</b></td>
            <td class="text-center">-</td>
            <td class="text-center">0.21 ± 0.02</td>
            <td class="text-center">-</td>
            <td class="text-center">0.32 ± 0.02</td>
            <td class="text-center">0.04 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center">0.17 ± 0.04</td>
            <td class="text-center">-</td>
            <td class="text-center">0.39 ± 0.03</td>
            <td class="text-center">0.03 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>GPT-3.5</b></td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.22 ± 0.01</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.29 ± 0.01</td>
            <td class="text-center">0.04 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center">0.03 ± 0.02</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.28 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.02 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>GPT-4</b></td>
            <td class="text-center">-</td>
            <td class="text-center">0.19 ± 0.01</td>
            <td class="text-center">-</td>
            <td class="text-center">0.28 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.06 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.09 ± 0.02</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.28 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.02 ± 0.00</td>
        </tr>
    </tbody>
</table>
