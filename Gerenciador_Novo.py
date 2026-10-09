import json
import random
import sys
from cgitb import reset

separador = "-" * 60

VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

def carregar_ativos():
    try:
        with open("ativos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# FUNÇÃO PARA SALVAR AS MUDANÇAS FEITAS NA MEMÓRIA PARA O ARQUIVO
def salvar_ativos(lista):
    with open("ativos.json", "w", encoding="utf-8") as file:
        json.dump(lista, file, indent=4, ensure_ascii=False)


ativos = carregar_ativos()

def gerar_index_aleatorio():

    while True:
        index_novo = str(random.randint(1, 9999))
        if not any(ativo.get("index") == index_novo for ativo in ativos):
            return index_novo


def certeza_operaçao(): #RETORNA TRUE SE O USUÁRIO DESEJA REALIZAR A OPERAÇÃO!

    while True:
        certeza = input(f"Tem certeza de que deseja realizar essa operação? O resultado {VERMELHO}NÃO{RESET} pode ser revertido! Y/N ").lower().strip()
        if certeza == "yes" or certeza == "y":
            escolha_usuario = True
            return escolha_usuario
        elif certeza == "n" or certeza == "no":
            escolha_usuario = False
            return escolha_usuario
        else:
            print(f"Escolha uma opção válida!\n{separador}")











class Ativo:
    def __init__(self, nome,index:str,responsavel,setor):
        self.nome = nome
        self.index = index
        self.responsavel = responsavel
        self.setor = setor

    @staticmethod
    def cadastrar_ativo():
        print(f"\nAdicionando um novo ativo!\n{separador}")
        nome_ativo = input("Qual o nome do ativo? ").capitalize().strip()
        index_ativo = gerar_index_aleatorio()
        responsavel_ativo = input("Qual o nome do responsável pelo ativo? ").title().strip()
        setor_ativo = input("Qual o setor do ativo? ").capitalize().strip()

        novo_ativo = {"nome": nome_ativo,"index": index_ativo, "responsavel": responsavel_ativo, "setor": setor_ativo}

        ativos.append(novo_ativo)
        salvar_ativos(ativos)

    @staticmethod
    def remover_ativo():
        print(f"Iniciando a {VERMELHO}remoção{RESET} de um ativo!")
        alvo = str(input("Digite o nome ou index do ativo que deseja remover: ").strip().lower())
        for ativo in ativos:
            if alvo in ativo["nome"].lower() or alvo in ativo["index"]:
                if certeza_operaçao():
                    ativos.remove(ativo)
                    salvar_ativos(ativos)
                    print(f"{separador}\nO ativo '{ativo['nome']}' foi removido com sucesso!")
                    return
                else:
                    print("Operação cancelada!")
        print(f"Não foi encontrado nenhum ativo com o nome ou index {alvo}.")

    @staticmethod
    def editar_ativo():

        opcoes_editaveis = {
            "1": "nome",
            "nome": "nome",
            "2": "vulnerabilidades",
            "vulnerabilidades": "vulnerabilidades",
            "vulnerabilidade": "vulnerabilidades",
            "3": "responsavel",
            "responsavel": "responsavel",
            "responsável": "responsavel",
            "4": "setor",
            "setor": "setor",
        }

        print("Digite o nome ou index do ativo que deseja editar!")
        alvo = input("-> ").lower().strip()
        for ativo in ativos:
            if alvo == ativo['nome'].lower() or alvo == ativo['index']:
                print(f"Iniciando edição do ativo {ativo['nome']}!")
                print("O que deseja editar?\n1.Nome\n2.Lista de vulnerabilidades\n3.Responsável\n4.Setor")
                alvo_entrada = input("").lower().strip()
                alvo_ediçao = opcoes_editaveis.get(alvo_entrada)
                if alvo_ediçao == "nome":
                    Ativo.ediçao_nome_ativo(ativo)
                elif alvo_ediçao == "vulnerabilidades":
                    pass
                elif alvo_ediçao == "setor":
                    pass
                elif alvo_ediçao == "responsavel":
                    pass


    @staticmethod
    def ediçao_nome_ativo(ativo): #TALVEZ PRECISE DE ALTERAÇÃO PARA CRIAR UM LOOP QUE SÓ SAI QUANDO O USUÁRIO COLOCA UM NOME DIFERENTE OU ESCOLHE CANCELAR
        print(f"Editando o nome do ativo '{ativo['nome']}'\n{separador}")
        print("Qual o nome que deseja atribuir a esse ativo?")
        novo_nome = input("->").lower().strip()
        if certeza_operaçao():
            if novo_nome != "":
                print(f"Ativo '{ativo['nome']}' teve seu nome substituido por '{novo_nome.capitalize()}'")
                ativo['nome'] = novo_nome
            else:
                print("O novo nome não pode ser igual ao nome anterior!")
        else:
            print(f"Operação cancelada!\n{separador}")





class Vulnerabilidade:
    def __init__(self,nome,descricao,index:str,status_tratamento,severidade,tipo): #tipo hardware/software/...
        self.nome = nome
        self.descricao = descricao
        self.index = index
        self.status_tratamento = status_tratamento
        self.severidade = severidade
        self.tipo = tipo


class gerenciador_ativos:
    def __init__(self):
        pass

    @staticmethod
    def mostrar_ativos(lista_ativos):
        print(f"ATIVOS CADASTRADOS\n{separador}")
        if not lista_ativos:
            print("Nenhum ativo cadastrado no momento!")
        for ativo in lista_ativos:
            print(f"{AZUL}Index:{RESET} {ativo.get('index')}\n{AZUL}Nome:{RESET} {AMARELO}{ativo.get('nome')}{RESET}\n{AZUL}Responsável:{RESET} {ativo.get('responsavel')}\n{AZUL}Setor:{RESET} {ativo.get('setor')}\n{separador}")


    @staticmethod
    def menu_controle():  #CHAMAR SEMPRE QUE O USUÁRIO TERMINAR ALGUMA OPERAÇÃO GRANDE. EX: CADASTRO OU REMOÇÃO DE ATIVO
        deseja_sair = input(f"{separador}\nPara continuar pressione enter, para fechar o programa digite 'quit' ->").strip().lower()
        while True:
            if deseja_sair == "quit":
                print("Fechando o Programa!")
                sys.exit()
            elif deseja_sair == "":
                continuar = True; return continuar
            else:
                print("Opção inválida. Por favor, pressione 'enter' ou digite 'quit'.")


    def executar(self):
        print(f"{VERDE}Bem vindo ao Gerenciador de Ativos!{RESET}\n")
        while True:
            gerenciador_ativos.mostrar_ativos(ativos)
            print(f"\nPara cadastrar um novo ativo digite 'add'\nPara deletar um ativo digite 'del'\nPara editar um ativo digite 'edit'\nPara sair do programa digite 'quit'")
            escolha_usuario = input("-> ").strip().lower()

            if escolha_usuario == "add":
                Ativo.cadastrar_ativo()
                gerenciador_ativos.menu_controle()
            elif escolha_usuario == "del":
                Ativo.remover_ativo()
                gerenciador_ativos.menu_controle()
            elif escolha_usuario == "edit":
                Ativo.editar_ativo()
                gerenciador_ativos.menu_controle()
            elif escolha_usuario == "quit":
                print("Fechando o programa!")
                sys.exit()
            else:
                print("Opção inválida! Escolha entre add, del, edit ou quit.")


# funçao_ativo = Ativo()
# funçao_vulnerabilidade = Vulnerabilidade()
funçao_gerenciador = gerenciador_ativos()
funçao_gerenciador.executar()
















