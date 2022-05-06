import shutil

def escreve_arquivo(texto):
    arq = open('/home/casa/Documentos/python/arquivos/notas.txt','w')#open cria(se não existir) ou abre um arquivo
    arq.write(texto)# write sobrescreve o conteúdo do arquivo
    arq.close()

def atualiza_arquivo(nome_arquivo, texto):
    caminho = '/home/casa/Documentos/python/arquivos/'+nome_arquivo
    arq = open(caminho,'a')#'a' usado quando se quer adicionar conteudo no arquivo
    arq.write(texto)
    arq.close()

def ler_arquivo(nome_arquivo):
    arq = open('/home/casa/Documentos/python/arquivos/'+nome_arquivo,'r')
    conteudo = arq.read()
    print(conteudo)

def media_notas(nome_arquivo):
    arq = open('/home/casa/Documentos/python/arquivos/'+nome_arquivo,'r')
    aluno_nota = arq.read()
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for i in aluno_nota:
        lista_notas = i.split('.')
        alunos = lista_notas[0]
        lista_notas.pop(0)#removendo o nome, para ficar só com as notas
        media = lambda notas: sum([int(i) for i in notas]) / 4 #convertendo a lista para inteiro e retornando a media
        lista_media.append({alunos: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy('/home/casa/Documentos/python/arquivos/'+nome_arquivo, '/home/casa/Documentos/python/')

def mover_arquivo(nome_arquivo):
    shutil.move('/home/casa/Documentos/python/arquivos/'+nome_arquivo,'/home/casa/Documentos/python')


if __name__ == "__main__":
    #escreve_arquivo('primeira linha\n')
    #atualiza_arquivo('notas.txt','\nJosé: 3,9,10,2')
    #ler_arquivo('notas.txt')
    lista_media = media_notas('notas.txt')
    print(lista_media)
    copia_arquivo('arquivo.txt')
    #mover_arquivo('arquivo.txt')
