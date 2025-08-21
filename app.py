from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import json
import os

# Configuração da API
genai.configure(api_key="AIzaSyBrtcJCuoPl5rYM9w_wnWqY9NILAg0sXp4")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

# Memória persistente
MEMORIA_ARQUIVO = "memoria_usuario.json"
historico = []
MAX_MENSAGENS = 2  # apenas últimas 2 mensagens para contexto curto
informacoes_usuario = {}

# carregar memória se existir
if os.path.exists(MEMORIA_ARQUIVO):
    with open(MEMORIA_ARQUIVO, "r", encoding="utf-8") as f:
        informacoes_usuario = json.load(f)

def salvar_memoria():
    with open(MEMORIA_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(informacoes_usuario, f, ensure_ascii=False, indent=4)

def enviar_mensagem_web(mensagem_usuario):
    # detectar nome
    if "meu nome é" in mensagem_usuario.lower():
        nome = mensagem_usuario.lower().split("meu nome é")[-1].strip().capitalize()
        informacoes_usuario['nome'] = nome
        salvar_memoria()

    nome_usuario = informacoes_usuario.get('nome', "amigo")

    # adicionar mensagem ao histórico
    historico.append(f"Você: {mensagem_usuario}")
    mensagens_para_modelo = historico[-MAX_MENSAGENS:]

    # prompt curto e natural
    prompt = (
        f"Você é um assistente virtual positivo e empático, que conversa como um amigo. "
        f"Responda de forma curta, natural e encorajadora. Use o nome {nome_usuario} quando possível.\n\n"
    )
    prompt += "\n".join(mensagens_para_modelo)
    prompt += "\nAssistente:"

    resposta = model.generate_content(prompt)
    historico.append(f"Assistente: {resposta.text}")

    return resposta.text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    mensagem = request.json.get("mensagem")
    resposta = enviar_mensagem_web(mensagem)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
