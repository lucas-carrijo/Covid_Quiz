from banco import sql
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('firstpage.html')

@app.route('/formincluir')
def formIncluir():
    return render_template('formIncluir.html')

@app.route('/formincluir', methods=['POST'])
def incluir():
    nome = request.form['nome']
    idade = request.form['idade']
    uf = request.form['uf']
    observacao = request.form['observacao']

    #incluindo no banco
    mysql = sql.SQL("root", "test")
    comando = "INSERT INTO tb_info_usu(nme_usu, age_usu, uf_usu, obs_usu) VALUES (%s, %s, %s, %s)"

    mysql.executar(comando, [nome, idade, uf, observacao])

    return render_template('formIncluir.html')



