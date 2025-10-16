from flask import Blueprint, request, jsonify
import decimal

import src.utils as utils
import src.database as database
from src.api import Server
import dbg

residue_route = Blueprint('/', __name__)

@residue_route.route('/residue', methods=['GET', 'POST'])
def handle_residue():
    # list all residues
    if request.method == 'GET':
        dbg.log_info("Listing all residues")
        residues = [
            {
                "id": 1,
                "type": utils.ResidueTypeEnum.METAL.value,
                "kg": 0.5
            },
            {
                "id": 2,
                "type": utils.ResidueTypeEnum.PAPER.value,
                "kg": 1.0
            }
        ]
        return jsonify(residues), 200
    
    # register new residue
    elif request.method == 'POST':
        """
            "type": 0
            "kg": 0.5
        """
        dbg.log_info("Registering new residue")
        try:
            raw_data = request.get_json()
            residue_type: int = int(raw_data.get('type', utils.ResidueTypeEnum.PAPER.value))
            residue_kg: float = float(raw_data.get('kg', 0.0))
            
            if not utils.ResidueTypeEnum.is_valid(residue_type):
                dbg.log_warn(f"Invalid residue type: {residue_type}")
                return jsonify(
                    {
                        "message": "Invalid residue type",
                        "error": f"Type {residue_type} is not valid"
                    }
                ), 400

            if residue_kg <= 0:
                dbg.log_warn(f"Invalid residue quantity: {residue_kg}")
                return jsonify(
                    {
                        "message": "Invalid residue quantity",
                        "error": f"Quantity {residue_kg} must be greater than zero"
                    }
                ), 400

            #
            
            q = database.Querier(Server.instance().db_conn)
            try:
                dbg.log_ok(f"Residue registered: id={0}, type={0}, kg={0.0}")
                
                return jsonify(
                    {
                        "id": 0,
                        "type": 0,
                        "kg": 0.0
                    }
                ), 201    
            except Exception as e:
                dbg.log_error(f"Database error: {str(e)}")
                print(utils.get_exception_trace(e))
                return jsonify(
                    {
                        "message": "Database error",
                        "error": str(e)
                    }
                ), 500
        except Exception as e:
            dbg.log_error(f"Error processing request: {str(e)}")
            return jsonify(
                {
                    "message": "Error processing request",
                    "error": str(e)
                }
            ), 400
        

@residue_route.route('/residue/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def residue_by_id(id: int):
    if request.method == 'GET':
        dbg.log_info(f"Getting residue with id {id}")
        residue = {
            "id": id,
            "type": utils.ResidueTypeEnum.METAL.value,
            "kg": 0.5
        }
        dbg.log_ok(f"Residue found: {residue}")
        return jsonify(residue), 200
    
    elif request.method == 'PUT':
        dbg.log_info(f"Updating residue with id {id}")

        raw_data = request.get_json()

        residue_type = raw_data.get('type', utils.ResidueTypeEnum.PAPER.value)
        residue_kg = raw_data.get('kg', 0.0)
        
        updated_residue = {
            "id": id,
            "type": residue_type,
            "kg": residue_kg
        }
        dbg.log_ok(f"Residue updated: {updated_residue}")
        return jsonify(updated_residue), 200
    
    elif request.method == 'DELETE':
        dbg.log_info(f"Deleting residue with id {id}")
        dbg.log_ok(f"Residue with id {id} deleted")
        return jsonify(
            {
                "message": f"Residue with id {id} deleted"
            }
        ), 200
