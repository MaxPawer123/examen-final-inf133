import json
from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

def roles_required(roles=[]):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                # Verifica si hay un token JWT en la solicitud
                verify_jwt_in_request()

                # Obtiene la identidad del usuario del token JWT
                current_user = get_jwt_identity()

                # Obtiene los roles del usuario como una lista
                user_roles = json.loads(current_user.get("roles", []))

                # Verifica si el usuario tiene al menos uno de los roles requeridos
                if not set(roles).intersection(user_roles):
                    return jsonify({"error": "Acceso no autorizado para este rol"}), 403

                # Si el usuario tiene los roles necesarios, ejecuta la función original
                return fn(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 401

        return wrapper

    return decorator
