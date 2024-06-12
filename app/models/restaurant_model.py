from app.database import db


# Define la clase `Restaurant` que hereda de `db.Model`
# `Restaurant` representa la tabla `Restaurants` en la base de datos
class Restaurant(db.Model):
    __tablename__ = "restaurants"

    # Define las columnas de la tabla `Restaurants`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    raiting = db.Column(db.Float, nullable=False)
    

    # Inicializa la clase `Restaurant`
    def __init__(self, name, address, raiting, phone, descrption, city):
        self.name = name
        self.address = address
        self.description = descrption
        self.city = city
        self.raiting = raiting
        self.phone = phone

    # Guarda un Restaurant en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los Restaurantes de la base de datos
    @staticmethod
    def get_all():
        return Restaurant.query.all()

    # Obtiene un Restaurant por su ID
    @staticmethod
    def get_by_id(id):
        return Restaurant.query.get(id)

    # Actualiza un Restaurant en la base de datos
    def update(self, name=None, address=None, description=None, city=None, raiting=None, phone=None):
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if description is not None:
            self.description = description
        if city is not None:
            self.city = city
        if raiting is not None:
            self.raiting = raiting
        if phone is not None:
            self.phone = phone
        db.session.commit()

    # Elimina un Restaurant de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()