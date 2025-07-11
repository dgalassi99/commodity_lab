# Introduction to Options

### What is an Option?

An option on a futures is the right (not the obbligation) to buy/sell the underlying futures at a pretedermined price on or before a given date.

The right to exercise the option has a price, called the price premium. Think about it as the cost of having the right to do something, quite similar to an insurance.

Option buyers pay teh premium to the seller, who gets the premium but also beras the risk of price movements. You can see that options can be used like: (1) insurance policies to limit losses; (2) speculative contracts as you can sell options to receive a premium; (3) hedging instruments bu offsetting gains in face of adverse price actions.

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

When picking an option you can choose froma a range of strike prices set by the exchange which are dynamically updated depending on the movements of the undrlying, and withing certain products the strike changes depending on the expiration. For example, options on corn futures have an interval of 0.05 USD for the two front months and then of 0.1 USD intervals for contracts of three months or more.

Generally, the full range of strik prices is determined by the previous day's daily settlement price for the underlying futures. Granularity of possibile strike prices can increae due to large market movements of proximity to expiration.

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

<img width="720" height="405" alt="image" src="https://github.com/user-attachments/assets/19da1091-cadb-4e1c-9862-dc752dc60f5a" />

The potential to profit on a call option comes with a cost. The seller or “writer” of the option will require compensation (similarly to an insurance policy premium) called the option premium. The buyer of a call option pays a premium to the seller of a call option.

As a result of the premium, the profit potential for a call is less than the profit potential of a futures contract by the amount of premium paid. The price of the future must rise enough to cover the original premium for the trade to be profitable. Moreover, options premiums are impacted by time decay and  changes in volatility (futures are not).

The breakeven point for a call is the strike price plus the premium paid. So if you paid 4.50 points for a 100 call option, the breakeven is 104.50. The most you could lose is the premium or 4.50 points.

<img width="855" height="452" alt="image" src="https://github.com/user-attachments/assets/a820855c-790a-43cf-9ff8-4ae9255284dc" />

#### Selling (Short) Calls

For every long call buyer, there is a corresponding call option “writer” or seller. If you sell the call option, then you receive the premium in return for the accepting the risk. Option sellers have unlimited risk if the futures price continues to rise. Call sellers will profit as long as the futures price does not increase beyond the value of the premium received from the buyer.

The breakeven point is exactly the same for the call seller as it is for the call buyer

<img width="856" height="387" alt="image" src="https://github.com/user-attachments/assets/f3e904f2-5265-49f3-88f8-5dd74117f472" />

### Put Options

<img width="752" height="371" alt="image" src="https://github.com/user-attachments/assets/0d448447-be24-4ab3-b517-ba43197bc701" />

