from flask import Flask, jsonify, request
from flask_cors import CORS
from parser_commands import parse
import time
app = Flask(__name__)
CORS(app)


# Respuesta de ejemplo
respuesta = {
    'estado': 'OK',
    'mensaje': '[Success] => Disco creado correctamente',
}

# Ruta para obtener la lista de productos≠
@app.route('/', methods=['GET'])
def obtener_productos():
    return jsonify(respuesta)

@app.route('/execute', methods=['POST'])
def get_first_word():
    data = request.get_json()
    message = data.get('command', '')

    # Dividir el mensaje en palabras
    words = message.split("\n")

    if words:
        message = ""
        for command in words:
            parse(command)
            word = command.split()
            
            message += f'[Success] => Comando {word[0]} ejecutado exitosamente\n'

    
    else:
        message = "No se encontraron palabras en el mensaje."

    respuesta = {
        'estado': 'OK',
        'mensaje': message,
    }

    # Esperamos 1 segundo, para simular proceso de ejecución
    time.sleep(1)

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)