# Importar as bibliotecas necessárias
from flask import Flask, jsonify
import pandas as pd

# Criação de uma planilha fictícia usando pandas
data = {
    'Nome': ['Ana', 'Pedro', 'João'],
    'Idade': [25, 32, 28],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df = pd.DataFrame(data)

# Criar uma instância da classe Flask
app = Flask(__name__)

# Definir uma rota para a API
@app.route('/api', methods=['GET'])
def api():
    # Converter o dataframe em um dicionário e depois em uma string JSON
    data = df.to_dict(orient='records')
    return jsonify(data)

# No colab, não é possível usar app.run(). Então, usamos um workaround com a biblioteca flask_ngrok
from flask_ngrok import run_with_ngrok
run_with_ngrok(app)

# Iniciar o servidor
app.run()
