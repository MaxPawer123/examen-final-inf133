def render_reservation_list(reservations):
    return[
        {
            "id": reservation.id,
            "user_id": reservation.user_id,
            "restaurant_id": reservation.restaurant_id,
            "reservation_date": reservation.price,
            "num_guests": reservation.stock,
            "special_requests": reservation.stock,
        }
        for reservation in products
    ]

def render_reservation_detail(reservation):
    return {
        "id": reservation.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
    }