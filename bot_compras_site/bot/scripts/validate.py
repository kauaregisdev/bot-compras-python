# código com funções de validação de informações fornecidas pelo usuário
def validar_pesquisa(valor):
    opcoes = {
        '1': 'whey protein concentrado 1kg',
        '2': 'creatina 250g',
        '3': 'pré-treino haze hardcore 300g',
        '4': 'pasta de amendoim integral',
        '5': 'beta-alanina em pó',
    }
    if valor in opcoes:
        pesquisa = opcoes[valor]
        return pesquisa
    else:
        return False

def validar_sabor_whey(valor):
    sabores_whey = {
        '1': "//div[@class='attrSimples_valores']//span[text()=' Natural ']",
        '2': "//div[@class='attrSimples_valores']//span[text()=' Chocolate Milk Shake ']",
        '3': "//div[@class='attrSimples_valores']//span[text()=' Morango ']",
        '4': "//div[@class='attrSimples_valores']//span[text()=' Cookies and Cream ']",
        '5': "//div[@class='attrSimples_valores']//span[text()=' Doce de leite ']"
    }   
    if valor in sabores_whey:
        sabor = sabores_whey[sabor]
        return sabor
    else:
        return False

def validar_creatina(valor):
    opcoes = ['1', '2']     
    if valor in opcoes:
        valor = 'creatina monohidratada 250g' if valor == '1' else 'creatina creapure 250g'
        return valor
    else:
        return False
    
def validar_sabor_pretreino(valor):
    sabores_pre_treino = {
        '1': "//div[@class='attrSimples_valores']//span[text()=' Limão ']",
        '2': "//div[@class='attrSimples_valores']//span[text()=' Laranja ']",
        '3': "//div[@class='attrSimples_valores']//span[text()=' Melancia ']",
        '4': "//div[@class='attrSimples_valores']//span[text()=' Uva ']",
        '5': "//div[@class='attrSimples_valores']//span[text()=' Açaí com Guaraná ']",
        '6': "//div[@class='attrSimples_valores']//span[text()=' Tutti-Fruti ']"
    }           
    if valor in sabores_pre_treino:
        sabor = sabores_pre_treino[sabor]
        return sabor
    else:
        return False

def digitos_verificadores(cpf_input):
    soma_cpf = 0
    multi = 10
    for digito in cpf_input:
        soma_cpf += multi*int(digito)
        multi -= 1

    mult_cpf = soma_cpf * 10
    resto1_cpf = mult_cpf % 11
    ver1_cpf = 0 if resto1_cpf > 9 else resto1_cpf

    soma_cpf = 0
    multi = 11

    for digito in cpf_input:
        soma_cpf += multi*(int(digito))
        multi -= 1

    mult_cpf = soma_cpf * 10
    ver2_cpf = mult_cpf % 11
    ver2_cpf = 0 if ver2_cpf > 9 else ver2_cpf

    cpf_input = str(cpf_input) + str(ver1_cpf) + str(ver2_cpf)
    return cpf_input

def gen_cpf():
    from random import randint
    cpf_input = ''
    for i in range(9):
        cpf_input += str(randint(0, 9))

    digitos_verificadores(cpf_input)

    print(f'O CPF gerado é {cpf_input}.')

def check_cpf(cpf_input):
    if not cpf_input.isnumeric() or len(cpf_input) != 11 or cpf_input == cpf_input[0] * len(cpf_input):
        return False
    else:
        cpf_v = cpf_input[:9]
        digitos_verificadores(cpf_v)

        if cpf_input == cpf_v:
            return cpf_input
        else:
            return False

def check_cep(valor):
    return valor if len(valor) == 8 and valor.isdigit() else False

def check_senha(valor):
    return valor if len(valor) >= 6 else False

def possui_conta(valor):
    return valor if valor in ['s', 'S', 'n', 'N'] else False

def check_nome(valor):
    return valor if ' ' in valor else False

def check_email(valor):
    from email_validator import validate_email, EmailNotValidError
    try:
        validate_email(valor)
        return valor
    except EmailNotValidError as e:
        return False
    
def check_telefone(valor):
    return False if not valor.isnumeric() or len(valor) != 11 else valor

def check_sexo(valor):
    return valor if valor in ['m', 'M', 'f', 'F'] else False

def possui_endereco(valor):
    return valor if valor in ['s', 'S', 'n', 'N'] else False

def validar_num_residencia(valor):
    if not valor.isdigit():
        return False
    else:
        return valor

def validar_cupom(valor):
    return valor if valor in ['s', 'S', 'n', 'N'] else False

def existe_cupom(valor):
    return 'cariani' if valor in ['s', 'S'] else False

def validar_metodo_pag(valor):  
    metodos = {
        '1': '//div[@data-tipo-pag="cartao"]',
        '2': '//div[@data-tipo-pag="boleto"]',
        '3': '//div[@data-tipo-pag="pix"]',
    }
    if valor in metodos:
        valor = metodos[valor]
        return valor
    else:
        return False

def validar_num_cartao(valor):
    return False if not valor.isdigit() or len(valor) != 16 else valor

def validar_nome_titular(valor):               
    return False if not ' ' in valor else valor

def validar_validade(valor):
    return False if not len(valor) == 7 or valor[2] != '/' else valor

def validar_mes_validade(valor):
    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    mes, ano = valor.split('/')
    return False if mes not in meses or int(ano) < 2026 or int(ano) > 2040 else mes, ano

def validar_cod_seg(valor):                
    return False if not valor.isdigit() or len(valor) != 3 else valor

def validar_parcelas(valor):   
    return False if not valor.isdigit() or int(valor) < 1 or int(valor) > 6 else valor