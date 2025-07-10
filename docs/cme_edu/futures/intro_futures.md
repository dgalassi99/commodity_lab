# Futures

## Introduction

### What a Future is

Forward and futures contracts allow market partipants to offset/assume risk of a price change of an asset overtime. Futures differ from forwars as: (1) a future is a legally binded contract; (2) future transactions are made via an exchange. Simply put *futures are standardized*. 

A future specifies the quality, quantity, delivery time and location for a given product. Specifications are identical for all market participants, allowing easiness of trades. Hence, teh only contract variable is the price, which is discovered by bid and aks, until a match (trade) occurs.

The exchange guarantees that the contract will be honored, eliminating counterparty risk. Technically we say that exchange-traded future contracts are centrally cleared. Fully offsetting the risk associated with the default of the seller/buyer party.

### Contract Specs

Every futures contract has an underlying asset, the quantity, the delivery location and date. When a party enters a contract, they agree to excahnge the underlying (physical commodity like oil or a foreign currency) at a defined time in the future. When the asset is physical the contract also specifies the minimum quality required. For example WTI Crude Oil contracs are 1000 barrels of a grade crude known as "light and sweet", which indicates the amount od H2S and CO2 the crude it contains.

As we can notice also the quantity is well specified...1000 barrels for oil or 5000 bushels for corn or treasury bonds with a face value of 100000 USD. When contract sizes are too big for retail investors, many exchange offer "mini" contracts (e.g. E-mini S&P 500).

Delivery date is also a key aspect, mostly for physiscal commodities, which bear transportation and storage cost. 

### Trading Codes

Understanding contract codes is key to comprehend pricing structures. Typical formats are:
- one- to three-letter codes identyfing the product
- one-character indicating the month and year of expiration

For example (CME standards) the ESF9 is E-mini S&P500 expiring in January 2019

[January-F, February-G, March-H, April-J, May-K, June-M, July-N, August-Q, September-U, October-V, November-X, December-Z]

### Expiration and Settlement 

Prior to the expiration date traders have the options to close, extend or settle the position.
Settlement is the fullfilling of the legal delivery obbligation associated with the contract. Even if physiscla delivery is a key mechanism, only a small percent of all commodities futures contrac are actually delivered. In most of the cases, delivery takes place in the form of cash settlement (mostly for forex, equities and interest rates futures).

### Minimum Price Fluctuation (Tick)

Ticks are set by exchanges and vary by contract instruments. For example, for the E-mini S&P 500 teh tick size is 1/4 of a point. Since an index point is 50 USD a movement of one tick is 12.5 USD. For NYMEX WTI Crude Oil the tick equals 0.01 USD/barrel, since contracts are of 1000 abrrels, the minimum tick is 10 USD. 

### Price Limits and Price Banding

#### Price Limits

Maximum price range permitted for a future contract in each trading session. These limits are measured in tick, thus vary acroos products. When price limits are hit different actions can occurr such has halting price until limits are expanded or the stopping the trading day. Price limits are re-calculated daily and remain active most of the times, expect when those limits are preventing futures to converge to the underlying spot price. Note that you can place orders outside the limits, tehse can eventually be executed after the re-calculation.

#### Price Bands

Price banding forces order to be in a given window. For example, f one commodity is trading at 100 USD you might be forced to place orders in a band [95-105] USD. Note that those bands dynamically evolve base don the current price and a fixed constant term.

### Contracts Value & Unit

#### Contract Unit

The contract unit is a standardized size unique to each futures contract and can be based on volume, weight, or a financial measurement. For example, a single COMEX Gold contract unit (GC) is 100 troy ounces, which is measured by weight. A NYMEX WTI Crude Oil contract unit (CL) is 1,000 barrels of oil, measured by volume. The E-mini S&P 500 contract unit (ES) is a financial calculation based on a fixed multiplier (50 USD) times the S&P 500 Index.

#### Contract Notional Value

Assume a Gold futures contract is trading at price of $1000. The notional value of the contract is calculated by: contract unit x contract price = notional value --> 100 (troy ounces) x 1000 USD/ounces = 100000 USD. Similarly, if WTI Crude Oil is trading at 50 USD/barrel and the contract unit is 1000 barrels, the notional would be 50 USD/barrel x 1000 barrel = 50000 USD. Now assume E-mini S&P 500 futures are trading at 2120.00 index points. The multiplier for this contract is 50 USD. The notional value is 50 USD/index points x 2120.00 index points = 106000 USD.

#### Hedge Ratio

Understanding the concepts of contrac value and unit is key. Suppose we have 10M USD in the E-mini and want to know how to hedge out position. We can use the hedge ratio (value at risk/notional value). In this example we have 10M USD at risk and a notional value of 106000 USD. The hedge ratio is thus 94.3. Hence we need to sell ~ 94 E-mini futures against the long position to fully hedge our market risk.



