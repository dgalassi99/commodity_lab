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

### Mark-to-Market

MTM is a defining characteristic of future contracts. That is, the final daily settlement price for futures is the same for everybody. After 2008 also forwards and swaps on OTC follow the MTM regulation. The official daily settlment price is set by the exchange, and while the formulas vary cotract by contract the methodology is the same. 

Futures contracts are marked-to-market (MTM) daily, meaning your position is revalued each day using an official settlement price set by the exchange, which determines your daily gain or loss. This ensures profits and losses are realized and transferred daily, reducing credit risk.  For example: (1) Corn futures settle using the last trade before the close; (2) E-mini S&P 500 futures use a volume-weighted average price (VWAP) over the last 30 seconds of trading.

This means that daily profit and losses (calcualted as the difference between previous and today's settlement price) are reported, and, if required (when daily losses fall behind the margin levels required) margin adjustment is made by providing additional cash to replanish back my position to the required level and avoid liquidation.

### Margin

Securities margin is the money you borrow as a partial downpayment (up to 50% of the purchase price) to buy and own a stock, bond or ETF. We call it buying on margin.

Futures margin, differently, is the amount you must deposit and keep in your broker account to opena futures position. This generally represent a small fraction of the notional value (3-12%). The fraction mosntly depend on the clearing house and the broker, who decide to increase this fraction when prices are more volatile.

We have:

- Initial margin: amount to deposit to open a position (set by clearing house and sometimes increased a bit by the exchange)
- Maintenance margin: minimum amount to be mantained at any time

If the accounf drops below the maintenance margin level:

- You may receive a margin call and be required to deposit more funds to bring back teh account to the initial margin level
- If you do not, you can reduce your position with the funds remaining
- Or, your position can be fully liquidated

### Expiration, Contract Roll and Settlement

A contract's expiraition date is the last date you can trade a contract (typically 3rd Friday of the expiration month). Prior to expiration we have three options:

1. Offseting or liquidating is the simplest solution by realizing all profit/losses associated witht a position without taking delivery. To offset you need to take an equal and opposite position to neutralize the trade. Say you are short on two WTI Crude contract expiring in Sep, to offset you need to buy two WTI contract expiring on the same date. The difference inprice between the initial and opposite position determines the net profit/loss on the trade.

2. Rolling over means moving the position to a contract further in the future. Usually, this is done my volume monitoration. When rolling, you are simultaneously offsetting the old posiiotn and enstablish a new one. Say you are long on four E-minis. To roll you need to short four contract with the same expiration and long four more contract with fdurther expiration.

3. Settlement occurs if no offset neither roll has occurred. Short traders have to deliver the underlying and long traders to accept it. Delivery can be either physical or represented by a cash settlement. 

### Price Discovery

Price discovery referes to the act of determining a common price for an asset. It is the result of the interactions between buyers and seller. In this way, traders living in two opposite corners of the world will experiecne the same bid/ask quotes at the same time (market transparency). Bid ans ask price costantly change based on supply and demand mechanism and known news, which are incorporated into the prices (market efficiency)

### PnL Calculation

Profit and losses are calculated based on the following information: (1) tick size, (2) contract size; (3) purchase price; (4) current price.

To be brief, let's take an example. Say the current price of WTI is 54 USD. The contract value is 54000 USD (remember WTI contract size is 1000 USD/barrel). We also know that for WTI the tick size is 0.01 USD.

Assume you bought at 53.6 USD, so the profit per contract is 54-53.6 = 0.4 USD. This means that we moved of 0.4/0.01 = 40 ticks. One tick move corresponds to 10 USD (0.01 USD *1000 USD/barrel). So the toal move in dollars is 40 ticks * 10 USD/tick = 400 USD. Hence the total profit is 400 USD per contract.

Notice how the size of the contract has a considerable multiplying effect on the Pnl!

### Speculators

A spaculator is any individual/firm accepting risk in order to make a profit. We have: (1) individual traders; (2) proprietary trading firms (prop shops) which profit from their traders'activity in the market. They supply traders with education, tools and capital; (3) portfolio/investment managers ar responsible for managing the assets of a fund via day-to-day trading activities; (4) hedge funds use advanced strategies to mazimize absolute returns or relative to a benchmark; (5) market makers are trading fimrs that provide liquidity to the market (both bid and ask) in exchange for a reduction in trading fees. They often profit by capturing the spread between the bid and the offer over a large volume of transactions.

### Hedgers

Hedgers are market participants who buy/sell the actual physical commodities. Examples are producers, wholesalers, manufacturers, and retailers. These individuals need protection from commodity prices, interest rates, and exchange rates changes.

- Buy-side (long) hedgers are concernced about rising prices. A wholesaler, for example, might long futures to lock in the purchase price. If the price falls he loses money on the future contract but buys the physical commodity at a lower price making a profit.
- Sell-side (short) hedgers are concerned about falling prices. A producer, for example, might short futures to lock in the selling price. If the price falls he loses money because he is forced to sell lower, but he makes profit from his short position on the futures contract.
- Merchandisers both buy and sell commodities. They have a bi-directional risk and they mostly care about the spread between the buying and selling price.

### Volume

Volume is the count of the number of contracts exchanged during a given time interval and can be used to make trading decisions as it can:

- Indicate price levels at which traders are more or less interested in trading
- During the roll, it indicates when to switch to the front contract
- Identify the moments when the market is more liquid

Changing volume indicates that contracts are moving towards certain levels. For example, during rollovers, expiring contracts lose volume and front contracts spike in volume, indicating when it is time to roll over the next contract.

Moreover, traders prefer to operate during high volume periods as bik-ask spread decline, orders are filled faster and smaller gaps exist between ticks. Notice that, a spike in volume does not necessarily indicate a bullish or bearish movement. For example, if the price of an E-mini decreases from 2375 to 2360 while volume increases it can describe an action where traders are opening long positions at key support levels but it can also be generated by closing long position or opening new shorts.

### Open Interest

Open interest (OI) is the total number of futures contracts held by the market participants at the end of the trading day. It is used as an indicator of the market sentiment and the strenght behind prices trends.

Differently from the total outstanding shares of a company (constant), thenumebr of outstadning futures varies day to day. Hence, the OI is calculated by adding all opened positions and subtracting all closed positions (regardless the direction long/short).

You can think of OI as the cash flowing into the futures market. As it increases, more money is flowing in and as it decreases money is moving out. As a consequence it can be used to confirm/reject the strenght of a trend (increasing OI is a trend confirmation signal).




