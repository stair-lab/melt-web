---
layout: default
permalink: /leaderboard/robustness-aware/knowledge
---
# Robustness-Aware Knowledge Leaderboard

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
    <thead>
        <tr>
            <th rowspan="2" class="text-center align-middle"><b>Models</b></th>
            <th colspan="2" class="text-center"><b>ZaloE2E</b></th>
            <th colspan="5" class="text-center"><b>ViMMRC</b></th>
        </tr>
        <tr>
            <th class="text-center"><b>EM<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>F1<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>AC<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>F1<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>AR<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>ECE<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>A@10<span style="vertical-align: super;">↑</span></b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="text-center"><b>URA-LLaMa 70B</b></td>
            <td class="text-center" style="background-color: cyan;">0.23 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.37 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.65 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.53 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.84 ± 0.00</td>
            <td class="text-center">0.11 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.77 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>URA-LLaMa 13B</b></td>
            <td class="text-center">0.18 ± 0.00</td>
            <td class="text-center">0.30 ± 0.00</td>
            <td class="text-center">0.41 ± 0.00</td>
            <td class="text-center">0.34 ± 0.00</td>
            <td class="text-center">0.61 ± 0.00</td>
            <td class="text-center">0.22 ± 0.00</td>
            <td class="text-center">0.58 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>URA-LLaMa 7B</b></td>
            <td class="text-center">0.10 ± 0.00</td>
            <td class="text-center">0.18 ± 0.00</td>
            <td class="text-center">0.33 ± 0.02</td>
            <td class="text-center">0.28 ± 0.02</td>
            <td class="text-center">0.61 ± 0.01</td>
            <td class="text-center">0.19 ± 0.02</td>
            <td class="text-center">0.33 ± 0.06</td>
        </tr>
        <tr>
            <td class="text-center"><b>LLaMa-2 13B</b></td>
            <td class="text-center">0.13 ± 0.00</td>
            <td class="text-center">0.21 ± 0.00</td>
            <td class="text-center">0.39 ± 0.00</td>
            <td class="text-center">0.31 ± 0.00</td>
            <td class="text-center">0.56 ± 0.00</td>
            <td class="text-center">0.46 ± 0.00</td>
            <td class="text-center">0.33 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>LLaMa-2 7B</b></td>
            <td class="text-center">0.02 ± 0.00</td>
            <td class="text-center">0.05 ± 0.00</td>
            <td class="text-center">0.26 ± 0.01</td>
            <td class="text-center">0.20 ± 0.01</td>
            <td class="text-center">0.51 ± 0.01</td>
            <td class="text-center">0.46 ± 0.01</td>
            <td class="text-center">0.13 ± 0.03</td>
        </tr>
        <tr>
            <td class="text-center"><b>Vietcuna 7B</b></td>
            <td class="text-center">0.05 ± 0.00</td>
            <td class="text-center">0.15 ± 0.00</td>
            <td class="text-center">0.26 ± 0.01</td>
            <td class="text-center">0.14 ± 0.00</td>
            <td class="text-center">0.50 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.01 ± 0.01</td>
            <td class="text-center">0.21 ± 0.07</td>
        </tr>
        <tr>
            <td class="text-center"><b>MixSUra 8x7B</b></td>
            <td class="text-center">0.13 ± -</td>
            <td class="text-center">0.24 ± -</td>
            <td class="text-center">0.57 ± -</td>
            <td class="text-center">0.45 ± -</td>
            <td class="text-center">0.53 ± -</td>
            <td class="text-center">0.35 ± -</td>
            <td class="text-center">0.58 ± -</td>
        </tr>
        <tr>
            <td class="text-center"><b>GPT-3.5</b></td>
            <td class="text-center" style="background-color: #f0f0f0;">0.45 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.61 ± 0.01</td>
            <td class="text-center">0.90 ± 0.01</td>
            <td class="text-center">0.72 ± 0.04</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.65 ± 0.01</td>
            <td class="text-center">0.88 ± 0.07</td>
        </tr>
        <tr>
            <td class="text-center"><b>GPT-4</b></td>
            <td class="text-center">0.44 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.61 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.91 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.73 ± 0.07</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.66 ± 0.07</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.88 ± 0.04</td>
        </tr>
    </tbody>
</table>
