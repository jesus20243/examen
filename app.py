Examen Unidad III
Autor: [Jesus Bolaños Sanchez]
Fecha: [5 noviembre 2025]


dispositivos = {}

@app.route('/dispositivos_html', methods=['GET'])
def mostrar_dispositivos_html():
    html = """
    <html>
    <head>
        <title>Listado de Dispositivos</title>
        <style>
            .dispositivo {
                color: orange;  /* corregido */
                font-family: Arial;
                background: yellow;
                border: 5px solid black;
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
