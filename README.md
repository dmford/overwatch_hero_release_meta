# Overwatch Hero Meta Tracker

An automated data-collection project that builds a longitudinal dataset of Overwatch hero statistics for future analysis of hero releases, balance patches, and meta shifts.

The project collects daily hero-level performance metrics and stores historical snapshots that would otherwise be difficult to reconstruct after the fact. Over time, the resulting dataset can be used to evaluate how game updates influence hero popularity and performance.

The system runs automatically through GitHub Actions and requires no manual data collection once deployed.

## Project Goal

The objective is to preserve historical Overwatch hero statistics and create a dataset suitable for future empirical analysis.

Many public gaming-stat websites emphasize current hero performance but do not provide convenient access to long-run historical snapshots. This project addresses that limitation by collecting and archiving daily observations in a structured format.

As the dataset grows, it becomes increasingly useful for studying hero releases, balance changes, and evolving player behavior.

## Current Status

The project is currently in the data-collection phase.

Daily snapshots are automatically collected and stored for future analysis.

The current workflow captures:

* Hero pick rates
* Hero win rates
* Multiple competitive ranks
* Multiple regions
* Multiple platforms

The resulting dataset is designed to support future longitudinal analysis of game balance and meta evolution.

## Data Collection Workflow

Each daily run:

1. Collects current hero statistics from public sources.
2. Captures hero-level pick-rate and win-rate metrics.
3. Records metadata including region, platform, and competitive rank.
4. Stores daily snapshots in a structured historical archive.
5. Updates supporting metadata files.
6. Preserves historical observations for future analysis.

The workflow is designed to create a consistent daily time series of hero performance metrics.

## Automation

The project uses GitHub Actions to automate collection and archival.

Benefits include:

* Fully automated daily execution
* Consistent data collection schedule
* Historical snapshot preservation
* Cloud-based operation without local maintenance
* Reproducible data pipeline

The workflow can also be executed manually through the GitHub Actions interface.

## Repository Structure

```text
data/
    raw/
        Daily hero-statistic snapshots
    processed/
        Derived datasets and future analysis outputs

scripts/
    collect_data.py

.github/
    workflows/
        daily_run.yml

README.md
requirements.txt
```

## Planned Future Analysis

Future versions of the project may examine:

* Hero release effects
* Balance patch effects
* Pick-rate trends
* Win-rate trends
* Meta shifts over time
* Persistence of hero popularity
* Competitive-rank differences
* Regional differences
* Long-run hero performance trajectories

## Technologies Used

* Python
* GitHub Actions
* Automated web data collection
* CSV-based historical storage
* Scheduled cloud workflows

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the collection script:

```bash
python scripts/collect_data.py
```

## Author

David Ford

This project was developed by David Ford with AI-assisted coding support (ChatGPT) used for debugging, documentation, workflow planning, and code review. Project design, implementation decisions, validation, interpretation, and final repository contents were reviewed and approved by the author.
