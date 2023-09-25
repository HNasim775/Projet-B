from app import db
class Order(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        product_it = db.Column(db.Integer, nullable=False)
        quantity = db.Column(db.Integer, nullable=False)
#.....Ajoutz d'autres champs si nécessaire
