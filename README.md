# overwatch_hero_release_meta

## Overview

This project analyzes how new hero releases affect the competitive Overwatch meta over time.

The primary goal is to measure:
- how disruptive new hero releases are,
- how quickly the meta stabilizes afterward,
- and whether consistent patterns emerge across roles, ranks, regions, and release periods.

The project is designed as a data analysis and statistical modeling exercise using Python, with a focus on event-study style analysis, ecosystem dynamics, and time-series visualization.

---

## Planned Research Questions

Examples of questions this project may explore:

- Do new hero releases measurably increase meta volatility?
- How long does the competitive meta take to stabilize after a release?
- Which hero roles create the largest disruption?
- Has adaptation speed changed over the lifespan of Overwatch?
- Do metas become more or less concentrated after hero releases?
- Are there consistent post-release adoption patterns?

---

## Planned Metrics

The core planned metric is a normalized **Meta Volatility Index (MVI)**, intended to measure how much hero pick-rate distributions change from one period to the next.

Additional planned metrics may include:
- role-specific volatility,
- hero concentration / diversity indices,
- adoption curves,
- stabilization windows,
- and comparative event-study summaries across hero releases.

---

## Planned Workflow

### Phase 1 — Data Collection
- Pull hero pick-rate / win-rate data
- Build a historical panel dataset
- Standardize hero role classifications
- Track hero release dates and major patches

### Phase 2 — Data Cleaning
- Construct consistent daily or weekly time-series data
- Harmonize role categories across Overwatch versions
- Exclude or flag structurally unusual releases/events

### Phase 3 — Analysis
- Build volatility and concentration metrics
- Run event-study style before/after analyses
- Compare disruption magnitude across hero releases

### Phase 4 — Visualization
- Meta volatility plots
- Hero adoption curves
- Stabilization timelines
- Role-level comparison figures

---

## Current Status

This repository is currently in the early data-collection and infrastructure phase.

Initial development priorities:
1. Validate accessible historical data sources
2. Build data pull scripts
3. Construct a clean reproducible dataset
4. Prototype the Meta Volatility Index

---

## Tools

Planned tools/libraries include:
- Python
- pandas
- numpy
- matplotlib
- requests

Additional libraries may be added later as needed.

---

## Repository Structure

```text
overwatch_hero_release_meta/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── figures/
├── tables/
├── output/
│
├── scripts/
│   ├── data_pull.py
│   ├── data_cleaning.py
│   └── analysis.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Notes

This project is exploratory and intended primarily as a learning and analytical portfolio project.

The analysis is not intended to make definitive claims about game balance or hero strength.

---

## Author

David Ford, assisted by ChatGPT