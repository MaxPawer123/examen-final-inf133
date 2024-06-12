from app.database import db
from datetime import datetime

# Define la clase `Reservation` que hereda de `db.Model`
# `Reservation` representa la tabla `Reservations` en la base de datos
class Reservation(db.Model):
    __tablename__ = "reservations"

    # Define las columnas de la tabla `Reservations`
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=False)
    reservation_date = db.Column(db.DateTime, nullable=False)
    num_guests = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)


    # Inicializa la clase `Reservation`
    def __init__(self, special_requests, status, user_id, restaurant_id, reservation_date, num_guests):
        self.special_requests = special_requests
        self.reservation_date = reservation_date
        self.num_guests = num_guests
        self.status = status
        self.user_id = user_id
        self.restaurant_id = restaurant_id

    # Guarda un Reservation en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los Reservationes de la base de datos
    @staticmethod
    def get_all():
        return Reservation.query.all()

    # Obtiene un Reservation por su ID
    @staticmethod
    def get_by_id(id):
        return Reservation.query.get(id)

    # Actualiza un Reservation en la base de datos
    def update(self, special_requests=None, reservation_date=None, num_guests=None, status=None, user_id=None, restaurant_id=None):
        if special_requests is not None:
            self.special_requests = special_requests
        if reservation_date is not None:
            self.reservation_date = reservation_date
        if num_guests is not None:
            self.num_guests = num_guests
        if status is not None:
            self.status = status
        if user_id is not None:
            self.user_id = user_id
        if restaurant_id is not None:
            self.restaurant_id = restaurant_id
        db.session.commit()

    # Elimina un Reservation de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()