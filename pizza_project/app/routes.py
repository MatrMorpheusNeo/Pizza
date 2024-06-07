from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath (os.path.dirname(__file__))
db = SQLAlchemy ()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "pizza.db")
db.init_app (app)

import app.models as models



@app.route("/")
def home():
    #conn = sqlite3.connect('pizza.db')
    #cur = conn.cursor()
    #cur.execute("SELECT PizzaName FROM Pizzas")
    #Pizza = cur.fetchall()
    # return render_template("layout.html", Pizza = Pizza)
    all_pizzas = models.Pizza.query.all()
    return render_template('home.html', all_pizzas = all_pizzas)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/pizzas/<int:id>')
def single_pizza(id):
    #conn = sqlite3.connect('pizza.db')
    #cur.conn.cursor()
    #cur.execute("SELECT * FROM pizza WHERE id=?",(id,))
    #pizza = cur.fetchone()
    pizza = models.Pizza.query.filter_by(id=id).first()
    return render_template("pizza.html", pizza = pizza)



if __name__ == "__main__":
    app.run(debug=True)