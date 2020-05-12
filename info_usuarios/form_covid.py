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
    email = request.form['email']
    sexo = request.form['sexo']
    cidade = request.form['cidade']
    uf = request.form['uf']

    #incluindo no banco
    mysql = sql.SQL("root", "test")
    comando = "INSERT INTO tb_info_usu(nme_usu, age_usu, email_usu, sexo_usu, cidade_usu, uf_usu) VALUES (%s, %s, %s, %s, %s, %s)"

    mysql.executar(comando, [nome, idade, email, sexo, cidade, uf])

    return render_template('formIncluir.html')



