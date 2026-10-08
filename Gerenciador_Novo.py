import json
import random

separador = "-" * 60

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

    continuar = True
    while continuar:
        index_novo = str(random.randint(1, 9999))
        for ativo in ativos:
            if ativo.get("index") == index_novo:
                #index já existe
                continuar = False
                break

            else:
                return index_novo














class Ativo:
    def __init__(self, nome,index:str,responsavel,setor):
        self.nome = nome
        self.index = index
        self.responsavel = responsavel
        self.setor = setor

    def cadastrar_ativo(self):
        print(f"Adicionando um novo ativo!\n{separador}")
        nome_ativo = input("Qual o nome do ativo? ").capitalize().strip()
        index_ativo = gerar_index_aleatorio()
        responsavel_ativo = input("Qual o nome do responsável pelo ativo? ").title().strip()
        setor_ativo = input("Qual o setor do ativo? ").capitalize().strip()

        novo_ativo = [{"nome": nome_ativo,"index": index_ativo, "responsavel": responsavel_ativo, "setor": setor_ativo}]

        ativos.append(novo_ativo)
        salvar_ativos(ativos)


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
        print(f"ATIVOS CADASTRADOS\n")
        for ativo in lista_ativos:
            print(f"Nome: {ativo.get('nome')}\nIndex: {ativo.get('index')}\nResponsável: {ativo.get('responsavel')}\nSetor: {ativo.get('setor')}\n")

    def executar(self):
        pass


gerenciador_ativos.mostrar_ativos(ativos)
















