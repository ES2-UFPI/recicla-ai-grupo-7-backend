from flask import Blueprint, request, jsonify
import src.utils as utils
import dbg

residuo_route = Blueprint('/', __name__)

@residuo_route.route('/residuo', methods=['GET', 'POST'])
def cadastrar_residuo():
    # listar todos os resíduos
    if request.method == 'GET':
        dbg.logInfo("Listando todos os resíduos")
        residuos = [
            {
                "id": 1,
                "tipo": utils.Residuo.METAL.value,
                "kg": 0.5
            },
            {
                "id": 2,
                "tipo": utils.Residuo.PAPEL.value,
                "kg": 1.0
            }
        ]
        
        return jsonify(residuos), 200
    
    # cadastrar novo resíduo
    elif request.method == 'POST':
        """
            "tipo": 0
            "kg": 0.5
        """
        dbg.logInfo("Cadastrando novo resíduo")
        try:
            raw_data = request.get_json()
            tipo_residuo: int = int( raw_data.get('tipo', utils.Residuo.PAPEL.value) )
            kg_residuo: float = float( raw_data.get('kg', 0.0) )
            
            if not utils.Residuo.is_valid(tipo_residuo):
                dbg.logWarn(f"Tipo de resíduo inválido: {tipo_residuo}")
                return jsonify(
                    {
                        "message": "Tipo de resíduo inválido",
                        "error": f"Tipo {tipo_residuo} não é válido"
                    }
                ), 400

            if kg_residuo <= 0:
                dbg.logWarn(f"Quantidade de resíduo inválida: {kg_residuo}")
                return jsonify(
                    {
                        "message": "Quantidade de resíduo inválida",
                        "error": f"Quantidade {kg_residuo} deve ser maior que zero"
                    }
                ), 400

            # simula
            dbg.logOk(f"Resíduo cadastrado: tipo={tipo_residuo}, kg={kg_residuo}")
            return jsonify(
                {
                    "id": 1,
                    "tipo": tipo_residuo,
                    "kg": kg_residuo
                }
            ), 201                
        except Exception as e:
            dbg.logError(f"Erro ao processar a requisição: {str(e)}")
            return jsonify(
                {
                    "message": "Erro ao processar a requisição",
                    "error": str(e)
                }
            ), 400
    
    

@residuo_route.route('/residuo/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_residuo(id: int):
    if request.method == 'GET':
        dbg.logInfo(f"Consultando resíduo de id {id}")
        residuo = {
            "id": id,
            "tipo": utils.Residuo.METAL.value,
            "kg": 0.5
        }
        dbg.logOk(f"Resíduo encontrado: {residuo}")
        return jsonify(residuo), 200
    
    elif request.method == 'PUT':
        dbg.logInfo(f"Atualizando resíduo de id {id}")

        raw_data = request.get_json()

        tipo_residuo = raw_data.get('tipo', utils.Residuo.PAPEL.value)
        kg_residuo = raw_data.get('kg', 0.0)
        
        residuo_atualizado = {
            "id": id,
            "tipo": tipo_residuo,
            "kg": kg_residuo
        }
        dbg.logOk(f"Resíduo atualizado: {residuo_atualizado}")
        return jsonify(residuo_atualizado), 200
    
    elif request.method == 'DELETE':
        dbg.logInfo(f"Deletando resíduo de id {id}")
        dbg.logOk(f"Resíduo de id {id} deletado")
        return jsonify(
            {
                "message": f"Resíduo de id {id} deletado"
            }
        ), 200