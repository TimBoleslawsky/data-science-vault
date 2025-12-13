Simulation, in a statistical context, means generating artificial (fabricated) data and treating it as real to perform analysis. But why do this?
- **Verification**: Used to check theoretical calculations and testing different experimental setups. For example testing the model assumptions used. 
- **Power analysis**: Helps determine the required sample size.
	- Generate data, run multiple studies with this data, aggregate power calculation.
- **Efficiency**: Saves time compared to analytical derivations.

How simulation can be used in praxis, can be seen here: [Simulation and Survival Analysis](../Projects/Survival%20Analysis/Simulation%20and%20Survival%20Analysis.pdf)
## Generating Synthetic Data
To generate synthetic data, we use a random number generator. But these random number generators usually create uniformly distributed random numbers and we usually need numbers from a variety of distributions. Therefore we use [inverse transform sampling](Sampling.md#inverse-transform-sampling). 

