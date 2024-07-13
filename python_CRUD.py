# Curso: Superior de Tecnologia em Análise e Desenvolvimento de Sistemas

import json

# Função para Mostrar o Menu Principal
def mostrar_menu_principal():
    print("------- MENU PRINCIPAL -------")
    print("")
    print("[ 1 ] Estudantes\n[ 2 ] Professores\n[ 3 ] Disciplinas\n[ 4 ] Turmas\n[ 5 ] Matriculas\n[ 0 ] Sair")
    print("") 

# Função para Mostrar o Menu secundário
def mostrar_menu_secundario():
    print("----- MENU DE OPERAÇÕES -----\n")

    if opcao ==1:
        print("[     Estudantes      ]\n")
    elif opcao ==2:
        print("[     Professores     ]\n") 
    elif opcao ==3: 
        print("[     Disciplinas     ]\n")
    elif opcao == 4:
        print("[     Turmas          ]\n")
    elif opcao == 5:
        print("[     Matriculas      ]\n")

    print("[ 1 ] Listar\n[ 2 ] Criar\n[ 3 ] Editar\n[ 4 ] Excluir\n[ 5 ] Voltar ao menu anterior\n")

# Função para Listar registros
def listar_cadastro(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    if lista:
        mostrar_menu_secundario()
        lista_ordenada = sorted(lista, key=lambda x: next(iter(x.values())))
        print("----- Lista de Registros -----\n")
        for registro in lista_ordenada:
            print(registro)
        print("\n-------------------------------\nPressione ENTER continuar!")
        input()
        limpar_terminal()
    else:
        print("[ Não há registros para mostrar]\n")
    

# Função para Validar Registro em duplicidade
def validar_inserir_codigo(codigo, nome_arquivo):
    codigo_antigo = ler_arquivo(nome_arquivo)
    for codigo_novo in codigo_antigo:
        if codigo_novo['cod'] == codigo:
            limpar_terminal()
            print(f"\nCódigo [ {codigo} ] já existe. Insira um novo código.\n")
            return False
    return True

# Função para Inserir registro
def inserir_cadastro(nome_arquivo):
    if opcao ==1:
        print("     [  Estudantes    ]\n\n ----- [ 2. Criar     ] -----\n")
    elif opcao ==2:
        print("     [  Professores   ]\n\n ----- [ 2. Criar     ] -----\n") 
    elif opcao ==3: 
        print("     [  Disciplinas   ]\n\n ----- [ 2. Criar     ] -----\n")
    elif opcao == 4:
        print("     [  Turmas        ]\n\n ----- [ 2. Criar     ] -----\n")
    elif opcao == 5:
        print("     [  Matriculas    ]\n\n ----- [ 2. Criar     ] -----\n")

    for i in range(1):
        codigo = validar_codigo(limpar_terminal)
        if not validar_inserir_codigo(codigo, nome_arquivo):
            return
        if opcao == 1:
            nome = input("Digite o Nome do Estudante: ")
            cpf = input("Digite o CPF do Estudante: ")
            novo = ({"cod" : codigo,"nome" : nome,"cpf" : cpf})
        elif opcao == 2:
            nome = input("Digite o Nome do Professor: ")
            cpf = input("Digite o CPF do Professor: ")
            novo = ({"cod" : codigo,"nome" : nome,"cpf" : cpf})
        elif opcao == 3:
            nome = input("Digite o Nome da Disciplina: ")
            novo = ({"cod" : codigo,"nome" : nome,})
        elif opcao == 4:
            while True: 
                try:
                    cod_professor = int(input("Digite o Código do Professor: "))
                    cod_disciplina = int(input("Digite o Código da Disciplina: "))
                    break
                except ValueError:
                    limpar_terminal()
                    print("Digite apenas números inteiros! Tente novamente.\n")
                return cod_professor, cod_disciplina
            novo = ({"cod" : codigo,"cod_p" : cod_professor,"cod_d" : cod_disciplina})  
        elif opcao == 5:
            while True: 
                try:
                    cod_estudante = int(input("Digite o Código do Estudante: "))
                    break
                except ValueError:
                    limpar_terminal()
                    print("Digite apenas números inteiros! Tente novamente.\n")
                return cod_estudante
            novo = ({"cod" : codigo,"cod_estud" : cod_estudante,})

    lista = ler_arquivo(nome_arquivo)
    lista.append(novo)
    salvar_arquivo(lista, nome_arquivo)
    limpar_terminal()


# Função para Editar registro
def editar_cadastro(nome_arquivo):
    if opcao ==1:
        print("     [  Estudantes    ]\n\n ----- [ 3. Editar     ] -----\n")
    elif opcao ==2:
        print("     [  Professores   ]\n\n ----- [ 3. Editar     ] -----\n") 
    elif opcao ==3: 
        print("     [  Disciplinas   ]\n\n ----- [ 3. Editar     ] -----\n")
    elif opcao == 4:
        print("     [  Turmas        ]\n\n ----- [ 3. Editar     ] -----\n")
    elif opcao == 5:
        print("     [  Matriculas    ]\n\n ----- [ 3. Editar     ] -----\n")

    codigo_editar = validar_codigo(limpar_terminal)
    limpar_terminal()
    lista = ler_arquivo(nome_arquivo)
    cadastro_editado = None
    for dic_cadastro in lista:
        if dic_cadastro["cod"] == codigo_editar:
            cadastro_editado = dic_cadastro
            
    if cadastro_editado is None:
        print(f"Código [ {codigo_editar} ] não encontrado!")
        print("")
    else:

        if opcao ==1:
            cadastro_editado["nome"] = input("Digite o novo Nome: ")
            cadastro_editado["cpf"] = input("Digite o novo CPF: ")
        elif opcao ==2:
            cadastro_editado["nome"] = input("Digite o novo Nome: ")
            cadastro_editado["cpf"] = input("Digite o novo CPF: ")
        elif opcao ==3: 
            cadastro_editado["nome"] = input("Digite o novo Nome: ")
        elif opcao == 4:
            while True: 
                try:
                    cadastro_editado["cod_p"] = int(input("Digite o Código do Professor: "))
                    cadastro_editado["cod_d"]= int(input("Digite o Código da Disciplina: "))
                    break
                except ValueError:
                    limpar_terminal()
                    print("Digite apenas números inteiros! Tente novamente.\n")
                return cadastro_editado["cod_p"], cadastro_editado["cod_d"] 
        elif opcao == 5:
            while True: 
                try:
                    cadastro_editado["cod_estud"] = int(input("Digite o Código do Estudante: "))
                    break
                except ValueError:
                    limpar_terminal()
                    print("Digite apenas números inteiros! Tente novamente.\n")
                return cadastro_editado["cod_estud"] 

        salvar_arquivo(lista, nome_arquivo)
        print("\nRegistro editado com sucesso!\n")

# Função para Excluir registro
def excluir_cadastro(nome_arquivo):
    if opcao ==1:
        print("     [  Estudantes    ]\n\n ----- [ 4. Excluir    ] -----\n")
    elif opcao ==2:
        print("     [  Professores   ]\n\n ----- [ 4. Excluir    ] -----\n") 
    elif opcao ==3: 
        print("     [  Disciplinas   ]\n\n ----- [ 4. Excluir    ] -----\n")
    elif opcao == 4:
        print("     [  Turmas        ]\n\n ----- [ 4. Excluir    ] -----\n")
    elif opcao == 5:
        print("     [  Matriculas    ]\n\n ----- [ 4. Excluir    ] -----\n")
            
    codigo_excluir = validar_codigo(limpar_terminal)
    print("")
    cadastro_removido = None
    lista = ler_arquivo(nome_arquivo)
    for dic_cadastro in lista:
        if dic_cadastro["cod"] == codigo_excluir:
            cadastro_removido = dic_cadastro
    
    if cadastro_removido is None:
        print(f"Código [ {codigo_excluir} ] não encontrado!\n")
    else:
        lista.remove(cadastro_removido)
        salvar_arquivo(lista, nome_arquivo)
        print("Registro excluido com sucesso!\n\nPressione ENTER continuar!")
        input()
        limpar_terminal()


# Sair do sistema
def sair_sistema():
    os.system('cls')
    print("Você pediu para Sair.")
    print("")
def limpar_terminal():
    os.system('cls')

# EXCEÇÃO = Validar input no menu principal
def validar_menu_principal(mostrar_menu_principal, limpar_terminal):
    while True: 
        mostrar_menu_principal()
        try:
            opcao = int(input("Digite uma opção do Menu Principal: "))
            break
        except ValueError:
            limpar_terminal()
            print("Digite apenas números inteiros! Tente novamente.\n")
    return opcao
# EXCEÇÃO = Validar input no menu secundario
def validar_menu_secundario(mostrar_menu_secundario, limpar_terminal):
    while True: 
        mostrar_menu_secundario()
        try:
            opcao_secundaria = int(input("Digite uma opção do Menu de Operações: "))
            break    
        except ValueError:
            limpar_terminal()
            print("Digite apenas números inteiros! Tente novamente.\n")
    return opcao_secundaria

# EXCEÇÃO = Validar input nas operações
def validar_codigo(limpar_terminal):
    while True: 
        try:
            if opcao == 1:
                # Solicitação do input até que seja um número inteiro maior que zero
                while True:
                    try:
                        cod = int(input("Digite o Código do Estudante: "))
                        if cod > 0:
                            break  # Sai do loop se o código for válido
                        else:
                            print("O número deve ser maior que zero. Tente novamente.")
                    except ValueError:
                        print("Por favor, digite um número inteiro válido.")
            elif opcao == 2:
                 while True:
                    try:
                        cod = int(input("Digite o Código do Professor: "))
                        if cod > 0:
                            break  # Sai do loop se o código for válido
                        else:
                            print("O número deve ser maior que zero. Tente novamente.")
                    except ValueError:
                        print("Por favor, digite um número inteiro válido.")
            elif opcao == 3:
                 while True:
                    try:
                        cod = int(input("Digite o Código da Disciplina: "))
                        if cod > 0:
                            break  # Sai do loop se o código for válido
                        else:
                            print("O número deve ser maior que zero. Tente novamente.")
                    except ValueError:
                        print("Por favor, digite um número inteiro válido.")
            elif opcao == 4 or opcao == 5:
                 while True:
                    try:
                        cod = int(input("Digite o Código da Turma: "))
                        if cod > 0:
                            break  # Sai do loop se o código for válido
                        else:
                            print("O número deve ser maior que zero. Tente novamente.")
                    except ValueError:
                        print("Por favor, digite um número inteiro válido.")
        except ValueError:
            limpar_terminal()
            print("Digite apenas números inteiros! Tente novamente.\n")
        return cod

# Função JSON para manipular arquivo
def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
        return lista
    except:
        return []

# Função para processar blocos de operações---------------------------------------
def processar_menu_operações(opcao_secundaria, nome_arquivo):
        if opcao_secundaria == 1:
            limpar_terminal()
            listar_cadastro(nome_arquivo)              
        elif opcao_secundaria == 2:
            limpar_terminal() 
            inserir_cadastro(nome_arquivo) 
        elif opcao_secundaria == 3:
            limpar_terminal()
            editar_cadastro(nome_arquivo) 
        elif opcao_secundaria == 4:
            limpar_terminal()
            excluir_cadastro(nome_arquivo)
        elif opcao_secundaria == 5:
            limpar_terminal()
            return False
        else:
            limpar_terminal()
            print("Você digitou uma opção no Menu de Operações\n        ** Inválida **\n")   
        return True

# FIM das funções

import os # para limpeza do terminal
limpar_terminal()
print("Bem-vindo ao SISTEMA PUC_CRUD")
print("")

arquivo_estudante = "estudantes.json"
arquivo_professor = "professores.json"
arquivo_disciplina = "disciplinas.json"
arquivo_turma = "turmas.json"
arquivo_matricula = "matriculas.json"


while True:
    opcao = validar_menu_principal(mostrar_menu_principal, limpar_terminal) 
    if opcao == 0:
        sair_sistema()
        break
    elif opcao == 1:
        limpar_terminal()
        while True:
            opcao_secundaria = validar_menu_secundario(mostrar_menu_secundario,limpar_terminal)
            if not processar_menu_operações(opcao_secundaria, arquivo_estudante):
                break
    elif opcao == 2:
        limpar_terminal()
        while True:
            opcao_secundaria = validar_menu_secundario(mostrar_menu_secundario,limpar_terminal)
            if not processar_menu_operações(opcao_secundaria, arquivo_professor):
                break
    elif opcao == 3:
        limpar_terminal()
        while True:
            opcao_secundaria = validar_menu_secundario(mostrar_menu_secundario,limpar_terminal)
            if not processar_menu_operações(opcao_secundaria, arquivo_disciplina):
                break
    elif opcao == 4:
        limpar_terminal()
        while True:
            opcao_secundaria = validar_menu_secundario(mostrar_menu_secundario,limpar_terminal)
            if not processar_menu_operações(opcao_secundaria, arquivo_turma):
                break
    elif opcao == 5:
        limpar_terminal()
        while True:
            opcao_secundaria = validar_menu_secundario(mostrar_menu_secundario,limpar_terminal)
            if not processar_menu_operações(opcao_secundaria, arquivo_matricula):
                break
    else:
        limpar_terminal()
        print("Você digitou uma opção no Menu Principal\n        ** Inválida **\n")