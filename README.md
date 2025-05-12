````markdown
🧾 Expense Tracker (Suivi de Dépenses)

Une mini application web en Python (Flask) pour suivre tes dépenses personnelles localement ou en ligne (Render).

---

📦 Prérequis

- Python 3.x installé
- Git installé (pour cloner le projet ou le déployer)
- Navigateur web (Chrome, Firefox, etc.)
- Connexion internet (pour Render)

---

🔧 Installation locale (PC)

1. **Clone le projet** ou télécharge le dossier :

   ```bash
   git clone https://github.com/ton-utilisateur/expense-tracker.git
   cd expense-tracker
````

2. **Crée un environnement virtuel** :

   ```bash
   python -m venv venv
   ```

3. **Active-le** :

   * Sous **Windows** :

     ```bash
     venv\Scripts\activate
     ```
   * Sous **macOS/Linux** :

     ```bash
     source venv/bin/activate
     ```

4. **Installe les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

5. **Lance l’application** :

   ```bash
   python app.py
   ```

6. **Accède à l’interface** :
   Ouvre ton navigateur à l’adresse suivante :

   ```
   http://localhost:5000
   ```

---

## ▶️ Mode d’utilisation (Web ou Local)

1. Dans la page d'accueil :

   * **Montant** : entre le montant de la dépense (ex. `12.50`)
   * **Catégorie** : choisis ou écris une catégorie (ex. `Transport`, `Alimentation`, `Santé`, etc.)
   * **Description** : note ce que c’était exactement (ex. `Taxi jusqu'à la gare`, `Déjeuner`, etc.)

2. Clique sur **Ajouter** pour enregistrer ta dépense.

3. La liste en bas affiche **l'historique de tes dépenses**, de la plus récente à la plus ancienne.

4. Tu peux recharger la page pour rafraîchir la liste si besoin.


## 📁 Structure du projet

```
expense_tracker/
├── app.py               # Backend Flask
├── requirements.txt     # Dépendances Python
├── README.md            # Documentation du projet
├── render.yaml          # (optionnel) Fichier de déploiement Render
├── templates/
│   └── index.html       # Interface HTML
├── static/
│   ├── style.css        # Styles CSS
│   └── script.js        # JS pour les requêtes
└── expenses.db          # Base de données SQLite (créée automatiquement)
```

---

## 📊 Fonctionnalités

* Ajouter des dépenses manuellement
* Visualiser l’historique complet
* Stockage local avec SQLite
* Déploiement possible sur Render (version gratuite)
* Code simple et extensible (statistiques, filtres, authentification…)

---

## ✍️ Auteur

Projet personnel pour la gestion simple et locale des dépenses, avec possibilité d'évoluer vers une version en ligne.
Développé en Python avec Flask et HTML/CSS/JS.
