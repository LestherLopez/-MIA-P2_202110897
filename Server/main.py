from flask import Flask, jsonify, request
from flask_cors import CORS
from parser_commands import parse
from classes.State import estado
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
        
        file_name = ""
        for i in range(1):
            for command in words:
                try:
                    estado.reportname = ""
                    palabra = command.strip()
                    print(palabra)
                    parse(palabra)
                    message += f'{estado.mensaje}'
                    if estado.reportname != "":
                        file_name += f'{estado.reportname}'
                except:
                    pass
    
    else:
        message = "No se encontraron palabras en el mensaje."
    print(file_name)
    respuesta = {
        'estado': 'OK',
        'mensaje': message,
        'filename': file_name,
    }

    # Esperamos 1 segundo, para simular proceso de ejecución
    time.sleep(1)

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)

#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 <- token