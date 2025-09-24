from flask import Flask, render_template
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Información del servidor
    server_info = {
        'fecha_actual': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'python_version': os.sys.version,
        'ruta': os.getcwd()
    }
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>App en la Nube - Industria 4.0</title>
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                max-width: 800px; 
                margin: 50px auto; 
                padding: 20px;
                background-color: #f5f5f5;
            }}
            .container {{ 
                background: white; 
                padding: 30px; 
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            h1 {{ color: #2c3e50; }}
            .info {{ background: #e8f4f8; padding: 15px; border-radius: 5px; }}
            .success {{ color: #27ae60; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 ¡Hola desde la Nube!</h1>
            <p class="success">Aplicación desplegada exitosamente - Industria 4.0</p>
            
            <div class="info">
                <h3>📊 Información del Servidor:</h3>
                <p><strong>Fecha y hora:</strong> {server_info['fecha_actual']}</p>
                <p><strong>Python version:</strong> {server_info['python_version'].split()[0]}</p>
                <p><strong>Ruta:</strong> {server_info['ruta']}</p>
            </div>
            
            <h3>🔗 Rutas disponibles:</h3>
            <ul>
                <li><a href="/">🏠 Inicio</a></li>
                <li><a href="/info">ℹ️ Información</a></li>
                <li><a href="/saludo/TuNombre">👋 Saludo personalizado</a></li>
            </ul>
        </div>
    </body>
    </html>
    """

@app.route("/info")
def info():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Información - App Nube</title>
        <style>body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }</style>
    </head>
    <body>
        <h1>📋 Información de la Aplicación</h1>
        <p><strong>Tecnologías utilizadas:</strong></p>
        <ul>
            <li>Python Flask</li>
            <li>Render.com (Cloud Computing)</li>
            <li>HTML5 + CSS</li>
        </ul>
        <p><strong>Propósito:</strong> Práctica de Computación en la Nube - Industria 4.0</p>
        <a href="/">← Volver al inicio</a>
    </body>
    </html>
    """

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Saludo - App Nube</title>
        <style>
            body {{ font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }}
            .saludo {{ color: #e74c3c; font-size: 24px; }}
        </style>
    </head>
    <body>
        <h1>👋 ¡Hola {nombre}!</h1>
        <p class="saludo">Bienvenido a tu aplicación en la nube</p>
        <p>Esta es una demostración de computación en la nube con Flask.</p>
        <a href="/">← Volver al inicio</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)