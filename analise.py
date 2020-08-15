

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

    arq.close()

    return str(status)+"\n"+str(p)



def dataset_a():
    ini = time.time()
    dados = analizador('dataset-1-a.csv')
    fim = time.time()
    r = fim-ini


    arq = open('resposta-dataset-1-a.txt', 'w')

    arq.write(dados+"\n"+str(r))
    arq.close()

def dataset_b():
    ini = time.time()
    dados = analizador('dataset-1-b.csv')
    fim = time.time()
    r = fim-ini


    arq = open('resposta-dataset-1-b.txt', 'w')

    arq.write(dados+"\n"+str(r))
    arq.close()

def dataset_c():
    ini = time.time()
    dados = analizador('dataset-1-c.csv')
    fim = time.time()
    r = fim-ini


    arq = open('resposta-dataset-1-c.txt', 'w')

    arq.write(dados+"\n"+str(r))
    arq.close()

dataset_a()
dataset_b()
dataset_c()
