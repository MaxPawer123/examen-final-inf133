def render_restaurant_list(restaurants):
    # Representa una lista de restaurantes como una lista de diccionarios
    return [
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "city": restaurant.city,
            "phone": restaurant.phone,
            "description": restaurant.description,
            "rating": restaurant.rating,
            
        }
        for restaurant in restaurants
    ]


def render_restaurant_detail(restaurant):
    # Representa los detalles de un restaurant como un diccionario
    return {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "city": restaurant.city,
        "phone": restaurant.phone,
        "description": restaurant.description,
        "rating": restaurant.rating,
    }