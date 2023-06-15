ocorrencias = []
ultimo_codigo = 0


def gerar_codigo():
    global ultimo_codigo
    ultimo_codigo += 1
    return str(ultimo_codigo)


def cadastrar_ocorrencia():
    categoria_opcoes = {
        "1": "Sugestão",
        "2": "Elogio",
        "3": "Reclamação"
    }

    print("==== Cadastrar Ocorrência ====")
    print("Categorias:")
    print("1. Sugestão")
    print("2. Elogio")
    print("3. Reclamação")
    categoria_opcao = input("Digite o número correspondente à categoria da ocorrência: ")

    while categoria_opcao not in categoria_opcoes:
        print("Opção inválida. Tente novamente.")
        categoria_opcao = input("Digite o número correspondente à categoria da ocorrência: ")

    descricao = input("Digite a descrição da ocorrência: ")
    codigo = gerar_codigo()
    categoria = categoria_opcoes[categoria_opcao]

    ocorrencias.append({"codigo": codigo, "categoria": categoria, "descricao": descricao})
    print("\nOcorrência cadastrada com sucesso!\n")


def listar_ocorrencias():
    if len(ocorrencias) == 0:
        print("Nenhuma ocorrência cadastrada.\n")
        return

    print("==== Lista de Ocorrências ====\n")
    for ocorrencia in ocorrencias:
        print(f"Código: {ocorrencia['codigo']}")
        print(f"Categoria: {ocorrencia['categoria']}")
        print(f"Descrição: {ocorrencia['descricao']}")
        print("---------------------")
    print()

    opcao = input(
        "1. Consultar por Código\n2. Consultar por Categoria\n3. Voltar\nDigite o número correspondente à opção "
        "desejada: ")
    print()

    if opcao == "1":
        consultar_ocorrencia_por_codigo()
    elif opcao == "2":
        pesquisar_ocorrencias_por_categoria()
    elif opcao == "3":
        return
    else:
        print("Opção inválida. Tente novamente.\n")


def consultar_ocorrencia_por_codigo():
    if len(ocorrencias) == 0:
        print("Nenhuma ocorrência cadastrada.\n")
        return

    codigo = input("Digite o código da ocorrência que deseja consultar: ")
    print()

    for ocorrencia in ocorrencias:
        if ocorrencia["codigo"] == codigo:
            print("==== Ocorrência Encontrada ====")
            print(f"Código: {ocorrencia['codigo']}")
            print(f"Categoria: {ocorrencia['categoria']}")
            print(f"Descrição: {ocorrencia['descricao']}")
            print("---------------------")
            return

    print("Ocorrência não encontrada.\n")


def pesquisar_ocorrencias_por_categoria():
    if len(ocorrencias) == 0:
        print("Nenhuma ocorrência cadastrada.\n")
        return

    print("Categorias disponíveis:")
    categorias = set(ocorrencia['categoria'] for ocorrencia in ocorrencias)
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")

    opcao = input("Digite o número correspondente à categoria que deseja pesquisar: ")
    print()

    while not opcao.isdigit() or int(opcao) < 1 or int(opcao) > len(categorias):
        print("Opção inválida. Tente novamente.")
        opcao = input("Digite o número correspondente à categoria que deseja pesquisar: ")
        print()

    categoria_selecionada = list(categorias)[int(opcao) - 1]
    ocorrencias_categoria = [ocorrencia for ocorrencia in ocorrencias if
                             ocorrencia['categoria'] == categoria_selecionada]

    if len(ocorrencias_categoria) == 0:
        print(f"Nenhuma ocorrência cadastrada na categoria {categoria_selecionada}.\n")
    else:
        print(f"==== Ocorrências na Categoria: {categoria_selecionada} ====\n")
        for ocorrencia in ocorrencias_categoria:
            print(f"Código: {ocorrencia['codigo']}")
            print(f"Categoria: {ocorrencia['categoria']}")
            print(f"Descrição: {ocorrencia['descricao']}")
            print("---------------------")
        print()


def apagar_ocorrencia():
    print("==== Apagar Ocorrência ====\n")
    if len(ocorrencias) == 0:
        print("Nenhuma ocorrência cadastrada.\n")
        return

    print("1. Apagar ocorrência específica")
    print("2. Apagar todas as ocorrências")
    opcao = input("Digite a opção desejada: ")
    print()

    if opcao == "1":
        codigo = input("Digite o código da ocorrência que deseja apagar: ")
        for ocorrencia in ocorrencias:
            if ocorrencia["codigo"] == codigo:
                ocorrencias.remove(ocorrencia)
                print("Ocorrência removida com sucesso!\n")
                return
        print("Ocorrência não encontrada.\n")
    elif opcao == "2":
        ocorrencias.clear()
        print("Todas as ocorrências foram removidas.\n")
    else:
        print("Opção inválida. Tente novamente.\n")


def sair():
    print("Saindo do sistema...")


opcao = ""
while opcao != "4":
    print("==== Menu ====")
    print("1. Cadastrar Ocorrências")
    print("2. Listar Ocorrências")
    print("3. Apagar Ocorrência")
    print("4. Sair")
    print()

    opcao = input("Digite a opção desejada: ")
    print()

    if opcao == "1":
        cadastrar_ocorrencia()
    elif opcao == "2":
        listar_ocorrencias()
    elif opcao == "3":
        apagar_ocorrencia()
    elif opcao == "4":
        sair()
    else:
        print("Opção inválida. Por favor, tente novamente.\n")
