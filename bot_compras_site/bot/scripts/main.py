# este código sofrerá mudanças em breve, para melhoria da compreensão do sistema como um todo
def executar_bot():
    import bot_compras_site.bot.scripts.validate as f
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import Select
    from pyautogui import press
    from os import system
    from time import sleep

    # introduzindo o bot
    print('Bem-vindo ao bot de automação de compras!' \
    '\n''Esse bot foi desenvolvido especificamente para automatizar o processo de compras no site da Growth.')
    sleep(10)
    system('cls')
    print('Você tem direito a escolher os seguintes produtos:' \
    '\n''1 - Whey Protein Concentrado 1kg (124,90 à vista, 139,00 no cartão)' \
    '\n''2 - Creatina 250g (normal ou Creapure)' \
    '\n''3 - Pré-treino Haze Hardcore 300g (104,90 à vista, 116,50 no cartão)' \
    '\n''4 - Pasta de amendoim integral 1kg (27,90 à vista, 31,00 no cartão)' \
    '\n''5 - Beta-alanina 250g (68,90 à vista, 76,50 no cartão)')

    # recebendo o produto desejado
    while True:
        pesquisa = input('Digite o dígito correspondente ao produto que deseja comprar no site da Growth: ')

        if pesquisa == '1':
            system('cls')
            print('Ótima escolha! Você tem direito a escolher os seguintes sabores:' \
            '\n''1 - Natural' \
            '\n''2 - Milkshake de chocolate' \
            '\n''3 - Morango' \
            '\n''4 - Cookies and Cream' \
            '\n''5 - Doce de leite')

            sabores_whey = {
                '1': "//div[@class='attrSimples_valores']//span[text()=' Natural ']",
                '2': "//div[@class='attrSimples_valores']//span[text()=' Chocolate Milk Shake ']",
                '3': "//div[@class='attrSimples_valores']//span[text()=' Morango ']",
                '4': "//div[@class='attrSimples_valores']//span[text()=' Cookies and Cream ']",
                '5': "//div[@class='attrSimples_valores']//span[text()=' Doce de leite ']"
            }

            while True: # escolhendo o sabor do whey
                sabor = input('Digite o dígito correspondente ao sabor desejado: ')
                if sabor in sabores_whey:
                    system('cls')
                    sabor = sabores_whey[sabor] # atribui o valor do dicionário ao sabor
                    break
                else:
                    system('cls')
                    print('Sabor inválido.')
                    continue
            pesquisa = 'whey protein concentrado 1kg'
            break

        elif pesquisa == '2': # escolhendo o tipo de creatina
            system('cls')
            print('Ótima escolha! Você tem direito a escolher as seguintes opções:' \
            '\n''1 - Creatina normal (64,90 à vista, 72,00 no cartão)' \
            '\n''2 - Creatina Creapure (109,90 à vista, 122,00 no cartão)')
            opcoes = ['1', '2']

            while True:
                pesquisa = input('Digite o dígito correspondente à opção desejada: ')
                if pesquisa in opcoes:
                    system('cls')
                    pesquisa = 'creatina monohidratada 250g' if pesquisa == '1' else 'creatina creapure 250g'
                    break
                else:
                    system('cls')
                    print('Opção inválida.')
                    continue
            break

        elif pesquisa == '3': # escolhendo o sabor do pré-treino
            system('cls')
            print('Ótima escolha! Você tem direito a escolher os seguintes sabores:' \
            '\n''1 - Limão' \
            '\n''2 - Laranja' \
            '\n''3 - Melancia' \
            '\n''4 - Uva' \
            '\n''5 - Açaí com Guaraná' \
            '\n''6 - Tutti-Fruti')

            sabores_pre_treino = {
                '1': "//div[@class='attrSimples_valores']//span[text()=' Limão ']",
                '2': "//div[@class='attrSimples_valores']//span[text()=' Laranja ']",
                '3': "//div[@class='attrSimples_valores']//span[text()=' Melancia ']",
                '4': "//div[@class='attrSimples_valores']//span[text()=' Uva ']",
                '5': "//div[@class='attrSimples_valores']//span[text()=' Açaí com Guaraná ']",
                '6': "//div[@class='attrSimples_valores']//span[text()=' Tutti-Fruti ']"
            }

            while True:
                sabor = input('Digite o dígito correspondente ao sabor desejado: ')
                if sabor in sabores_pre_treino:
                    system('cls')
                    sabor = sabores_pre_treino[sabor] # atribui o valor do dicionário ao sabor
                    break
                else:
                    system('cls')
                    print('Sabor inválido.')
                    continue
            pesquisa = 'pré-treino haze hardcore 300g'
            break

        elif pesquisa == '4':
            system('cls')
            pesquisa = 'pasta de amendoim integral'
            break

        elif pesquisa == '5':
            system('cls')
            pesquisa = 'beta-alanina em pó'
            break

        else:
            system('cls')
            print('Produto inválido.')
            continue

    # recebendo o CPF do usuário
    while True:
        cpf = input('Digite o seu CPF (apenas números): ')
        f.check_cpf(cpf) # chamando a função de validação de CPF
        if not f.check_cpf(cpf):
            system('cls')
            print('CPF inválido.')
            continue
        else:
            system('cls')
            break

    # recebendo o login e a senha do usuário, ou criando uma conta para o usuário
    while True:
        login = input('Você já possui uma conta no site da Growth? (s/n): ')

        if login.lower() == 's':
            system('cls')
            login = True
            while True: # recebendo a senha do usuário
                print('Digite sua senha abaixo. Certifique-se de que a senha está correta, ou o bot não funcionará!')        
                senha = input('')
                if not f.check_senha(senha): # chamando a função de validação de senha
                    system('cls')
                    print('Senha inválida.')
                    continue
                else:
                    system('cls')
                    break

            while True:
                endereco = input('Você já possui endereço cadastrado? (s/n): ')
                opcoes = ['s', 'S', 'n', 'N']
                if not endereco in opcoes:
                    system('cls')
                    print('Opção inválida.')
                    continue
                else:
                    system('cls')
                    escolha = endereco
                    endereco = True if escolha in ['s', 'S'] else False
                    break
            break

        elif login.lower() == 'n': # recebendo os dados do usuário pra criar uma conta
            system('cls')
            login = False
            while True: # recebendo a senha do usuário   
                print('Você deverá preencher alguns dados para prosseguir com a criação de sua conta.' \
                '\n''Você deve criar uma senha contendo pelo menos 6 caracteres para sua conta.')
                senha = input('Digite uma senha para sua conta: ')
                if not f.check_senha(senha): # chamando a função de validação de senha
                    system('cls')
                    print('Senha inválida.')
                    continue
                else:
                    system('cls')
                    break

            while True: # recebendo o nome completo do usuário
                nome = input('Digite o seu nome completo: ') 
                if not f.check_nome(nome): # chamando a função de validação de nome
                    system('cls')
                    print('Nome inválido.')
                    continue
                else:
                    system('cls')
                    break

            while True:
                email = input('Digite o seu e-mail: ')
                if not f.check_nome(email): # chamando a função de validação de nome
                    system('cls')
                    print('E-mail inválido.')
                    continue
                else:
                    system('cls')
                    break

            while True:
                print('Abaixo, digite o seu telefone (apenas números, com DDD e 9 na frente). Ex.: 85988888888 ')
                tel = input('') 
                if not f.check_telefone(tel): # chamando a função de validação de telefone
                    system('cls')
                    print('Telefone inválido.')
                    continue
                else:
                    system('cls')
                    break

            while True:
                sexo = input('Digite o seu sexo, masculino ou feminino (m/f): ')
                if not f.check_sexo(sexo): # chamando a função de validação de sexo
                    system('cls')
                    print('Sexo inválido.')
                    continue
                else:
                    system('cls')
                    break
            break

        else:
            system('cls')
            print('Opção inválida.')
            continue

    # recebendo o CEP do usuário
    while True:
        cep = input('Digite o seu CEP: ')
        if not f.check_cep(cep): # chamando a função de validação de CEP
            system('cls')
            print('CEP inválido.')
            continue
        else:
            system('cls')
            cep = cep[:5]+'-'+cep[5:] # inserindo o hífen no meio do CEP
            break

    # recebendo o número da residência do usuário, caso necessário
    if not endereco:
        while True:
            num_residencia = input('Digite o número da sua residência: ')
            if not num_residencia.isdigit(): # verificando se o número da casa é um número
                system('cls')
                print('Número inválido.')
                continue
            else:
                system('cls')
                break

    '''
    while True:
        id_residencia = input('Você mora em casa ou apartamento? (c/a): ')
        if id_residencia not in ['c', 'C', 'a', 'A']: # verificando se o usuário digitou c ou a
            system('cls')
            print('Opção inválida.')
            continue
        else:
            system('cls')
            id_residencia = 'Casa' if id_residencia in ['c', 'C'] else 'Apartamento'
            break
    '''

    # escolhendo o cupom de desconto
    while True:
        cupom = input('Você pode usar o cupom de 5% de desconto "cariani" no site da Growth.' \
        '\n''Deseja cupom de 5% de desconto? (s/n): ')
        if cupom == 's':
            system('cls')
            cupom = 'cariani'
            break
        
        elif cupom == 'n':
            system('cls')
            cupom = None
            break
        
        else:
            system('cls')
            print('Opção inválida.')
            continue

    # escolhendo a forma de pagamento
    while True:
        print('Você tem direito a escolher as seguintes formas de pagamento:' \
            '\n''1 - Cartão de crédito' \
            '\n''2 - Boleto à vista' \
            '\n''3 - Pix à vista')
        
        metodos = {
            '1': '//div[@data-tipo-pag="cartao"]',
            '2': '//div[@data-tipo-pag="boleto"]',
            '3': '//div[@data-tipo-pag="pix"]',
        }

        metodo_pagamento = input('Digite o dígito correspondente à forma de pagamento desejada: ')
        if metodo_pagamento in metodos:
            system('cls')
            digito_escolhido = metodo_pagamento
            metodo_pagamento = metodos[metodo_pagamento] # atribui o valor do dicionário ao método de pagamento

            if digito_escolhido == '1': # se o usuário escolheu cartão de crédito
                while True:
                    num_cartao = input('Digite o número do cartão de crédito (apenas números): ')
                    if not num_cartao.isdigit() or len(num_cartao) != 16: # verificando se o número do cartão é um número
                        system('cls')
                        print('Número inválido.')
                        continue

                    nome_titular = input('Digite o nome do titular, como está no cartão: ')
                    if not ' ' in nome_titular:
                        system('cls')
                        print('Nome inválido.')
                        continue

                    validade = input('Digite a validade do cartão (MM/AAAA): ')
                    if not len(validade) == 7 or validade[2] != '/':
                        system('cls')
                        print('Validade inválida.')
                        continue

                    mes, ano = validade.split('/')
                    if mes not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                        system('cls')
                        print('Mês inválido.')
                        continue
                    if int(ano) < 2026 or int(ano) > 2040:
                        system('cls')
                        print('Ano inválido.')
                        continue

                    cod_seg = input('Digite o código de segurança do cartão (apenas números): ')
                    if not cod_seg.isdigit() or len(cod_seg) != 3: # verificando se o código de segurança é um número
                        system('cls')
                        print('Código inválido.')
                        continue

                    parcelas = input('Quantas parcelas você deseja? (1 a 6): ')
                    if not parcelas.isdigit() or int(parcelas) < 1 or int(parcelas) > 6:
                        system('cls')
                        print('Número de parcelas inválido.')
                        continue
                    else:
                        system('cls')
                        break
            break

        else:
            system('cls')
            print('Método de pagamento inválido.')
            continue
        
    
    print('Aguarde enquanto o bot faz a compra...')

    # configurando o webdriver
    driver_path = r"C:\Users\kauar\OneDrive\Documentos\GitHub\bot-compras-python\bot_compras_site\bot\scripts\chromedriver.exe" # caminho do chromedriver
    driver = webdriver.Chrome(service=Service(driver_path), options=webdriver.ChromeOptions()) # criando o objeto do webdriver

    # iniciando o bot
    try:
        # abrindo um site no chromium
        driver.get('https://gsuplementos.com.br') # abre o site da Growth
        driver.maximize_window() # maximiza a janela do navegador
        sleep(5) # espera 5 segundos para carregar a página

        # localizando a barra de pesquisa
        search_bar = driver.find_element(By.ID, 'busca-principal-topo') # localizar barra de pesquisa
        search_bar.click() # clica na barra de pesquisa
        sleep(1)
        search_bar.send_keys(pesquisa) # digita o que o usuário quer comprar
        sleep(1)
        search_bar.send_keys(Keys.ENTER) # pressiona enter para pesquisar
        sleep(5)

        # localizando e escolhendo o produto
        produto = driver.find_element(By.CLASS_NAME, 'cardProd-topo') # encontra o produto pesquisado
        produto.click()
        sleep(10) # espera 10 segundos para carregar a página do produto

        if sabor: # escolhendo o sabor do produto, caso necessário
            lista_sabores = driver.find_element(By.ID, 'attrSimples') # localiza o botão de sabor
            lista_sabores.click()
            sleep(1)

            botao_escolher_sabor = driver.find_element(By.XPATH, sabor) # localiza o botão de sabor desejado (erro no XPATH)
            botao_escolher_sabor.click()
            sleep(1)
        
        # adicionando ao carrinho
        botao_add_carrinho = driver.find_element(By.ID, 'btComprar') # localiza o botão de adicionar ao carrinho
        driver.execute_script("arguments[0].click();", botao_add_carrinho) # usa JavaScript para clicar no botão
        sleep(1)

        botao_ir_carrinho = driver.find_element(By.ID, 'externo-carrinhoLateral-carrinho') # localiza o botão para ir para o carrinho
        botao_ir_carrinho.click()
        sleep(1)

        # calculando o frete
        botao_cep = driver.find_element(By.NAME, 'cep') # localiza o campo de CEP
        botao_cep.click() # clica no campo de CEP
        sleep(1)
        botao_cep.send_keys(cep) # digita o CEP
        sleep(1)

        # preenchendo o cupom de desconto, se houver
        if cupom:
            botao_cupom = driver.find_element(By.NAME, 'cupom') # localiza o campo de cupom
            botao_cupom.click()
            sleep(1)
            botao_cupom.send_keys(cupom) # digita o cupom
            sleep(1)
        
        press('enter') # pressiona enter para aplicar o CEP e, se houver, o cupom
        sleep(5) # esperando o cupom ser aplicado
        
        # indo pra página de finalização de compra
        botao_finalizar = driver.find_element(By.CLASS_NAME, 'resumoPedidoBotoes-finalizar') # localiza o botão de fechar pedido
        botao_finalizar.click() # clica no botão de fechar pedido
        sleep(5)
        
        # preenchendo os dados pessoais
        campo_cpf = driver.find_element(By.NAME, 'email') # localiza o campo de preenchimento com e-mail ou CPF (nesse caso usei CPF)
        campo_cpf.click() # clica no campo de CPF
        sleep(1)
        campo_cpf.send_keys(cpf) # digita o CPF
        sleep(1)
        campo_cpf.send_keys(Keys.ENTER) # pressiona enter para validar o CPF
        sleep(5)

        if login: # entrando na conta do usuário
            campo_senha = driver.find_element(By.NAME, 'senha') # localiza o campo de senha
            campo_senha.send_keys(senha) # digita a senha
            sleep(1)
            campo_senha.send_keys(Keys.ENTER) # pressiona enter para validar a senha
            sleep(10)

        else: # criando uma conta para o usuário
            campo_nome = driver.find_element(By.ID, 'nome-cadastro')
            campo_nome.click()
            sleep(1)
            campo_nome.send_keys(nome)
            campo_nome.send_keys(Keys.ENTER)
            sleep(1)

            campo_email = driver.find_element(By.ID, 'email-cadastro')
            campo_email.click()
            sleep(1)
            campo_email.send_keys(email)
            campo_email.send_keys(Keys.ENTER)
            sleep(1)

            campo_telefone = driver.find_element(By.ID, 'celular-cadastro')
            campo_telefone.click()
            sleep(1)
            campo_telefone.send_keys(tel)
            campo_telefone.send_keys(Keys.ENTER)
            sleep(1)

            campo_sexo = driver.find_element(By.ID, 'masc') if sexo in ['m', 'M'] else driver.find_element(By.ID, 'fem')
            campo_sexo.click()
            sleep(1)
            campo_sexo.send_keys(Keys.ENTER)
            sleep(1)

            campo_senha = driver.find_element(By.ID, 'senha-cadastro')
            campo_senha.click()
            sleep(1)
            campo_senha.send_keys(senha)
            campo_senha.send_keys(Keys.ENTER)
            sleep(10)

        # preenchendo os dados de endereço, caso necessário
        if endereco:
            campo_num_casa = driver.find_element(By.NAME, 'numeroRapido') # localiza o campo de número da casa
            driver.execute_script("arguments[0].click();", campo_num_casa) # clica no campo de número da casa
            sleep(1)
            campo_num_casa.send_keys(num_residencia)
            sleep(1)
            botao_cadastrar_endereco = driver.find_element(By.NAME, 'btnEnviar') # localiza o botão de cadastrar endereço
            botao_cadastrar_endereco.click() # clica no botão de cadastrar endereço
            sleep(1)

        botao_ir_pagamento = driver.find_element(By.ID, 'btnEnderecoIrPagamento') # localiza o botão de ir para a aba de pagamento
        botao_ir_pagamento.click() # clica no botão de ir para a aba de pagamento
        sleep(5)

        # preenchendo os dados de pagamento
        botao_metodo = driver.find_element(By.XPATH, metodo_pagamento) # localiza o botão do método escolhido
        botao_metodo.click() # clica no botão do método escolhido

        if digito_escolhido == '1': # se o usuário escolheu cartão de crédito        
            campo_num_cartao = driver.find_element(By.ID, 'cardNumber') # localiza o campo de número do cartão
            campo_num_cartao.click()
            sleep(1)
            campo_num_cartao.send_keys(num_cartao)
            sleep(1)

            campo_nome_cartao = driver.find_element(By.ID, 'cardholderName') # localiza o campo de nome do titular
            campo_nome_cartao.click()
            sleep(1)
            campo_nome_cartao.send_keys(nome_titular)
            sleep(1)

            campo_cpf_cartao = driver.find_element(By.ID, 'docNumber') # localiza o campo de CPF do titular
            campo_cpf_cartao.click()
            sleep(1)
            campo_cpf_cartao.send_keys(cpf)
            sleep(1)

            campo_select_mes = driver.find_element(By.ID, 'cardExpirationMonth')
            campo_select_mes.click()
            sleep(1)
            campo_mes_val = Select(campo_select_mes)
            campo_mes_val.select_by_value(mes) # seleciona o mês de validade do cartão
            sleep(1)

            campo_select_ano = driver.find_element(By.ID, 'cardExpirationYear')
            campo_select_ano.click()
            sleep(1)
            campo_ano_val = Select(campo_select_ano)
            campo_ano_val.select_by_value(ano) # seleciona o ano de validade do cartão
            sleep(1)

            campo_cod_seg = driver.find_element(By.ID, 'securityCode') # localiza o campo de código de segurança
            campo_cod_seg.click()
            sleep(1)
            campo_cod_seg.send_keys(cod_seg)
            sleep(1)

            campo_parcelas = driver.find_element(By.ID, 'parcelasCartaoMercadoPago') # localiza o campo de parcelas
            campo_parcelas.click()
            sleep(1)

            campo_select_parcelas = Select(campo_parcelas)
            campo_select_parcelas.select_by_value(parcelas) # seleciona o número de parcelas

        sleep(5)
        botao_finalizar_compra = driver.find_element(By.ID, 'finalizarPedido') # localiza o botão de finalizar compra

    finally:
        # fechando o navegador
        driver.quit()

executar_bot()