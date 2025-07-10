# Commodity Market Basics

## What is a Commodity?
*Tradable raw materials that can be used as inputs in the prodcution of other goods/services*

So those are basic resources interchangable with other goods of the same type. The quality might change but it needs to meet minimum standards: basis grade (e.g. for oil is the content of hydrogen and sulphur). 
Commodities are usually exchanged via futures contract on exchanges that standardie the quantity and the minimum 
quality of the goods.

The fact that commodities are produced/sold by many firms and are uniform in quality gives them a key feature: *fungibility*.
For example, diamonds vary too much in quality and in volumes so are not commodities (differently from oil)

There are two types of commodity traders:(1) consumers/producers who buy/sell futures to hedge against price changes; 
(2) speculators who try to profit from price actions/movements and never intend to take the actual delivery when the future contract expires 

Generally speaking, commodity prices increase with inflation as they offer a protection agais purchasing power loss. Tho prices are determined by supply/demand mechanism such as booms, economic shocks and so on.

We can split them into hard commodities (minerals, ores and oil/gas) and soft commodities (wheat, cotton sugar, coffee)

links...

- https://www.investopedia.com/terms/c/commodity.asp
- https://www.thoughtco.com/commodity-economics-definition-1146936
## Spot vs Futures Prices

*Why commodities have two prices?*

Spot and futures prices are quotes for a contrac agreed by the two parties. What makes them different is the 
timing of the transaction and the delivery date of the commodity (immediate vs in the future).

The use of futures is needed to lock the price in adavance. Future's prices are based on spot prices plut the *cost of carry* (cost of storage, interest and insurance on it).
So the future price (F) is the sum of spot price (S) and storage cost (C) times the exponential of the product between time to maturity (t) and the difference between risk free (r) and convenience yield (y) rate.

$F = (S + C) e^{(r-y)t}$ or sometimes $F = S e^{(c+r-y)t}$

Note: y acts a s a negative cost, so F < S when y > (r+c). The convenience yield takes into account expectations of supply and demand.

A key concept is the *basis*. The *difference between local spot price and the price of teh earliest available future*. The basis can vary regionally as the transportation costs are different (local term is key in the definition)
Assume the spot price for oil is 54 USD/barrel and the future one is 50 USD/barrel. The basis is 4 USD/barrel and is crucial... why?

- It affects the value of the contract used in hedging
- It is used by traders do choose the best time to buy/sell (if it is strenghtening/weakening)
- It is not accurate, there are gap prices and quality difference: the *basis is an imperfect indicator*

links...

- https://www.investopedia.com/ask/answers/062315/how-are-commodity-spot-prices-different-futures-prices.asp

## Contango and Backwardation

They refer to the patter on contract prices overtime. 

**Contango:** future price above the expected spot price (confused with a normal curve)

**Backwardation:** future price below the expected spot price (confused with an inverted curve)

A future curve is **normal** if future prices are higher at longer maturities, **inverted** in the opposite case.

Let's take a curve future prices vs maturity (similarly to interest rates). 
![image](https://github.com/user-attachments/assets/ed964439-b816-4287-9351-28de9627ca21)

Why a curve should be inverted? Because market participants (taking into account the cost of carry) update continously their
views about the future expected spot price. For example, a traditional oil curve is nromal in the short term and inverted in the long one.

Let's focus on two ideas: (1) as we approach maturity the future price approaches the spot one (no arbitrage); 
(2) the most rational future price is the expected futurre spot price.

Now we can *redefine* contanco and backwardation. Suppose we entered in a 12/23 futures contract today at 100 USD. Now, one month from today,
the same contract could be 100 USD, 110 USD (normal backwardation) or 90 USD (contango).

**Contango:** future price above the expected spot price. Because converge must occurr, contango
implies that future prices are falling over time. 

**Backwardation:** future price below the expected spot price. Because converge must occurr, backwardation
implies that future prices are increasing over time. 

Consider we purchase today a future contract due in one year (spot at 60 USD). If today's future price is 
90 USD we are in a contango scenario. Unless the spot price changes the contract price must drop.
![image](https://github.com/user-attachments/assets/614e1951-5ac5-4db2-a7c6-bd6955f44c53)

Note:

- Markets evolve, so if for example a spully shock causes a shortage in a commodity, the spot price will
increase and we can shift from a contango to a backwardation market
- You can determine the situation by plotting the future price with the expected spot price

links...

- https://www.investopedia.com/articles/07/contango_backwardation.asp
