"""
Script pour reconvertir le modèle .h5 en format .keras moderne
"""
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import json

# Charger les données Pima
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
cols = ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigree","Age","Outcome"]
df = pd.read_csv(url, names=cols)
X = df.iloc[:,0:8].values
y = df.iloc[:,8].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Créer le modèle avec Input explicite (compatible TF 2.15)
model = Sequential([
    Input(shape=(8,)),
    Dense(12, activation="relu"),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=50, batch_size=16, verbose=0)

# Évaluer
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy: {acc:.4f}")

# Sauvegarder au format .keras (moderne)
model.save("model/model.keras")
print("✓ Modèle sauvegardé: model/model.keras")

# Sauvegarder aussi en .h5 compatible
model.save("model/model.h5", save_format='h5')
print("✓ Modèle sauvegardé: model/model.h5")

# Sauvegarder les métadonnées du scaler
meta = {
    "mean": scaler.mean_.tolist(),
    "scale": scaler.scale_.tolist(),
    "feature_names": cols[:-1]  # Exclure 'Outcome'
}
with open("model/scaler_meta.json", "w") as f:
    json.dump(meta, f, indent=2)
print("✓ Scaler sauvegardé: model/scaler_meta.json")
