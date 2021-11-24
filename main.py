import re

def probabilidade_de_mensagem(mensagem_usuario, palavras_reconhecidas, resposta_unica=False, palavra_requeridas=[]):
    certeza_de_mensagem = 0
    tem_palavras_requeridas = True

    #conta quantas palavras estão presentes em cada mensagem pré-definida
    for palavra in mensagem_usuario:
        if palavra in palavras_reconhecidas:
            certeza_de_mensagem +=1

    #calcula a porcentagem de palavras reconhecidas em uma menssagem do usuário
    porcentagem = float(certeza_de_mensagem) / float(len(palavras_reconhecidas))

    for palavra in palavra_requeridas:
        if palavra not in mensagem_usuario:
            tem_palavras_requeridas = False
            break
    if tem_palavras_requeridas or resposta_unica:
        return int(porcentagem*100)
    else:
        return 0

def checar_todas_mensagens (mensagem):
    lista_maior_probabilidade = {}

    def resposta(bot_resposta, lista_de_palavras, resposta_unica =False,palavras_requeridas=[]):
       nonlocal  lista_maior_probabilidade
       lista_maior_probabilidade[bot_resposta] = probabilidade_de_mensagem(mensagem, lista_de_palavras, resposta_unica, palavras_requeridas)


    #Respostas__________________________________________________________________________

    resposta('E ai!',['ola','eai','oi','oie'], resposta_unica = True)
    resposta('Eu estou ótimo, e você?', ['como','voce','esta','vc','ta','vai','bem'], palavras_requeridas=['como'])
    resposta('Eu estou de boa, e você?', ['tudo', 'voce', 'esta', 'vc', 'ta', 'joia', 'bem'], palavras_requeridas=['tudo'])
    resposta('Valeu! O Gustavo me fez assim 😎', ['voce','e','inteligente'], palavras_requeridas=['voce'])
    resposta('Gustavo é o Dev que me criou.', ['quem','é','gustavo','te','criou'], palavras_requeridas=['quem'])
    resposta('Meu nome (Bud) significa Bot Unico de Diálogo.', ['o','que','significa','bud'], palavras_requeridas=['bud'])
    resposta('Meu nome é Bud.', ['nome', 'qual', 'seu'], palavras_requeridas=['nome'])

    melhor_combinacao = max(lista_maior_probabilidade, key=lista_maior_probabilidade.get)
    print(lista_maior_probabilidade)

    return melhor_combinacao

#Definindo função para split e ignorar caracteres(+|[,;?!.-]\)

def pegar_resposta(usuario_input):
    split_mensagem =  re.split(r'\s+|[,;?!.-]\s*', usuario_input.lower())
    resposta = checar_todas_mensagens (split_mensagem)
    return resposta

#Testando o sistema de respostas
while True:
    print('	\033[1;36m Bud: '+ pegar_resposta(input('Você: ')))

