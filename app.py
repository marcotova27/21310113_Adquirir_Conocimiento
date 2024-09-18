from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

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
    if request.method == "POST":
        entrada_usuario = request.form['entrada_usuario']
        respuesta = obtener_respuesta(entrada_usuario)

        if respuesta:
            return render_template("index.html", entrada=entrada_usuario, respuesta=respuesta)
        else:
            return redirect(url_for("nuevo_conocimiento", entrada=entrada_usuario))

    return render_template("index.html")

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo_conocimiento():
    entrada_usuario = request.args.get("entrada")
    if request.method == "POST":
        nueva_respuesta = request.form['nueva_respuesta']
        agregar_conocimiento(entrada_usuario, nueva_respuesta)
        return redirect(url_for("chat"))

    return render_template("nuevo.html", entrada=entrada_usuario)

if __name__ == "__main__":
    inicializar_db()
    app.run(debug=True)
