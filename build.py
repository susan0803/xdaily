# -*- coding: utf-8 -*-
"""Assemble index.html for the xDailyBench project page, reusing the
workflow-gym academic template's inline <style> block for visual fidelity."""

STYLE = open('/tmp/style_block.html', encoding='utf-8').read()

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>xDailyBench</title>
  <meta name="description" content="xDailyBench: a rubric-grounded benchmark of 248 expert-curated daily-life tasks for evaluating large language models on complex, open-ended real-user requests.">
  <meta name="keywords" content="LLM evaluation, benchmark, rubric, daily-life tasks, agentic, capability diagnostics">
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

  <link rel="icon" type="image/svg+xml" href="static/images/bytedance-color.svg">
  <link rel="stylesheet" href="static/css/bulma.min.css">
  <link rel="stylesheet" href="static/css/index.css">
  <link rel="stylesheet" href="static/css/fontawesome.all.min.css">
  <link rel="stylesheet" href="static/css/bulma-carousel.min.css">
  <link rel="stylesheet" href="static/css/bulma-slider.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&display=swap" rel="stylesheet">
  <link rel="preload" href="static/fonts/ProductSans-Regular.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="static/fonts/ProductSans-Medium.ttf" as="font" type="font/ttf" crossorigin>
  <link rel="preload" href="static/fonts/ProductSans-Bold.ttf" as="font" type="font/ttf" crossorigin>
  __STYLE__
  <style>
    /* xDailyBench page-specific helpers layered on top of the template */
    .xd-prose p { margin: 10px 0; color: #2b3648; font-size: 1.04rem; line-height: 1.62; }
    .kpi-cards { display:flex; flex-wrap:wrap; gap:16px; justify-content:center; margin:6px 0 22px; }
    .kpi-card { flex:1 1 150px; max-width:210px; background:#FBFDFD; border:1px solid rgba(46,60,80,0.10);
      border-radius:18px; padding:18px 14px; text-align:center;
      box-shadow:0 10px 26px rgba(24,39,75,0.06); }
    .kpi-num { display:block; font-weight:800; font-size:2.0rem; line-height:1.05; color:#1f6e4d; letter-spacing:-0.02em; }
    .kpi-label { display:block; margin-top:6px; font-size:0.92rem; color:#52607a; font-weight:600; }
    .xd-table-wrap { overflow-x:auto; margin:14px 0 4px; }
    table.xd-table { width:100%; border-collapse:collapse; font-size:0.94rem; background:#fff;
      border-radius:14px; overflow:hidden; box-shadow:0 8px 22px rgba(24,39,75,0.06); }
    table.xd-table th, table.xd-table td { padding:9px 12px; text-align:center; border-bottom:1px solid #eef1f5; }
    table.xd-table th { background:#0f1626; color:#fcfdfb; font-weight:700; font-size:0.9rem; white-space:nowrap; }
    table.xd-table td:first-child, table.xd-table th:first-child { text-align:left; }
    table.xd-table tbody tr:hover { background:#f3faf7; }
    table.xd-table td.best { color:#1f6e4d; font-weight:800; }
    .tier-dot { display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:7px; vertical-align:middle; }
    .figure-card { text-align:center; }
    .figure-card img { max-width:100%; height:auto; border-radius:14px; }
    .figure-card figcaption { margin-top:10px; color:#52607a; font-size:0.92rem; font-style:italic; }
    .two-col { display:grid; grid-template-columns:1fr 1fr; gap:26px; align-items:center; }
    @media (max-width: 860px){ .two-col{ grid-template-columns:1fr; } }
    .pill-list { display:flex; flex-wrap:wrap; gap:8px; margin:10px 0 0; }
    .pill-list span { background:rgba(52,178,125,0.12); color:#1f6e4d; border-radius:999px;
      padding:5px 12px; font-size:0.86rem; font-weight:600; }
    .lb-note { margin-top:10px; color:#6a768c; font-size:0.84rem; line-height:1.5; }
    .copy-bibtex-btn { cursor:pointer; border:none; background:#0f1626; color:#fcfdfb; border-radius:10px;
      padding:7px 14px; font-weight:600; font-size:0.9rem; }
    .copy-bibtex-btn:hover { background:#1e2a44; }
    .bibtex-header { display:flex; align-items:center; gap:14px; margin-bottom:10px; }
    pre.bibtex-code { background:#0f1626; color:#e6edf3; border-radius:14px; padding:18px 20px;
      overflow-x:auto; font-size:0.86rem; line-height:1.55; }
    .footer-mini { text-align:center; color:#6a768c; font-size:0.9rem; padding:26px 0 40px; }
  </style>
</head>'''.replace('__STYLE__', STYLE)

NAV = '''
<body>
  <nav class="wfg-nav" aria-label="Page sections">
    <div class="wfg-nav-inner">
      <a class="wfg-nav-brand" href="#top">
        <img class="wfg-nav-logo" src="static/images/bytedance-color.svg" alt="ByteDance"/>
        <span>xDailyBench</span>
      </a>
      <div class="wfg-nav-links">
        <a href="#pipeline">Pipeline</a>
        <a href="#stats">Data Statistics</a>
        <a href="#leaderboard">Leaderboard</a>
        <a href="#capability">Capability</a>
        <a href="#failure">Failure Analysis</a>
        <a href="#bibtex">BibTeX</a>
      </div>
    </div>
  </nav>

  <main id="main-content">'''

HERO = '''
  <section class="wfg-hero" id="top">
    <div class="wfg-hero-shell">
      <div class="wfg-hero-stage">
        <img class="wfg-hero-bg" src="static/images/background.png" alt="xDailyBench hero background" />
        <div class="wfg-hero-scrim" aria-hidden="true"></div>
        <div class="wfg-hero-overlay">
          <h1 class="wfg-hero-title">
            <span class="wfg-brand">xDailyBench</span>: A Rubric-Grounded Benchmark for Evaluating LLMs on Real-World Daily-Life Tasks
          </h1>
          <p class="wfg-hero-aff">
            <span class="wfg-hero-aff-item"><sup>1</sup>ByteDance Seed,</span>
            <span class="wfg-hero-aff-item"><sup>2</sup>Peking University</span>
          </p>
          <ul class="wfg-hero-bullets">
            <li>xDailyBench is a benchmark designed to evaluate whether large language models can handle the complex, open-ended requests that real users encounter in daily life &mdash; rather than standardized exams or narrow domain tasks.</li>
            <li>It comprises <strong>248 expert-curated tasks</strong> across <strong>56 scenario categories</strong> spanning personal life, white-collar work, and learning &amp; research, each paired with a fine-grained scoring rubric (mean 13.3 criteria per task).</li>
            <li>A two-level capability taxonomy (5 L1 &times; 9 L2 dimensions) annotates every criterion, enabling multi-dimensional diagnostic profiling of model strengths and weaknesses without reliance on reference answers.</li>
            <li>Evaluating nine frontier models, the best (GPT-5.5) reaches only a <strong>0.730</strong> criterion-level pass rate and all models fall below 0.50 on the most demanding tier &mdash; losses concentrate in grounding and reasoning, not presentation.</li>
          </ul>
          <div class="wfg-hero-cta">
            <span class="link-block">
              <a href="#" aria-disabled="true" tabindex="-1" class="external-link button is-normal is-rounded is-dark">
                <span class="icon"><img class="wfg-arxiv-logo" src="static/images/arxiv-logo-1.png" alt="arXiv"/></span>
                <span>Paper (Coming Soon)</span>
              </a>
            </span>
            <span class="link-block">
              <a href="#" aria-disabled="true" tabindex="-1" class="external-link button is-normal is-rounded is-dark">
                <span class="icon"><img src="static/images/hf-logo.svg" alt="HuggingFace logo"/></span>
                <span>Dataset (Coming Soon)</span>
              </a>
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>'''

PIPELINE = '''
  <section class="hero teaser" id="pipeline">
    <div class="wfg-card">
      <h2 class="cool-title title is-3 card-title">Construction Pipeline</h2>
      <div class="xd-prose">
        <p>
          The construction of xDailyBench follows a rigorous, multi-stage pipeline that integrates expert knowledge, AI-assisted review, and iterative human quality control. Tasks are contributed by domain experts recruited through a crowdsourcing platform &mdash; researchers, graduate students, and senior practitioners across finance, healthcare, education, legal, and media &mdash; who submit scenarios identical or similar to those they genuinely encounter in their daily lives, professional workflows, or research.
        </p>
        <p>
          Each task passes a four-stage quality-control loop: <strong>(1)</strong> AI pre-screening at submission, <strong>(2)</strong> AI-powered prompt &amp; rubric quality assessment (Gemini-3.1-Pro), <strong>(3)</strong> human expert review with &ge;2 rounds and &ge;2 reviewers, and <strong>(4)</strong> AI consistency verification that flags low human-machine agreement for revision. Only tasks passing all stages enter the final benchmark.
        </p>
      </div>
      <figure class="figure-card" style="margin-top:18px;">
        <img src="static/images/pipeline_wb.png" alt="xDailyBench end-to-end construction pipeline"/>
        <figcaption>The end-to-end construction pipeline of xDailyBench: task sourcing &rarr; multi-layer quality control &rarr; rubric construction &rarr; capability-dimension annotation.</figcaption>
      </figure>
    </div>
  </section>'''

STATS = '''
  <section class="hero teaser" id="stats">
    <div class="wfg-card">
      <h2 class="cool-title title is-3 card-title">Data Statistics</h2>
      <p class="stats-lead">
        xDailyBench covers a total of <strong>248 tasks</strong> across <strong>3 Level-1 domains</strong> (+1 Others) and <strong>56 Level-2 scenario categories</strong>, each paired with a human-written rubric (mean 13.3 criteria per task) and annotated with a two-level capability taxonomy.
      </p>

      <div class="kpi-cards">
        <div class="kpi-card"><span class="kpi-num">248</span><span class="kpi-label">Expert-curated tasks</span></div>
        <div class="kpi-card"><span class="kpi-num">56</span><span class="kpi-label">L2 scenario categories</span></div>
        <div class="kpi-card"><span class="kpi-num">13.3</span><span class="kpi-label">Mean rubric criteria / task</span></div>
        <div class="kpi-card"><span class="kpi-num">5&times;9</span><span class="kpi-label">L1 &times; L2 capability dims</span></div>
        <div class="kpi-card"><span class="kpi-num">9</span><span class="kpi-label">Frontier models evaluated</span></div>
      </div>

      <div class="two-col">
        <figure class="figure-card">
          <img src="static/images/task_composition.png" alt="xDailyBench nested task composition donut"/>
          <figcaption>Nested task composition: distribution of 248 tasks across L1 domains (inner ring) and L2 scenarios (outer ring).</figcaption>
        </figure>
        <div>
          <div class="xd-table-wrap">
            <table class="xd-table">
              <thead><tr><th>L1 Domain</th><th>Tasks</th><th>% of Total</th><th>L2 Cats</th></tr></thead>
              <tbody>
                <tr><td>Personal Life</td><td>104</td><td>41.9%</td><td>26</td></tr>
                <tr><td>White-Collar Work</td><td>92</td><td>33.1%</td><td>13</td></tr>
                <tr><td>Learning &amp; Research</td><td>48</td><td>19.4%</td><td>14</td></tr>
                <tr><td>Others</td><td>14</td><td>5.6%</td><td>3</td></tr>
                <tr><td><strong>Total</strong></td><td><strong>248</strong></td><td><strong>100%</strong></td><td><strong>56</strong></td></tr>
              </tbody>
            </table>
          </div>
          <p style="margin-top:14px; color:#52607a; font-size:0.92rem;">Representative L2 categories:</p>
          <div class="pill-list">
            <span>Legal consultation (16)</span><span>Shopping decisions (15)</span>
            <span>Project management (14)</span><span>Content creation (12)</span>
            <span>Creative planning (11)</span><span>Data analysis (9)</span>
            <span>Info retrieval (9)</span><span>Document formatting (9)</span>
            <span>Academic writing (9)</span><span>Financial planning (9)</span>
          </div>
        </div>
      </div>
    </div>
  </section>'''

LEADERBOARD = '''
  <section class="hero teaser" id="leaderboard">
    <div class="wfg-card">
      <h2 class="cool-title title is-3 card-title">Leaderboard</h2>
      <p class="stats-lead">
        Nine frontier worker models are evaluated on the agentic harness and scored by a single fixed LLM judge (Claude Opus 4.7), with bootstrap 95% confidence intervals. Models split into three tiers: a top cluster, a mid-band, and a collapsed long tail.
      </p>

      <div class="leaderboard-tabs" id="lbTabs">
        <button class="is-active" data-tab="overall">Overall Pass Rate</button>
        <button data-tab="difficulty">Difficulty-Stratified</button>
        <button data-tab="importance">Importance-Stratified</button>
      </div>

      <div class="lb-panels-wrap">
        <div class="lb-panel is-active" data-panel="chart">
          <svg id="lbChart" class="lb-chart" viewBox="0 0 1000 560" preserveAspectRatio="xMidYMid meet" role="img" aria-label="xDailyBench leaderboard"></svg>
        </div>
      </div>

      <div class="xd-table-wrap" style="margin-top:18px;">
        <table class="xd-table">
          <thead><tr><th>Rank</th><th>Model</th><th>Pass rate</th><th>95% CI</th><th>Routine</th><th>Interm.</th><th>Demanding</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><span class="tier-dot" style="background:#4a85c4"></span>GPT-5.5</td><td class="best">0.730</td><td>[0.695, 0.764]</td><td>0.939</td><td>0.781</td><td>0.468</td></tr>
            <tr><td>2</td><td><span class="tier-dot" style="background:#4a85c4"></span>Claude Opus 4.7</td><td>0.692</td><td>[0.655, 0.728]</td><td>0.936</td><td>0.680</td><td>0.460</td></tr>
            <tr><td>3</td><td><span class="tier-dot" style="background:#4a85c4"></span>Qwen3.7-Max</td><td>0.664</td><td>[0.628, 0.701]</td><td>0.886</td><td>0.716</td><td>0.387</td></tr>
            <tr><td>4</td><td><span class="tier-dot" style="background:#4a85c4"></span>DeepSeek-V4-Pro</td><td>0.660</td><td>[0.624, 0.697]</td><td>0.873</td><td>0.674</td><td>0.433</td></tr>
            <tr><td>5</td><td><span class="tier-dot" style="background:#2f8a57"></span>Qwen3.6-Max-Preview</td><td>0.614</td><td>[0.575, 0.653]</td><td>0.874</td><td>0.592</td><td>0.373</td></tr>
            <tr><td>6</td><td><span class="tier-dot" style="background:#2f8a57"></span>GLM-5.1</td><td>0.589</td><td>[0.544, 0.634]</td><td>0.869</td><td>0.582</td><td>0.312</td></tr>
            <tr><td>7</td><td><span class="tier-dot" style="background:#2f8a57"></span>Doubao Seed 2.0 Pro</td><td>0.549</td><td>[0.513, 0.587]</td><td>0.782</td><td>0.553</td><td>0.309</td></tr>
            <tr><td>8</td><td><span class="tier-dot" style="background:#cf8642"></span>Gemini-3.1-Pro</td><td>0.352</td><td>[0.310, 0.396]</td><td>0.575</td><td>0.324</td><td>0.154</td></tr>
            <tr><td>9</td><td><span class="tier-dot" style="background:#cf8642"></span>Kimi-K2.6</td><td>0.218</td><td>[0.179, 0.261]</td><td>0.360</td><td>0.195</td><td>0.097</td></tr>
          </tbody>
        </table>
      </div>
      <p class="lb-note">
        Switching task-level aggregation from uniform to importance-weighted yields Spearman &rho; = 1.000 (zero rank flips). Across a 4&times; sweep of step budget (60&ndash;240) and context window (64k&ndash;256k), scores with clean ablation runs stay on a plateau (range &le; 0.07, non-monotonic) &mdash; the bottleneck is model capability, not interaction budget.
      </p>
    </div>
  </section>'''

CAPABILITY = '''
  <section class="hero teaser" id="capability">
    <div class="wfg-card">
      <h2 class="cool-title title is-3 card-title">Capability Profiling</h2>
      <p class="stats-lead">
        Every rubric criterion is tagged with a capability dimension (5 L1 &times; 9 L2). Aggregating per dimension turns a flat score into a structured capability profile. <strong>Presentation is uniformly high and no longer separates models, whereas Correctness opens the widest gap</strong> between the top tier and the long tail.
      </p>
      <div class="two-col">
        <figure class="figure-card">
          <img src="static/images/l1_radar.jpg" alt="L1 capability radar for four annotated models"/>
          <figcaption>L1 capability profile (criterion-level pass rate) for the four annotated workers.</figcaption>
        </figure>
        <div>
          <div class="xd-table-wrap">
            <table class="xd-table">
              <thead><tr><th>L1 Dimension</th><th>Opus-4.7</th><th>DeepSeek-V4</th><th>Doubao-2.0Pro</th><th>Kimi-K2.6</th></tr></thead>
              <tbody>
                <tr><td>Correctness</td><td>0.527</td><td class="best">0.535</td><td>0.291</td><td>0.362</td></tr>
                <tr><td>Compliance</td><td class="best">0.564</td><td>0.543</td><td>0.382</td><td>0.400</td></tr>
                <tr><td>Sufficiency</td><td class="best">0.647</td><td>0.593</td><td>0.485</td><td>0.415</td></tr>
                <tr><td>Harmlessness</td><td class="best">0.652</td><td>0.554</td><td>0.378</td><td>0.482</td></tr>
                <tr><td>Presentation</td><td>0.641</td><td class="best">0.694</td><td>0.617</td><td>0.413</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <h3 class="title is-5" style="margin-top:26px;">L2 Weakness Localization</h3>
      <div class="xd-prose"><p>
        Grounding is uniformly low (0.23&ndash;0.44): models assert conclusions without sufficiently citing concrete source evidence. Reasoning is likewise weak, especially in the second tier. In contrast, execution is a clear strength of the strong models (Opus 0.706, DeepSeek 0.649). The bulk of zero-scored criteria fall into <strong>grounding, reasoning, and accuracy</strong> rather than presentation &mdash; setting the improvement priority on sourcing and cross-source reasoning.
      </p></div>
      <div class="xd-table-wrap">
        <table class="xd-table">
          <thead><tr><th>L2 Dimension</th><th>Opus-4.7</th><th>DeepSeek-V4</th><th>Doubao-2.0Pro</th><th>Kimi-K2.6</th></tr></thead>
          <tbody>
            <tr><td>Accuracy (computation/fact)</td><td>0.544</td><td class="best">0.548</td><td>0.295</td><td>0.413</td></tr>
            <tr><td>Reasoning (judgment)</td><td>0.490</td><td class="best">0.505</td><td>0.282</td><td>0.253</td></tr>
            <tr><td>Compliance (instruction following)</td><td class="best">0.551</td><td>0.534</td><td>0.368</td><td>0.404</td></tr>
            <tr><td>Execution (parsing/tool use)</td><td class="best">0.706</td><td>0.649</td><td>0.533</td><td>0.357</td></tr>
            <tr><td>Completeness</td><td class="best">0.676</td><td>0.627</td><td>0.520</td><td>0.430</td></tr>
            <tr><td>Grounding (sourcing)</td><td class="best">0.436</td><td>0.370</td><td>0.231</td><td>0.321</td></tr>
            <tr><td>Boundary (caution)</td><td class="best">0.652</td><td>0.554</td><td>0.378</td><td>0.482</td></tr>
            <tr><td>Presentation (formatting)</td><td>0.641</td><td class="best">0.694</td><td>0.617</td><td>0.413</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>'''

FAILURE = '''
  <section class="hero teaser" id="failure">
    <div class="wfg-card">
      <h2 class="cool-title title is-3 card-title">Failure Analysis</h2>
      <p class="stats-lead">
        The two long-tail models fail in nearly opposite ways: <strong>Gemini-3.1-Pro fails by doing too much and never converging</strong>, whereas <strong>Kimi-K2.6 fails by doing too little and stopping too early</strong>. Yet both share one upstream mistake &mdash; redirecting tasks solvable from the supplied attachments toward the web or parametric knowledge.
      </p>
      <div class="xd-table-wrap">
        <table class="xd-table">
          <thead><tr><th>Failure mode</th><th>Trigger</th><th>Trace signature</th></tr></thead>
          <tbody>
            <tr><td>Retrieval over-reliance</td><td>Task solvable from supplied attachments is redirected to web search or parametric knowledge</td><td>High share of search/fetch calls; attachments read late or never</td></tr>
            <tr><td>Non-recovery from tool failure</td><td>A tool errors out and the model neither rewrites the query, switches tools, nor falls back to local computation</td><td>Repeated near-identical calls after an error; no strategy change</td></tr>
            <tr><td>Repetitive action looping</td><td>The model re-issues an action that did not advance the task</td><td>Long runs of consecutive identical calls; budget consumed without output</td></tr>
            <tr><td>Premature termination</td><td>The model abandons the task after a brief look instead of entering the read&ndash;plan&ndash;act&ndash;deliver loop</td><td>Very few tool calls; no deliverable file written; short chat-only reply</td></tr>
          </tbody>
        </table>
      </div>
      <div class="two-col" style="margin-top:22px; align-items:start;">
        <div>
          <h3 class="title is-6" style="margin-bottom:8px;">Gemini-3.1-Pro &mdash; failure by over-action</h3>
          <div class="xd-prose"><p style="font-size:0.98rem;">
            Web search becomes its default action: 40% of all tool calls in the low-score group are web searches (vs. 11% when it succeeds). When search times out it re-issues an even longer query &mdash; a &ldquo;timeout, worse retry, timeout&rdquo; loop forms and the run hits the step-budget ceiling, ending with an empty or partial reply. The most predictive sign of a failed Gemini task is that it touches the budget cap.
          </p></div>
        </div>
        <div>
          <h3 class="title is-6" style="margin-bottom:8px;">Kimi-K2.6 &mdash; failure by under-action</h3>
          <div class="xd-prose"><p style="font-size:0.98rem;">
            The mirror image: ~10 tool calls on average, roughly a third of failed tasks finish with three or fewer calls. Only about a quarter ever write a file, so &gt;70% produce no target artifact and answer purely in chat. Many rubric criteria check concrete artifacts, so absent files score zero by default &mdash; directly explaining Kimi&rsquo;s collapse on the necessary tier.
          </p></div>
        </div>
      </div>
    </div>
  </section>'''

BIBTEX = '''
  <section class="hero teaser" id="bibtex">
    <div class="wfg-card">
      <div class="bibtex-header">
        <h2 class="cool-title title is-3 card-title" style="margin:0!important;border:none!important;">BibTeX</h2>
        <button class="copy-bibtex-btn" onclick="copyBibTeX()"><i class="fas fa-copy"></i> Copy</button>
      </div>
      <pre class="bibtex-code" id="bibtex-code"><code>@misc{xdailybench2026,
  title  = {xDailyBench: A Rubric-Grounded Benchmark for Evaluating LLMs on Real-World Daily-Life Tasks},
  author = {ByteDance Seed and Peking University},
  year   = {2026},
  note   = {Project page},
}</code></pre>
    </div>
  </section>
  </main>

  <footer class="footer-mini">
    <p>xDailyBench &middot; ByteDance Seed &amp; Peking University &middot; Page styled with the academic project template.</p>
  </footer>'''

SCRIPTS = '''
  <script defer src="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css"></script>
  <script>
  // ---- Interactive leaderboard chart (data-driven SVG) ----
  (function(){
    var SVGNS = "http://www.w3.org/2000/svg";
    var models = [
      {name:"GPT-5.5",             tier:"#4a85c4", overall:0.730, ciLo:0.695, ciHi:0.764, diff:[0.939,0.781,0.468], imp:[0.733,0.753,0.607]},
      {name:"Claude Opus 4.7",     tier:"#4a85c4", overall:0.692, ciLo:0.655, ciHi:0.728, diff:[0.936,0.680,0.460], imp:[0.692,0.747,0.618]},
      {name:"Qwen3.7-Max",         tier:"#4a85c4", overall:0.664, ciLo:0.628, ciHi:0.701, diff:[0.886,0.716,0.387], imp:[0.670,0.682,0.483]},
      {name:"DeepSeek-V4-Pro",     tier:"#4a85c4", overall:0.660, ciLo:0.624, ciHi:0.697, diff:[0.873,0.674,0.433], imp:[0.675,0.678,0.494]},
      {name:"Qwen3.6-Max-Preview", tier:"#2f8a57", overall:0.614, ciLo:0.575, ciHi:0.653, diff:[0.874,0.592,0.373], imp:[0.637,0.655,0.551]},
      {name:"GLM-5.1",             tier:"#2f8a57", overall:0.589, ciLo:0.544, ciHi:0.634, diff:[0.869,0.582,0.312], imp:[0.631,0.656,0.455]},
      {name:"Doubao Seed 2.0 Pro", tier:"#2f8a57", overall:0.549, ciLo:0.513, ciHi:0.587, diff:[0.782,0.553,0.309], imp:[0.557,0.546,0.438]},
      {name:"Gemini-3.1-Pro",      tier:"#cf8642", overall:0.352, ciLo:0.310, ciHi:0.396, diff:[0.575,0.324,0.154], imp:[0.395,0.392,0.264]},
      {name:"Kimi-K2.6",           tier:"#cf8642", overall:0.218, ciLo:0.179, ciHi:0.261, diff:[0.360,0.195,0.097], imp:[0.288,0.351,0.253]}
    ];
    var GROUPS = {
      difficulty: [{label:"Routine",color:"#4a85c4"},{label:"Intermediate",color:"#2f8a57"},{label:"Demanding",color:"#cf8642"}],
      importance: [{label:"Necessary",color:"#4a85c4"},{label:"Important",color:"#2f8a57"},{label:"Optional",color:"#cf8642"}]
    };
    var chart = document.getElementById("lbChart");
    var X0 = 180, X1 = 940, Y0 = 64, Y1 = 488, MAX = 1.0;
    function el(t,a){ var e=document.createElementNS(SVGNS,t); for(var k in a){ e.setAttribute(k,a[k]); } return e; }
    function sx(v){ return X0 + (v/MAX)*(X1-X0); }
    function clear(){ while(chart.firstChild) chart.removeChild(chart.firstChild); }
    function axes(){
      for(var t=0;t<=10;t+=2){
        var x=sx(t/10);
        chart.appendChild(el("line",{class:"grid-line",x1:x,y1:Y0,x2:x,y2:Y1}));
        var tx=el("text",{class:"axis-text",x:x,y:Y1+24,"text-anchor":"middle"}); tx.textContent=(t/10).toFixed(1); chart.appendChild(tx);
      }
      chart.appendChild(el("line",{x1:X0,y1:Y1,x2:X1,y2:Y1,stroke:"#9aa6b8","stroke-width":1}));
      var at=el("text",{class:"axis-title",x:(X0+X1)/2,y:Y1+50,"text-anchor":"middle"}); at.textContent="Criterion-level pass rate"; chart.appendChild(at);
    }
    function animate(){
      var bars=chart.querySelectorAll("rect.bar");
      bars.forEach(function(b){
        var w=+b.getAttribute("width"), x=+b.getAttribute("x");
        b.animate([{transform:"translateX(0px) scaleX(0.001)"},{transform:"translateX(0px) scaleX(1)"}],
          {duration:650,easing:"cubic-bezier(.22,.61,.36,1)"});
        b.style.transformBox="fill-box"; b.style.transformOrigin="left center";
      });
    }
    function render(tab){
      clear(); axes();
      var n=models.length, band=(Y1-Y0)/n;
      if(tab==="overall"){
        models.forEach(function(m,i){
          var cy=Y0+band*i+band/2, h=Math.min(22,band*0.5), y=cy-h/2;
          var lbl=el("text",{class:"axis-text",x:X0-16,y:cy+4,"text-anchor":"end"}); lbl.textContent=m.name; chart.appendChild(lbl);
          chart.appendChild(el("rect",{class:"bar",x:X0,y:y,width:sx(m.overall)-X0,height:h,rx:3,fill:m.tier}));
          chart.appendChild(el("line",{x1:sx(m.ciLo),y1:cy,x2:sx(m.ciHi),y2:cy,stroke:"#3a4254","stroke-width":1.4}));
          chart.appendChild(el("line",{x1:sx(m.ciLo),y1:cy-4,x2:sx(m.ciLo),y2:cy+4,stroke:"#3a4254","stroke-width":1.4}));
          chart.appendChild(el("line",{x1:sx(m.ciHi),y1:cy-4,x2:sx(m.ciHi),y2:cy+4,stroke:"#3a4254","stroke-width":1.4}));
          var v=el("text",{class:"value-label",x:sx(m.ciHi)+8,y:cy+4}); v.textContent=m.overall.toFixed(3); chart.appendChild(v);
        });
      } else {
        var grp=GROUPS[tab], key=(tab==="difficulty"?"diff":"imp");
        var lg=el("g",{transform:"translate("+(X0+10)+",28)"});
        grp.forEach(function(g,j){
          lg.appendChild(el("rect",{x:j*160,y:0,width:14,height:14,rx:2,fill:g.color}));
          var lt=el("text",{class:"legend-text",x:j*160+20,y:12}); lt.textContent=g.label; lg.appendChild(lt);
        });
        chart.appendChild(lg);
        models.forEach(function(m,i){
          var top=Y0+band*i, sub=(band*0.78)/3;
          var lbl=el("text",{class:"axis-text",x:X0-16,y:top+band/2+4,"text-anchor":"end"}); lbl.textContent=m.name; chart.appendChild(lbl);
          m[key].forEach(function(val,j){
            var y=top+band*0.11+sub*j, h=sub*0.82;
            chart.appendChild(el("rect",{class:"bar",x:X0,y:y,width:sx(val)-X0,height:h,rx:2,fill:grp[j].color}));
            var v=el("text",{class:"value-label",x:sx(val)+6,y:y+h-1}); v.textContent=val.toFixed(3); chart.appendChild(v);
          });
        });
      }
      animate();
    }
    var tabs=document.getElementById("lbTabs");
    tabs.addEventListener("click",function(e){
      var b=e.target.closest("button"); if(!b) return;
      tabs.querySelectorAll("button").forEach(function(x){x.classList.remove("is-active");});
      b.classList.add("is-active"); render(b.getAttribute("data-tab"));
    });
    render("overall");
  })();

  function copyBibTeX(){
    var t=document.getElementById("bibtex-code").innerText;
    navigator.clipboard.writeText(t).then(function(){
      var btn=document.querySelector(".copy-bibtex-btn");
      var old=btn.innerHTML; btn.innerHTML='<i class="fas fa-check"></i> Copied';
      setTimeout(function(){btn.innerHTML=old;},1600);
    });
  }
  </script>
  <script defer src="static/js/fontawesome.all.min.js"></script>
</body>
</html>'''

html = HEAD + NAV + HERO + PIPELINE + STATS + LEADERBOARD + CAPABILITY + FAILURE + BIBTEX + SCRIPTS
open('/mnt/bn/zixin0803/xdailybench-page/index.html','w',encoding='utf-8').write(html)
print("index.html bytes:", len(html))
