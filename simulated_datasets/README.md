# Simulated Datasets for HexSplit Evaluation

## Overview

This repository contains simulated sequence datasets used to evaluate the performance of **HexSplit** under various evolutionary scenarios. All datasets were generated using **Seq-Gen** under the **GTR model** with gamma-distributed rates, and default settings for other parameters.

The datasets explore variations in PGT region properties, substitution rates, and region locations to assess algorithm robustness.

## Baseline Dataset

The baseline dataset consists of 100 gene families simulated with the following default parameters:

- PGT evolution rate: 0.4  
- Sequence length: 1000 nt  
- Substitution rates: 0.5 for both genic and PGT regions  
- PGT-region fraction: 40% appended to the end of the genic region  

This dataset serves as the reference for all parameter variation experiments.

---

## Parameter Variation Datasets

All other datasets were derived from the baseline by varying **one parameter at a time**:

1. PGT region length: 20%, 30%, 50%, 60% of the total alignment length.  
2. Equal substitution rates: Both genic and PGT regions evolved at identical rates of 0.1 and 5 substitutions per site per unit branch length.  
3. PGT region location: Three datasets with PGT regions shifted into the interior (offsets of 34, 84, and 134 bp).  
4. Multiple PGT regions: One dataset with two PGT regions:  
   - Genic region: 40%  
   - PGT 1 region: 40%  
   - PGT 2 region: 20%  
   Each region encodes distinct evolutionary histories.  
5. No Transfer: Control dataset with no PGT events.

## Additional Evolutionary Scenarios

To explore the effects of differing evolutionary rates between genic and PGT regions, we generated:

1. High genic-region evolution:  
  - 0.5 genic / 0.25 PGT  
  - 1 genic / 0.5 PGT  
  - 2 genic / 0.5 PGT  

2. High PGT-region evolution: 
  - 0.25 genic / 0.5 PGT  
  - 0.5 genic / 1 PGT  
  - 0.5 genic / 2 PGT  

## Dataset Summary

| Category | Number of Datasets | Notes |
|----------|-----------------|------|
| Baseline | 1 | Reference dataset |
| No Transfer | 1 | Control |
| PGT region length | 4 | 20%, 30%, 50%, 60% |
| Equal substitution rates | 2 | Rates = 0.1 and 5 |
| PGT region location | 3 | Offsets: 34, 84, 134 bp |
| Multiple PGT regions | 1 | Two PGT regions with 3 evolutionary histories |
| High genic-region evolution | 3 | Genic region evolves faster |
| High PGT-region evolution | 3 | PGT region evolves faster |
| **Total** | 18 | All datasets combined |

