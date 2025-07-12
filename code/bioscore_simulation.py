import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Mock spectral data: NIR absorbance values for common plastics
spectral_data = np.array([
    [0.1, 0.2, 0.3, 0.4],  # PET (non-biodegradable)
    [0.4, 0.5, 0.6, 0.7],  # PLA (biodegradable)
    [0.2, 0.3, 0.4, 0.5],  # HDPE (recyclable)
    [0.3, 0.4, 0.5, 0.6]   # PP (non-biodegradable)
])
labels = ["Non-Biodegradable", "Biodegradable", "Recyclable", "Non-Biodegradable"]

# Train a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(spectral_data, labels)

# Simulate scanning a new plastic sample
new_sample = np.array([[0.35, 0.45, 0.55, 0.65]])  # Mock sample (close to PLA)
prediction = model.predict(new_sample)[0]

# Assign BioScore based on prediction
bioscore_map = {
    "Biodegradable": 85,
    "Recyclable": 50,
    "Non-Biodegradable": 20
}
bioscore = bioscore_map[prediction]

# Determine disposal recommendation
disposal = "Compost" if bioscore >= 80 else "Recycle" if bioscore >= 50 else "Landfill"

# Output result
color = "Green" if bioscore >= 80 else "Yellow" if bioscore >= 50 else "Red"
print(f"Prediction: {prediction}")
print(f"BioScore: {bioscore} ({color})")
print(f"Disposal Recommendation: {disposal}")
