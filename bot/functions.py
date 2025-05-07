def gen_cpf():
    from random import randint
    cpf_input = ''
    soma_cpf = 0
    multi = 10
    
    for i in range(9):
        cpf_input += str(randint(0, 9)) 

    for digito in cpf_input:     
        soma_cpf += multi*(int(digito))
        multi -= 1

    mult_cpf = soma_cpf * 10
    ver1_cpf = mult_cpf % 11
    ver1_cpf = 0 if ver1_cpf > 9 else ver1_cpf
            
    soma_cpf = 0
    multi = 11
    cpf_input = cpf_input + str(ver1_cpf)

    for digito in cpf_input:
        soma_cpf += multi*(int(digito))
        multi -= 1

    mult_cpf = soma_cpf * 10
    ver2_cpf = mult_cpf % 11
    ver2_cpf = 0 if ver2_cpf > 9 else ver2_cpf
            
    cpf_input = cpf_input + str(ver2_cpf)

    print(f'O CPF gerado é {cpf_input}.')

def check_cpf(a):
    from os import system
    soma_cpf = 0
    multi = 10
    
    if not a.isnumeric():
        system('cls')
        print('Digite números, sem letras ou espaços vazios.')
    
    char_repeat = a == a[0] * len(a)
    if char_repeat:
        system('cls')
        print('Digite números distintos.')
    
    if len(a) != 11:
        system('cls')
        print('Digite os 11 números do CPF.')

    else:
        system('cls')
        cpf_v = a[:9]

        for digito in cpf_v:     
            soma_cpf += multi*(int(digito))
            multi -= 1

        mult_cpf = soma_cpf * 10
        ver1_cpf = mult_cpf % 11
        ver1_cpf = 0 if ver1_cpf > 9 else ver1_cpf
            
        soma_cpf = 0
        multi = 11
        cpf_v = cpf_v + str(ver1_cpf)

        for digito in cpf_v:
            soma_cpf += multi*(int(digito))
            multi -= 1

        mult_cpf = soma_cpf * 10
        ver2_cpf = mult_cpf % 11
        ver2_cpf = 0 if ver2_cpf > 9 else ver2_cpf
            
        cpf_calculo = cpf_v + str(ver2_cpf)

        if a == cpf_calculo:
            return True
        else:
            return False

def check_cep(a):
    return True if len(a) == 8 and a.isdigit() else False

def check_senha(a):
    return a if len(a) >= 6 else False

def check_nome(a):
    return False if not ' ' in a else a

def check_email(a):
    from email_validator import validate_email, EmailNotValidError
    try:
        validate_email(a)
        return True
    except EmailNotValidError as e:
        return False
    
def check_telefone(a):
    return False if not a.isnumeric() or len(a) != 11 else a

def check_sexo(a):
        return a if a in ['m', 'M', 'f', 'F'] else False