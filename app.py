from flask import Flask, request, render_template, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    return conn


# Crée la table si elle n'existe pas
with get_db_connection() as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        )
    ''')
    conn.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_expense():
    data = request.get_json()
    amount = data.get('amount')
    category = data.get('category')
    description = data.get('description')
    date = datetime.now().strftime("%Y-%m-%d")

    with get_db_connection() as conn:
        conn.execute('''
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?, ?, ?, ?)
        ''', (amount, category, description, date))
        conn.commit()

    return jsonify({"message": "Dépense ajoutée avec succès !"})


@app.route('/expenses')
def get_expenses():
    with get_db_connection() as conn:
        expenses = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()
        return jsonify([dict(expense) for expense in expenses])


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
