
    var ponto=0;
    function pontuacao(form) {
     for (var i=0;i<form.length;i++){
      if (form[i].checked){
       break
      }
     }
     var resposta=""
     if (i<form.length){
      resposta = form[i].value
     }
     return resposta;
    }

    function resultado(form) {
     var pontos= 0 
     var comentarios = ""
     var res = document.getElementById('res')
     if (pontuacao(form.questao1)=="V") {pontos+=1}
     if (pontuacao(form.questao2)=="F") {pontos+=1}
     if (pontuacao(form.questao3)=="F") {pontos+=1}
     if (pontuacao(form.questao4)=="F") {pontos+=1}
     if (pontuacao(form.questao5)=="V") {pontos+=1}
     if (pontuacao(form.questao6)=="V") {pontos+=1}
     if (pontuacao(form.questao7)=="V") {pontos+=1}
     if (pontuacao(form.questao8)=="V") {pontos+=1}
     if (pontuacao(form.questao9)=="F") {pontos+=1}
     if (pontuacao(form.questao10)=="F") {pontos+=1}

    
    if (pontos == 0){comentarios ='Você não acertou nem uma questão'}
    if (pontos == 1){comentarios+=`Que pena Você acertou apenas ${pontos} Questão`}
    if (pontos == 2){comentarios+=`Que pena Você acertou apenas ${pontos} Questão`}
    if (pontos == 3){comentarios+=`Que pena Você acertou apenas ${pontos} Questão`}
    if (pontos == 4){comentarios+=`Que pena Você acertou apenas ${pontos} Questão`}
    if (pontos == 5){comentarios+=`Você teve ${pontos} Acertos tente novamente`}
    if (pontos == 6){comentarios+=`Muito bom seu Resultado foi ${pontos} questões corretas`}
    if (pontos == 7){comentarios+=`Muito bom seu Resultado foi ${pontos} questões corretas`}
    if (pontos == 8){comentarios+=`Muito bom seu Resultado foi ${pontos} questões corretas`}
    if (pontos == 9){comentarios+=`Muito bom seu Resultado foi ${pontos} questões corretas`}
    if (pontos == 10){comentarios+=`Parábens Você acertou todas as ${pontos} questões`}

        alert(`${comentarios}`)
       
}

function enviar(){
    window.location.replace("resultado.html")
}