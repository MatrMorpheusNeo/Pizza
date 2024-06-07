from app.routes import db


PizzaToppings = db.Table('PizzaToppings',
                        db.Column('pid', db.Integer,
                                  db.ForeignKey('Pizza.id')),
                        db.Column('tid', db.Integer,
                                  db.ForeignKey('Toppings.id')))


class Pizza(db.Model):
    __tablename__ = "Pizza"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text())
    description = db.Column(db.Text())
    price = db.Column(db.Integer())
    base = db.Column(db.Integer, db.ForeignKey("Base.id"))
    base_desc = db.relationship("Base", backref="pizza_base")
    toppings = db.relationship('Topping', 
                               secondary = 'PizzaToppings',
                               back_populates = 'pizzas')


class Base(db.Model):
    __tablename__ = "Base"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())


class Topping(db.Model):
    __tablename__ = "Toppings"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    pizzas = db.relationship('Pizza', secondary='PizzaToppings',
                             back_populates='toppings')

    def __repr__(self):
        return self.name





