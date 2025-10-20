# 🚀 Guide pour publier sur GitHub

## Étapes à suivre :

### 1. Créer le repository sur GitHub
1. Allez sur [GitHub.com](https://github.com)
2. Cliquez sur le bouton vert **"New"** ou **"+"** → **"New repository"**
3. Remplissez :
   - **Repository name** : `ann-diabetes-api`
   - **Description** : `API Flask pour prédiction du diabète avec ANN`
   - **Public** ou **Private** (votre choix)
   - **❌ NE PAS COCHER** : "Add a README file"
   - **❌ NE PAS COCHER** : "Add .gitignore" 
   - **❌ NE PAS COCHER** : "Choose a license"
4. Cliquez sur **"Create repository"**

### 2. Connecter votre projet local
Une fois le repository créé, GitHub vous montrera des commandes. Copiez l'URL et exécutez :

```bash
cd "/Users/macbook/Downloads/TP Synthese/ann_diabete_api"
git remote add origin https://github.com/VOTRE_USERNAME/ann-diabetes-api.git
git push -u origin main
```

### 3. Vérifier sur GitHub
Après le push, vous devriez voir :
- ✅ Tous vos fichiers
- ✅ README.md avec documentation
- ✅ Workflow CI/CD dans `.github/workflows/`
- ✅ Dockerfile
- ✅ Structure complète du projet

### 4. Fonctionnalités disponibles
- **Code** : Navigation dans le code
- **Actions** : CI/CD automatique
- **Issues** : Signalement de problèmes
- **Pull Requests** : Contributions

## 🎯 Résultat attendu
Votre projet sera visible publiquement sur GitHub avec toute la documentation et le code source !
