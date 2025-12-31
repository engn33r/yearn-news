# Yearn News Generator

Weekly newsletter generator for "The Blue Pill" - Yearn ecosystem updates.

## Running

Run via Docker container:
```bash
docker exec objective_robinson bash -c "cd /projects && uv run python src/generate.py"
```

## Architecture

- `src/generate.py` - Main generator, renders all sections to Markdown
- `src/content.py` - Editable text content for each section
- `src/tvl.py` - TVL data from DefiLlama API
- `src/vaults.py` - On-chain vault data from registries
- `src/ycrv.py` - yCRV rewards from RewardDistributor
- `src/yyb.py` - yYB data (TODO)
- `src/utils.py` - Shared helpers (web3, multicall, caching, formatting)
- `src/abis/` - Contract ABIs

## Key Contracts

- Registries: `0xd40ecF29e001c76Dcc4cC0D9cd50520CE845B038`, `0xff31A1B020c868F6eA3f61Eb953344920EeCA3af`
- APR Oracle: `0x1981AD9F44F2EA9aDd2dC4AD7D075c102C70aF92`
- RewardDistributor (yCRV): `0xB226c52EB411326CdB54824a88aBaFDAAfF16D3d`
- yvcrvUSD-2 vault: `0xBF319dDC2Edc1Eb6FDf9910E39b37Be221C8805F`

## Caching

Data is cached in `data/` with week/year tracking for WoW comparisons:
- `tvl_cache.json`
- `ycrv_cache.json`

## Output

Generates `output.md` in Markdown format for copy-paste to publication platform.
