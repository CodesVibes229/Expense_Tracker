```markdown
🧾 Expense Tracker (Suivi de Dépenses)

Une mini application web en Python (Flask) pour suivre tes dépenses personnelles localement.

🔧 Installation

1. Clone ou télécharge ce dépôt.
2. Place-toi dans le dossier du projet et crée un environnement virtuel :
   ```bash
   python -m venv venv
````

3. Active l'environnement virtuel :

   * **Sous Windows** :

     ```bash
     venv\Scripts\activate
     ```
   * **Sous macOS/Linux** :

     ```bash
     source venv/bin/activate
     ```
4. Installe les dépendances Python avec :

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Lancer l'application

1. Lance le serveur Flask :

   ```bash
   python app.py
   ```

2. Ouvre ton navigateur et accède à l'application à l'adresse : [http://localhost:5000](http://localhost:5000)

## 📁 Structure du projet

```
expense_tracker/
├── app.py               # Backend Flask
├── requirements.txt     # Dépendances Python
├── README.md            # Documentation du projet
├── templates/
│   └── index.html       # Page HTML principale
├── static/
│   ├── style.css        # Styles CSS
│   └── script.js        # Scripts JS
└── expenses.db          # Base de données SQLite (créée automatiquement)
```

## 💾 Base de données

La base `expenses.db` est automatiquement créée au premier lancement. Elle contient les champs :

* `id` (identifiant unique de la dépense)
* `amount` (montant de la dépense)
* `category` (catégorie de la dépense)
* `description` (description de la dépense)
* `date` (date à laquelle la dépense a été ajoutée)

## 🛠 Fonctionnalités

* **Ajouter une dépense** via un formulaire simple.
* **Voir l'historique des dépenses** dans une liste chronologique.
* **Base de données locale** pour stocker les informations sur les dépenses.

## ✍️ Auteur

Projet personnel pour la gestion des dépenses locales avec interface simple.
