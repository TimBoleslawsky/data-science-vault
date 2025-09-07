In general we have three approaches when choosing how to handle missing values: 
1. **Imputation** – Filling in missing values using statistical or machine learning methods (e.g., mean, median, KNN imputation, predictive models).
2. **Informative Missingness** – Treating missingness as meaningful by creating a separate category or indicator variable (e.g., “missing” as a feature).
3. **Deletion (Dropping Records)** – Removing rows or columns with missing values if the dataset is large enough or if the missing values are random and not too frequent.
## Imputation
**Simple Imputation**
One possible approach here would be **simple imputation**. Simple imputation could for example be: 
- Heuristically setting a reasonable value, so just guessing as best as possible.
- Setting the value to mean which preserves the mean (but this can be inappropriate if the reason for a value missing is systematic). 
- Setting the value to a random value in the same column; this can also preserve statistical properties, but one needs to be sure that this does not have unintended side effects.  
- Setting the value to match that of the nearest neighbor, but this requires a reasonable metric for determining the nearest neighbor.  
- Interpolating the missing value using a simple model, like linear regression.

**Multiple Imputation by Chained Equations (MICE)**
The idea behind MICE is to generate **several possible values** for each missing entry, creating multiple datasets. Then a model is trained on each dataset, and results are combined for a more robust estimate.
## Informative Missingness
Imputation methods may fail when data is not missing at random (MAR), meaning missing values can not be reliably imputed. 
A common method is to assign a simple imputation, for example 0, and take this imputation together with the missingness mask 𝑀, as binary indicators, for prediction.
