

#Bruno Fortaleza, Lucas Gabriel, Nalberthy Sousa


import csv
import time

def analizador(arquivo):
    arq = open(arquivo,'r')
    linhas = csv.reader(arq)

    cont = 2

    dados= []


    for linha in linhas:
        dados.append(linha[0])


    n = dados[0]
    t = dados[1]
    d = dados[2:]
    p = 0

    status= False
    for i in d:
        cont+= 1

        if n == i:
            p = cont
            status = True

    if status == False:
        p=-1



    print(p)
    print(status)
    arq.close()

    return str(p)+"\n"+str(status)




ini = time.time()
dados = analizador('dataset-1-c.csv')
fim = time.time()
r = fim-ini


arq = open('saida.txt', 'w')

arq.write(dados+"\n"+str(r))
arq.close()


