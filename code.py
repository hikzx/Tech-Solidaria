import json
from time import sleep
import os

# Caminho do arquivo JSON
dados_usuario = 'usuarios.json'

# Função para salvar dados em JSON
def salvar_usuario(nome, senha):
    dados = {"nome": nome, "senha": senha}
    with open(dados_usuario, 'w') as arquivo:
        json.dump(dados, arquivo)

# Função para carregar dados do JSON
def carregar_usuario():
    if os.path.exists(dados_usuario):
        with open(dados_usuario, 'r') as arquivo:
            return json.load(arquivo)
    return None

# Função para excluir os dados do JSON
def excluir_dados():
    if os.path.exists(dados_usuario):
        os.remove(dados_usuario)

# Dicionário de perguntas
dict_perguntas = {
    "fácil": [
        {
            "pergunta": "1) Qual função usamos para exibir algo na tela em Python?",
            "alternativas": ["A) show()", "B) print()", "C) echo()", "D) display()"],
            "resposta_correta": "B",
            "pontos": 2
        },
        {
            "pergunta": "2) Qual símbolo usamos para comentar uma linha em Python?",
            "alternativas": ["A) //", "B) <!--", "C) ##", "D) #"],
            "resposta_correta": "D",
            "pontos": 2
        },
        {
            "pergunta": "3) Qual é o tipo de dado da expressão: 'Olá Mundo'?",
            "alternativas": ["A) int", "B) str", "C) float", "D) bool"],
            "resposta_correta": "B",
            "pontos": 2
        },
        {
            "pergunta": "4) Como declaramos uma variável em Python corretamente?",
            "alternativas": ["A) var nome = 'Ana'", "B) nome := 'Ana'", "C) nome = 'Ana'", "D) let nome = 'Ana'"],
            "resposta_correta": "C",
            "pontos": 2
        },
        {
            "pergunta": "5) Qual comando é usado para ler algo digitado pelo usuário?",
            "alternativas": ["A) input()", "B) read()", "C) scan()", "D) get()"],
            "resposta_correta": "A",
            "pontos": 2
        }
    ],
    "médio": [
        {
            "pergunta": "1) Qual estrutura usamos para repetir algo enquanto uma condição for verdadeira?",
            "alternativas": ["A) if", "B) while", "C) for", "D) def"],
            "resposta_correta": "B",
            "pontos": 2
        },
        {
            "pergunta": "2) Qual função transforma uma string em número inteiro?",
            "alternativas": ["A) float()", "B) str()", "C) int()", "D) input()"],
            "resposta_correta": "C",
            "pontos": 2
        },
        {
            "pergunta": "3) O que o operador '==' verifica?",
            "alternativas": ["A) Atribuição", "B) Diferença", "C) Igualdade", "D) Soma"],
            "resposta_correta": "C",
            "pontos": 2
        },
        {
            "pergunta": "4) Como definimos uma função em Python?",
            "alternativas": ["A) function nome()", "B) def nome():", "C) func nome()", "D) def nome[]"],
            "resposta_correta": "B",
            "pontos": 2
        },
        {
            "pergunta": "5) O que significa 'len(lista)' em Python?",
            "alternativas": ["A) Soma dos itens", "B) Último valor", "C) Tamanho da lista", "D) Ordenar a lista"],
            "resposta_correta": "C",
            "pontos": 2
        }
    ],
    "difícil": [
        {
            "pergunta": "1) Qual o resultado de: print(2 ** 3)?",
            "alternativas": ["A) 6", "B) 8", "C) 9", "D) 5"],
            "resposta_correta": "B",
            "pontos": 2
        },
        {
            "pergunta": "2) O que faz o método .append() em uma lista?",
            "alternativas": ["A) Remove um item", "B) Adiciona no início", "C) Adiciona no final", "D) Ordena a lista"],
            "resposta_correta": "C",
            "pontos": 2
        },
        {
            "pergunta": "3) Qual dessas opções cria um dicionário em Python?",
            "alternativas": ["A) {'chave':'valor'}", "B) ['chave','valor']", "C) ('chave','valor')", "D) <chave:valor>"],
            "resposta_correta": "A",
            "pontos": 2
        },
        {
            "pergunta": "4) Qual estrutura é imutável em Python?",
            "alternativas": ["A) lista", "B) dicionário", "C) conjunto", "D) tupla"],
            "resposta_correta": "D",
            "pontos": 2
        },
        {
            "pergunta": "5) Como tratamos erros em Python?",
            "alternativas": ["A) try/except", "B) do/catch", "C) if/else", "D) loop/error"],
            "resposta_correta": "A",
            "pontos": 2
        }
    ]
}

print('=' * 33)
print('BEM-VINDO AO SITE TECHSOLIDÁRIA!')
print('=' * 33)

nome_usuario = input('Como podemos te chamar? ').strip().title()
print(f'Ótimo ter você no TECHSOLIDÁRIA, {nome_usuario}!')
print('=' * 40)

while True:
    opcao = int(input('[1] - Realizar cadastro\n[2] - Excluir meus dados\n[0] - Sair do TECHSOLIDÁRIA \n\nDigite uma opção: '))
    if opcao == 1:
        nome = input('Digite seu nome completo: ').strip().title()
        senha = input('Digite sua senha: ').strip()
        salvar_usuario(nome, senha)
        print('Cadastro salvo com sucesso!')
        print('Você pode excluir seus dados quando quiser')
        print('carregando...')
        sleep(2)
        break
    elif opcao == 2:
        excluir_dados()
        print('Seus dados foram excluídos com sucesso.')
        exit()
    elif opcao == 0:
        print('Sessão finalizada. Obrigado por usar a Techsolidária!')
        exit()
    else:
        print('Por favor, escolha uma opção válida.')

usuario = carregar_usuario()
if not usuario:
    print("Nenhum usuário cadastrado.")
    exit()

nome_split = usuario['nome'].split()
print(f"Bem-vindo à tela de login, {nome_split[0]}!")
tentativas = 3
while tentativas > 0:
    senha_digitada = input('Digite sua senha: ').strip()
    if senha_digitada == usuario['senha']:
        print('Login realizado com sucesso!')
        break
    else:
        tentativas -= 1
        print(f'Senha incorreta. Tentativas restantes: {tentativas}')
else:
    print('Número de tentativas excedido. Saindo por segurança...')
    exit()

# Contadores
cont_quiz = 0
cont_curiosidades = 0

while True:
    print('=' * 33)
    print('QUIZ TECH')
    print(f'Bem-vindo {nome_split[0]} à área de QUIZ da TECHSOLIDÁRIA!!')
    ano = int(input('Em qual ano do ensino médio você se encontra no momento 1, 2 ou 3 ? '))
    if ano == 1:
        nivel = 'fácil'
        print('Você será direcionado ao nível fácil.')
    elif ano == 2:
        nivel = 'médio'
        print('Você será direcionado ao nível médio.')
    elif ano == 3:
        nivel = 'difícil'
        print('Você será direcionado ao nível difícil.')
    else:
        nivel = 'fácil'
        print('Opa! Parece que você não está no ensino médio. Vamos mesclar o nível das perguntas.')

    pontuacao = 0
    for pergunta in dict_perguntas[nivel]:
        print(pergunta["pergunta"])
        for alt in pergunta["alternativas"]:
            print(alt)
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == pergunta["resposta_correta"]:
            pontuacao += pergunta["pontos"]
            print("Resposta correta!\n")
        else:
            print(f"Resposta incorreta. A resposta certa era: {pergunta['resposta_correta']}\n")

    print(f"Sua pontuação final foi: {pontuacao} pontos.")
    cont_quiz += 1

    curiosidade = input("Gostaria de saber curiosidades sobre Ética, Cidadania, Sustentabilidade e Direitos Humanos? (sim/não): ").strip().lower()
    if curiosidade == 'sim':
        print("\n== CURIOSIDADES TECH ==")
        print("- Ética é o conjunto de valores que orienta o comportamento humano.")
        print("- Cidadania envolve direitos e deveres dentro de uma sociedade.")
        print("- Sustentabilidade busca equilíbrio entre o progresso e o cuidado com o meio ambiente.")
        print("- Os Direitos Humanos garantem dignidade, liberdade e igualdade a todos os seres humanos.\n")
        cont_curiosidades += 1

    jogar_novamente = input("Gostaria de responder o quiz novamente? (sim/não): ").strip().lower()
    if jogar_novamente != 'sim':
        sair = input("Você deseja sair do site TECHSOLIDÁRIA? (sim/não): ").strip().lower()
        if sair == 'sim':
            print("\nObrigado por usar o site TECHSOLIDÁRIA!")
            print(f"Você acessou o quiz {cont_quiz} vez(es).")
            print(f"Você acessou a área de curiosidades {cont_curiosidades} vez(es).")
            break
        else:
            print("\nReiniciando o quiz...")
