from brownie import config, accounts, interface, network
from scripts.helper_functions import get_address_provider, get_token, get_account, get_lending_pool

# Accepts token_name as string
def supply_token(token_name, amount):
    acct = get_account()
    token = get_token(token_name)
    provider = get_address_provider()
    pool = get_lending_pool()
    approval_tx = token.approve(pool, amount, {"from": acct})
    tx = pool.supply(token, amount, acct, 0, {"from": acct})
    return web3.eth.get_transaction_receipt(tx)

# Accepts token name as string
def main(token_name, amount):
    supply_token(token_name, amount)