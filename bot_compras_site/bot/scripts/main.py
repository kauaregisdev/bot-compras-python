# código desorganizado por enquanto, logo vou reorganizá-lo por arquivos, cada um contendo uma função que será desempenhada num arquivo main.py
from . import inputs as f
from os import system


# recebendo o produto desejado
while True:
    

    if pesquisa == '1':
        system('cls')
        

        sabores_whey = {
            '1': "//div[@class='attrSimples_valores']//span[text()=' Natural ']",
            '2': "//div[@class='attrSimples_valores']//span[text()=' Chocolate Milk Shake ']",
            '3': "//div[@class='attrSimples_valores']//span[text()=' Morango ']",
            '4': "//div[@class='attrSimples_valores']//span[text()=' Cookies and Cream ']",
            '5': "//div[@class='attrSimples_valores']//span[text()=' Doce de leite ']"
        }

        while True: # escolhendo o sabor do whey
            
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
        
        opcoes = ['1', '2']

        while True:
            
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
        

        sabores_pre_treino = {
            '1': "//div[@class='attrSimples_valores']//span[text()=' Limão ']",
            '2': "//div[@class='attrSimples_valores']//span[text()=' Laranja ']",
            '3': "//div[@class='attrSimples_valores']//span[text()=' Melancia ']",
            '4': "//div[@class='attrSimples_valores']//span[text()=' Uva ']",
            '5': "//div[@class='attrSimples_valores']//span[text()=' Açaí com Guaraná ']",
            '6': "//div[@class='attrSimples_valores']//span[text()=' Tutti-Fruti ']"
        }

        while True:
            
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
    

    if login.lower() == 's':
        system('cls')
        login = True
        while True: # recebendo a senha do usuário
            
            if not f.check_senha(senha): # chamando a função de validação de senha
                system('cls')
                print('Senha inválida.')
                continue
            else:
                system('cls')
                break

        while True:
            
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
             
            if not f.check_nome(nome): # chamando a função de validação de nome
                system('cls')
                print('Nome inválido.')
                continue
            else:
                system('cls')
                break

        while True:
            
            if not f.check_nome(email): # chamando a função de validação de nome
                system('cls')
                print('E-mail inválido.')
                continue
            else:
                system('cls')
                break

        while True:
             
            if not f.check_telefone(tel): # chamando a função de validação de telefone
                system('cls')
                print('Telefone inválido.')
                continue
            else:
                system('cls')
                break

        while True:
            
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
    
    
    metodos = {
        '1': '//div[@data-tipo-pag="cartao"]',
        '2': '//div[@data-tipo-pag="boleto"]',
        '3': '//div[@data-tipo-pag="pix"]',
    }

    
    if metodo_pagamento in metodos:
        system('cls')
        digito_escolhido = metodo_pagamento
        metodo_pagamento = metodos[metodo_pagamento] # atribui o valor do dicionário ao método de pagamento

        if digito_escolhido == '1': # se o usuário escolheu cartão de crédito
            while True:
                
                if not num_cartao.isdigit() or len(num_cartao) != 16: # verificando se o número do cartão é um número
                    system('cls')
                    print('Número inválido.')
                    continue

                
                if not ' ' in nome_titular:
                    system('cls')
                    print('Nome inválido.')
                    continue

                
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

                
                if not cod_seg.isdigit() or len(cod_seg) != 3: # verificando se o código de segurança é um número
                    system('cls')
                    print('Código inválido.')
                    continue

                
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