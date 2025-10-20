#!/usr/bin/env python3
"""
Script de test pour l'API ANN Diabète
"""
import requests
import json

# URL de base
BASE_URL = "http://localhost:5001"

def test_ping():
    """Test de l'endpoint ping"""
    print("🔍 Test de l'endpoint /ping...")
    response = requests.get(f"{BASE_URL}/ping")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200

def test_predict():
    """Test de l'endpoint predict"""
    print("\n🔍 Test de l'endpoint /predict...")
    
    # Données de test (exemple de patient diabétique)
    test_data = {
        "instances": [
            [6, 148, 72, 35, 0, 33.6, 0.627, 50],  # Patient diabétique
            [1, 85, 66, 29, 0, 26.6, 0.351, 31]    # Patient non diabétique
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/predict",
        headers={"Content-Type": "application/json"},
        json=test_data
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Predictions: {result['predictions']}")
        print(f"Probabilities: {result['probabilities']}")
        return True
    else:
        print(f"Error: {response.text}")
        return False

if __name__ == "__main__":
    print("🚀 Test de l'API ANN Diabète")
    print("=" * 40)
    
    # Tests
    ping_ok = test_ping()
    predict_ok = test_predict()
    
    print("\n" + "=" * 40)
    if ping_ok and predict_ok:
        print("✅ Tous les tests sont passés avec succès !")
    else:
        print("❌ Certains tests ont échoué.")
