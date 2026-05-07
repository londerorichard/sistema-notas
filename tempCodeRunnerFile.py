    while True:
        nome = input("Nome do aluno: ").lower().strip()

        if nome.replace(" ", "").isalpha():
            break

        print("Nome inválido!")
