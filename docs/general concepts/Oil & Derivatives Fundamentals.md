# Oil and Derivatives: Fundamentals

## Basics: Brent vs WTI 

Crude oil is a mixture of hydrocarbons formed by decomposition of organic matter and used for the production of several products (gasoline, jet fuel, diesel...).
In global trading the most important benchmarks are:

- **Brent**: it is a **light** and **sweet** crude produced in the north sea and delivered via seaborn cargoes, so it reflects *global waterborne pricing*.
- **WTI**: it is **light** and **sweet** crude delivered inland because it is landlocked. Its price divergence with the brent reflects the situation of US pipelines, storage and logistics.

*The Brent-WTI spread* --> often reflects US infrastructure bottlenecks, freight economics and global supply/demand shifts

**Q&A**

- *What global waterborne pricing means?* --> waterborne crude is the oil that is moved via ships (tankers). Brent is FOB (free on board), which means that, once loaded, tankers are under the responsibility of the trader who cand ship it wherever is more conveninet  This means that we can decide where to buy and where to sell and maximize the profit. Which means that arbitrage is possible. For example, if Brent price at north terminals plus the cost of freight to Asia is smaller than Dubai crude price in Asia it is worth to pick the first option. Due to the no-free meal rule of market the price of Brent will adjust to close this arbitrage chance.
- *What seaborne cargoes are?* --> a cargo is a shipload of crude/products (typically between 0.5-2 mbbl) 
- *Why WTI is inland and mor regional?* --> historically US had export restrictions (till 2015), even after the opening WTI is largerly a domestic benchmark tied to US storage, pipelines and refining dyamics. In fact the crude must be piped frominland hub to the Gulf Coast before "floating into the market", this slows down the dynamics and recude the chances of arbitrage.
- *Some examples of Brent/WTI divergences?*
    - US infrastructure bottleneck --> During the "Cushing Glut" in 2011-2013 US shale surged but pipelines in the Gulf Coast were not ready. As a result the WTI price collapsed of 20 USD wrt Brent since barrels could not reach the export market
    - Freight Economics --> During the 2020 pandemic tanker freight rates exploded due to the necessity of floating storage (inland storage were already full and supply was constant while demand plunged). This made arbitrage (shipping WTI barrels to Europe/Asia) uneconomic because the freight cost exploded since most of the tankers were used for floating storage.
    - Global Shocks --> Due to the Ukraine-Russia conflict Russian oil lost access to EU markets pulling brent higher (supply shock) as refineries competed for Atlantic barrels. WTI initially lagged due to time required to redirect US exports to fill the gap

## Crude Quality and Metrics

The most important qualities are API Gravity, Sulphur content and other. All of these are measure in a free-condition, that is, after water has already been almost fully demoved by decantation and electrostatic dehydration.

1. **API gravity** 
Measures the inverse of oil density --> higher API --> lower density --> lighter crude --> higher contnet of low HC (yields more fuels) --> higher value

$$ API gravity = \fra{141.5}{specific gravity at 60°} -131.5 $$

$$ Specific gravity (T) = \frac{\rho_oil(T)}{\rho_water(T)} $$

Classification: Heavy (API < 22° such as Maya Mexico), Light (API > 31° such as Brent, WTI), Medium (API in between)  

2. **Sulphur Content**
Measure S %w, the crude is *sweet* if S < 0.5 %w (WTI, Brent), *sour* if S > 1 %w (Urals)

3. **Other Metrics**

- Pour point (solidification temperature) --> the lower the better (specially in cold regions)
- Viscosity --> the lower the better as in increase cost of pumping 
- Ni/Vn content --> the lower the better as it poisons catatalysts in refining processes 

## Arbitrage, Freight and Logistics

Arbitrage is the exploration of price differences between two markets for the sma eor similar commodity. We can have

- Spatial arbitrage --> ex. WAF (West African) or USGC (US Gulf Coast) oils to EU --> depends on FOB price, freight cost, port logistics and timing
- Calendar arbitrage --> ex. Brent front-month or n-th-month --> depends on futures curves (contango/backwardation)
- Quality/Crack Spread arbitrage --> ex. Brent (light and sweet) or Urals (heavy and sour) --> refineris profit max. problem 

Freight cost is an important factor in the arbitrage equation is it embeds the cost per barrel from load port to destination. We can calculate the landed cost as:

$$ Landed Cost = FOB Price + Freight + Insurance+ Demurrage + (Storage) $$

- FOB price: price at which the product is bought --> seller responsability ends here
- Freight: cost of shipping which depends on tanker type --> dirty tankers cheaper (for crude), clean tankers more expenisive (distilled/refined products)
- Insurance: covers risk of issues (0.5-1% of the cargo value)
- Demurrage: penalties for delays to/from destination/leaving port 
- Storage: if barrels are stored at terminals there are tank lease costs, handling (pumping/monitoring) costs and optional insurance on storing itself 

## Refining Margins 

It is the profit refineries make from processing crude into refined products. Roughly:

$$ Refining Margins = Final Producs Value - Cost of Crude - Cost of Processing $$

In this equation the final products yiels is the cumulative product between the final product price and the yield: $\sum_i{Price_i * Yield_i}$. Commercially speaking margins vary depending on crude types and on the current status of the market. For example:
- Light and sweet crude --> higher gasoline yield --> higher margins when gasoline price is strong
- Heavy and sour crude --> higher fuel oil/jet fuel yield --> higher margins when those products are selling high

Another really importnat concept to understand how refineries move is the **Crack Spread**, which is nothing than a simplified figure for margins. It measures
the value of refined products vs crude input. For example, a 3:2:1 crack spread means that from 3 bbl of crude we make 2 bbl of gasoline and 1 bbl of distillate. 

| Product          | Price ($/bbl)  | Yield | Contribution ($/bbl crude)  |
| ---------------- | -------------- | ----- | --------------------------- |
| Gasoline         | 120            | 2     | (120x2)/3 80                |
| Diesel           | 110            | 1     | (110x1)/3 = 36.7            |
| **Sum**          | —              | —     | 116.7                       |
| Crude Brent      | 90             | —     | —                           |
| **Crack Spread** | —              | —     | 116.7 − 90 = 26.7           |


Note: 
- "Distillate" (engineerly speaking wrong term ...) includes jet fuel, diesel and fuel oil (mid column products)
- C1-C4 are not in the metric as NG, LNG and LPG are sold in another market and moves mostly by pipelines


*How do refineries decide runs?*

There are several factors...

1. **Crack Spreads**

Depending on the spread they move towards the product to be maximized. For example:
- Summer --> high demand for gasoline so price goes up --> refineries increase gasoline production
- Winter --> high demand for heating (diesel, fuel oils) --> refineries shift towards distillates

Note that this is always a constrained opmization problem depending on starting crude quality, refinery configuration, catalytic yields...

Traders monitor closely crack spreads to forecast refinery activities and leverage possible physical aribitrage flows

2. **Refinery Configuration**

The technical development of a refinery makes it more flexible and less bounded to market volatility/seasonal cycles.

- Simple/Hydroskimming refineries -->base units: Atmospheric Distillation + HydroDesulphurization (HDS) + Reforming (SM) --> mostly treat light crude
- Complex refineries --> adding complex units: Decoking + Hydrocracking(HC)/Fluid Catalytic Cracking (FCC) --> can also treat heavy oils

Note for engineers:
- Hydrogenation (HDS) --> catalytic hydrogenation  of thiols R-H + H2 -> R + H2S --> follows H2S removal by absorption with MEA/DEA
- Reforming (CR) --> isomerization and aromatization of paraffines to increase octane number --> H2 byproduct used in HDS
- Delayed Coking (DC) --> convert heavy residues into lighter ones and petroleum coke
- Cracking (FCC) --> crack long chain into ligher products --> if catalytic FCC less coke deposits and higher gasoline/olefines/LPG

3. **Inventory Levels & Seasonal Demand **

Increase/Decrease production (supply) when storage is empty/full or demand is high/low 
