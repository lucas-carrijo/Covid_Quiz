from banco import sql

mysql = sql.SQL("root", "test")

comando = "CREATE TABLE tb_info_usu (idt_usu INT AUTO_INCREMENT PRIMARY KEY, " + \
          "nme_usu VARCHAR(50) NOT NULL, " + \
          "age_usu INT NOT NULL, " + \
          "email VARCHAR(50) NOT NULL, " + \
          "sexo VARCHAR(3) NOT NULL, " + \
          "cidade VARCHAR(50) NOT NULL, " + \
          "uf_usu VARCHAR(2) NOT NULL);"

if mysql.executar(comando, ()):
    print ("Tabela criada!")