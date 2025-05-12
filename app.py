from flask import Flask, render_template, request, redirect, url_for
import psycopg
import os
from urllib.parse import urlparse

app = Flask(__name__)

# 🔐 Lire l'URL de la base depuis la variable d'environnement (Render la fournit automatiquement)
DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    # Parse DATABASE_URL en éléments pour psycopg
    result = urlparse(DATABASE_URL)
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    port = result.port

    return psycopg.connect(
        dbname=database,
        user=username,
        password=password,
        host=hostname,
        port=port
    )

# 🔧 Créer la table si elle n'existe pas encore
with get_db_connection() as conn:
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id SERIAL PRIMARY KEY,
                amount REAL,
                category TEXT,
                description TEXT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM expenses ORDER BY date DESC')
            expenses = cur.fetchall()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    amount = request.form['amount']
    category = request.form['category']
    description = request.form['description']

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO expenses (amount, category, description)
                VALUES (%s, %s, %s)
            ''', (amount, category, description))
            conn.commit()
    return redirect(url_for('index'))

# 🔁 Déploiement Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
