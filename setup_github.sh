#!/bin/bash

echo "🚀 Configuration Git et GitHub pour le TP ANN Diabète"
echo "====================================================="

# Initialiser Git
echo "1️⃣ Initialisation de Git..."
git init

# Ajouter tous les fichiers
echo "2️⃣ Ajout des fichiers..."
git add .

# Premier commit
echo "3️⃣ Premier commit..."
git commit -m "API Flask pour modèle ANN diabète"

# Renommer la branche principale
echo "4️⃣ Configuration de la branche main..."
git branch -M main

echo ""
echo "📋 Instructions pour GitHub :"
echo "============================"
echo "1. Allez sur https://github.com et créez un nouveau repository :"
echo "   - Nom : ann-diabetes-api"
echo "   - Description : API Flask pour prédiction du diabète avec ANN"
echo "   - Public ou Private (votre choix)"
echo "   - NE PAS initialiser avec README, .gitignore, ou licence"
echo ""
echo "2. Une fois le repository créé, copiez l'URL et exécutez :"
echo "   git remote add origin https://github.com/VOTRE_USERNAME/ann-diabetes-api.git"
echo "   git push -u origin main"
echo ""
echo "3. Pour configurer les secrets Docker Hub (optionnel) :"
echo "   - Allez dans Settings > Secrets and variables > Actions"
echo "   - Ajoutez DOCKERHUB_USERNAME et DOCKERHUB_TOKEN"
echo ""
echo "✅ Votre projet sera alors visible sur GitHub !"
