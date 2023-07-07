import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loginmk2"
)
mycursor = mydb.cursor()

while True:
    print("Estudo de banco de dados Python&MySQL")                                  
    print("Selecione uma opção:")
    print("1 - Cadastro")
    print("2 - Login")

    escolha = input()

    if escolha == '1':                                                        
        username = input("*Escolha seu nome de usuário: ")
        while not username:
            print("É obrigatório responder aos campos com *")                  
            username = input("*Escolha seu nome de usuário: ")                     
        sql = "SELECT * FROM logins WHERE usuario = %s"                      
        ver = (username,)
        mycursor.execute(sql, ver)
        result = mycursor.fetchone()
        if result:
            print("Usuário já existe. Escolha outro nome de usuário.")
        else:
            usersenha = input("*Crie uma senha: ")                            
            while not usersenha:
                print("É obrigatório responder aos campos com *")
                usersenha = input("*Crie uma senha: ")
            contry = input("De onde você é? ")                                
            print("Cadastro realizado com sucesso !")                         

            sql = "INSERT INTO logins (usuario, senha, contry) VALUES (%s, %s, %s)"   
            val = (username, usersenha, contry)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Cadastro criado !")     
        reiniciar = input("Deseja voltar ao início? (S/N) ")
        if reiniciar.upper() != "S":
            break

    elif escolha == '2':                                                     
        confirmusername = input("Login: ")
        confirmpassword = input("Senha: ")
        sql = "SELECT * FROM logins WHERE usuario = %s AND senha = %s"        
        val = (confirmusername, confirmpassword)                              
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            print("Login bem-sucedido!")
        else:
            print("Usuário ou senha incorretos.")

    elif escolha >= '3':                                                     
        print("Comando inválido")

mydb.close()                                                           
