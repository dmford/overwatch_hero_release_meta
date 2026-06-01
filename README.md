# Overwatch Hero Release Meta

## Overview

This project builds an automated historical dataset of Overwatch hero statistics.

The current version focuses on daily data collection rather than final analysis. The purpose is to preserve hero-level pick-rate and win-rate snapshots over time so that future analyses can evaluate hero releases, balance patches, and meta shifts.

The project uses GitHub Actions to run automatically and append new daily observations without requiring manual collection.

## Current Status

This repository is currently in the data-collection phase.

It automatically captures daily hero statistics and stores them for future analysis. Planned analysis will evaluate how hero releases, balance updates, and broader meta changes affect pick rates and win rates over time.

## Project Motivation

Public game-stat websites often emphasize current performance rather than preserving long-run historical snapshots.

This project addresses that problem by collecting hero statistics every day and storing them in a structured format. The dataset becomes more useful over time as additional observations accumulate.

## Repository Structure

- data/
  - raw/
  - processed/
- scripts/
  - collect_data.py
- .github/
  - workflows/
    - daily_run.yml
- README.md
- requirements.txt

## Planned Future Analysis

Future versions of this project may examine:

- Hero release effects
- Balance patch effects
- Pick-rate trends
- Win-rate trends
- Meta shifts over time
- Persistence of hero popularity

## How to Run

Install dependencies:

    pip install -r requirements.txt

Run the data collection script:

    python scripts/collect_data.py

## Author

David Ford

This project was developed by David Ford with AI-assisted coding support (ChatGPT) used for debugging, documentation, workflow planning, and code review. Project design, implementation decisions, validation, interpretation, and final repository contents were reviewed and approved by the author.
