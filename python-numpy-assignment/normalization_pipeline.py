import numpy as np

data = np.array([10, 20, 30, 40])

mean = np.mean(data)
std = np.std(data)

normalized = (data - mean) / std

reshaped = normalized.reshape(2, 2)

print("Original data:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized data:", normalized)
print("Reshaped data shape:", reshaped.shape)
