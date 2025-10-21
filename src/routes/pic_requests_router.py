from flask import Blueprint, request, jsonify
from pydantic import ValidationError

import src.utils as utils
from src.database.connection import get_db
from src.models.models import RecyclableMaterial as MaterialModel
from src.schemas.pic_requests_schema import RecyclableMaterial, RecyclableMaterialOut, PickupRequest
from src.database.repository import pic_requests_repo as prs_repo
import dbg

prq = Blueprint('/prq', __name__)


@prq.route('/material_reciclavel', methods=['GET'])
def list_materials():
    """Lista todos os materiais recicláveis"""
    try:
        with get_db() as db:
            repo = prs_repo.PicRequestsRepo(db)
            materials = repo.get_all_recyclable_materials()
            
            result = [
                RecyclableMaterialOut.model_validate(m).model_dump()
                for m in materials
            ]
            
            dbg.log_ok(f"Listed {len(result)} materials")
            return jsonify(result), 200
            
    except Exception as e:
        dbg.log_error(f"Error listing materials: {str(e)}")
        return jsonify({
            "message": "Error fetching materials",
            "error": str(e)
        }), 500


@prq.route('/material_reciclavel', methods=['POST'])
def create_material():
    """Cria um novo material reciclável"""
    try:
        # Valida dados de entrada com Pydantic
        data = request.get_json()
        material_data = RecyclableMaterial(**data)
        
        # Context manager para banco de dados
        with get_db() as db:
            repo = prs_repo.PicRequestsRepo(db)
            response = repo.register_recyclable_material(material_data)
            
            response = RecyclableMaterialOut.model_validate(response)

            dbg.log_ok(f"Material created: {response.id}")
            return jsonify(response.model_dump()), 201
            
    except ValidationError as e:
        dbg.log_warn(f"Validation error: {e.errors()}")
        return jsonify({
            "message": "Validation error",
            "errors": e.errors()
        }), 400
        
    except Exception as e:
        dbg.log_error(f"Error creating material: {str(e)}")
        return jsonify({
            "message": "Error creating material",
            "error": str(e)
        }), 500


@prq.route('/pickup_request', methods=['POST'])
def create_pickup_request():
    """Cria uma nova solicitação de coleta"""
    try:
        # Valida dados de entrada com Pydantic
        data = request.get_json()
        pickup_request_data = PickupRequest(**data)
        
        # Context manager para banco de dados
        with get_db() as db:
            repo = prs_repo.PicRequestsRepo(db)
            response = repo.create_pickup_request(pickup_request_data)
            
            dbg.log_ok(f"Pickup request created: {response.id}")
            return jsonify({
                "id": response.id,
                "producer_id": response.producer_id,
                "address_id": response.address_id,
                "scheduled_time": response.scheduled_time.isoformat()
            }), 201
            
    except ValidationError as e:
        dbg.log_warn(f"Validation error: {e.errors()}")
        return jsonify({
            "message": "Validation error",
            "errors": e.errors()
        }), 400
        
    except Exception as e:
        dbg.log_error(f"Error creating pickup request: {str(e)}")
        return jsonify({
            "message": "Error creating pickup request",
            "error": str(e)
        }), 500