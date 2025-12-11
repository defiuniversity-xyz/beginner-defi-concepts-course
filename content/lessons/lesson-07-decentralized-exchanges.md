---
module: 2
lesson_number: 7
course: defi-concepts
---

<audio controls>
  <source src="https://storage.googleapis.com/beginner-defi-crypto-concepts-gitbook-media/lesson-07/audio/lesson7 AMM_Math_and_Impermanent_Loss_Explained.m4a" type="audio/mp4">
  Your browser does not support the audio element.
</audio>

<video width="100%" controls>
  <source src="https://storage.googleapis.com/beginner-defi-crypto-concepts-gitbook-media/lesson-07/video/lesson7 Engine_of_DeFi_Trading.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

# Lesson 7: Decentralized Exchanges

## 🎯 Core Concept: Automated Market Makers (AMMs)

TradFi and Centralized Exchanges utilize Central Limit Order Books (CLOBs), where buyers and sellers list prices. DeFi introduced a novel primitive: the Automated Market Maker (AMM), which uses mathematical formulas instead of order books to determine prices.


![AMM vs Order Book Comparison](https://storage.googleapis.com/beginner-defi-concepts-gitbook-images/lessons/lesson_07/bdc07_01_amm_vs_order_book_comparison.png)


## 📚 The Constant Product Formula

The fundamental equation governing early AMMs (like Uniswap V2) is:

$$x \times y = k$$

Where:
- **x**: The quantity of Token A in the pool
- **y**: The quantity of Token B in the pool  
- **k**: A constant (must remain the same after every trade)

**How It Works**: When a trader buys Token A from the pool, the supply of x decreases. To keep k constant, the supply of y must increase. This algorithmic relationship automatically adjusts the price based on supply and demand.


![Constant Product Formula Visualization](https://storage.googleapis.com/beginner-defi-concepts-gitbook-images/lessons/lesson_07/bdc07_02_constant_product_formula_visualization.png)


## 📚 Liquidity Pools

Instead of matching a buyer with a seller, the AMM matches a trader against a "pool" of assets (smart contract) provided by Liquidity Providers (LPs).

**Key Concepts**:
- **Liquidity Providers**: Users who deposit tokens into pools to earn fees
- **Price Discovery**: Prices adjust automatically based on trades
- **Impermanent Loss**: LPs face risk if token prices diverge significantly


![Liquidity Pool Components Diagram](https://storage.googleapis.com/beginner-defi-concepts-gitbook-images/lessons/lesson_07/bdc07_03_liquidity_pool_components_diagram.png)

## 🎮 Interactive: DEX Swap Simulator

Experience how AMM swaps work with this interactive simulator. See how trades affect pool reserves and cause slippage:

{% embed url="https://defi-university-app.web.app/interactives/defi-concepts/dex-swap-simulator.html?courseId=defi-concepts&interactionId=dex-swap-simulator" %}

### Interactive DeFi Protocol Explorer

Use this interactive tool to explore and compare different DeFi protocols:

{% embed url="https://defi-university-app.web.app/interactives/beginner-defi-concepts/defi-protocol-explorer.html?course=defi-concepts&id=defi-protocol-explorer-lesson7&topic=Decentralized%20Exchanges" %}

### Interactive Yield Farming Calculator

Use this interactive tool to calculate potential yields from liquidity provision:

{% embed url="https://defi-university-app.web.app/interactives/beginner-defi-concepts/yield-farming-calculator.html?course=defi-concepts&id=yield-farming-calculator-lesson7&topic=Yield%20Farming" %}

### Interactive Gas Fee Estimator

Use this interactive tool to estimate gas fees for DEX transactions:

{% embed url="https://defi-university-app.web.app/interactives/beginner-defi-concepts/gas-fee-estimator.html?course=defi-concepts&id=gas-fee-estimator-lesson7&topic=DEX%20Transactions" %}

## 🔑 Key Takeaways

1. **AMMs Replace Order Books**: Mathematical formulas determine prices automatically
2. **Liquidity Pools**: Traders swap against pools, not individual orders
3. **Constant Product Formula**: x × y = k ensures liquidity always exists
4. **Price Impact**: Larger trades move prices more (slippage)
5. **LP Risks**: Providing liquidity has risks (impermanent loss)

---

**Next Lesson**: In Lesson 8, we'll explore DeFi lending and borrowing protocols.
