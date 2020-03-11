from pafy import *
from requests import get
from requests.exceptions import ConnectionError


def internet():
    try:
        get('http://meuip.com/api/meuip.php')
    except ConnectionError:
        return False
    else:
        return True


def menu_texto(num, qualidade, formato, tamanho):
    if num < 10:
        print('', num, end='       ')
    if len(qualidade) < 4:
        print(qualidade, end='       ')
    if len(qualidade) >= 4:
        print(qualidade, end='      ')
    if len(formato) < 4:
        print(formato, end='       ')
    if len(formato) >= 4:
        print(formato, end='      ')
    print(tamanho)


def info_texto(video):
    print('\n============= INFORMAÇÕES ===========')
    print(f'* Título:  {video.title}\n* Autor:   {video.author}\n* Duração: {video.duration}')
    print('=====================================\n')


def link_valido(link):
    try:
        video = new(link)
        return True
    except:
        return False


print('>>> Verificando conexão.')
if internet() == False:
    print('>>> Não foi possível estabelecer uma conexão.')
    exit()

link = input('\nLink: ').strip()
while link_valido(link) == False:
    print('>>> Link inválido.')
    link = input('\nLink: ').strip()

video = new(link)
info_texto(video)
audiostreams = video.audiostreams

print('NUM   QUALIDADE   FORMATO   TAMANHO')
print('===   =========   =======   =========')
num = 0
for s in audiostreams:
    num += 1
    qualidade = s.bitrate
    formato   = s.extension.upper()
    tamanho   = f'{s.get_filesize() / (1024 * 1024):.2f} MB'
    menu_texto(num, qualidade, formato, tamanho)

opcao = input('\nOpção: ').strip()
while not opcao.isnumeric() or int(opcao) > num - 1 or int(opcao) < 0:
    print('>>> Digite uma opção válida.')
    opcao = input('\nOpção: ').strip()
opcao = int(opcao) - 1

audiostreams[opcao].download()
print('>>> Donwload concluído.')
