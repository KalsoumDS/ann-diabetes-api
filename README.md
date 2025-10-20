# API ANN Diabète

API Flask pour la prédiction du diabète basée sur un modèle de réseau de neurones artificiels (ANN).

## Structure du projet

```
ann_diabete_api/
├── app.py                    # Application Flask principale
├── requirements.txt          # Dépendances Python
├── Dockerfile               # Configuration Docker
├── test_api.py             # Script de test
├── model/
│   ├── model.h5            # Modèle ANN sauvegardé
│   └── scaler_meta.json    # Métadonnées du scaler
└── .github/workflows/
    └── docker-image.yml    # Workflow CI/CD
```

## Installation et utilisation

### Installation locale

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Lancer l'application :
```bash
python app.py
```

L'API sera disponible sur `http://localhost:5001`

### Avec Docker

```bash
# Construire l'image
docker build -t ann-diabete-api .

# Lancer le conteneur
docker run -p 5001:5000 ann-diabete-api
```

## Endpoints API

### GET /ping
Vérifie que l'API est prête.

**Réponse :**
```json
{"status": "API ready"}
```

### POST /predict
Effectue une prédiction de diabète.

**Corps de la requête :**
```json
{
  "instances": [
    [6, 148, 72, 35, 0, 33.6, 0.627, 50]
  ]
}
```

**Réponse :**
```json
{
  "predictions": [1],
  "probabilities": [[0.6782733798027039]]
}
```

## Format des données

Les features attendues sont (dans l'ordre) :
1. Pregnancies (nombre de grossesses)
2. Glucose (concentration de glucose)
3. BloodPressure (pression artérielle)
4. SkinThickness (épaisseur de la peau)
5. Insulin (insuline)
6. BMI (indice de masse corporelle)
7. DiabetesPedigree (fonction pedigree du diabète)
8. Age (âge)

## Tests

Lancer les tests :
```bash
python test_api.py
```

## CI/CD

Le projet inclut un workflow GitHub Actions qui :
- Construit l'image Docker
- Teste l'application
- Valide le bon fonctionnement de l'API
