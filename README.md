<html>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f9f9f9;
            color: #333;
            padding: 20px;
        }

        h1 {
            color: #2c3e50;
            text-align: center;
        }

        h2 {
            color: #2980b9;
            margin-top: 20px;
        }

        p {
            margin: 10px 0;
        }

        pre {
            background-color: #ecf0f1;
            padding: 10px;
            border-left: 5px solid #3498db;
            overflow-x: auto;
        }

        code {
            color: #e74c3c;
        }

        .note {
            background-color: #e7f7ff;
            padding: 10px;
            border-left: 5px solid #3498db;
            margin: 10px 0;
        }

        .warning {
            background-color: #fff3cd;
            padding: 10px;
            border-left: 5px solid #ffcc00;
            margin: 10px 0;
        }

        .steps {
            margin-left: 20px;
            list-style-type: decimal;
        }

        .highlight {
            color: #16a085;
            font-weight: bold;
        }
    </style>
<body>

<h1>Chatbot con Flask y SQLite</h1>

<p>Este proyecto es un chatbot básico implementado con Flask y SQLite, que permite al chatbot aprender respuestas nuevas de los usuarios y almacenarlas en una base de datos.</p>

<h2>Características del Chatbot</h2>
<ul>
    <li>Responde a entradas predefinidas.</li>
    <li>Aprende nuevas respuestas y las guarda para futuras interacciones.</li>
    <li>Visualiza las últimas 5 interacciones entre el usuario y el chatbot.</li>
</ul>

<h2>Requisitos</h2>
<p>Para ejecutar este proyecto necesitas tener instalado:</p>
<ul>
    <li>Python 3.x</li>
    <li>Flask</li>
    <li>SQLite</li>
</ul>

<h2>Pasos para la Implementación</h2>
<ol class="steps">
    <li><span class="highlight">Clona el repositorio</span>:
        <pre><code>git clone https://github.com/tuusuario/chatbot-flask.git</code></pre>
    </li>
    <li><span class="highlight">Navega al directorio del proyecto</span>:
        <pre><code>cd chatbot-flask</code></pre>
    </li>
    <li><span class="highlight">Crea y activa un entorno virtual</span>:
        <pre><code>conda create --name sistemasExp python=3.8
conda activate sistemasExp</code></pre>
    </li>
    <li><span class="highlight">Instala las dependencias</span> desde el archivo <code>requirements.txt</code>:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><span class="highlight">Ejecuta la aplicación</span>:
        <pre><code>python app.py</code></pre>
    </li>
    <li>Abre tu navegador y visita <span class="highlight">http://127.0.0.1:5000/</span> para comenzar a interactuar con el chatbot.</li>
</ol>

<h2>Estructura del Proyecto</h2>
<p>La estructura del proyecto es la siguiente:</p>
<pre><code>
chatbot-flask/
├── app.py                 # Archivo principal de la aplicación Flask
├── requirements.txt       # Dependencias necesarias para ejecutar la aplicación
├── templates/             # Carpeta que contiene las plantillas HTML
│   ├── index.html         # Página web para interactuar con el chatbot
│   └── nuevo.html         # Página para ingresar nuevo conocimiento
├── static/                # Carpeta para archivos estáticos
│   └── styles.css         # Archivo CSS para el diseño de la página
├── database.db            # Base de datos SQLite que almacena las respuestas
└── README.md              # Archivo de documentación del proyecto
</code></pre>

<h2>Archivos Clave</h2>

<h3>1. <code>app.py</code></h3>
<p>Este es el archivo principal que contiene la lógica del chatbot, la conexión a la base de datos y las rutas de la aplicación Flask.</p>

<h3>2. <code>index.html</code> y <code>nuevo.html</code></h3>
<p>Las plantillas HTML que forman la interfaz de usuario del chatbot. Se encuentran dentro de la carpeta <code>templates/</code>.</p>

<h3>3. <code>styles.css</code></h3>
<p>Archivo CSS que contiene los estilos para las páginas del chatbot, mejorando la apariencia visual.</p>

<h2>Consideraciones</h2>
<div class="note">
    <p>Este proyecto está diseñado para funcionar en un entorno de desarrollo local. No debe usarse en un entorno de producción sin las configuraciones adecuadas de seguridad y un servidor WSGI como Gunicorn.</p>
</div>

<div class="warning">
    <p><strong>Nota:</strong> Asegúrate de no subir el archivo <code>database.db</code> a GitHub para evitar problemas de seguridad y tamaño. Usa un archivo <code>.gitignore</code> para excluirlo.</p>
</div>

<h2>Contribuciones</h2>
<p>Las contribuciones son bienvenidas. Si deseas mejorar el chatbot o agregar nuevas funcionalidades, siéntete libre de hacer un fork del proyecto y enviar un pull request.</p>

</body>
</html>
