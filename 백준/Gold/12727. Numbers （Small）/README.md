# [Gold III] Numbers (Small) - 12727 

[문제 링크](https://www.acmicpc.net/problem/12727) 

### 성능 요약

메모리: 109108 KB, 시간: 92 ms

### 분류

임의 정밀도 / 큰 수 연산, 수학, 런타임 전의 전처리

### 제출 일자

2024년 7월 14일 13:43:11

### 문제 설명

<p>In this problem, you have to find the last three digits before the decimal point for the number (3 + √5)<sup><strong>n</strong></sup>.</p>

<p>For example, when <strong>n</strong> = 5, (3 + √5)<sup>5</sup> = 3935.73982... The answer is 935.</p>

<p>For <strong>n</strong> = 2, (3 + √5)<sup>2</sup> = 27.4164079... The answer is 027.</p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>T</strong>. <strong>T</strong> test cases follow, each on a separate line. Each test case contains one positive integer <strong>n</strong>.</p>

<p>Limits</p>

<ul>
	<li>1 <= <strong>T</strong> <= 100</li>
	<li>2 <= <strong>n</strong> <= 30</li>
</ul>

### 출력 

 <p>For each input case, you should output:</p>

<pre>Case #<strong>X</strong>: <strong>Y</strong></pre>

<p>where <strong>X</strong> is the number of the test case and <strong>Y</strong> is the last three integer digits of the number (3 + √5)<sup><strong>n</strong></sup>. In case that number has fewer than three integer digits, add leading zeros so that your output contains exactly three digits.</p>

