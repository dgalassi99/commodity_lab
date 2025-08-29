# Trading and Market Structure 

## Market Basics

### What is a Commodity?
*Tradable raw materials that can be used as inputs in the prodcution of other goods/services*

So those are basic resources interchangable with other goods of the same type. The quality might change but it needs to meet minimum standards: basis grade (e.g. for oil is the content of hydrogen and sulphur). 
Commodities are usually exchanged via futures contract on exchanges that standardize the quantity and the minimum 
quality of the goods.

The fact that commodities are produced/sold by many firms and are uniform in quality gives them a key feature: *fungibility*.
For example, diamonds vary too much in quality and in volumes so are not commodities (differently from oil).

There are two types of commodity traders:(1) consumers/producers who buy/sell futures to hedge against price changes; 
(2) speculators who try to profit from price actions/movements and never intend to take the actual delivery when the future contract expires .

Generally speaking, commodity prices increase with inflation as they offer a protection agais purchasing power loss. Tho prices are determined by supply/demand mechanism such as booms, economic shocks and so on.

We can split them into hard commodities (minerals, ores and oil/gas) and soft commodities (wheat, cotton sugar, coffee)

links...

- https://www.investopedia.com/terms/c/commodity.asp
- https://www.thoughtco.com/commodity-economics-definition-1146936
### Spot vs Futures Prices

*Why commodities have two prices?*

Spot and futures prices are quotes for a contract agreed by the two parties. What makes them different is the 
timing of the transaction and the delivery date of the commodity (immediate vs in the future).

The use of futures is needed to lock the price in adavance. Future's prices are based on spot prices plus the *cost of carry* (cost of storage, interest and insurance on it).
So the future price (F) is the sum of spot price (S) and storage cost (C) times the exponential of the product between time to maturity (t) and the difference between risk free rate (r) and convenience yield rate (y).

$F = (S + C) e^{(r-y)t}$ or sometimes $F = S e^{(c+r-y)t}$

Note: y acts a s a negative cost, so F < S when y > (r+c). The convenience yield takes into account expectations of supply and demand.

A key concept is the *basis*. The *difference between **local** spot price and the price of the earliest available future*. The basis can vary regionally as the transportation costs are different (local term is key in the definition)
Assume the spot price for oil is 54 USD/barrel and the future one is 50 USD/barrel. The basis is 4 USD/barrel and is crucial... why?

- It affects the value of the contract used in hedging
- It is used by traders do choose the best time to buy/sell (if it is strenghtening/weakening)
- It is not accurate, there are gap prices and quality difference: the *basis is an imperfect indicator*

links...

- https://www.investopedia.com/ask/answers/062315/how-are-commodity-spot-prices-different-futures-prices.asp

### Contango and Backwardation

They refer to the pattern on contract prices overtime. 

**Contango:** future price above the expected spot price (confused with a normal curve)

**Backwardation:** future price below the expected spot price (confused with an inverted curve)

A future curve is **normal** if future prices are higher at longer maturities, **inverted** in the opposite case.

Let's take a curve future prices vs maturity (similarly to interest rates). 
![image](https://github.com/user-attachments/assets/ed964439-b816-4287-9351-28de9627ca21)

Why a curve should be inverted? Because market participants (taking into account the cost of carry) update continously their
views about the future expected spot price. For example, a traditional oil curve is normal in the short term and inverted in the long one.

Let's focus on two ideas: (1) as we approach maturity the future price approaches the spot one (no arbitrage); 
(2) the most rational future price is the expected future spot price.

Now we can *redefine* contango and backwardation. Suppose we entered in a 12/23 futures contract today at 100 USD. Now, one month from today,
the same contract could be 100 USD, 110 USD (normal backwardation) or 90 USD (contango).

**Contango:** future price above the expected spot price. Because convergence must occurr, contango
implies that future prices are falling over time. 

**Backwardation:** future price below the expected spot price. Because convergence must occurr, backwardation
implies that future prices are increasing over time. 

Consider we purchase today a future contract due in one year (spot at 60 USD). If today's future price is 
90 USD we are in a contango scenario. Unless the spot price changes the contract price must drop.
![image](https://github.com/user-attachments/assets/614e1951-5ac5-4db2-a7c6-bd6955f44c53)

Note:

- Markets evolve, so if for example a suplly shock causes a shortage in a commodity, the spot price will
increase and we can shift from a contango to a backwardation market
- You can determine the situation by plotting the future price with the expected spot price

links...

- https://www.investopedia.com/articles/07/contango_backwardation.asp

## Futures (Term) Structure

Term structure refers to the relationship between future prices for different maturity dates. This reflects 
market expectations of future demand, supply and storage cost. By analizing this traders can understand poterntial returns,
risk and make informed decisions.

For example, if we want to hedge against rising prices (hedging as a consumer) we might buy long-term contracts when the market is in contango. In backwardation instead 
we might want to buy short-term contracts. Traders indeed can anticipate future structures by studying supply/demand mechanisms.
If demand rises we expect growing prices, leading to a contango. The opposite occurs with increasing supply. 

### Term Structures Effect

Contango and backwardation arise as a result of inequality between the long and short positions of hedgers, which requires the 
intervention of speculators to restore the equilibrium (Keynes 1930 and Cootner 1960). Shwayder and James in *Returns to the Commodity Carry Trade*
show a strategy where investors long backwardated contracts and short contangoes [to read!].
The idea is simple, if the supply by short hedgers exceeds the demand by long hedgers (hedgers are net short), then the future price will be 
downward biased.

Term-structure strategies have interesting properties such as: (1) low max drawdowns; (2) high max run-ups and (3) both lower minimum and 
higher maximum 12-months rolling return than the benchmark; (4) higher sortino ratio than the benchmark (passive); (5) ups and downs of the strategy and of the benchmark (
S&P GSCI) are non correlated to the S&P500.

Erb and Harvey in *The Tactical and Strategic Value of Commodity Futures* state that: (1) the average annualized excess return of commodity futures is around 0; (2)
commodity futures returns are uncorrelated with one another. Similar properties are highlighted by Durr and Voegeli in *Structural Properties of Commodity Futures Term Structures and Their Implications for Basic Trading Strategies*.

### Roll Yield

The roll yield is the *return generated by rolling a short-term contract into a longer-term one*. This is the profits we can get from the convergence 
of the futures toward a higher spot/cash price. The roll yield, hence is positive in backwardation (with inverted curve - it can rarely happen backwardation and normal curve)

| Case # | Market Type           | Curve Shape     | Example Price Path                 | Roll Yield (long futures)                                                                |
| ------ | --------------------- | --------------- | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| 1      | Backwardation | likely Inverted (down) | Spot = 100, 1M F = 95, 2M F = 90   | **Positive**: futures rise toward spot as they mature                                    |

| 2      | Contango       | likely Normal (up)     | Spot = 100, 1M F = 105, 2M F = 110 | **Negative**: futures fall toward spot as they mature                                    |

Now there is a subtle difference between backwardation/inverted curve and contango/normal curve. Backwardation means that the front-month price is higher than long-term prices, while inverted curve means that spot > front > mid > long. So inverted --> backwardation but the opposite is not ncessarily true.

$$
\text{Roll Yield} = \Delta F - \Delta S = (F_{t+1} - F_t) - (S_{t+1} - S_t)
$$

### Inverted Markets

The most common reason of an inverted market are short-term disruption of supply. For crude oil, for example, OPEC policies restricting exports or, generally speaking,
whichever events reduces the supply (e.g. Russia-Ukraine conflict). For agricultural commodities, indeed, examples might be weather issues.

Normal curves are due to the cost of carry (storage, interest and insurance). They also include the opportunity cost as having money tied up in the commodity. A market is said to be in full carry when 
the future price is exacly equal to the cost of carry plus the spot price.

Let's have an example. Since 2020 some futures have been consistently inverted. Have a look at the BRENT between 2023 and 2024.

![image](https://github.com/user-attachments/assets/f2b62f90-35a9-44b1-ba1e-b2806efa0b56)


links...

- https://www.investopedia.com/terms/r/roll-yield.asp
- https://quantpedia.com/strategies/term-structure-effect-in-commodities
- https://www.investopedia.com/terms/i/invertedmarket.asp


## Options


### What is an Option?

An option on a futures is the right (not the obbligation) to buy/sell the underlying futures at a pretedermined price on or before a given date.

The right to exercise the option has a price, called the price premium. Think about it as the cost of having the right to do something, quite similar to an insurance.

Option buyers pay the premium to the seller, who gets the premium but also bears the risk of price movements. You can see that options can be used like: (1) insurance policies to limit losses; (2) speculative contracts as you can sell options to receive a premium; (3) hedging instruments by offsetting gains in face of adverse price actions.

### Contract Details

The most important details are:

- Underlying: which can be a futures, interest rates, ...
- Expiration/Maturity date: this is the last day on which an option can be exercised into teh underlying
- Strike price: the agreed price at which the transaction will (if) occur.
- Type: we can have a call option (right to buy at the strike price) or a put option (right to sell at the strike price)

### Options on Futures

Very few new futures contracts are listed on major exchanges without an associated option contract. Hedgers and speculators alike spend a great deal of time examining price behavior unique to each underlying futures contract. Historic price data along with other statistics, such as open interest, volatility, delta, etc., are useful in choosing the strike price and time frame for an option contract.

Both futures and options on futures are called derivatives because they “derive” their value from something other than themselves. An option on a future is no different in this regard, but the underlier is another derivative.

Option contracts span a variety of asset classes, including Interest Rates, Equity Indexes, Foreign Exchange, and physical commodities. In each case, the underlying contract influences the value of the option: the strike range, the premium, and the timing for each option. Doing your homework on the underlying futures contract, may help you identify opportunities in the associated options contracts.

### Strike Price

When picking an option you can choose froma a range of strike prices set by the exchange which are dynamically updated depending on the movements of the underlying, and withing certain products the strike changes depending on the expiration. For example, options on corn futures have an interval of 0.05 USD for the two front months and then of 0.1 USD intervals for contracts of three months or more.

Generally, the full range of strik prices is determined by the previous day's daily settlement price for the underlying futures. Granularity of possibile strike prices can increase due to large market movements of proximity to expiration.

### Expiration (Maturity) Date

Options are tied to the underlying, thus if the futures expires clearly also the option does. 

When it comes to options on futures, there may be a variety of option expiration dates for the same futures contract.

Some option expirations align with the expiration of the underlying futures contract. In other cases a futures product could have a variety of shorter term options listed. These shorter term options offer traders greater precision and flexibility to expand their trading strategies.

Let's see some examples considering options on the ES futures.

- Quarterly options contracts are offered on the E-mini S&P 500 futures contract. In this case the June quarterly option contract would expire at the same time as the futures contract.

<img width="720" height="405" alt="image" src="https://github.com/user-attachments/assets/dda599fe-646a-478e-b4f7-a21236f7b1b9" />

- Monthly contracts are also offered for the same futures product. With a monthly option contract you can express a short term opinion on this longer dated futures contract. For each listed month, such as May and April, you can trade an option that will expire within a month and settles into the same June ES futures contract. 

<img width="720" height="405" alt="image" src="https://github.com/user-attachments/assets/9a0c75cf-c246-4ac3-ac92-f5c2bde22855" />

- There are also weekly options on the E-mini S&P 500 futures contract. A rolling list of five weekly options that expire each Friday is offered on most products. After each weekly front-end contract expires, another back-end weekly is listed. 

<img width="720" height="405" alt="image" src="https://github.com/user-attachments/assets/b25c4ee2-f34e-4c95-9825-c0dc4aeb4404" />


For physically-delivered commodities, option expirations will expire prior to the futures settlement. This happens so that traders have an opportunity to mitigate delivery of the physical product. For example, when WTI Crude Oil futures settle in June, the WTI option will have a May expiration date. If the option is exercised into the active futures contract, the trader has time to adjust their futures position to either offset the position or make plans to take delivery.

### Call Options

A call option is the right to buy the underlying futures contract at a certain price.

#### Buying (Long) Calls

When prices move upward the call owner can exercise the option to buy the future at the original strike price. This is why the call will have the same profit potential as the underlying futures contract. However, when prices move down you are not obligated to buy the future at the strike price.

<img width="880" height="518" alt="image" src="https://github.com/user-attachments/assets/438470bf-b54f-47af-bef5-0fd7460f9f0a" />

The potential to profit on a call option comes with a cost. The seller or “writer” of the option will require compensation (similarly to an insurance policy premium) called the option premium. The buyer of a call option pays a premium to the seller of a call option.

As a result of the premium, the profit potential for a call is less than the profit potential of a futures contract by the amount of premium paid. The price of the future must rise enough to cover the original premium for the trade to be profitable. Moreover, options premiums are impacted by time decay and changes in volatility (futures are not).

The breakeven point for a call is the strike price plus the premium paid. So if you paid 4.50 points for a 100 call option, the breakeven is 104.50. The most you could lose is the premium or 4.50 points.

<img width="855" height="452" alt="image" src="https://github.com/user-attachments/assets/a820855c-790a-43cf-9ff8-4ae9255284dc" />

#### Selling (Short) Calls

For every long call buyer, there is a corresponding call option “writer” or seller. If you sell the call option, then you receive the premium in return for the accepting the risk. Option sellers have unlimited risk if the futures price continues to rise. Call sellers will profit as long as the futures price does not increase beyond the value of the premium received from the buyer.

The breakeven point is exactly the same for the call seller as it is for the call buyer

<img width="856" height="387" alt="image" src="https://github.com/user-attachments/assets/f3e904f2-5265-49f3-88f8-5dd74117f472" />

### Put Options

A put option is the right to sell the underlying futures contract at a certain price.

#### Buying (Long) Puts

A put option has a similar profit potential to a short future. When prices move downward the put owner can exercise the option to sell the futures contract at the original strike price. However, when prices move up you are not obligated to sell the future at the strike price.  

<img width="752" height="371" alt="image" src="https://github.com/user-attachments/assets/0d448447-be24-4ab3-b517-ba43197bc701" />

The potential to profit on a put option does come with a cost. The seller of the option will require a compensation under the form of a premium. The buyer of a put pays a premium to the seller of a put option.

As a result of the premium, the profit potential for a put is less than the profit potential of a futures contract by the amount of premium paid. The price of the futures contract must fall enough to cover the original premium for the trade to be profitable. The breakeven point for a put is where the profit on the futures contract that you can purchase at the strike price is equal to the premium paid for the call.

<img width="742" height="397" alt="image" src="https://github.com/user-attachments/assets/79e2869d-481b-4141-946a-faff0849ec0e" />

#### Selling (Short) Puts

If you have written the put option, then you receive the premium in return for the accepting the risk that you may need to buy a futures contract at a higher price than the current market price for that future.

While Put option sellers don’t have unlimited risk, the risk of writing puts can still be very large. The most a put option seller can lose is the full strike price minus the premium received. If you sell a 100 put option, and the underlying future drops to 20. You will have an 80pt loss minus the premium you took in which will only offset a small portion of the loss.  

Put sellers will profit as long as the futures price does not fall beyond the value of the premium received subtracted from the strike price. For example, if you sell a 100 put strike and receive a premium of 6.00 pts. You will profit as long as the future is above 94 (strike minus the put premium).

The breakeven point is exactly the same for the put seller as it is for the put buyer.

<img width="788" height="345" alt="image" src="https://github.com/user-attachments/assets/97bce99d-f45f-4170-849c-93cbac9edcab" />

### AM/PM Expirations

Options expiring ad the close of the market are PM and options expiring the morning of the last trading day are AM.

Most of the options expire PM, but there are exceptions. Options with AM expiration are generally written on a futture that has the same expiration date and time and this is typical of financially settled (cash) commodities.

In the case of S&P500 futures, the final settlement is determined by the opening prices of all the companies forming the index. The calcualtion is done by the administrator (Standard and Poor's), who provide a special opening quote (SOQ) indicating the final settlement price. PM options instead have a settlement price equal to the closing price of the underlying on the last trading day. For example, a long call is exercised if SOQ > Strike!

### Exercise and Assignment

Option buyers (owners - who is long) can exercise their option. In this case the sellers (writers - who is short) are assigned. What does it mean?

Owners of a long calls can exercise by "calling the underlying away" from the seller. While owners of long put can exercise by "putting the underlying back" to the seller. Summarizing, only buyers (long) have the right of exercise. 

Sellers, instead, are obliged to sell to you/buy from you the option at the strike price, regardless the current price. This obbligation is embedded in the premium they received to take the risk on, and the exchange/clearing house makes sure this obligation is respected by assigning.

<img width="858" height="560" alt="image" src="https://github.com/user-attachments/assets/65c5a161-bd6f-40f1-a2a2-c757af7e1ff0" />

### European and American Options

- American style options can be exercised at any time prior to expiration
- European style options can be can be exercised only at expiration

### Moneyness & Intrinsic Value

Moneyness indicates whether a contract is *in the money (ITM)*, *out of the money (OTM)* or *at the money (ATM)*. A call (put) is in the money if the price is bigger (smaller) than the strike.

When an option is ITM it is said to have instrisic value. Hence, if an options expires OTM we said that it expired worthless as it has not been exercised. The intrisinc value express the value of the option if it expired in this instant.

But what is the value of an option contract before expiration?

Option Value = Intrinsic Value + Time Value

Instrinsic value is the payoff if the option is exercised now, that is:

- Call option: $max(Spot Price - Strike Price, 0)$
- Put option: $max(Strike Price - Spot Price, 0)$ 

The time value (always positive) reflects the extra premium the option has because of the possibility of price movements. The time value gets to zero as the option approaches expiration.

Note that the time value decay is exponential and called $\theta = -dV/dt$. For American options there is no closed form for the decay as they can be exercised in any moment. For european one there is a complex formula:

<img width="537" height="135" alt="image" src="https://github.com/user-attachments/assets/a561e823-02bb-4092-8240-6ec2266d626b" />

<img width="637" height="585" alt="image" src="https://github.com/user-attachments/assets/3bcfb5ee-bc7d-460e-9c95-5f038b3cf947" />

<img width="692" height="372" alt="image" src="https://github.com/user-attachments/assets/a5462936-3def-469f-899b-d703cc3686d3" />

Note that N'(d1) is maximized at S = K (options at the money) because if ATM a small movement can make it profitable or not, that is why ATM options have a faster decay.

### PnL

Let's make an example for a call for both the perspective of the seller and the buyer (tables are self explanatory)

For the seller...

<img width="661" height="267" alt="image" src="https://github.com/user-attachments/assets/ae5724e5-7e08-4791-ac28-dce0618c1e7c" />

For the buyer...

<img width="645" height="260" alt="image" src="https://github.com/user-attachments/assets/eb0b6ad6-e028-46b9-b366-d3076581e4c6" />

### Options Pricing

Option pricing is based on the unknown future outcome for the underlying asset.
No one knows where the price will be, but we can draw some conclusions using pricing models.

When looking at call options, a higher strike will cost less than a lower strike.

To get an idea of how much the premium should be at each strike, we are going to use a simple model. Assume an asset is priced at $100 and has the characteristic of moving one dollar each month (either up or down). In this model, we will assume the price movement repeats every month over the life of the option and the option expiration will occur in four months.

What is the probability for each of the possible price outcomes after four months? In this model there are 16 possible paths that lead to each of the five price outcomes. The probability of each outcome can be calculated by aggregating the paths for each price. The probabaility is obtain dividing the numebr of paths that can lead to a price poitn by total number of paths.

<img width="735" height="465" alt="image" src="https://github.com/user-attachments/assets/4436f7c0-9a4e-45e2-ab7a-a0a1576ae8da" />

Now that we have the probability for each price point, we can start pricing options with different strike prices. First, you need to know the payoff for each strike price at the defined price level.

For a strice of 97 USD for example, a price point of 96 gives 0 payoff as it is OTM, 98 gives a payoff of 1, 100 of 3, and so on...

Then we multiply the payoff by the probability of occurence of a given price. Adn finf the price by summing up all those quantities. In this case the result is 3.0625.

<img width="807" height="282" alt="image" src="https://github.com/user-attachments/assets/cf754a37-f408-469a-ae6a-7fe65f1d4079" />

We can repeat the process for different strike prices. As you can see higher strikes are priced less as the probability of being ITM is less.

<img width="862" height="403" alt="image" src="https://github.com/user-attachments/assets/154618b2-d748-40bb-b6ee-724bd71c5bbb" />

### Option Volatility

Volatility is the "bounciness" of the underlying contract of the option. For option the time adjusted standard deviation is reported. Calculated as the volatility times the square root of the time period we are considering.

For example... 

<img width="877" height="363" alt="image" src="https://github.com/user-attachments/assets/fedffa77-9f89-4f69-bf4c-c1aa47acb168" />

### Put-Call Parity

The PCP states that Futures Price(F) - Call Price(C) + Put Price (P) - Strike Price(K) = 0. If this is not satisfied an arbitrage opportunity exists regardless of where the market closes

Let's see how...
P = 8 and C = 2, K = 105 and F = 100  --> 100 - 2 + 8 - 105 = +1 --> No PPC

We can short the put, long the call and short the futures.

1. At expiration F < K (say 104):
- We lose 104-100 on the short futures --> -4
- We lose 2 on the call (not exercised) --> -2
- We gain 8 on the put minus one to pay becuase the buyer exercises --> +7
- Net profit is +1

2. At expiration F > K (say 106):  
- We lose 106-100 on the short futures --> -6
- We paid 2 for the the call and get back 1 (exercised) --> -1
- We gain 8 on the put bacuse the buyer does not exercise --> +8
- Net profit is +1

## Rule-based Strategies

### Momentum Strategies

Concept: prices tend to continue in the same direction for some time --> Buy when prices are rising, sell when prices are falling.

Implementation with WTI daily returns:

- If 5-day moving average > 20-day moving average → long
- If 5-day moving average < 20-day moving average → short

Works well in trending markets, e.g., during strong geopolitical shocks or seasonal demand shifts.

- Pros: Captures trends, simple to code.
- Cons: Fails in choppy, sideways markets.

### Mean Reversion Strategies

Concept: prices tend to revert to a historical mean or fair value over time --> Buy when price < mean, sell when price > mean.

Applications in commodities:

1. Spot vs Futures 

Example --> if spot is cheap relative to rolling futures --> long spot / short future
 
2. Inventory-based signals

Example --> if high inventory prices expected to revert downward --> long spot

- Pros: Works in range-bound markets.
- Cons: Risky in strong trending markets.

### Spread Arbitrage (Relative Value / Calendar Spreads)

Concept: trade price differences between related contracts or commodities rather than outright prices.

Common types:

- Calendar Spreads: Front-month vs back-month futures (WTI Oct vs Dec)
- Crack Spreads: Crude vs refined products (3:2:1 gasoline/distillate spread)
- Inter-commodity spreads: WTI vs Brent, gasoline vs diesel

Example --> Crack Spread Changes/Expecations

Suppose a 3:2:1 scenario where we expect a rising demand for gasoline (at constant supply) --> increase in price of oil and derivatives

- Current prices of [90,110,120] for [crude,distillate,gasoline] --> current spread (120x2+110x1-90x3)/3 = 26.7 USD/bbl
- Expected future prices [91,112,125] for [crude,distillate,gasoline] --> current spread (125x2+112x1-91x3)/3 = 29.7 USD/bbl

Operationally?
 - long 2 RBOB gasoline futures and 1 ULSD distillate future
 - short 3 WTI crude futures

 Profit? --> 29.7-26.7 = 3 USD/bbl

 Explanation? --> product prices increased faster than crude --> increased crack spread window --> syntehtic spread position
