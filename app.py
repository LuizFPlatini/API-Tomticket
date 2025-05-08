from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Token da API Tomticket
TOKEN = 'Seu Token do TomTicket aqui'
API_URL = f'https://api.tomticket.com/chamados/{TOKEN}/'

# Mapeamento de prioridades
PRIORIDADES = {
    1: 'Baixa',
    2: 'Média',
    3: 'Alta',
    4: 'Urgente'
}

@app.route('/')
def tomticket():
    url = "http://127.0.0.1:5000/api/chamados"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Erro ao buscar dados da API: {response.status_code}", 500

    data = response.json()
    chamados = data.get('data', [])

    # Filtros da URL
    filtro_categoria = request.args.get('categoria', '').lower()
    filtro_atendente = request.args.get('atendente', '').lower()
    filtro_prioridade = request.args.get('prioridade', '')

    PRIORIDADES = {1: 'Baixa', 2: 'Média', 3: 'Alta', 4: 'Urgente'}

    chamados_filtrados = []
    for chamado in chamados:
        chamado['prioridade'] = PRIORIDADES.get(chamado.get('prioridade'), 'Desconhecida')
        chamado['atendente'] = chamado.get('atendente') or 'Sem atendente'

        # Aplica filtros
        if filtro_categoria and filtro_categoria not in (chamado.get('categoria') or '').lower():
            continue
        if filtro_atendente and filtro_atendente not in (chamado.get('atendente') or '').lower():
            continue
        if filtro_prioridade and filtro_prioridade != chamado.get('prioridade'):
            continue

        chamados_filtrados.append(chamado)

    return render_template('TomTicket.html', chamados=chamados_filtrados)



@app.route('/api/chamados')
def listar_chamados():
    pagina = request.args.get('pagina', 1, type=int)
    idcliente = request.args.get('idcliente')
    tipo_identificacao = request.args.get('tipo_identificacao', 'I')
    situacao = request.args.get('situacao')
    ordem = request.args.get('ordem', 0, type=int)
    coluna = request.args.get('coluna', 'protocolo')

    url = f"{API_URL}{pagina}?tipo_identificacao={tipo_identificacao}&ordem={ordem}&coluna={coluna}"
    
    if idcliente:
        url += f"&idcliente={idcliente}"
    if situacao:
        url += f"&situacao={situacao}"

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"erro": "Erro ao acessar a API"}), 500

    try:
        data = response.json()
    except ValueError:
        return jsonify({"erro": "Resposta da API não é JSON válido"}), 500

    for chamado in data.get('chamados', []):
        prioridade_valor = chamado.get('prioridade')
        chamado['prioridade'] = PRIORIDADES.get(prioridade_valor, 'Desconhecida')
        chamado['atendente'] = chamado.get('atendente') or 'Sem atendente'

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
