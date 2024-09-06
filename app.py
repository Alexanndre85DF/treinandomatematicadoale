from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogo')
def jogo():
    return render_template('jogo.html')

@app.route('/verificar', methods=['POST'])
def verificar():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    resposta = request.form['resposta']
    
    try:
        resposta = int(resposta)
    except ValueError:
        return render_template('jogo.html', mensagem="Por favor, insira um número válido!", num1=num1, num2=num2)

    resultado_correto = num1 * num2
    if resposta == resultado_correto:
        mensagem = "Você acertou, parabéns!"
    else:
        mensagem = f"Errado, a resposta correta é {resultado_correto}."

    return render_template('jogo.html', mensagem=mensagem, num1=num1, num2=num2)

if __name__ == '__main__':
    app.run(debug=True)
