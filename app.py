from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")  # Sirve el index.html desde el mismo directorio

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Usar el puerto definido en Coolify
    app.run(host="0.0.0.0", port=port)
