from app.database import db
from datetime import datetime

class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, nullable=False)
    reservation_date = db.Column(db.DateTime, nullable=False)
    num_guests = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.String(100), nullable=True)

    # Inicializar la clase 'Reservation'
    def __init__(self, user_id, reservation_date, restaurant_id, num_guests, special_requests=None):
        self.user_id = user_id
        self.reservation_date = reservation_date
        self.restaurant_id = restaurant_id
        self.num_guests = num_guests
        self.special_requests = special_requests

    # Guardar una reserva en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtener todas las reservas de la base de datos
    @staticmethod
    def get_all():
        return Reservation.query.all()

    # Obtener una reserva por su id
    @staticmethod
    def get_by_id(id):
        return Reservation.query.get(id)

    # Actualizar una reserva
    def update(self, user_id=None, reservation_date=None, restaurant_id=None, num_guests=None, special_requests=None):
        if user_id is not None:
            self.user_id = user_id
        if reservation_date is not None:
            self.reservation_date = reservation_date
        if restaurant_id is not None:
            self.restaurant_id = restaurant_id
        if num_guests is not None:
            self.num_guests = num_guests
        if special_requests is not None:
            self.special_requests = special_requests
        db.session.commit()

    # Eliminar una reserva
    def delete(self):
        db.session.delete(self)
        db.session.commit()
