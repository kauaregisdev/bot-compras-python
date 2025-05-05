def get_cpf(a):
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

def get_cep(a):
    if len(a) == 8 and a.isdigit():
        # Inserindo um hífen no meio do CEP
        return True
    else:
        return False

def get_senha(a, b):
    from os import system

    if a.lower() == 's':
        system('cls')
        a = True
        print('Digite sua senha abaixo. Certifique-se de que a senha está correta, ou o bot não funcionará!')
        b = input('')
        if len(b) >= 6:
            system('cls')
            return a, b
        else:
            system('cls')
            print('A senha deve ter pelo menos 6 caracteres.')         
    elif a.lower() == 'n':
        system('cls')
        a = False
        print('Você não possui uma conta. Você deverá criar uma senha para sua conta.')
        print('Você deverá preencher alguns dados para prosseguir.' \
        '\n''Você deve criar uma senha contendo pelo menos 6 caracteres para sua conta.')
        b = input('Digite uma senha para sua conta: ')
        if len(b) >= 6:
            system('cls')
            return a, b
        else:
            system('cls')
            print('A senha deve ter pelo menos 6 caracteres.')
    else:
        return False

def get_nome(a):
    if not ' ' in a:
        return False
    else:
        return a

def get_email(a):
    from email_validator import validate_email, EmailNotValidError
    try:
        validate_email(a)
        return a
    except EmailNotValidError as e:
        return False
    
def get_telefone(a):
    if not a.isnumeric():
        return False
    if len(a) != 11:
        return False
    else:
        return a

def get_sexo(a):
    if a in ['m', 'M', 'f', 'F']:
        return a
    else:
        return False