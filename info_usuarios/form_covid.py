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
    questao1 = request.form['questao1']
    questao2 = request.form['questao2']
    questao3 = request.form['questao3']
    questao4 = request.form['questao4']
    questao5 = request.form['questao5']
    questao6 = request.form['questao6']
    questao7 = request.form['questao7']
    questao8 = request.form['questao8']
    questao9 = request.form['questao9']
    questao10 = request.form['questao10']
    #incluindo no banco
    mysql = sql.SQL("root", "test")
    comando = "INSERT INTO tb_infos_usua(nme_usu, age_usu, email, sexo, cidade, uf_usu, perguntaum, perguntadois, perguntatres, perguntaquatro, perguntacinco, perguntaseis, perguntasete, perguntaoito, perguntanove, perguntadez) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    if mysql.executar(comando, [nome, idade, email, sexo, cidade, uf, questao1, questao2, questao3, questao4, questao5, questao6, questao7, questao8, questao9, questao10]):
        msg = "Usuário " + nome + " cadastrado com sucesso! Questionario Liberado"
    else:
        msg = "Falha na inclusão de Usuário."

    return render_template('resultado.html', msg=msg)

@app.route('/resultado')
def resultados():
    return render_template('resultado.html')


@app.route('/gabarito')
def gabarito():
    return render_template('gabarito.html')

@app.route('/estatisticas')
def estatisticas():
    mysql = sql.SQL("root", "test")

    comando = "select 'total' idt_usu, count(idt_usu) from tb_infos_usua;"
    cs = mysql.consultar(comando, ())
    busca = ""

    for[total, nome] in cs:

        busca += "<h2>" + total + "</h2>"
        busca += "<h2>" + str(nome) + "</h2>"

    comando = "select 'total' idt_usu, count(idt_usu) from tb_infos_usua where perguntatres='V';"
    cs = mysql.consultar(comando, ())
    buscadois = ""

    for [total, nome] in cs:
        buscadois += "<h2>" + total + "</h2>"
        buscadois += "<h2>" + str(nome) + "</h2>"

    comando = "select 'total' idt_usu, count(idt_usu) from tb_infos_usua where perguntaoito='V';"
    cs = mysql.consultar(comando, ())
    buscatres = ""

    for [total, nome] in cs:
        buscatres += "<h2>" + total + "</h2>"
        buscatres += "<h2>" + str(nome) + "</h2>"

    comando = "select 'total' idt_usu, count(idt_usu) from tb_infos_usua where perguntadez='V' and age_usu between 20 and 40;"
    cs = mysql.consultar(comando, ())
    buscaquatro = ""

    for [total, nome] in cs:
        buscaquatro += "<h2>" + total + "</h2>"
        buscaquatro += "<h2>" + str(nome) + "</h2>"

    cs.close()
    return render_template('estatisticas.html', totais=busca, totaisdois=buscadois, totaistres=buscatres, totaisquatro=buscaquatro)
