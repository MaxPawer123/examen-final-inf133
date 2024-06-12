from flask import Blueprint, request, jsonify
from app.models.restaurant_model import Restaurant
from app.views.restaurant_view import render_restaurant_detail, render_restaurant_list
from app.utils.decorators import jwt_required, roles_required

#Crear un blueprint para el controlador
restaurant_bp = Blueprint("restaurant", __name__)
#Ruta para obtener la lista de productos
@restaurant_bp.route("/restaurants", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "customer"])
def get_restaurants():
    restaurants = Restaurant.get_all()
    return jsonify(render_restaurant_list(restaurants))
   

#Ruta para obtener un producto especifico por id 
@restaurant_bp.route("/restaurants/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "customer"])
def get_restaurant(id):
    product = Restaurant.get_by_id(id)
    if product:
        return jsonify(render_restaurant_detail(product))
    return jsonify({"error":"Restaurant no encontrado"}), 404

#Ruta para crear un nuevo producto y guardarlo en la base de datos
@restaurant_bp.route("/restaurants", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_restaurant():
    data = request.json 
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description = data.get("description")
    rating = data.get("rating")
    #Validadcion simple de datos de entrada
    if not name or not address or not city or not phone or not rating:
        return jsonify({"error":"Faltan datos requeridos"}), 400
   
    #Crear un nuevo producto
    restaurant = Restaurant(name=name, description=description, address=address, city=city, phone=phone, rating=rating)
    restaurant.save()
    return jsonify(render_restaurant_detail(restaurant)), 201


#Ruta para actualizar un producto existente
@restaurant_bp.route("/restaurants/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_restaurant(id):
    restaurant = Restaurant.get_by_id(id)
    if not restaurant:
        return jsonify({"error":"Restaurant no encontrado"}), 404
    
    data = request.json 
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description = data.get("description")
    rating = data.get("rating")

    #Actualziar los datos del producto
    restaurant.update (name=name, description=description, address=address, city=city, phone=phone, rating=rating)
    return jsonify(render_restaurant_detail(restaurant))

#Ruta para eliminar un producto existente
@restaurant_bp.route("/restaurants/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_restaurant(id):
    restaurant =Restaurant.get_by_id(id)
    if not restaurant:
        return jsonify({"error":"restaurant no encontrado"}),404
    
    #eliminar el producto de la base de datos
    restaurant.delete()
    
    #Respuesta vacia con codigo de estado 204
    return "", 204

