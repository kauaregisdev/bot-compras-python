# código com funções de coleta de informações do usuário
def exibir_boas_vindas():
    print('Bem-vindo ao bot de automação de compras!' \
    '\n''Esse bot foi desenvolvido especificamente para automatizar o processo de compras no site da Growth.')

def escolher_produto():
    pesquisa = input('Você tem direito a escolher os seguintes produtos:' \
    '\n''1 - Whey Protein Concentrado 1kg (124,90 à vista, 139,00 no cartão)' \
    '\n''2 - Creatina 250g (normal ou Creapure)' \
    '\n''3 - Pré-treino Haze Hardcore 300g (104,90 à vista, 116,50 no cartão)' \
    '\n''4 - Pasta de amendoim integral 1kg (27,90 à vista, 31,00 no cartão)' \
    '\n''5 - Beta-alanina 250g (68,90 à vista, 76,50 no cartão)' \
    '\n''Digite o dígito correspondente ao produto que deseja comprar no site da Growth: ')
    return pesquisa

def escolher_sabor_whey():
    sabor = input('Ótima escolha! Você tem direito a escolher os seguintes sabores:' \
    '\n''1 - Natural' \
    '\n''2 - Milkshake de chocolate' \
    '\n''3 - Morango' \
    '\n''4 - Cookies and Cream' \
    '\n''5 - Doce de leite' \
    '\n''Digite o dígito correspondente ao sabor desejado: ')
    return sabor

def escolher_creatina():
    tipo_creatina = input('Ótima escolha! Você tem direito a escolher as seguintes opções:' \
    '\n''1 - Creatina normal (64,90 à vista, 72,00 no cartão)' \
    '\n''2 - Creatina Creapure (109,90 à vista, 122,00 no cartão)' \
    '\n''Digite o dígito correspondente à opção desejada: ')
    return tipo_creatina

def escolher_sabor_pretreino():
    sabor = input('Ótima escolha! Você tem direito a escolher os seguintes sabores:' \
    '\n''1 - Limão' \
    '\n''2 - Laranja' \
    '\n''3 - Melancia' \
    '\n''4 - Uva' \
    '\n''5 - Açaí com Guaraná' \
    '\n''6 - Tutti-Fruti' \
    '\n''Digite o dígito correspondente ao sabor desejado: ')
    return sabor

def receber_cpf():
    cpf = input('Digite o seu CPF (apenas números): ')
    return cpf

def possui_conta():
    conta = input('Você já possui uma conta no site da Growth? (s/n): ')
    return conta

def receber_senha():
    senha = input('Digite sua senha. Lembre-se que ela deve possuir pelo menos 6 caracteres: ')
    return senha

def receber_endereco():
    endereco = input('Você já possui endereço cadastrado? (s/n): ')
    return endereco

def receber_nome():
    nome = input('Digite o seu nome completo: ')
    return nome

def receber_email():
    email = input('Digite o seu e-mail: ')
    return email

def receber_telefone():
    tel = input('Abaixo, digite o seu telefone (apenas números, com DDD e 9 na frente). Ex.: 85988888888' \
    '\n''')
    return tel

def receber_sexo():
    sexo = input('Digite o seu sexo, masculino ou feminino (m/f): ')
    return sexo

def receber_cep():
    cep = input('Digite o seu CEP: ')
    return cep

def receber_num_residencia():
    num_residencia = input('Digite o número da sua residência: ')
    return num_residencia

def escolher_cupom():
    cupom = input('Você pode usar o cupom de 5% de desconto "cariani" no site da Growth.' \
    '\n''Deseja cupom de 5% de desconto? (s/n): ')
    return cupom

def escolher_metodo_pag():
    metodo_pagamento = input('Você tem direito a escolher as seguintes formas de pagamento:' \
    '\n''1 - Cartão de crédito' \
    '\n''2 - Boleto à vista' \
    '\n''3 - Pix à vista' \
    '\n''Digite o dígito correspondente à forma de pagamento desejada: ')
    return metodo_pagamento

def receber_num_cartao():
    num_cartao = input('Digite o número do cartão de crédito (apenas números): ')
    return num_cartao

def receber_nome_titular():
    nome_titular = input('Digite o nome do titular, como está no cartão: ')
    return nome_titular

def receber_validade_cartao():
    validade = input('Digite a validade do cartão (MM/AAAA): ')
    return validade

def receber_cod_seg():
    cod_seg = input('Digite o código de segurança do cartão (apenas números): ')
    return cod_seg

def escolher_parcelas():
    parcelas = input('Quantas parcelas você deseja? (1 a 6): ')
    return parcelas