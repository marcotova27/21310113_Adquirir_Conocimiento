from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Clave secreta para manejar las sesiones

# Conectar a la base de datos
def conectar_db():
    conn = sqlite3.connect('database.db')
    return conn

# Inicializar la base de datos con respuestas precargadas
def inicializar_db():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS respuestas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        entrada TEXT NOT NULL,
                        respuesta TEXT NOT NULL)''')
    # Respuestas precargadas
    cursor.executemany('INSERT INTO respuestas (entrada, respuesta) VALUES (?, ?)', [
        ("Hola", "Hola, ¿cómo estás?"),
        ("¿Cómo estás?", "Estoy bien, gracias por preguntar."),
        ("¿De qué te gustaría hablar?", "Hablemos de cualquier tema que te interese.")
    ])
    conn.commit()
    conn.close()

# Obtener respuesta desde la base de datos
def obtener_respuesta(entrada_usuario):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT respuesta FROM respuestas WHERE entrada = ?', (entrada_usuario,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0]
    else:
        return None

# Agregar nueva entrada y respuesta a la base de datos
def agregar_conocimiento(entrada, respuesta):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO respuestas (entrada, respuesta) VALUES (?, ?)', (entrada, respuesta))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def chat():
    # Inicializa la sesión de historial si no existe
    if 'historial' not in session:
        session['historial'] = []

    if request.method == "POST":
        entrada_usuario = request.form['entrada_usuario']
        respuesta = obtener_respuesta(entrada_usuario)

        if respuesta:
            # Agregar el mensaje y la respuesta al historial
            session['historial'].append({"usuario": entrada_usuario, "chatbot": respuesta})
        else:
            # Redirige a la página de nuevo conocimiento con la entrada del usuario
            return redirect(url_for("nuevo_conocimiento", entrada=entrada_usuario))

        # Limita el historial a los últimos 5 mensajes
        if len(session['historial']) > 5:
            session['historial'].pop(0)

        # Guarda la sesión actualizada
        session.modified = True

    # Renderiza la página con el historial de mensajes
    return render_template("index.html", historial=session.get('historial', []))

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo_conocimiento():
    # Captura la entrada desde los argumentos de la URL o el formulario
    entrada_usuario = request.args.get("entrada") or request.form.get("entrada")

    # Verifica si entrada_usuario se capturó correctamente
    if not entrada_usuario:
        return "Error: La entrada del usuario no se capturó correctamente.", 400

    if request.method == "POST":
        nueva_respuesta = request.form['nueva_respuesta']
        if nueva_respuesta and entrada_usuario:  # Asegura que ambas entradas no estén vacías
            agregar_conocimiento(entrada_usuario, nueva_respuesta)
            return redirect(url_for("chat"))
        else:
            return "Error: No se pudo agregar el conocimiento. Verifica la entrada y la respuesta.", 400

    return render_template("nuevo.html", entrada=entrada_usuario)

if __name__ == "__main__":
    inicializar_db()
    app.run(debug=True, use_reloader=False)
