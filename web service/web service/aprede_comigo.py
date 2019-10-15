import mysql
from bottle import route, run, response, request
import json
import mysql.connector

########################################################################################################################
#                                          DADOS DE LOGIN E AFINS                                                      #
########################################################################################################################

################################# login
@route('/loginCredenciais', method = 'POST')
def loginCredenciais():

    response.content_type = 'application/json;charset=utf-8'

    if "email" in request.json:
        email = int(request.json.get("email"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo email em falta"

    if "encarregado" in request.json:
        encarregado = request.json.get("encarregado")
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Encarregado em falta"

    if "pass" in request.json:
        password = request.json.get("pass")
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Pass em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.crianca SET email = %s, encarregado = %s, pass = %s where id_crianca=1;"
    args = (email, encarregado, password)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200


# confirmar pass
@route('/verificaCredenciais', method = "GET")
def verificaCredenciais():
    response.content_type = 'application/json;charset=utf-8'
    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                      database='AprendeComigo', user='projecto',
                                      password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1="SELECT pass FROM AprendeComigo.crianca;"
    cnx_cursor1.execute(sql1)

    coiso = []
    l = cnx_cursor1.fetchone()

    while l is not None:
         dic_verificaCredenciais = {"pass": l["pass"]}
         coiso += [dic_verificaCredenciais]
         l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso)


############################################################### CAIXA DE ENTRADA ######################################
@route('/caixaEntrada', method="GET")
def caixaEntrada():
    response.content_type = 'application/json;charset=utf-8'
    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                      database='AprendeComigo', user='projecto',
                                      password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    nada = []

    sql1 = "SELECT disciplina, ano FROM AprendeComigo.pergunta;"

    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()

    while l is not None:
        sei = {"disciplina": l["disciplina"], "ano": l["ano"]}
        nada += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()

    return json.dumps(nada)

####################################################################################################################
@route('/caixaVariavel', method="GET")
def caixaEntrada():
    response.content_type = 'application/json;charset=utf-8'

    dic_caixaIdoso = {"questoes": ["Português 1º ano", "Português 2º ano", "Português 3º ano", "Português 4º ano",
                               "Estudo do Meio 1º ano", "Estudo do Meio 2º ano", "Estudo do Meio 3º ano", "Estudo do Meio 4º ano",
                              "Matemática 1º ano", "Matemática 2º ano", "Matemática 3º ano", "Matemática 4º ano"]}
    return json.dumps(dic_caixaIdoso)
####################################################################################################################






########################################################################################################################
#                                          RESPOSTAS NÃO AUTOMATICAS                                                       #
########################################################################################################################


###########################################     PORTUGUÊS       ########################################################

#Português 1º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/portugues1/naoAutomatica/POST', method = "POST")
def portugues1NaoAutomaticaPost():
        response.content_type = 'application/json;charset=utf-8'

        if "resposta" in request.json:
            resposta = int(request.json.get("resposta"))
        else:
            response.status = 409
            response.content_type = 'text/plain'
            return "Campo resposta em falta"

        cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                      database='AprendeComigo', user='projecto',
                                      password='FfV7C3ijp5hb')

        cnx_cursor1 = cnx.cursor(dictionary=True)

        sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s where id_formulario=4;"
        args = (resposta)
        cnx_cursor1.execute(sql1, args)

        cnx.commit()
        cnx.close()

        response.status = 200

#MÉTODO 'GET' PARA LER NA BD
@route('/portugues1/naoAutomatica/get', method = "GET")
def portugues1NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'
    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta FROM AprendeComigo.formulario where id_formulario=4;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso2 = []

    while l is not None:
        sei = {"resposta": l["resposta"]}
        coiso2 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso2)




#Português 2º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/portugues2/naoAutomatica/POST', method = "POST")
def portugues2NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s where id_formulario=5;"
    args = (resposta)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200


#MÉTODO 'GET' PARA LER NA BD
@route('/portugues2/naoAutomatica/get', method = "GET")
def portugues2NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'
    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                              database='AprendeComigo', user='projecto',
                              password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta FROM AprendeComigo.formulario where id_formulario=5;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso3 = []

    while l is not None:
        sei = {"resposta": l["resposta"]}
        coiso3 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso3)




#Português 3º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/portugues3/naoAutomatica/post', method = "POST")
def portugues3NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s where id_formulario=6;"
    args = (resposta)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200

#MÉTODO 'GET' PARA LER NA BD
@route('/portugues3/naoAutomatica/get', method = "GET")
def portugues3NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'
    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                              database='AprendeComigo', user='projecto',
                              password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta FROM AprendeComigo.formulario where id_formulario=6;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso4 = []

    while l is not None:
        sei = {"resposta": l["resposta"]}
        coiso4 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso4)



#Português 4º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/portugues4/naoAutomatica/post', method = "POST")
def portugues4NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    if "respostab" in request.json:
        respostab = int(request.json.get("respostab"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostab em falta"

    if "respostac" in request.json:
        respostac = int(request.json.get("respostac"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostac em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s, respostab = %s, respostac = %s where id_formulario=7;"
    args = (resposta, respostab, respostac)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200

#MÉTODO 'GET' PARA LER NA BD
@route('/portugues4/naoAutomatica/get', method = "GET")
def portugues4NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'
    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                              database='AprendeComigo', user='projecto',
                              password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta, respostab, respostac FROM AprendeComigo.formulario where id_formulario=7;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso5 = []

    while l is not None:
        sei = {"resposta": l["resposta"], "respostab": l["respostab"], "respostac": l["respostac"]}
        coiso5 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso5)




##########################################     ESTUDO MEIO       #######################################################



#Estudo do Meio 1º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/estudoMeio1/naoAutomatica/get', method = "POST")
def estudoMeio1NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    if "respostab" in request.json:
        respostab = int(request.json.get("respostab"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostab em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s, respostab = %s where id_formulario= 8;"
    args = (resposta, respostab)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200



#MÉTODO 'POST' PARA PÔR NA BD
@route('/estudoMeio1/naoAutomatica/get', method = "GET")
def estudoMeio1NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                              database='AprendeComigo', user='projecto',
                              password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta, respostab FROM AprendeComigo.formulario where id_formulario=8;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso6 = []

    while l is not None:
        sei = {"resposta": l["resposta"], "respostab": l["respostab"]}
        coiso6 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso6)



#Estudo do Meio 2º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/estudoMeio2/naoAutomatica/post', method = "POST")
def estudoMeio2NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    if "respostab" in request.json:
        respostab = int(request.json.get("respostab"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostab em falta"

    if "respostac" in request.json:
        respostac = int(request.json.get("respostac"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostac em falta"

    if "respostad" in request.json:
        respostad = int(request.json.get("respostad"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostad em falta"

    if "respostae" in request.json:
        respostae = int(request.json.get("respostae"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostae em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                   database='AprendeComigo', user='projecto',
                                   password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s, respostab = %s, respostac = %s, , respostad = %s, , respostae = %s where id_formulario= 9;"
    args = (resposta, respostab, respostac, respostad, respostae)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200

#MÉTODO 'GET' PARA LER NA BD
@route('/estudoMeio2/naoAutomatica/get', method = "GET")
def estudoMeio2NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                              database='AprendeComigo', user='projecto',
                              password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta, respostab,respostac,respostad,respostae FROM AprendeComigo.formulario where id_formulario=9;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso7 = []

    while l is not None:
        sei = {"resposta": l["resposta"], "respostab": l["respostab"], "respostac": l["respostac"],"respostad": l["respostad"],"respostae": l["respostae"]}
        coiso7 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso7)



#Estudo do Meio 3º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/estudoMeio3/naoAutomatica/post', method = "POST")
def estudoMeio3NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    if "respostab" in request.json:
        respostab = int(request.json.get("respostab"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostab em falta"

    if "respostac" in request.json:
        respostac = int(request.json.get("respostac"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostac em falta"

    if "respostad" in request.json:
        respostad = int(request.json.get("respostad"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostad em falta"

    if "respostae" in request.json:
        respostae = int(request.json.get("respostae"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostae em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                   database='AprendeComigo', user='projecto',
                                   password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s, respostab = %s, respostac = %s, respostad = %s, , respostae = %s where id_formulario= 10;"
    args = (resposta, respostab, respostac, respostad, respostae)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200


#MÉTODO 'GET' PARA LER NA BD
@route('/estudoMeio3/naoAutomatica/get', method = "GET")
def estudoMeio3NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                              database='AprendeComigo', user='projecto',
                              password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta, respostab,respostac,respostad,respostae FROM AprendeComigo.formulario where id_formulario=10;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso8 = []

    while l is not None:
        sei = {"resposta": l["resposta"], "respostab": l["respostab"], "respostac": l["respostac"],"respostad": l["respostad"],"respostae": l["respostae"]}
        coiso8 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso8)



#Estudo do Meio 4º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/estudoMeio4/naoAutomatica/post', method = "POST")
def estudoMeio4NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    if "respostab" in request.json:
        respostab = int(request.json.get("respostab"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostab em falta"


    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                   database='AprendeComigo', user='projecto',
                                   password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s, respostab = %s where id_formulario= 11;"
    args = (resposta, respostab)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200

#MÉTODO 'GET' PARA LER NA BD
@route('/estudoMeio4/naoAutomatica/get', method = "GET")
def estudoMeio4NaoAutomaticaGet ():
    response.content_type = 'application/json;charset=utf-8'

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta, respostab FROM AprendeComigo.formulario where id_formulario=11;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso9 = []

    while l is not None:
        sei = {"resposta": l["resposta"], "respostab": l["respostab"]}
        coiso9 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso9)


##########################################     Matematica      #######################################################




#Matematica 1º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/matematica1/naoAutomatica/post', method = "POST")
def matematica1NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    if "respostab" in request.json:
        respostab = int(request.json.get("respostab"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostab em falta"

    if "respostac" in request.json:
        respostac = int(request.json.get("respostac"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostac em falta"

    if "respostad" in request.json:
        respostad = int(request.json.get("respostad"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostad em falta"

    if "respostae" in request.json:
        respostae = int(request.json.get("respostae"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostae em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                   database='AprendeComigo', user='projecto',
                                   password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s, respostab = %s, respostac = %s, , respostad = %s, , respostae = %s where id_formulario= 1;"
    args = (resposta, respostab, respostac, respostad, respostae)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200

#MÉTODO 'GET' PARA LER NA BD
@route('/matematica1/naoAutomatica/get', method = "GET")
def matematica1NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta, respostab,respostac,respostad,respostae FROM AprendeComigo.formulario where id_formulario=1;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso10 = []

    while l is not None:
        sei = {"resposta": l["resposta"], "respostab": l["respostab"], "respostac": l["respostac"],
               "respostad": l["respostad"], "respostae": l["respostae"]}
        coiso10 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso10)




#Matematica 2º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/matematica2/naoAutomatica/post', method = "POST")
def matematica2NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    if "respostab" in request.json:
        respostab = int(request.json.get("respostab"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo respostab em falta"


    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                   database='AprendeComigo', user='projecto',
                                   password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s, respostab = %s where id_formulario= 2;"
    args = (resposta, respostab)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200

#MÉTODO 'GET' PARA LER NA BD
@route('/matematica2/naoAutomatica/get', method = "GET")
def matematica2NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta, respostab FROM AprendeComigo.formulario where id_formulario=2;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso11 = []

    while l is not None:
        sei = {"resposta": l["resposta"], "respostab": l["respostab"]}
        coiso11 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso11)



#Matematica 3º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/matematica3/naoAutomatica/post', method="POST")
def matematica3NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "id_formulario" in request.json:
        id_formulario = int(request.json.get("id_formulario"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Id em falta"

    if "resposta" in request.json:
        resposta = request.json.get("resposta")
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Resposta em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s where id_formulario=%s;"
    args = (resposta, id_formulario)
    cnx_cursor1.execute(sql1, args)  # o args tem sempre que ser um tuplo. Se so tiver uma varivael entao tens de por virgula no final

    cnx.commit()
    cnx.close()

    response.status = 200


#MÉTODO 'GET' PARA LER NA BD
@route('/matematica3/naoAutomatica/get', method = "GET")
def matematica3NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'

    #
    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                database='AprendeComigo', user='projecto',
                                password='FfV7C3ijp5hb')

    # o cursor é responsavel pela interação com a bd
    cnx_cursor1 = cnx.cursor(dictionary=True)
    #
    dados={}
    #
    sql1 = "SELECT resposta FROM AprendeComigo.formulario where id_formulario=0;"
    #
    cnx_cursor1.execute(sql1)
    #
    l=cnx_cursor1.fetchone()
    #
    while l is not None:
        #dados["numeroGalinhas"]=l["resposta"]
        dados=l["resposta"]
        l=cnx_cursor1.fetchone()

    #
    cnx.close()

    return json.dumps(dados)



#Matematica 4º ano
#MÉTODO 'POST' PARA PÔR NA BD
@route('/matematica4/naoAutomatica/post', method = "POST")
def matematica4NaoAutomaticaPost():
    response.content_type = 'application/json;charset=utf-8'

    if "resposta" in request.json:
        resposta = int(request.json.get("resposta"))
    else:
        response.status = 409
        response.content_type = 'text/plain'
        return "Campo resposta em falta"

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                   database='AprendeComigo', user='projecto',
                                   password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)

    sql1 = "UPDATE AprendeComigo.formulario SET resposta = %s where id_formulario= 3;"
    args = (resposta)
    cnx_cursor1.execute(sql1, args)

    cnx.commit()
    cnx.close()

    response.status = 200

#MÉTODO 'GET' PARA LER NA BD
@route('/matematica4/naoAutomatica/get', method = "GET")
def matematica4NaoAutomaticaGet():
    response.content_type = 'application/json;charset=utf-8'

    cnx = mysql.connector.connect(host='projecto-mp5.cp7jwa5nhz40.us-east-1.rds.amazonaws.com',
                                  database='AprendeComigo', user='projecto',
                                  password='FfV7C3ijp5hb')

    cnx_cursor1 = cnx.cursor(dictionary=True)
    sql1 = "SELECT resposta FROM AprendeComigo.formulario where id_formulario=3;"
    cnx_cursor1.execute(sql1)

    l = cnx_cursor1.fetchone()
    coiso12 = []

    while l is not None:
        sei = {"resposta": l["resposta"]}
        coiso12 += [sei]
        l = cnx_cursor1.fetchone()

    cnx.close()
    return json.dumps(coiso12)


run(host='192.168.1.8', port=8080, debug=True)