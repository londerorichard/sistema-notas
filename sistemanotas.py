
materias = [
    "1 - Lógica de programação",
    "2 - Ciência da computação",
    "3 - UX/UI",
    "4 - Cyber Segurança"
  ]

# OPÇÃO 1 - CADASTRAR ALUNO

def calcular_media_aluno(alunos, materias):
    print("\n1 - Calcular média")

    # nome
    while True:
        nome = input("Nome do aluno: ").lower().strip()

        if nome.replace(" ", "").isalpha():
            break

        print("Nome inválido!")

    # mostrar matérias
    for m in materias:
        print(m)

    # escolher matéria
    try:
        opcao_materia = int(input("Escolha a matéria: "))

        if opcao_materia < 1 or opcao_materia > len(materias):
            print("Opção inválida!")
            return

    except ValueError:
        print("Digite um número válido!")
        return

    materia = materias[opcao_materia - 1]
    print(f"Matéria selecionada: {materia}")

    # quantidade de notas
    try:
        qtd_notas = int(input("\nQuantas notas deseja incluir? "))
        if qtd_notas <= 0:
            print("Quantidade inválida!")
            return
    except ValueError:
        print("Valor inválido!")
        return
    
    soma = 0

    # leitura das notas
    for i in range(qtd_notas):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1}: "))

                if nota >= 0 and nota <= 10:
                    soma += nota
                    break

                else:
                    print("Nota inválida! Digite uma nota entre 0 e 10.")

            except ValueError:
                print("Digite um número válido!")
                continue
                
    media = soma / qtd_notas

    if media >= 7:
        situacao = "Aprovado(a)"
    elif media >= 5 and media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado(a)"

    alunos.append({
        "nome": nome,
        "materia": materia,
        "media": media,
        "situacao": situacao
    })

    print(f"\n{nome} cadastrado com média {media:.2f} - {situacao}")

# OPÇÃO 4 - INFORMAÇÕES

def mostrar_informacoes(alunos):

    if not alunos:
        print("Nenhuma média cadastrada")
        return

    soma = 0
    maior = alunos[0]
    menor = alunos[0]
    aprovados = 0

    for aluno in alunos:
        soma += aluno["media"]

        if aluno["media"] > maior["media"]:
            maior = aluno

        if aluno["media"] < menor["media"]:
            menor = aluno

        if aluno["situacao"] == "Aprovado(a)":
            aprovados += 1

    media_geral = soma / len(alunos)

    print(f"\nMédia geral: {media_geral:.2f}")
    print(f"Maior média: {maior['nome']} - {maior['media']:.2f}")
    print(f"Menor média: {menor['nome']} - {menor['media']:.2f}")
    print(f"Número de aprovados: {aprovados}")

# buscar alunos

def buscar_alunos(alunos, nome_busca):
    resultados = []

    nome_busca = nome_busca.strip().lower()

    for aluno in alunos:
        if nome_busca in aluno["nome"].strip().lower():
            resultados.append(aluno)

    return resultados

# MENU PRINCIPAL

opcao = -1
alunos = []

while opcao != 0:

    print("\n===== SISTEMA DE NOTAS =====")
    print("\n1 - Calcular média de um aluno")
    print("2 - Lista de matérias")
    print("3 - Alunos cadastrados")
    print("4 - Média geral")
    print("5 - Buscar aluno cadastrado")
    print("0 - Sair")

    try:
        opcao = int(input("\nEscolha uma opção: "))

    except ValueError:
        print("Digite um número válido!")
        continue

    match opcao:
        case 1:
            calcular_media_aluno(alunos, materias)

        case 2:
            for materia in materias:
              print(materia)

        case 3:
            if alunos:
                for aluno in alunos:
                    print(f"Aluno: {aluno['nome']} - Média: {aluno['media']:.2f} - Situação: {aluno['situacao']}")

            else:
                print("Nenhum aluno foi cadastrado")

        case 4:
            mostrar_informacoes(alunos)

        case 5:
            nome_busca = input("Qual aluno deseja buscar? ").strip().lower()
            if nome_busca == "":
                print("Nome inválido!")
            
            resultado = buscar_alunos(alunos, nome_busca)
            
            if resultado:
                for aluno in resultado:
                    print(f"Aluno: {aluno['nome']} - Média: {aluno['media']:.2f} - Situação: {aluno['situacao']}")
            else:
                print("Nenhum aluno foi encontrado.")
 
        case 0:
            print("Saindo...")
            break

        case _:
            print("Opção inválida")

print("Programa encerrado.")