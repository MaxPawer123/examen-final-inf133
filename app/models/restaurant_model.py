from app.database import db

class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    phone =  db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    
    
    def __init__(self, name,address, city,phone,description, rating):
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.phone=phone
        self.rating

    #Guardar un producto en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    #Obtener todos los productos de la base de datos
    @staticmethod
    def get_all():
        return Restaurant.query.all()

    #Obtener un producto por su id
    @staticmethod
    def get_by_id(id):
        return Restaurant.query.get(id)
    #Actualizar un producto
    def update(self, name=None, description=None, city=None, phone=None,rating=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if city is not None:
            self.city = city
        if phone is not None:
            self.phone = phone
        if rating is not None:
            self.rating = rating

        db.session.commit()

    #Eliminar un producto
    def delete(self):
        db.session.delete(self)
        db.session.commit()
