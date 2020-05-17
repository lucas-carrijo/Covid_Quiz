from banco import sql

mysql = sql.SQL("root", "test")

comando = "CREATE TABLE tb_infos_usua (idt_usu INT AUTO_INCREMENT PRIMARY KEY, " + \
          "nme_usu VARCHAR(50) NOT NULL, " + \
          "age_usu INT NOT NULL, " + \
          "email VARCHAR(50) NOT NULL, " + \
          "sexo VARCHAR(3) NOT NULL, " + \
          "cidade VARCHAR(50) NOT NULL, " + \
          "uf_usu VARCHAR(50) NOT NULL, " + \
          "perguntaum VARCHAR(1) NOT NULL, " + \
          "perguntadois VARCHAR(1) NOT NULL, " + \
          "perguntatres VARCHAR(1) NOT NULL, " + \
          "perguntaquatro VARCHAR(1) NOT NULL, " + \
          "perguntacinco VARCHAR(1) NOT NULL, " + \
          "perguntaseis VARCHAR(1) NOT NULL, " + \
          "perguntasete VARCHAR(1) NOT NULL, " + \
          "perguntaoito VARCHAR(1) NOT NULL, " + \
          "perguntanove VARCHAR(1) NOT NULL, " + \
          "perguntadez VARCHAR(1) NOT NULL); "

if mysql.executar(comando, ()):
    print ("Tabela criada!")