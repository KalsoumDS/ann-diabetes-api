# API Prédiction Diabète - Déploiement avec CI/CD

API Flask pour la prédiction du diabète basée sur un modèle de réseau de neurones (ANN) entraîné sur le dataset Pima Indians Diabetes.

## 📋 Structure du projet

```
ann_diabete_api/
├── .github/
│   └── workflows/
│       └── docker-image.yml    # Workflow GitHub Actions pour CI/CD
├── model/
│   ├── model.keras             # Modèle ANN entraîné
│   └── scaler_meta.json        # Métadonnées du StandardScaler
├── app.py                      # Application Flask
├── Dockerfile                  # Configuration Docker
├── docker-compose.yml          # Configuration Docker Compose
├── requirements.txt            # Dépendances Python
└── .dockerignore              # Fichiers exclus du build Docker
```

## 🚀 Déploiement

### Option 1: Docker Hub (CI/CD automatique)

L'image Docker est automatiquement construite et poussée sur Docker Hub via GitHub Actions à chaque push sur la branche `main`.

```bash
docker pull kalsoumdS/ann-diabetes-api:latest
docker run -p 5000:5000 kalsoumdS/ann-diabetes-api:latest
```

### Option 2: Build local

```bash
# Construire l'image
docker build -t ann-diabetes-api .

# Lancer le conteneur
docker run -p 5000:5000 ann-diabetes-api
```

### Option 3: Docker Compose

```bash
docker-compose up
```

## 🧪 Tests de l'API

### Test de disponibilité
```bash
curl http://localhost:5000/ping
```

**Réponse attendue:**
```json
{"status": "API ready"}
```

### Test de prédiction
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"instances": [[6, 148, 72, 35, 0, 33.6, 0.627, 50]]}'
```

**Réponse attendue:**
```json
{
  "predictions": [1],
  "probabilities": [[0.6753365993499756]]
}
```

## 📊 Format des données

Les données d'entrée doivent contenir 8 caractéristiques dans l'ordre suivant:
1. Pregnancies (Grossesses)
2. Glucose
3. BloodPressure (Pression artérielle)
4. SkinThickness (Épaisseur de la peau)
5. Insulin (Insuline)
6. BMI (Indice de masse corporelle)
7. DiabetesPedigree (Fonction de pédigrée du diabète)
8. Age (Âge)

## 🔧 Technologies utilisées

- **Flask** 3.0.0 - Framework web Python
- **TensorFlow** 2.17.0 - Framework de deep learning
- **Docker** - Conteneurisation
- **GitHub Actions** - CI/CD automatique

## 📝 CI/CD Pipeline

Le workflow GitHub Actions (`.github/workflows/docker-image.yml`) automatise:
1. Checkout du code
2. Configuration de Docker Buildx
3. Connexion à Docker Hub
4. Build de l'image Docker
5. Push sur Docker Hub avec tag `:latest`

## 👨‍🎓 Auteur

Projet réalisé dans le cadre du TP Synthèse - Déploiement d'un modèle ANN avec Flask et CI/CD
