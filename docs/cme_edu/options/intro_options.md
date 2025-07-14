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

<img width="880" height="518" alt="image" src="https://github.com/user-attachments/assets/438470bf-b54f-47af-bef5-0fd7460f9f0a" />

The potential to profit on a call option comes with a cost. The seller or “writer” of the option will require compensation (similarly to an insurance policy premium) called the option premium. The buyer of a call option pays a premium to the seller of a call option.

As a result of the premium, the profit potential for a call is less than the profit potential of a futures contract by the amount of premium paid. The price of the future must rise enough to cover the original premium for the trade to be profitable. Moreover, options premiums are impacted by time decay and  changes in volatility (futures are not).

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

While Put option sellers don’t have unlimited risk, the risk of writing puts can still be very large. The most a put option seller can lose is the full strike price minus the premium received.  If you sell a 100 put option, and the underlying future drops to 20.  You will have an 80pt loss minus the premium you took in which will only offset a small portion of the loss.  

Put sellers will profit as long as the futures price does not fall beyond the value of the premium received subtracted from the strike price. For example, if you sell a 100 put strike and receive a premium of 6.00 pts.  You will profit as long as the future is above 94 (strike minus the put premium).

The breakeven point is exactly the same for the put seller as it is for the put buyer.

<img width="788" height="345" alt="image" src="https://github.com/user-attachments/assets/97bce99d-f45f-4170-849c-93cbac9edcab" />

### AM/PM Expirations

Options expiring ad the close of the market are PM and options expiring the morning of the last trading day are AM.

Most of the options expire PM, but there are exceptions. Options with AM expiration are generally written on a futture that has the same expiration date and time and this is typical of financially settled (cash) commodities.

In the case of S&P500 futures, the final settlement is determined by the opening prices of all the companies forming the index. The calcualtion is done by the administrator (Standard and Poor's), who provide a special opening quote (SOQ) indicating the final settlement price. PM options instead have a settlement price equal to the closing price of the underlying on the last trading day. For example, a long call is exercised if SOQ > Strike!

### Exercise and Assignment

Option buyers (owners - who is long) can exercise their option. In this case the sellers (writers - who is short) are assigned. What does it mean?

Owners of a long calls can exercise by "calling the underlying away" from the seller. While owners of long put can exercise by "putting the underlying back" to the seller. Summarizing, only buyers (long) have the right of exercise. 

Sellers, instead, are obliged to sell to you/buy from you the option at the strike price, regardless thecurrent price. This obbligation is embedded in the premium tehy received to take the risk on, and the exchange/clearing house makes sure this obligation is respected by assigning.

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

Let's an example for a call for both the perspective of the seller and the buyer (tables are self explanatory)

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

### Options on Futures vs ETFs


