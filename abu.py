from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    resposta = ""

    if request.method == "POST":
        mensagem = request.form["mensagem"].lower()

        if mensagem == "oi":
            resposta = "Olá!"

        elif mensagem == "tudo bem?":
            resposta = "Sim!"

        elif mensagem == "tchau":
            resposta = "Até mais!"

        else:
            try:
                resposta = str(eval(mensagem))
            except:
                resposta = "Não entendi"

    return f"""
    <h1>Meu Chatbot 🤖</h1>

    <form method="post">
        <input name="mensagem" placeholder="Digite algo">
        <button>ENVIAR</button>
    </form>

    <h3>BOT: {resposta}</h3>
    """

app.run(host="0.0.0.0", port=5000)