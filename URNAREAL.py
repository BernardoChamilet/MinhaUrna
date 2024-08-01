import graphics as gf
import time
janela = gf.GraphWin('Urna Eletrônica',600,400)
def desenhaUrna():
    urna = gf.Rectangle(gf.Point(50,50),gf.Point(550,350))
    urna.setFill("gray")
    urna.draw(janela)
    teclado = gf.Rectangle(gf.Point(340,85),gf.Point(530,335))
    teclado.setFill("black")
    teclado.draw(janela)
    tela = gf.Rectangle(gf.Point(70,85),gf.Point(320,335))
    tela.setFill("white")
    tela.draw(janela)
    tecla1 = gf.Rectangle(gf.Point(370,95),gf.Point(400,125))
    tecla1.setOutline("white")
    tecla1.draw(janela)
    texto1 = gf.Text(gf.Point(385,110),"1")
    texto1.setSize(20)
    texto1.setTextColor("white")
    texto1.draw(janela) 
    tecla2 = gf.Rectangle(gf.Point(420,95),gf.Point(450,125))
    tecla2.setOutline("white")
    tecla2.draw(janela)
    texto2 = gf.Text(gf.Point(435,110),"2")
    texto2.setSize(20)
    texto2.setTextColor("white")
    texto2.draw(janela) 
    tecla3 = gf.Rectangle(gf.Point(470,95),gf.Point(500,125))
    tecla3.setOutline("white")
    tecla3.draw(janela)
    texto3 = gf.Text(gf.Point(485,110),"3")
    texto3.setSize(20)
    texto3.setTextColor("white")
    texto3.draw(janela) 
    tecla4 = gf.Rectangle(gf.Point(370,145),gf.Point(400,175))
    tecla4.setOutline("white")
    tecla4.draw(janela)
    texto4 = gf.Text(gf.Point(385,160),"4")
    texto4.setSize(20)
    texto4.setTextColor("white")
    texto4.draw(janela) 
    tecla5 = gf.Rectangle(gf.Point(420,145),gf.Point(450,175))
    tecla5.setOutline("white")
    tecla5.draw(janela)
    texto5 = gf.Text(gf.Point(435,160),"5")
    texto5.setSize(20)
    texto5.setTextColor("white")
    texto5.draw(janela) 
    tecla6 = gf.Rectangle(gf.Point(470,145),gf.Point(500,175))
    tecla6.setOutline("white")
    tecla6.draw(janela)
    texto6 = gf.Text(gf.Point(485,160),"6")
    texto6.setSize(20)
    texto6.setTextColor("white")
    texto6.draw(janela) 
    tecla7 = gf.Rectangle(gf.Point(370,195),gf.Point(400,225))
    tecla7.setOutline("white")
    tecla7.draw(janela)
    texto7 = gf.Text(gf.Point(385,210),"7")
    texto7.setSize(20)
    texto7.setTextColor("white")
    texto7.draw(janela) 
    tecla8 = gf.Rectangle(gf.Point(420,195),gf.Point(450,225))
    tecla8.setOutline("white")
    tecla8.draw(janela)
    texto8 = gf.Text(gf.Point(435,210),"8")
    texto8.setSize(20)
    texto8.setTextColor("white")
    texto8.draw(janela) 
    tecla9 = gf.Rectangle(gf.Point(470,195),gf.Point(500,225))
    tecla9.setOutline("white")
    tecla9.draw(janela)
    texto9 = gf.Text(gf.Point(485,210),"9")
    texto9.setSize(20)
    texto9.setTextColor("white")
    texto9.draw(janela) 
    tecla0 = gf.Rectangle(gf.Point(420,245),gf.Point(450,275))
    tecla0.setOutline("white")
    tecla0.draw(janela)
    texto0 = gf.Text(gf.Point(435,260),"0")
    texto0.setSize(20)
    texto0.setTextColor("white")
    texto0.draw(janela) 
    teclaBranco = gf.Rectangle(gf.Point(355,295),gf.Point(400,325))
    teclaBranco.setFill("white")
    teclaBranco.draw(janela)
    textoBranco = gf.Text(gf.Point(379,310),"BRANCO")
    textoBranco.setSize(8)
    textoBranco.setTextColor("black")
    textoBranco.draw(janela) 
    teclaVermelho = gf.Rectangle(gf.Point(414,295),gf.Point(459,325))
    teclaVermelho.setOutline("white")
    teclaVermelho.setFill("red")
    teclaVermelho.draw(janela)
    textoCorrige = gf.Text(gf.Point(437,310),"CORRIGE")
    textoCorrige.setSize(8)
    textoCorrige.setTextColor("black")
    textoCorrige.draw(janela) 
    teclaVerde = gf.Rectangle(gf.Point(470,290),gf.Point(524,325))
    teclaVerde.setOutline("white")
    teclaVerde.setFill("Green")
    teclaVerde.draw(janela)
    textoConfirma = gf.Text(gf.Point(498,309),"CONFIRMA")
    textoConfirma.setSize(8)
    textoConfirma.setTextColor("black")
    textoConfirma.draw(janela) 
    teclaFim = gf.Rectangle(gf.Point(470,245),gf.Point(524,275))
    teclaFim.setOutline("white")
    teclaFim.setFill("orange")
    teclaFim.draw(janela)
    textoFim = gf.Text(gf.Point(498,260),"FIM")
    textoFim.setSize(8)
    textoFim.setTextColor("black")
    textoFim.draw(janela) 

def pegaTecla():
    coordenada = janela.getMouse()
    if (coordenada.getX() >=370 and coordenada.getX() <= 400) and (coordenada.getY() >= 95 and coordenada.getY() <= 125):
        return("1")
    if (coordenada.getX() >=420 and coordenada.getX() <= 450) and (coordenada.getY() >= 95 and coordenada.getY() <= 125):
        return("2")
    if (coordenada.getX() >=470 and coordenada.getX() <= 500) and (coordenada.getY() >= 95 and coordenada.getY() <= 125):
        return("3")
    if (coordenada.getX() >=370 and coordenada.getX() <= 400) and (coordenada.getY() >= 145 and coordenada.getY() <= 175):
        return("4")
    if (coordenada.getX() >=420 and coordenada.getX() <= 450) and (coordenada.getY() >= 145 and coordenada.getY() <= 175):
        return("5")
    if (coordenada.getX() >=470 and coordenada.getX() <= 500) and (coordenada.getY() >= 145 and coordenada.getY() <= 175):
        return("6")
    if (coordenada.getX() >=370 and coordenada.getX() <= 400) and (coordenada.getY() >= 195 and coordenada.getY() <= 225):
        return("7")
    if (coordenada.getX() >=420 and coordenada.getX() <= 450) and (coordenada.getY() >= 195 and coordenada.getY() <= 225):
        return("8")
    if (coordenada.getX() >=470 and coordenada.getX() <= 500) and (coordenada.getY() >= 195 and coordenada.getY() <= 225):
        return("9")
    if (coordenada.getX() >= 420 and coordenada.getX() <= 450) and (coordenada.getY() >= 245 and coordenada.getY() <= 275):
        return("0")
    if (coordenada.getX() >=355 and coordenada.getX() <= 400) and (coordenada.getY() >= 295 and coordenada.getY() <= 325):
        return("branco")
    if (coordenada.getX() >=414 and coordenada.getX() <= 459) and (coordenada.getY() >= 295 and coordenada.getY() <= 325):
        return("corrige")
    if (coordenada.getX() >=470 and coordenada.getX()) <= 524 and (coordenada.getY() >= 290 and coordenada.getY() <= 325):
        return("confirma")
    if (coordenada.getX() >=470 and coordenada.getX()) <= 524 and (coordenada.getY() >= 245 and coordenada.getY() <= 275):
        return("fim")
    return(False)
desenhaUrna()
quadrado1 = gf.Rectangle(gf.Point(85,280),gf.Point(115,320))
quadrado1.setOutline("black")
quadrado1.draw(janela)
quadrado2 = gf.Rectangle(gf.Point(120,280),gf.Point(150,320))
quadrado2.setOutline("black")
quadrado2.draw(janela)
#listaN é a lista com os gf.text de cada tecla em cada posição
listaN = []
cont = 0
a = 100
while cont < 10:
    while a < 141:
        numero = gf.Text(gf.Point(a,300),str(cont))
        numero.setSize(30)
        numero.setTextColor("black")
        listaN.append(numero)
        a += 35
    a = 100
    cont += 1
numero = gf.Text(gf.Point(190,250),"BRANCO")
numero.setSize(30)
numero.setTextColor("black")
listaN.append(numero)
#abrindo arquivos e transformando em listas
presidentes = open("presidentes.txt","r")
tpresidentes = presidentes.read()
presidentes.close()
governadores = open("governadores.txt","r")
tgovernadores = governadores.read()
governadores.close()
listaPresidentes = tpresidentes.split("\n")
contcand = 0
while contcand < len(listaPresidentes):
    listaPresidentes[contcand] = listaPresidentes[contcand].split(";")
    contcand += 1
listaGovernadores = tgovernadores.split("\n")
contcand = 0
while contcand < len(listaGovernadores):
    listaGovernadores[contcand] = listaGovernadores[contcand].split(";")
    contcand += 1
#criando listas com numeros válidos para apertar confirma
NumerosValidos = ["branco"]
contcand = 0
while contcand < len(listaPresidentes):
    NumerosValidos.append(listaPresidentes[contcand][0])
    contcand += 1
#criando o nome do cargo que a pessoa ta votando que vai aparecer no topo da tela
topoG = gf.Text(gf.Point(150,110),"Governador")
topoG.setSize(15)
topoG.setTextColor("black")
topoP = gf.Text(gf.Point(150,110),"Presidente")
topoP.setSize(15)
topoP.setTextColor("black")
#criando o texto de senha de encerramento
topoFim = gf.Text(gf.Point(195,110),"Senha de encerramento.")
topoFim.setSize(15)
topoFim.setTextColor("black")
topoFim2 = gf.Text(gf.Point(195,130),"(digite 00 caso queira voltar)")
topoFim2.setSize(14)
topoFim2.setTextColor("black")
topoErrou = gf.Text(gf.Point(190,180),"Senha errada")
topoErrou.setSize(15)
topoErrou.setTextColor("red")
topoAcertou = gf.Text(gf.Point(190,180),"Eleiçao encerrada!")
topoAcertou.setSize(20)
topoAcertou.setTextColor("black")
#Criando listas com numeros dos candidatos e os gf.texts e gf.image de cada um
cont = 0
cont2 = 1
y = 290
while cont < len(listaPresidentes):
    while cont2 < 4:
        texto = gf.Text(gf.Point(240,y),listaPresidentes[cont][cont2])
        texto.setSize(10)
        texto.setTextColor("black")
        listaPresidentes[cont][cont2] = texto 
        cont2 += 1
        y += 15
    cont2 = 1
    cont += 1
    y = 290
cont = 0
cont2 = 4
y = 140
while cont < len(listaPresidentes):
    while cont2 < 6:
        imagem = gf.Image(gf.Point(y,200),listaPresidentes[cont][cont2])
        listaPresidentes[cont][cont2] = imagem
        cont2 += 1
        y += 120
    cont2 = 4
    cont += 1
    y = 140
cont = 0
cont2 = 1
y = 290
while cont < len(listaGovernadores):
    while cont2 < 4:
        texto = gf.Text(gf.Point(240,y),listaGovernadores[cont][cont2])
        texto.setSize(10)
        texto.setTextColor("black")
        listaGovernadores[cont][cont2] = texto 
        cont2 += 1
        y += 15
    cont2 = 1
    cont += 1
    y = 290
cont = 0
cont2 = 4
y = 140
while cont < len(listaGovernadores):
    while cont2 < 6:
        imagem = gf.Image(gf.Point(y,200),listaGovernadores[cont][cont2])
        listaGovernadores[cont][cont2] = imagem
        cont2 += 1
        y += 120
    cont2 = 4
    cont += 1
    y = 140
#programa de fato
cont = 0
Digitadas = [] 
contcargo = 3
StringDigitada = ""
desenhado = False
senhaCerta = "12"
acertou = False
while True:
    #definindo cargo
    if contcargo % 2 == 0:
        listaCanditado = listaPresidentes
        topoP.draw(janela)
        nomedoArquivo = "votospresidente.txt"
        arquivoVotos = open(nomedoArquivo,"r")
        textoVotos = arquivoVotos.read()
        arquivoVotos.close()
    else:
        listaCanditado = listaGovernadores
        topoG.draw(janela)
        nomedoArquivo = "votosgovernador.txt"
        arquivoVotos = open(nomedoArquivo,"r")
        textoVotos = arquivoVotos.read()
        arquivoVotos.close()
    while cont < 3:
        numero = pegaTecla()
        #se tecla for um numero ou branco
        if cont != 2:
            if numero == "branco" and cont == 0:
                cont += 2
                listaN[20].draw(janela)
                digitada = listaN[20]
                Digitadas.append(digitada)
                StringDigitada += numero
            if numero != "branco" and numero != False and numero != "corrige" and numero != "confirma" and numero != "fim":
                if cont == 0:
                    listaN[int(numero)*2].draw(janela)
                    digitada = listaN[int(numero)*2]
                    Digitadas.append(digitada)
                    StringDigitada += numero
                if cont == 1:
                    listaN[(int(numero)*2)+1].draw(janela)
                    digitada = listaN[(int(numero)*2)+1]
                    Digitadas.append(digitada)
                    StringDigitada += numero
                cont += 1
        #se tecla for corrige
        if numero == "corrige":
            cont2 = 0
            while cont2 < len(Digitadas):
                Digitadas[cont2].undraw()
                cont2 += 1
            Digitadas = []
            if cont == 2 and StringDigitada in NumerosValidos and StringDigitada != "branco":
                nome.undraw()
                nome2.undraw()
                nome3.undraw()
                foto1.undraw()
                foto2.undraw()
            cont = 0
            StringDigitada = ""
            desenhado = False
        if cont == 2:
            #se tecla for confirma
            if numero == "confirma" and StringDigitada in NumerosValidos:
                cont2 = 0
                while cont2 < len(Digitadas):
                    Digitadas[cont2].undraw()
                    cont2 += 1
                Digitadas = []
                cont = 4
                if StringDigitada != "branco":
                    nome.undraw()
                    nome2.undraw()
                    nome3.undraw()
                    foto1.undraw()
                    foto2.undraw()
                desenhado = False
                #contando votos
                listaVotos = textoVotos.split("\n")
                cont2 = 0
                while cont2 < len(listaVotos):
                    listaVotos[cont2] = listaVotos[cont2].split(";")
                    cont2 += 1
                cont2 = 0
                while cont2 < len(listaVotos):
                    if StringDigitada == listaVotos[cont2][0]:
                        listaVotos[cont2][2] = str(int(listaVotos[cont2][2]) + 1)
                    cont2 += 1
                cont2 = 0
                while cont2 < len(listaVotos):
                    listaVotos[cont2] = ";".join(listaVotos[cont2])
                    cont2 += 1
                textoVotos = "\n".join(listaVotos)
                arquivoVotos = open(nomedoArquivo,"w")
                arquivoVotos.write(textoVotos)
                arquivoVotos.close()
                StringDigitada = ""
            #mostrando coisas na tela caso numero seja valido
            if StringDigitada in NumerosValidos and desenhado == False:
                if StringDigitada != "branco":
                    contador = 0
                    while contador < len(listaCanditado):
                        if StringDigitada == listaCanditado[contador][0]:
                            nome = listaCanditado[contador][1]
                            nome.draw(janela)
                            nome2 = listaCanditado[contador][2]
                            nome2.draw(janela)
                            nome3 = listaCanditado[contador][3]
                            nome3.draw(janela)
                            foto1 = listaCanditado[contador][4]
                            foto1.draw(janela)
                            foto2 = listaCanditado[contador][5]
                            foto2.draw(janela)
                            desenhado = True
                        contador += 1
        #tecla fim e suas opcoes
        if numero == "fim" and contcargo % 2 != 0:
            cont2 = 0
            while cont2 < len(Digitadas):
                Digitadas[cont2].undraw()
                cont2 += 1
            Digitadas = []
            if cont == 2 and StringDigitada in NumerosValidos and StringDigitada != "branco":
                nome.undraw()
                nome2.undraw()
                nome3.undraw()
                foto1.undraw()
                foto2.undraw()
            StringDigitada = ""
            desenhado = False
            topoG.undraw()
            topoFim.draw(janela)
            topoFim2.draw(janela)
            cont5 = 0
            senhaTentada = ""
            while cont5 < 2:
                senha = pegaTecla()
                if senha != False and senha != "confirma" and senha != "fim" and senha != "branco" and senha != "corrige":
                    senhaTentada += senha
                    if cont5 == 0:
                        digito1 = listaN[int(senha)*2]
                        digito1.draw(janela)
                    else:
                        digito2 = listaN[(int(senha)*2)+1]
                        digito2.draw(janela)
                    cont5 += 1
                #00, senha certa ou errada
                if len(senhaTentada) == 2:
                    if senhaTentada == senhaCerta:
                        cont = 4
                        topoAcertou.draw(janela)
                        acertou = True
                    elif senhaTentada == "00":
                        cont = 0
                        if acertou == True:
                            topoAcertou.undraw()
                        topoFim.undraw()
                        topoFim2.undraw()
                        topoG.draw(janela)
                        digito1.undraw()
                        digito2.undraw()
                    else:
                        cont5 = 0
                        senhaTentada = ""
                        topoErrou.draw(janela)
                        time.sleep(0.5)
                        topoErrou.undraw()
                        digito1.undraw()
                        digito2.undraw()
                        if acertou == True:
                            topoAcertou.undraw()
                #corrige senha
                if senha == "corrige" and len(senhaTentada) == 1:
                    digito1.undraw()
                    senhaTentada = ""
                    cont5 = 0
    cont = 0
    if contcargo % 2 == 0:
        topoP.undraw()
    else:
        #registrando resultado e finalizando o programa
        if acertou == True:
            arquivoP = open("votospresidente.txt","r")
            textoP = arquivoP.read()
            arquivoP.close()
            arquivoG = open("votosgovernador.txt","r")
            textoG = arquivoG.read()
            arquivoG.close()
            listaP = textoP.split("\n")
            listaG = textoG.split("\n")
            cont2 = 0
            while cont2 < len(listaP):
                listaP[cont2] = listaP[cont2].split(";")
                cont2 += 1
            cont2 = 0
            while cont2 < len(listaG):
                listaG[cont2] = listaG[cont2].split(";")
                cont2 += 1
            totalvotos = 0
            cont2 = 0
            while cont2 < len(listaP):
                totalvotos = totalvotos + int(listaP[cont2][2])
                cont2 += 1
            textoRP = "Presidente"
            cont2 = 0
            while cont2 < len(listaP):
                textoRP += "\n" + listaP[cont2][1] + ":" + listaP[cont2][2] + " Porcentagem:" + str((((int(listaP[cont2][2]))/(totalvotos))*100))[0:4] + "%"
                cont2 += 1
            textoRG = "Governador"
            cont2 = 0
            while cont2 < len(listaG):
                textoRG += "\n" + listaG[cont2][1] + ":" + listaG[cont2][2] + " Porcentagem:" + str((((int(listaG[cont2][2]))/(totalvotos))*100))[0:4] + "%"
                cont2 += 1
            arquivoR = open("resultadoseleicao.txt","w")
            arquivoR.write(textoRP + "\n" + textoRG)
            arquivoR.close()
            time.sleep(1)
            break
        topoG.undraw()
    contcargo += 1