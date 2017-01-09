import os
from shutil import copy

#for nome in os.listdir('.'):
#    novo_nome = 'MEET_' + nome
#    os.rename(nome, novo_nome)
#print 'OK'
#
#a = []
#for x in range (5):
#    a.append(x)
#    print (a)

def copiar (origem, destino):
    print (origem, destino)
    if not os.path.exists(destino):
        os.makedirs(destino)
    for nomeArq in os.listdir(origem):
        nomeArq = origem + "\\" + nomeArq 
        copy(nomeArq, destino)


def rename(endereco, indice):
    for nomeArq in os.listdir(endereco):
        filename, file_extension = os.path.splitext(nomeArq)
        if index < 10 :
            nvNome = "Teste-TBBT-S09-E0%d" %indice
        else:
            nvNome = "Teste-TBBT-S09-E%d" %indice
        nvNome = endereco + "\\" + nvNome + file_extension
        nomeArq = endereco + "\\" + nomeArq
        os.rename(nomeArq, nvNome)


pasta = "C:\\Users\\thyag\\Desktop\\TBBT-S09-HDTV\\"
finalizado = "C:\\Users\\thyag\\Desktop\\TBBT-S09-HDTV\\TBBT-S09"
caminhos = [os.path.join(pasta, nome ) for nome in os.listdir(pasta)]
for index, caminho in enumerate(caminhos):
    rename(caminho, index +1 )
    copiar(caminho, finalizado)
print ("OK")