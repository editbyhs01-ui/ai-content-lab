# Konten Studio — Short-Form Content Engine

A starter scaffold for adapting `ai-content-lab` into a short-form content production workflow for @editbyhs6.

## Brand
- Positioning: Islamic Cinematic Reflection
- Format: short-form vertical video
- Core pillars: Islamic life reflection, verified spiritual reminders, cinematic storytelling with a consistent virtual hijab-wearing character
- Distribution targets: TikTok, Facebook Reels, Instagram Reels, YouTube Shorts

## Workflow
Brief → research and fact-check → audience analysis → script → editorial review → platform optimization → production package → performance evaluation.

## Important scope notes
This repository currently provides a starter scaffold, not a live autonomous production system. It does not run external agents, perform live web research, generate media, publish content, or retrieve analytics unless those integrations are implemented and configured separately. Religious claims and quotations must be verified against reliable primary sources before publication. Never fabricate performance data or guarantee virality or revenue.

## Setup
1. Create a Python 3.11+ environment.
2. Install dependencies: `pip install -e ".[dev]"`
3. Copy `.env.example` to `.env` and fill only the API credentials for integrations you intentionally configure.
4. Run tests with `pytest`.

## Starter CLI
Run `python -m konten_studio` to print the workflow overview.

## Upstream
This work is intended as an adaptation layer alongside the upstream project: https://github.com/tiagomonteiro0715/ai-content-lab

Review the upstream MIT license and retain required attribution when redistributing upstream-derived code.