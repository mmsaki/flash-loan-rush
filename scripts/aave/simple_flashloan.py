from brownie import accounts, config, network, interface, RushSimpleFlashLoan
from scripts.aave.helper_functions import get_address_provider, get_token, get_account


tx_url = "https://goerli.etherscan.io/tx/{}"
pool = interface.IPool(get_address_provider().getPool())
flashloan_receiver = RushSimpleFlashLoan[len(RushSimpleFlashLoan) -1]
usdc = get_token("USDC")
usdc_amount = 1_000_000 * 10** usdc.decimals()


def run_flashloan():
    dev = get_account()
    receiver = flashloan_receiver.address
    assets = usdc.address
    amount = usdc_amount
    # 'flashLoanSimple': "0x42b0b77c"
    params = "0x42b0b77c"
    referral = 0
    tx = pool.flashLoanSimple(receiver, assets, amount, params, referral, {"from": dev})
    print(f"Congrats! You have flipped a flashloan. Check it out! {tx_url.format(tx.txid)}")
    return tx

def main():
    run_flashloan()