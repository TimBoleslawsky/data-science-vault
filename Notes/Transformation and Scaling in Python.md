Here is an example, of how to transform, standardize and normalize data using Python: 

``` Python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import zscore

# Generate exponentially distributed data
np.random.seed(42)
data = expon.rvs(scale=1, size=1000)  # Exponential distribution with lambda=1

# Apply log transformation
log_transformed_data = np.log(data)

# Standardize the log-transformed data using z-score
standardized_data = zscore(log_transformed_data)

# Normalize the data
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(log_transformed_data.reshape(-1, 1)).flatten()  # Reshaping data for the scaler

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 7))

# Original Data
axs[0, 0].hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
axs[0, 0].set_title('Original Exponential Data')
axs[0, 0].set_xlabel('Value')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].grid(alpha=0.3)

# Log-Transformed Data
axs[0, 1].hist(log_transformed_data, bins=30, color='salmon', edgecolor='black', alpha=0.7)
axs[0, 1].set_title('Log-Transformed Data')
axs[0, 1].set_xlabel('Value')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].grid(alpha=0.3)

# Standardized Data
axs[1, 0].hist(standardized_data, bins=30, color='mediumseagreen', edgecolor='black', alpha=0.7)
axs[1, 0].set_title('Z-Score Standardized Data (Log-Transformed)')
axs[1, 0].set_xlabel('Z-Score')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].grid(alpha=0.3)

# Normalized Data
axs[1, 1].hist(normalized_data, bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
axs[1, 1].set_title('Normalized Data')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].grid(alpha=0.3)

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()
```

![[Pasted image 20241219103609.png]]