#!/bin/bash

echo "🚀 Script pour pousser sur GitHub"
echo "================================="
echo ""

# Vérifier si un remote existe déjà
if git remote get-url origin >/dev/null 2>&1; then
    echo "✅ Remote 'origin' existe déjà"
    echo "URL actuelle : $(git remote get-url origin)"
    echo ""
    echo "Pour pousser : git push -u origin main"
else
    echo "❌ Aucun remote 'origin' configuré"
    echo ""
    echo "📋 Instructions :"
    echo "1. Créez d'abord le repository sur GitHub.com"
    echo "2. Copiez l'URL du repository (ex: https://github.com/USERNAME/ann-diabetes-api.git)"
    echo "3. Exécutez : git remote add origin VOTRE_URL"
    echo "4. Puis : git push -u origin main"
    echo ""
    echo "💡 Ou utilisez cette commande (remplacez VOTRE_USERNAME) :"
    echo "git remote add origin https://github.com/VOTRE_USERNAME/ann-diabetes-api.git"
fi

echo ""
echo "📊 État actuel du repository :"
git log --oneline -3
echo ""
echo "📁 Fichiers prêts à être poussés :"
ls -la
