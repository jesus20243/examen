# Autor: isaak
# Fecha: 29_
# Descripción:
# API básica en Flask para administrar dispositivos de red.
# Permite agregar, modificar y mostrar dispositivos en formato HTML.

from flask import Flask, request, jsonify, render_template_string


app = Flask(__name__)


# Diccionario de dispositivos
dispositivos = {}


# Mostrar los dispositivos
@app.route('/dispositivos_html', methods=['GET'])
def mostrar_dispositivos_html():
    html = """
    <html>
    <head>
        <title>Listado de Dispositivos</title>
        <style>
            .dispositivo {
                color-font: orange;
                font-family: Arial;
                background: yellow;
                border: 5px solid #000000;
                padding: 10px;
                margin: 10px;
            }
        </style>
    </head>
    <body>
        <h1>Dispositivos de Red</h1>
        {% for d in dispositivos.values() %}
        <div class="dispositivo">
            <h2>{{ d.nombre }}</h2>
            <p><b>Descripción:</b> {{ d.descripcion }}</p>
            <p><b>IP:</b> {{ d.ip }}</p>
            <p><b>MAC:</b> {{ d.mac }}</p>
            <p><b>Ubicación:</b> {{ d.ubicacion }}</p>
            <p><b>Tipo:</b> {{ d.tipo }}</p>
            <p><b>Otros:</b> {{ d.otros }}</p>
        </div>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html, dispositivos=dispositivos)


# Agregar un nuevo dispositivo
@app.route('/dispositivos', methods=['POST'])
def agregar_dispositivo():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Faltan datos o ID"}), 400


    dispositivos[data["id"]] = data
    return jsonify({"mensaje": "Dispositivo agregado", "dispositivo": data}), 201


# Modificar un dispositivo existente
@app.route('/dispositivos/<id>', methods=['PUT'])
def modificar_dispositivo(id):
    if id not in dispositivos:
        return jsonify({"error": "Dispositivo no encontrado"}), 404


    data = request.get_json()
    for clave, valor in data.items():
        dispositivos[id][clave] = valor


    return jsonify({"mensaje": "Dispositivo modificado", "dispositivo": dispositivos[id]}), 200


# Ruta de prueba
@app.route('/', methods=['GET'])
def test():
    return "API funcionando correctamente"


if __name__ == '__main__':
    app.run(debug=True)
