from flask import Flask, request, jsonify
from scrape import get_google_suggestions
import os
import json  
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) 

BASE_PATH = os.path.join(os.path.dirname(__file__), "data", "base.json")

def load_data():
    """Carrega os dados do arquivo JSON."""
    if not os.path.exists(BASE_PATH):
        return []  
    with open(BASE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    """Salva os dados no arquivo JSON."""
    with open(BASE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    """Rota para obter sugestões de autocomplete."""
    q = request.args.get("q", "").lower()
    data = load_data() 
    resultados = [item for item in data if q in item.lower()]  
    return jsonify(resultados)  

@app.route("/autocomplete/scrape", methods=["POST"])
def autocomplete_scrape():
    """Rota para realizar scraping e adicionar sugestões ao arquivo JSON."""
    body = request.get_json() 
    base = body.get("base", "")
    
    if not base:
        return jsonify({"erro": "base ausente"}), 400  

    data = load_data()
    

    resultados_existentes = [item for item in data if base.lower() in item.lower()]
    
    if resultados_existentes:
        
        return jsonify({"sugestoes_existentes": resultados_existentes})

   
    sugestoes = get_google_suggestions(base)
    adicionados = []


    for item in sugestoes:
        if item not in data:
            data.append(item)
            adicionados.append(item)

    save_data(data) 
    return jsonify({"adicionados": adicionados}) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True) 
