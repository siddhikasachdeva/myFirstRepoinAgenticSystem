import numpy as np

np.random.seed(42)

data = np.random.rand(100, 3)

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

normalized = (data - mean) / std

split_index = int(0.8 * normalized.shape[0])

train_data = normalized[:split_index]
test_data = normalized[split_index:]

train_data[0,0] = 999

print("Original data shape:", data.shape)
print("Mean shape:", mean.shape)
print("Standard deviation shape:", std.shape)

print("Training data shape:", train_data.shape)
print("Test data shape:", test_data.shape)

print("Modified value in training data:", train_data[0,0])
print("Corresponding value in normalized array:", normalized[0,0])

print("Note: Modifying the slice affected the original array because NumPy slices are views.")
