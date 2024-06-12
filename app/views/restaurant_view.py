def render_restaurant_list(restaurants):
    return[
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "city": restaurant.city,
            "phone": restaurant.phone,
            "description": restaurant.description,
        }
        for restaurant in restaurants
    ]

def render_restaurant_detail(restaurant):
    return {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "city": restaurant.city,
            "phone": restaurant.phone,
            "description": restaurant.description,
    }