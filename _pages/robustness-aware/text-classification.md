---
layout: default
permalink: /leaderboard/robustness-aware/text-classification
---
# Robustness-Aware Text Classification Leaderboard

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
    <thead>
        <tr>
            <th rowspan="2" class="text-center align-middle"><b>Models</b></th>
            <th colspan="5" class="text-center"><b>UiT-VSMEC</b></th>
            <th colspan="5" class="text-center"><b>PhoATIS</b></th>
        </tr>
        <tr>
            <th class="text-center"><b>AC<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>F1<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>AR<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>ECE<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>A@10<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>AC<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>F1<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>AR<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>ECE<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>A@10<span style="vertical-align: super;">↑</span></b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="text-center"><b>Our 70B</b></td>
            <td class="text-center">0.25 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.16 ± 0.00</td>
            <td class="text-center">0.56 ± 0.02</td>
            <td class="text-center">0.20 ± 0.00</td>
            <td class="text-center">0.33 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.16 ± 0.02</td>
            <td class="text-center" style="background-color: cyan;">0.26 ± 0.03</td>
            <td class="text-center" style="background-color: cyan;">0.79 ± 0.00</td>
            <td class="text-center">0.79 ± 0.02</td>
            <td class="text-center" style="background-color: cyan;">0.08 ± 0.06</td>
        </tr>
        <tr>
            <td class="text-center"><b>Our 13B</b></td>
            <td class="text-center" style="background-color: cyan;">0.30 ± 0.00</td>
            <td class="text-center">0.11 ± 0.00</td>
            <td class="text-center">0.51 ± 0.01</td>
            <td class="text-center">0.26 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.44 ± 0.00</td>
            <td class="text-center">0.01 ± 0.01</td>
            <td class="text-center">0.05 ± 0.01</td>
            <td class="text-center">0.47 ± 0.01</td>
            <td class="text-center">0.84 ± 0.01</td>
            <td class="text-center">0.00 ± 0.04</td>
        </tr>
        <tr>
            <td class="text-center"><b>Our 7B</b></td>
            <td class="text-center">0.29 ± 0.00</td>
            <td class="text-center">0.10 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.57 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">0.17 ± 0.00</td>
            <td class="text-center">0.30 ± 0.00</td>
            <td class="text-center">0.02 ± 0.01</td>
            <td class="text-center">0.04 ± 0.00</td>
            <td class="text-center">0.55 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">0.18 ± 0.01</td>
            <td class="text-center">0.01 ± 0.02</td>
        </tr>
        <tr>
            <td class="text-center"><b>LLaMa-2 13B</b></td>
            <td class="text-center">0.19 ± 0.00</td>
            <td class="text-center">0.07 ± 0.00</td>
            <td class="text-center">0.52 ± 0.01</td>
            <td class="text-center">0.47 ± 0.00</td>
            <td class="text-center">0.43 ± 0.00</td>
            <td class="text-center">0.02 ± 0.00</td>
            <td class="text-center">0.06 ± 0.00</td>
            <td class="text-center">0.57 ± 0.01</td>
            <td class="text-center">0.91 ± 0.00</td>
            <td class="text-center">0.01 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>LLaMa-2 7B</b></td>
            <td class="text-center">0.17 ± 0.00</td>
            <td class="text-center">0.10 ± 0.00</td>
            <td class="text-center">0.55 ± 0.00</td>
            <td class="text-center">0.33 ± 0.00</td>
            <td class="text-center">0.29 ± 0.00</td>
            <td class="text-center">0.01 ± 0.01</td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">0.56 ± 0.00</td>
            <td class="text-center">0.69 ± 0.01</td>
            <td class="text-center">0.02 ± 0.02</td>
        </tr>
        <tr>
            <td class="text-center"><b>Vietcuna 7B</b></td>
            <td class="text-center">0.09 ± 0.00</td>
            <td class="text-center">0.09 ± 0.00</td>
            <td class="text-center">0.51 ± 0.01</td>
            <td class="text-center">0.91 ± 0.00</td>
            <td class="text-center">0.09 ± 0.00</td>
            <td class="text-center">0.02 ± 0.01</td>
            <td class="text-center">0.01 ± 0.00</td>
            <td class="text-center">0.55 ± 0.01</td>
            <td class="text-center">0.23 ± 0.01</td>
            <td class="text-center">0.02 ± 0.01</td>
        </tr>
        <tr>
            <td class="text-center"><b>MixSUra 8x7B</b></td>
            <td class="text-center">0.35 ± -</td>
            <td class="text-center">0.27 ± -</td>
            <td class="text-center">0.70 ± -</td>
            <td class="text-center">0.58 ± -</td>
            <td class="text-center">0.70 ± -</td>
            <td class="text-center">0.80 ± -</td>
            <td class="text-center">55 ± -</td>
            <td class="text-center">0.94 ± -</td>
            <td class="text-center">0.15 ± -</td>
            <td class="text-center">0.88 ± -</td>
        </tr>
        <tr>
            <td class="text-center"><b>GPT-3.5</b></td>
            <td class="text-center">0.42 ± 0.00</td>
            <td class="text-center">0.41 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.28 ± 0.00</td>
            <td class="text-center">0.30 ± 0.00</td>
            <td class="text-center">0.68 ± 0.02</td>
            <td class="text-center">0.64 ± 0.03</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.62 ± 0.02</td>
            <td class="text-center">0.70 ± 0.05</td>
        </tr>
        <tr>
            <td class="text-center"><b>GPT-4</b></td>
            <td class="text-center" style="background-color: #f0f0f0;">0.48 ± 0.00</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.45 ± 0.00</td>
            <td class="text-center">-</td>
            <td class="text-center">0.33 ± 0.00</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.40 ± 0.00</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.86 ± 0.01</td>
            <td class="text-center">0.80 ± 0.02</td>
            <td class="text-center">-</td>
            <td class="text-center">0.80 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.91 ± 0.03</td>
        </tr>
    </tbody>
</table>
