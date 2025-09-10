# Refinery: Main Processes

Notes from "Petroleum Refining" by W.L. Leffler + Some insights of a chemical engineer!

The refinery is a very complex system of separation, reacting and mixing units. The main goal of a refinery system is, of course, the profit maximization. Technicalities, tho, play a crucial role. Understanding how the different "organs" of the refinery communicate and exchange fluids/streams is a prerequisiste to understand oil supply.

Ah, almost forgot, you can visit this board where a general schema of all the units I describe here is shown --> https://miro.com/app/board/uXjVJLgIsSU=/

## Before getting to the refinery

### How oil formes

In writing this document, I would like to take the perpective of the crude itself. What do I mean by this? I mean that I will describe the units and the process as if I am a little molecule dispersed in the complex crude system, who, being part ogf this moving fluid will follow different tratments and see the units one by one.

Before getting to the refinery (this part is not described in the book but I think is as important as the refinery system itself) the crude is pre-treated.

Crude is nothing than organic complex material that went through (veeeeeery) slow cracking and isomeriation reactions in the underground (we will see some of those reactions later...). Organic material is mostly made of C, H, O, S (hope you know which atoms we are talking about), those atoms form complex molecular structures that are the precursors of the black gold.

Organic material cumulates in the underground, and, if we are lucky gets trapped there in between non permeable rocks (oil reservoirs). Now, organic molecules are big, long, complex molecules that undergo mostly cracking reactions. 

What?

Well cracking has to be literally interpret. Those molecules are broken down to simpler, lighter and more linear ones. Cracking occurs in the underground due to high pressure environments and some geological heat that favors the thermodynamic of those reactions. Now, we need not to get too much into those mechanism, but here is what you need to know:

- the older the reservoir the longer the time span during which moleculues are cracked --> there will be ligher (smaller) molecules in the crude composition
- the light molecules (butane, propane, ethane, methane ...) are vapors in normal condition 
- water is also formed during those reactions

So how does a reservoir look like? Imagine it as a undeground hole with an unpermeable rock layer (dome) that traps the fluids from rising. Now this dome is full of fluids that stratify due to density differences and immiscibility. To say it simple, take an old jar and fill 1/3 of it with water, then fill another 1/3 of it with cooking oil, finally take the cork and close it. 

This simple sistem has three different phases (chemically speaking phases). There will be air on top, than a layer of oil and finally a layer of water. This si because teh air density < oil density < water density and because oil and water are immiscible liquids. Well an oil dome looks like this (other than air is replaced with hydrocarburic vapors).

### Extracting oil

Great, now we have an idea of what an oil reservoir looks like. Now, we are interesting in extracting the oil and the vapors while keeping the water there. Unfortunately, this is not fully possible and some water will come out dispersed in the oil phase (we have little water droplets like when you make mayonnaise). I will not go into the extraction details but here are some key bullet points:

- Vapors are either extracted first as they come out naturally and than we pump out the oil or we use the pressure of teh vapor to favor the oil extraction and then extract the vapors
- During the extraction water content will increase as we keep extracting (the bottom of the dome is rich in water) and the extraction process will stop when the water content reaches a given threshold (the cost of water removal is too high and the future processes become unprofitable)
- Even with care, water, salts, sulphur and other impurities will  be present in the crude. In loco treatments are necessary such as:
    - Decantation to remove most of the water and solid particles
    - Electrical desalting (coagulation of water and removal by application of an electric field)

Et voila, more or less now the oil is ready to be shipped to a refinery!

## Distilling

Distillation (or fractioning) is the first and the only non-chemicalish step that occurs in the refinery. Imagine the distilltion column as a splitting point. Here the components of the crude are separatated into several main actors.

The separation occurs by leveraging the wide spectrum of volatilities (boiling points or vapor pressurese... whichever concept is easier for you) of the oil species. Large and tall trayed columns are used for this operation. Now, as much as would like to get into the concepts of transport phenomena, I prefer to keep it as non-technical as possible. So here is a brief explanation.

Imagine the column as a sky scraper, by going up, at each floor, you feel colder and colder. What is happening is that a thermal gradient/profile is present along the vertical axis. Each chemical species into the crude mixture is characterized by a different boiling point, hence a molecule that is liquid at the seventh floor is maybe vapor at the third one. 

By extracting several streams (cut points) along this height we obtain streams of different compositions. Those streams contain lighter products as we go up along the height. Simply speaking we will extract the followings strams (top-down order here):
- Butane and lighter
- Straight run gasoline (SRG)
- Naphta (NP)
- Kerosene (KS)
- Light gas oil (LGO)
- Heavy gas oil (HGO)
- Straight run residue (SRR)

Seems easy no? Well some issues occur. Those streams are mixture of compounds so their boiling points are not unique (if you boil water, a pure species, it will evaporate at 100 °C). There are indeed an initial and an end boiling points (IBP, EBP). The IBP of an heavier stream (say HGO) overlaps with the EBP of a lighter one (say LGO), hence by changing a bit the cut point we can shift the production volumes (an the composition of the involved streams as a consequence). Those cut points operations are used to be flexible and adjust the supply of different raw products as the demand mutates.

## Vacuum Flashing 

The main limitation of distilling crude is the maximum temperature we can reach befora cracking phenomena occur. As a result the SRR contains a super wide range of components that can't be veporized. What is the solution? Applying vacuum!

As we reduce the pressure, the boiling temperature of molecules drops. We can use this principle to desing the vacuum flasher (VF) unit. Simply speking we take a vacuum pump and connect it to a traiyed column. The SRR is fed into the column and by the same principles of fractioning we split the SRR into the flasher tops (light and heavy tops) and flasher bottoms. The tops are usually send to catalytic cracking to reduce teh average molecular size (we will see...) and the bottom is used as asphault or sent to units such as visbreaker, coker or thermal cracker.

## Refinery Gas Plants

During a lot of operations (distillation, cracking, ...) light streams (C4-) are formed and need to be managed. Where?

### Saturated Gas Plants

Saturated gas (only single C-H bonds) aka paraffines are treated in the sat gas plant. The separation occurs mostly by fractionating and absorption, but here, due to very similar volatilities between the species the separation is harder and sometimes requires cryogenic techniques (this is my current expertise, so its very hard for me not to get into details...). 

Now, imagine to be a little molecule of this gas stream... which unit will you encounter?
- The gas is compressed and sent to a phase separator buffer (compression increases the boiling T) where vapor species (ethane and ligher) and a liquid stream (propane and heavier) are splitted. 
- Now some C2- will be present int the C3+ liquid stream. This current is depressurized to vapor and sent to an absorption column (*) to selectively absorb the C3+ via a lean oil (eptane/octane solvent mixture). The solvent traps C3+ and does not interact with the C2- which exit from the top as vapors. The fat oil (lean oil after C3+ are captured) is sent to a stripping column where we remove the absorbed compounds and regenerate the solvent to send it back to the first column.
- The C3+ mixture (propane, n-butane, iso-butane) are separated by using the depropanizer (fractioning teh C3 on top and n/i-C4 at the bottom) and the deisobutanizer (fractioning i-C4 as the top and the n-C4 as the bottom). 
- Last but not least, during the absorption some of the lean oil gets out as vapor with the C2- --> wet gas. This wet gas goes into another absorption process where the dry teh C2- stream by absorbing the lean oil with an heavier solvent (sponge oil)...
 
Note: given a mixture of K species, we need K-1 distillation units to separate them all!

(*) An absorption unit is similar to a distillation column. Here, usually, we do not have trays but a packing material (random or structured) with a very high specific surface area (area/volume ratio) which favors the contact between the vapors we want to absorb and the solvent (the liquid that absorbs selectively). 

### Cracked Gas Plants

Light gases formed during reforming or cracking ops have a wider variety. Non saturated hydrocarbons such as olefins or some naphtenes are present. The CGP is similar to the SGP but more distillation units are needed are the number of species is higher.

## Catalytic Cracking 

As a result of the increasing demand for light products the need to crack heavy molecules to smaller ones became the standard. 

### CC Process 

HGO and flasher tops are cracked at high T, high P in catalytic reactors. I know... here is some context. Catalysts are chemical species that interfere (usually positively) with reactants speeding up specific reactions without reacting themselves. Two key things:

1. Speed up a reaction?

- A chemical reaction is nothing else than something occurring because an equilibrium has been broken. For example, changing temperature or pressure might shift an equilibrium and initialize a reaction (this is THERMODYNAMICS!). The speed of reaction, instead, has nothing to do with thermodynamic, but it is a matter of KINETIC. Imagine a species a chemical species as something that can potentially change status. Now, a nice methaphor is the following. Suppose you are lying on your sofa and you wonder to or not to go for a jogging. Usually, there is a "force" (like you wan to lose weight, or whatever the reaosn is) driving you to leave the confort of your sofa and get out. The hardest step is not, at least in the common opinion, is to stand up, change, and go out. Once you go over the "energetic barries" the jog is usually smooth and pleasent. The same occurs during a chemical reaction. Once we go over the energetic barries (Gibbs free energy of reaction) everything goes smooth.

2. I said "specific reactions"... why?

- Now, imagine there are thousands potential joggers in the same situation as you. Similarly thousands of parallel reactions can occur. What a catalyst does is to selectively promote some reactions by altering their kinetics. Imagine them as a personal trainers that selectively picks some potential joggers and motivates them to go out and with different intensities. The probability distribution of the joggers is not uniform anymore but is skewed. The same occurs with a catalyst. SO those alter the KINETIC of reactions by speeding up some and keeping other inaltered. So, even if thermodinamically speaking all molecules are potential joggers, some are so slow to get up that the other already finished the run. 

I hope this little metaphor made you understand the difference. Now, let's get back to hte CC unit. The goal is to maximixe th eproduction of gasoline by triggering cracking reactions up to a certain extent. Ofc, chem. engineering is a matter of probabilities and detrministic outcomes are quite unlikely. In other words, issues occurs...

- Since we start with a mixture of molecules of different sizes we will crack those into a spectra of lighter products. Some of those are non sat molecules such as olefines, cycloalkanes and aromatics.
- As cracking occurs, due to hydrogen deficiency, coke is formed. Coke is poisonous for the catalyst as it deposits on its surface "masking out" a lot of reactive area.
- Bigger molecules are likely to be cracked on side chains (weaker bonds). As a result the average density of the mixture increases (ironically to an higher density of the feed itslef)

How do we deal with it? Three stage process --> reactor, catalyst regenerator and fractionator

## Hydrogen, Hydrotreating and Sulphur Plants

### Hydrotreating

Any stream of C6+ will contain some sulphur even in sweet crudes. Moslty as a constituent of aromatic rings it has to be removed by hydrotreating. It consists in blending those streams with H2, chlorine and heat them up in a catalytic bed of Co-Mo-W. 

Basically, H2
- combines with S to form H2S
- reduces nitrogen compounds are NH4
- saturates olefins and aromatics into paraffines

Moreover Cl2 reacts with metals and form chlorides.

Simple config as heater, reactor and flash to exhaust H2 to be recycled and a stabilizer to split C4- and hydrotreated products. This step is key as:
- Removal of metals, S and N which can poison cats in cracking and reforming ops.
- Reduces S to meet environmental policies
- Increases the sat fraction of the crude

Hydrotreating also improves:
- the quality fo jet fuel as increasing the H/C ratio imbroves the combustion and reduces the smoke point (smoke due to non full oxidations to H2O and CO2). 
- it also promotes more sats which increase the CI of diesels
- protects reformers catalyst increasing the converions

On thhe other end:
- more sats less AKI in gasolines 

### Hydrogen Sources

Mostly produced during the car reforming but also via:
- SMR (Steam Methane Reformer) is an high T high P reactor to process CH4 + H20 -> CO + 3H2 ---> CO + H2O -> CO2 + H2 then CO2 removed by absorption
- Swing adsorption or cryogenic distillation of light stream separating H2

### Sulphur Facilities

Once formed, H2S must be removed as it oxidate to SOx during combustion reactions. The most common way is an absorption with methyl ammines (MEA, DEA, TEA) followed by a stripping unit to regenerate the solvent.

The H2S is further oxidated via the Claus process:
1. Combustion 2H2S + 2O2 -> SO2 + S + 2H2O

LINK TO BLOCK PROCESS DIAGRAM --> https://miro.com/app/board/uXjVJLgIsSU=/


## Isomerization 

### Isobutane

Refineries with hydrocrackers are likelyto have a surplus of iC4, but with a cat cracekr and an alky plant only it is hard to produce enough iC4 to match propylene and butylenes feeds. 

So two options:
- But some iC4
- Produce it via butane isomerization (BI plant)

The feed is mostly iC4-nC4. Normally we deisobutanize and feed the nC4 to a pt-catalyzed reactor. H2 is added to minimize coke formation, still we have by-products auch as C3-.
A stabiliezer separates the light components on top and recycles the iC4/nC4 back at the feed point (iC4 is extracted the the first deisobutanizer).

### C5/C6

If we want to increase the octane number (ON) we can isomerize C5 (ON from 62 to 95) and C6 (from 25 to 75).

Teb are iC5 < nC5 < iC6 < nC6.

The process is similar to C4 isomerization but more columns are needed for separation. That is we extract the isomerates and recycle the normal hydrocarbons back to the reactor feed.

## Residue Reduction

The main goal is to crack the vacuum flashing bottom (or straight run bottoms) to lighter components. 

We can use several units depending on:
- the capital we can invest in
- quality of the feed and prices od the products 
- coke quality production and value added by coking 

Generally:

- If feedstock quality is high (HGO and flasher tops) --> HC and FCC --> as yield in light products is high --> high value added
- If feed quality is low (stright run residue/ flasher bottoms) and capital is low --> coking, visbreaking and thermal cracking --> low light yield
- If feed quality is low (stright run residue/ flasher bottoms) and capital is high --> RHU and RFCC -->  decent yields 



### Thermal Cracking and Visbreaking (Low capital)

Feed mostly made of straight run bottom and/or flasher bottoms and/or cat HGO. Fed through a furnace at high P and low residence time (minimize coke formation).
The mixu=ture is quenched to stop the cracking process and a flash + fractionator follow. C4 and lighter go to gas plants or to alky plants. Gasoline and oil used as blends for gasoline and distillates.

### Coking (Medium Capital)

We can have three configs: delayed, fluid and flexi cokers. We focus on the first on being the most commonly used.

In the thermal crackinig we saw that increasing the space velocity (decreasing residence time) in the furnace pipes reduces coking. So the idea is to insert come drums and increase the residence time of the mixture there so force the coking formation to happen here (big drus where the removal is easier than inside heatEx pipes!).

The config is a fast pass in a furance to heat up and a "slow bbq cooking" in the coke drums. Vapors exit from the top and are separated via distillation. What is left behind are very heavy, low hydrogen compounds that are mostly coke.

To decoke the drums we use high pressure water jets. The coke left is similar to carbon but with some heavy hydrocarbons inside. If untreated is sold as green coke for combustion in cement klinks or blended with coal. If could be coked at very high T to remove leftover and have a sponge coke or needle coke. Those application in high temperature industries (electric arcs, welding machines...)

## Residue Cat/Hydro Cracking

### Residue Fluid Cat Cracking (RFCC)

The plant structure is similar but bigger risers (higher residence time) and bigger regeneration chambers (more coking) are designed. Also catalysts are engineered for the specific heavy feed.

### Residue Hydro Cracking (RHC)

Again scaled up wrt lighter feed plants. Usually the cat is a fludized bed with a strong hydrogen excess.

## Aromatics Recovery

Removal of aromatics is done due to:
1. Pollution
2. They are more valuable when not mixed with other hydrocarbons (Xilene, Benzene, Toluene)
3. Recude values of products (benzene in gasoline, smoke point in kerosene)

### Solvent Extraction for BTX

The solvent must be selective vs aromatics and have a different volatility to facilitate its regeneration via distillation. 

Let's use the BTX recovery as an example. Straight run gasoline or reformate are fed to a distillation unit where light compouns are extracted as distillates. The bottom rich in aromatics is feed in another column. Heavy aromatics exit from the bottom while the column head (rich in BTX) is sent to a solvent extraction unit. The solvent extracts BTX, and then is fractionated to recover the solvent and get the BTX. The raffinate stream is a de-aromatized gasoline cut that can be used in gasoline blending.

## Simple and Complex Refineries

### Measuring Profitability 

The essence of the structure around pricing and profitability is relative to the refineries ability to vary the production and to produce high value chemicals. 

Hence, the refinery structure/configuration allows several mods and production flexibility. There are three main kind of refinery:

- Simple (Hydroskimming) --> distillation + reforming + hydrotreating
- Complex --> as before + flasher + cracker + gas processing
- Very Complex --> as before + coker + visbreaker

Increasing complexity increases the ratio light to heavy products --> higher value products --> higher margins 

Let's do a calculation to compare. Suppose we have a simple and a complex refinery:

1. Production from 1 bbl of medium quality crude:

- --> Gain is the extra volume produced as we make ligher than feed avg. products

- Simple refinery: 0.3 gasoline, 0.1 jet fuel, 0.2 distillate fuel, 0.35 residual fuel, 0.08 refinery fuel --> gain 0.03 
- Complex refinery: 0.5 gasoline, 0.1 jet fuel, 0.25 distillate fuel, 0.1 residual fuel, 0.12 refinery fuel --> gain 0.1 

2. Margins

Assuming prices are: 90 USD/bbl gasoline, 85 USD/bbl jet fuel, 80 USD/bbl distillate fuel, 55 USD/bbl residual fuel, 0 USD/bbl refinery fuel, 65 USD/bbl crude
- Simple refinery revenues: 70.75 USD/bbl - 65 USD/bbl - 1 USD/bbl (other costs) = 4.75 USD/bbl
- Complex refinery revenues: 79 USD/bbl - 65 USD/bbl - 3 USD/bbl (other costs) = 11 USD/bbl

Notice: (1) complex refinery produce more light products; (2) ligher products sell at higher prices; (3) operating cost are higher for complex refineries; (4) overall revenues increases with complexity; (5) this delta/spread increase as the quality of the crude goes down.

Point (5) is key --> when crude quality is very low --> simple refineries do not have enough processing power to make it profitable --> can't take advantage of the light/heavy price differential (LHPD)

Now suppose refining margins today, for different crudes, are (LHPD ~ 7 USD/bbl):

- light crude --> simple 1 USD/bbl, complex 5 USD/bbl, very complex 10 USD/bbl
- medium crude --> simple -2 USD/bbl, complex 8 USD/bbl, very complex 13 USD/bbl
- light crude --> simple -1 USD/bbl, complex 4 USD/bbl, very complex 18 USD/bbl

You can notice that simple refineries can't exploit the LHPD and can only process light crude, simple refineries should push to improve their structure and increase complexity.
This results in:

- decrease LHPD as more refineris profit from heavy crudes --> price of heavy cruce increase more relatively to light one
- margins are reduces for all and sometimes simple can outperform the complex --> complex may want to be simplified and the cycle restarts...

What set prices?

We have to think and consider several points which are the usual demand supply equilibria... for example:
- Strong demand --> complex refinery fill up first as they can make valuable products from any feed. But if they are full product prices rise and also simple refineries are profitable even if feeding light crudes
- If cokers and crackers fill up (bottleneck) heavy crudes are less attractive than light ones and the LHPD increases 

This is an example, each case must be logically developed!
