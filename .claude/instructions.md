# Yearn News - The Blue Pill

Weekly newsletter generator for the Yearn ecosystem.

## Project Overview

This project generates "The Blue Pill" - a weekly newsletter covering Yearn protocol activity. The newsletter is generated programmatically by fetching on-chain data and aggregating it into a formatted article.

## Newsletter Sections

Each section has its own Python script in `src/`:

1. **TVL & Protocol Metrics** (`tvl.py`)
   - Fetches current TVL across all chains
   - Calculates week-over-week changes

2. **Governance** (`governance.py`)
   - Fetches active/recent governance proposals (YIPs)

3. **V3 Vaults** (`v3_vaults.py`)
   - Top yielding V3 vaults across chains
   - APY and TVL data

4. **V2 Vaults** (`v2_vaults.py`)
   - Top yielding V2 vaults across chains
   - APY and TVL data

5. **yCRV** (`ycrv.py`)
   - Weekly yCRV fees
   - Vault token deposits and underlying value
   - Week-over-week fee changes

6. **yYB** (`yyb.py`)
   - yYB metrics and updates

7. **Alpha Corner** (manual)
   - This section is written manually by the team
   - Contains unreleased features, upcoming strategies, etc.

## Usage

Run the main generator script:

```bash
python src/generate.py
```

This will:
1. Execute each section script to fetch fresh data
2. Aggregate all data into a formatted newsletter
3. Output the final article to stdout

Copy the output and paste it into the publication website.

## Code Style

- Python 3.12+
- Use `ruff` for linting and formatting
- Use `mypy` for type checking
- **KISS** - Keep It Simple, Stupid. No over-engineering. Write the simplest code that works.
- **DRY** - Don't Repeat Yourself. Extract shared logic into reusable functions.
- Clean, minimal code. No unnecessary abstractions, comments, or boilerplate.
- Each section script exposes a `get_data()` function returning structured data.
- Use `.env` for API keys and RPC URLs.

## Data Sources

**On-chain only** - all data comes from:
- **DeFiLlama API**: TVL data (`https://api.llama.fi/`)
- **On-chain RPC**: Direct contract calls for vault data, APYs, governance, etc.

Do NOT use centralized Yearn APIs. Fetch everything from on-chain or DeFiLlama.

## Output Format

```
## Overview
[Introduction text]

## Yearn at a glance
[TVL metrics, governance summary]

## V3 Vaults
[Top 5 vaults with APY and TVL]

## V2 Vaults
[Top 5 vaults with APY and TVL]

## yCRV
[Fee metrics and week-over-week changes]

## yYB
[yYB metrics]

## Alpha Corner
[Manual section - placeholder for team input]
```

## Development Notes

- "Alpha Corner" requires manual input - script includes a placeholder
- Week-over-week comparisons use a simple JSON cache for previous data
- Format monetary values with appropriate decimals
- Format APY as percentages with 2 decimal places
