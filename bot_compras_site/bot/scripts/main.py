def execute():
    import automation as a
    import terminal as t
    import validate as v
    from time import sleep
    from os import system

    print(f'Executando o bot para o produto: {produto}')
    t.exibir_boas_vindas() # apresenta o sistema
    sleep(10)
    system('cls')

    while True: # recebe e valida a pesquisa
        sabor = None
        produto = t.escolher_produto()
        pesquisa = v.validar_pesquisa(produto)
        if not pesquisa:
            system('cls')
            print('Produto inválido!')
            continue
        else:
            system('cls')
            break

    if produto == '1': # escolhe o sabor do whey
        while True:
            sabor = t.escolher_sabor_whey()
            sabor = v.validar_sabor_whey(sabor)
            if not sabor:
                system('cls')
                print('Sabor inválido!')
                continue
            else:
                system('cls')
                break

    if produto == '2': # escolhe o tipo de creatina
        while True:
            tipo = t.escolher_creatina()
            tipo = v.validar_creatina(tipo)
            if not tipo:
                system('cls')
                print('Sabor inválido!')
                continue
            else:
                system('cls')
                break

    if produto == '3': # escolhe o sabor do pré-treino
        while True:
            sabor = t.escolher_sabor_pretreino()
            sabor = v.validar_sabor_pretreino(sabor)
            if not sabor:
                system('cls')
                print('Sabor inválido!')
                continue
            else:
                system('cls')
                break

    while True:
        cpf = t.receber_cpf()
        cpf = v.check_cpf(cpf)
        if not cpf:
            system('cls')
            print('CPF inválido!')
            continue
        else:
            system('cls')
            break

    while True:
        cep = t.receber_cep()
        cep = v.check_cep(cep)
        if not cep:
            system('cls')
            print('CEP inválido!')
            continue
        else:
            system('cls')
            break

    while True:
        conta = t.informa_conta()
        conta = v.possui_conta(conta)
        if not conta:
            system('cls')
            print('Input inválido!')
            continue
        else:
            system('cls')
            break

    while True:
        senha = t.receber_senha()
        senha = v.check_senha(senha)
        if not senha:
            system('cls')
            print('Senha inválida!')
            continue
        else:
            system('cls')
            break

    if conta in ['n', 'N']:
        while True:
            nome = t.receber_nome()
            nome = v.check_nome(nome)
            if not nome:
                system('cls')
                print('Nome inválido!')
                continue
            else:
                system('cls')
                break

        while True:
            email = t.receber_email()
            email = v.check_email(email)
            if not email:
                system('cls')
                print('E-mail inválido!')
                continue
            else:
                system('cls')
                break

        while True:
            tel = t.receber_telefone()
            tel = v.check_telefone(tel)
            if not tel:
                system('cls')
                print('Telefone inválido!')
                continue
            else:
                system('cls')
                break

        while True:
            sexo = t.receber_sexo()
            sexo = v.check_sexo(sexo)
            if not sexo:
                system('cls')
                print('Sexo inválido!')
                continue
            else:
                system('cls')
                break

    else:
        while True:
            endereco = t.receber_endereco()
            endereco = v.possui_endereco(endereco)
            if not endereco:
                system('cls')
                print('Input inválido!')
                continue
            else:
                system('cls')
                break

        if not endereco:
            while True:
                num_residencia = t.receber_num_residencia()
                num_residencia = v.validar_num_residencia(num_residencia)
                if not num_residencia:
                    system('cls')
                    print('Número inválido!')
                    continue
                else:
                    system('cls')
                    break

    while True:
        cupom = t.escolher_cupom()
        cupom = v.validar_cupom(cupom)
        if not cupom:
            system('cls')
            print('Input inválido!')
            continue
        else:
            system('cls')
            cupom = v.existe_cupom(cupom)
            break

    while True:
        escolha_metodo = t.escolher_metodo_pag()
        metodo_pag = v.validar_metodo_pag(escolha_metodo)
        if not metodo_pag:
            system('cls')
            print('Método inválido!')
            continue
        else:
            system('cls')
            break

    if escolha_metodo == '1':
        while True:
            num_cartao = t.receber_num_cartao()
            num_cartao = v.validar_num_cartao(num_cartao)
            if not num_cartao:
                system('cls')
                print('Número inválido!')
                continue
            else:
                system('cls')
                break

        while True:
            nome_titular = t.receber_nome_titular()
            nome_titular = v.check_nome(nome_titular)
            if not nome_titular:
                system('cls')
                print('Número inválido!')
                continue
            else:
                system('cls')
                break
        
        while True:
            cpf_titular = t.receber_cpf_titular()
            cpf_titular = v.check_cpf(cpf_titular)
            if not cpf_titular:
                system('cls')
                print('CPF inválido!')
                continue
            else:
                system('cls')
                break

        while True:
            validade_cartao = t.receber_validade_cartao()
            validade_cartao = v.validar_validade(validade_cartao)
            if not validade_cartao:
                system('cls')
                print('Validade inválida!')
                continue
            else:
                system('cls')
                mes, ano = v.validar_mes_ano(validade_cartao)
                break

        while True:
            cod_seg = t.receber_cod_seg()
            cod_seg = v.validar_cod_seg(cod_seg)
            if not cod_seg:
                system('cls')
                print('Código inválido!')
                continue
            else:
                system('cls')
                break

        while True:
            parcelas = t.escolher_parcelas()
            parcelas = v.validar_parcelas(parcelas)
            if not parcelas:
                system('cls')
                print('Parcela inválida!')
                continue
            else:
                system('cls')
                break

    driver = a.iniciar()
    try: # executa o bot
        a.abrir_site(driver)
        a.barra_pesquisa(driver, pesquisa)
        a.localizar_produto(driver)

        if sabor:
            a.localizar_sabor(driver, sabor)

        a.adicionar_carrinho(driver)
        a.ir_carrinho(driver)
        a.calcular_frete(driver, cep)

        if cupom:
            a.preencher_cupom(driver, cupom)

        a.ir_pagina_final(driver)
        a.preencher_cpf(driver, cpf)

        if conta in ['s', 'S']:
            a.inserir_senha(driver, senha)
        else:
            a.inserir_nome(driver, nome)
            a.inserir_email(driver, email)
            a.inserir_telefone(driver, tel)
            a.inserir_sexo(driver, sexo)
            a.criar_senha(driver, senha)

        if endereco in ['n', 'N']:
            a.cadastrar_endereco(driver, num_residencia)
        a.ir_pagamento(driver)
        a.localizar_metodo_pag(driver, metodo_pag)

        if escolha_metodo == '1':
            a.inserir_num_cartao(driver, num_cartao)
            a.inserir_nome_titular(driver, nome_titular)
            a.inserir_cpf_titular(driver, cpf_titular)
            a.inserir_mes_validade(driver, mes)
            a.inserir_ano_validade(driver, ano)
            a.inserir_cod_seg(driver, cod_seg)
            a.inserir_campo_parcelas(driver, parcelas)

        a.finalizar_compra(driver)

    finally: # fecha o navegador
        a.finalizar(driver)

execute()