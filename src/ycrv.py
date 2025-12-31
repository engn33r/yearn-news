from typing import Any

from utils import get_previous_week_data, get_web3, get_week_and_year, load_abi, save_cache

REWARD_DISTRIBUTOR_ADDRESS = "0xB226c52EB411326CdB54824a88aBaFDAAfF16D3d"
YVCRVUSD2_ADDRESS = "0xBF319dDC2Edc1Eb6FDf9910E39b37Be221C8805F"


def get_data() -> dict[str, Any]:
    """Fetch previous week's yCRV rewards from RewardDistributor."""
    w3 = get_web3("mainnet")
    week, year = get_week_and_year()

    # Get reward distributor data
    rd_abi = load_abi("reward_distributor")
    rd_contract = w3.eth.contract(
        address=w3.to_checksum_address(REWARD_DISTRIBUTOR_ADDRESS),
        abi=rd_abi,
    )

    current_week = rd_contract.functions.getWeek().call()
    prev_week = current_week - 1
    reward_amount = rd_contract.functions.weeklyRewardAmount(prev_week).call()

    # Rewards are in yvcrvUSD-2 vault tokens (18 decimals)
    rewards_vault_tokens = reward_amount / 1e18

    # Get pricePerShare to convert to crvUSD
    vault_abi = load_abi("vault")
    vault_contract = w3.eth.contract(
        address=w3.to_checksum_address(YVCRVUSD2_ADDRESS),
        abi=vault_abi,
    )
    price_per_share = vault_contract.functions.pricePerShare().call()
    pps = price_per_share / 1e18

    rewards_crvusd = rewards_vault_tokens * pps

    # Get previous week data for WoW comparison
    prev_data = get_previous_week_data("ycrv", week, year)
    wow_pct = None
    prev_rewards_crvusd = None
    if prev_data and prev_data.get("rewards_crvusd"):
        prev_rewards_crvusd = prev_data["rewards_crvusd"]
        if prev_rewards_crvusd > 0:
            wow_pct = ((rewards_crvusd - prev_rewards_crvusd) / prev_rewards_crvusd) * 100

    # Cache current week data
    cache_data = {
        "week": week,
        "year": year,
        "distributor_week": prev_week,
        "rewards_vault_tokens": rewards_vault_tokens,
        "rewards_crvusd": rewards_crvusd,
        "price_per_share": pps,
    }
    save_cache("ycrv", cache_data)

    return {
        "rewards_crvusd": rewards_crvusd,
        "prev_rewards_crvusd": prev_rewards_crvusd,
        "wow_pct": wow_pct,
        "distributor_week": prev_week,
    }
