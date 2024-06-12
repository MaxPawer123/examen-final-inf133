from app.database import db

class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Interger, nullable=False)
    restaurant_id = db.Column(db.Interger, nullable=False)
    num_guests = db.Column(db.Interger, nullable=False)
    special_requests= db.Column(db.String(100), nullable=False)

    #Iniciar la clase 'Product'
    def __init__(self, user_id , restaurant_id , num_guests , special_requests):
        self.user_id  = user_id 
        self.restaurant_id  = restaurant_id 
        self.num_guests  = num_guests 
        self.special_requests= special_requests

    #Guardar un producto en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    #Obtener todos los productos de la base de datos
    @staticmethod
    def get_all():
        return Reservation.query.all()

    #Obtener un producto por su id
    @staticmethod
    def get_by_id(id):
        return Reservation.query.get(id)
    #Actualizar un producto
    def update(self, user_id=None, restaurant_id =None, num_guests =None, special_requests=None):
        
        if user_id is not None:
            self.user_id = user_id
        if restaurant_id is not None:
            self.restaurant_id = restaurant_id
        if num_guests is not None:
            self.num_guests = num_guests
        if special_requests is not None:
            self.special_requests = special_requests
        db.session.commit()

    #Eliminar un producto
    def delete(self):
        db.session.delete(self)
        db.session.commit()