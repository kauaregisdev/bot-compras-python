# código com funções de coleta de informações do usuário
def exibir_boas_vindas():
    print('Bem-vindo ao bot de automação de compras!' \
    '\n''Esse bot foi desenvolvido especificamente para automatizar o processo de compras no site da Growth.')

def escolher_produto():
    return input('Você tem direito a escolher os seguintes produtos:' \
    '\n''1 - Whey Protein Concentrado 1kg (124,90 à vista, 139,00 no cartão)' \
    '\n''2 - Creatina 250g (normal ou Creapure)' \
    '\n''3 - Pré-treino Haze Hardcore 300g (104,90 à vista, 116,50 no cartão)' \
    '\n''4 - Pasta de amendoim integral 1kg (27,90 à vista, 31,00 no cartão)' \
    '\n''5 - Beta-alanina 250g (68,90 à vista, 76,50 no cartão)' \
    '\n''Digite o dígito correspondente ao produto que deseja comprar no site da Growth: ')

def escolher_sabor_whey():
    return input('Ótima escolha! Você tem direito a escolher os seguintes sabores:' \
    '\n''1 - Natural' \
    '\n''2 - Milkshake de chocolate' \
    '\n''3 - Morango' \
    '\n''4 - Cookies and Cream' \
    '\n''5 - Doce de leite' \
    '\n''Digite o dígito correspondente ao sabor desejado: ')

def escolher_creatina():
    return input('Ótima escolha! Você tem direito a escolher as seguintes opções:' \
    '\n''1 - Creatina normal (64,90 à vista, 72,00 no cartão)' \
    '\n''2 - Creatina Creapure (109,90 à vista, 122,00 no cartão)' \
    '\n''Digite o dígito correspondente à opção desejada: ')

def escolher_sabor_pretreino():
    return input('Ótima escolha! Você tem direito a escolher os seguintes sabores:' \
    '\n''1 - Limão' \
    '\n''2 - Laranja' \
    '\n''3 - Melancia' \
    '\n''4 - Uva' \
    '\n''5 - Açaí com Guaraná' \
    '\n''6 - Tutti-Fruti' \
    '\n''Digite o dígito correspondente ao sabor desejado: ')

def receber_cpf():
    return input('Digite o seu CPF (apenas números): ')

def receber_cep():
    return input('Digite o seu CEP: ')

def informa_conta():
    return input('Você já possui uma conta no site da Growth? (s/n): ')

def receber_senha():
    return input('Digite sua senha. Lembre-se que ela deve possuir pelo menos 6 caracteres: ')

def receber_nome():
    return input('Digite o seu nome completo: ')

def receber_email():
    return input('Digite o seu e-mail: ')

def receber_telefone():
    return input('Abaixo, digite o seu telefone (apenas números, com DDD e 9 na frente). Ex.: 85988888888' \
    '\n''')

def receber_sexo():
    return input('Digite o seu sexo, masculino ou feminino (m/f): ')

def receber_endereco():
    return input('Você já possui endereço cadastrado? (s/n): ')

def receber_num_residencia():
    return input('Digite o número da sua residência: ')

def escolher_cupom():
    return input('Você pode usar o cupom de 5% de desconto "cariani" no site da Growth.' \
    '\n''Deseja cupom de 5% de desconto? (s/n): ')

def escolher_metodo_pag():
    return input('Você tem direito a escolher as seguintes formas de pagamento:' \
    '\n''1 - Cartão de crédito' \
    '\n''2 - Boleto à vista' \
    '\n''3 - Pix à vista' \
    '\n''Digite o dígito correspondente à forma de pagamento desejada: ')

def receber_num_cartao():
    return input('Digite o número do cartão de crédito (apenas números): ')

def receber_nome_titular():
    return input('Digite o nome do titular, como está no cartão: ')

def receber_cpf_titular():
    return input('Digite o CPF do titular do cartão: ')

def receber_validade_cartao():
    return input('Digite a validade do cartão (MM/AAAA): ')

def receber_cod_seg():
    return input('Digite o código de segurança do cartão (apenas números): ')

def escolher_parcelas():
    return input('Quantas parcelas você deseja? (1 a 6): ')