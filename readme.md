
# Rush
![Rush](./images/rush_contracts/rush_contracts.002.jpeg)

## What Category does your project belong to?
- **Decentralized Finance (Defi)**

## Emoji
- **🎠**

## GitHub Repository
- [**Rush Flashloans**](https://github.com/mmsaki/flash-loan-rush)

## Short Description
- **Rush** makes it easy for Defi users to use **Aave's lending pool** to borrow and retrun assets assets using **flashloans**.

## Long Description

- **Rush** is a service that interacts with **Aave  v3 Lending pools** to supply and borrow assets using its **flashloan contracts**. Defi users can rely on simple tools to trade borrow assets. Sometimes trading assests can cause major shifts in prices. Defi users who **borrow assets** are sometimes forced to **liquiditate automatically** to pay off their debt. This can lead to **max losses**. Rush Flashloans provides an easy way to  borrow positions from outstanding **collateral on aave**. We also want common Defi users without any technical backgrounds to use learn how to use flashloans without any complications. We want to offer **secure contracts** when borrowing assests. Any debt is paid off after a flashloan including a **flashloan premium fee**.

## How It's Made

- We used Aave V3 Core contracts and build Rush using their protocol. 
    - We use **Optimism Goerli** for testing
    - We deployed two contracts
        - `RushFlashLoan`
            - For borrowing multiple tokens
        - `RushSimpleFlashLoan`
            - For borrowing a single token
    - We supply liquidity to aave and received **atokens**
    - We call `.flashloan( )` on the lendign pool contract
        - Our receiver will be the `RushFlashloan` contract we deployed
        - We can swap tokens by providing an array of token addresses and amounts.
        - With enough net worth colllateral you can swap millions.

![](./images/rush_contracts/rush_contracts.006.jpeg)

- Aave Flash loan fee
    - The flash loan fee is **initialized at deployment** to `0.09%` which is updated via aave Governance Vote. Use `FLASHLOAN_PREMIUM_TOTAL` to get current value.
    - Flashloan fee can be shared by the LPs (liquidity providers) and the **protocol treasury**. The `FLASHLOAN_PREMIUM_TOTAL` represents the total fee paid by the borrowers of which:
        - Fee to LP: `FLASHLOAN_PREMIUM_TOTAL - FLASHLOAN_PREMIUM_TO_PROTOCOL`
        - Fee to Protocol: `FLASHLOAN_PREMIUM_TO_PROTOCOL`

<!-- - Setting Up
    - Ensure we have enough funds when flashloaning
    - Calculate the profitability of liquidating loans vs gas costs
    - Ensure we have access toe the latest protocol user data
    - Fail safe security 
- Aave contracts and registry on Optimism 
    - [V3 Testnet Aave Address on Optimism Görli](https://docs.aave.com/developers/deployed-contracts/v3-testnet-addresses) -->


## Project Roadmap

- [x] Create Project 
    - [Loan Rush]()
- [ ] Checkin #1
    - Update: We Missed checkin #1
- [x] Create Logo
    - [Rush logo](./images/carousel.png)
- [x] Create Discord
    - [Discord](https://discord.gg/57TA3bHx62)
- [x] Submit Checkin #2 
    - How is the project coming along?
- [ ] Create test scripts
- [x] Project feedback Session Thu, Sep 15 02:00 PM
- [ ] Create Presentation Sun, Sep 18 11:00 AM
    - Project Table of Contents
    - Problem Rush is solving in Defi
    - How to use Rush
- [ ] Create Live Demo URL Mon Sep 19 11:00 AM
    - Front end landing page
    - Users can connect metamask
    - User can call deposit WETH function
    - User can send flashloan
- [ ] Project Check-in #3 Tue, Sep 20 11:00 AM
    - Is everything going as expected
    - What are some things you need help with
    - What do you need to complete your project?
- [ ] Project feedback Session Wed, Sep 21 02:00 PM
    - Present project for feedback
- [ ] ETHOnline Summit Fri, Sep 23 11:00 AM
    - If ready submit project
    - Record Video demonstration on how to use app
- [ ] Submissions Due! Sun, Sep 25 02:00 PM
    - Submit project by 2:00pm
- [ ] Project Judging Mon, Sep 26 11:00 AM
    - Present to judges and sponsors
 