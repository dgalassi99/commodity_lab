# CME Education Related Projects

This folder contains small hands-on projects and experiments inspired by my theoretical study of futures, options and commodity markets primarily based on CME Group educational materials. This lectures are very interesting but it is always great to mix in some hands-on action!

The goal is to solidify concepts such as:
- Futures pricing and term structures
- Contango and backwardation in commodity markets
- Roll yield and strategies around contract rollover
- Basic hedging mechanics using futures
- Options on futures payoffs and strategies (later)

## Folder structure
- README.md (this file): contains motivation and structure of the folder
- data/
    CSV or other files with market data 
- **term_structure.ipynb:** Downloads futures data across different maturities (e.g. CL1, CL2, CL3 for crude oil) and visualizes the term structure of futures prices. Analyzes contango vs backwardation.
- **roll_yield.ipynb**  
  Calculates roll yield between consecutive futures contracts, exploring how rolling positions forward impacts returns.
- **hedging_example.py**  
  Simulates a simple producer or consumer hedge using futures contracts, showing outcomes under different spot price scenarios.
