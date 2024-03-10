---
layout: default
permalink: /leaderboard/zero-shot/language-modeling
---
# Zero-Shot Language Modeling Leaderboard

<table class="table table-bordered table-sm w-100 dtHorizontalTable" cellspacing="0">
    <thead>
        <tr>
            <th rowspan="2" class="text-center align-middle"><b>Models</b></th>
            <th colspan="6" class="text-center"><b>MLQA-MLM</b></th>
            <th colspan="6" class="text-center"><b>VSEC</b></th>
        </tr>
        <tr>
            <th class="text-center"><b>EM<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>CER<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>WER<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>CED<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>WED<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>PLX<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>EM<span style="vertical-align: super;">↑</span></b></th>
            <th class="text-center"><b>CER<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>WER<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>CED<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>WED<span style="vertical-align: super;">↓</span></b></th>
            <th class="text-center"><b>PLX<span style="vertical-align: super;">↓</span></b></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="text-center"><b>Our 70B</b></td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.50 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">0.64 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">519.09 ± 10.96</td>
            <td class="text-center" style="background-color: cyan;">115.82 ± 2.45</td>
            <td class="text-center" style="background-color: cyan;">1.08 ± 0.01</td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">0.88 ± 0.00</td>
            <td class="text-center">1.01 ± 0.00</td>
            <td class="text-center">113.51 ± 0.57</td>
            <td class="text-center">29.91 ± 0.15</td>
            <td class="text-center" style="background-color: cyan;">1.09 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>Our 13B</b></td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">0.67 ± 0.00</td>
            <td class="text-center">0.78 ± 0.00</td>
            <td class="text-center">697.85 ± 11.62</td>
            <td class="text-center">161.34 ± 2.64</td>
            <td class="text-center">1.16 ± 0.02</td>
            <td class="text-center" style="background-color: cyan;">0.01 ± 0.00</td>
            <td class="text-center" style="background-color: cyan;">0.42 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">0.56 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">54.88 ± 0.77</td>
            <td class="text-center" style="background-color: cyan;">14.50 ± 0.19</td>
            <td class="text-center">1.26 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>Our 7B</b></td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">0.73 ± 0.00</td>
            <td class="text-center">0.88 ± 0.01</td>
            <td class="text-center">684.00 ± 13.18</td>
            <td class="text-center">166.87 ± 3.18</td>
            <td class="text-center">1.25 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">0.01 ± 0.00</td>
            <td class="text-center">3.33 ± 0.04</td>
            <td class="text-center">3.14 ± 0.03</td>
            <td class="text-center">420.34 ± 5.66</td>
            <td class="text-center">85.79 ± 0.96</td>
            <td class="text-center">1.33 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>LLaMa-2 13B</b></td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">0.90 ± 0.00</td>
            <td class="text-center">1.00 ± 0.00</td>
            <td class="text-center">881.97 ± 11.23</td>
            <td class="text-center">208.52 ± 2.52</td>
            <td class="text-center">1.10 ± 0.01</td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">1.32 ± 0.01</td>
            <td class="text-center">1.40 ± 0.01</td>
            <td class="text-center">160.06 ± 1.16</td>
            <td class="text-center">38.12 ± 0.23</td>
            <td class="text-center">1.11 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>LLaMa-2 7B</b></td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">0.95 ± 0.00</td>
            <td class="text-center">1.07 ± 0.01</td>
            <td class="text-center">860.42 ± 13.18</td>
            <td class="text-center">210.21 ± 3.18</td>
            <td class="text-center">1.25 ± 0.01</td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">1.54 ± 0.04</td>
            <td class="text-center">1.55 ± 0.03</td>
            <td class="text-center">171.28 ± 5.66</td>
            <td class="text-center">40.18 ± 0.96</td>
            <td class="text-center">1.14 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>Vietcuna 7B</b></td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center">1.00 ± 0.00</td>
            <td class="text-center">1.00 ± 0.00</td>
            <td class="text-center">951.53 ± 12.37</td>
            <td class="text-center">208.57 ± 2.73</td>
            <td class="text-center">1.48 ± 0.01</td>
            <td class="text-center" style="background-color: cyan;">0.01 ± 0.00</td>
            <td class="text-center">1.11 ± 0.01</td>
            <td class="text-center">1.20 ± 0.01</td>
            <td class="text-center">139.90 ± 1.39</td>
            <td class="text-center">33.94 ± 0.33</td>
            <td class="text-center">1.61 ± 0.00</td>
        </tr>
        <tr>
            <td class="text-center"><b>GPT-3.5</b></td>
            <td class="text-center">0.00 ± 0.00</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.34 ± 0.01</td>
            <td class="text-center">0.50 ± 0.01</td>
            <td class="text-center">422.30 ± 10.79</td>
            <td class="text-center">100.33 ± 2.44</td>
            <td class="text-center">-</td>
            <td class="text-center">0.02 ± 0.00</td>
            <td class="text-center">0.16 ± 0.00</td>
            <td class="text-center">0.30 ± 0.00</td>
            <td class="text-center" style="background-color: #f0f0f0;">12.63 ± 0.34</td>
            <td class="text-center" style="background-color: #f0f0f0;">3.48 ± 0.09</td>
            <td class="text-center">-</td>
        </tr>
        <tr>
            <td class="text-center"><b>GPT-4</b></td>
            <td class="text-center" style="background-color: #f0f0f0;">0.04 ± 0.00</td>
            <td class="text-center">0.40 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.45 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">381.88 ± 10.26</td>
            <td class="text-center" style="background-color: #f0f0f0;">93.34 ± 2.39</td>
            <td class="text-center">-</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.60 ± 0.01</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.14 ± 0.00</td>
            <td class="text-center" style="background-color: #f0f0f0;">0.26 ± 0.00</td>
            <td class="text-center">13.58 ± 0.45</td>
            <td class="text-center">3.67 ± 0.12</td>
            <td class="text-center">-</td>
        </tr>
    </tbody>
</table>
