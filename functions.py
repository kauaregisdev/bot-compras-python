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
            print(f'Este CPF não é válido.')
            return False

def get_cep(a):
    from os import system

    if len(a) == 8 and a.isdigit():
        system('cls')
        # Inserindo um hífen no meio do CEP
        return True
    else:
        system('cls')
        print('CEP inválido.')
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
        system('cls')
        print('Digite "s" ou "n".')
        return False

def get_nome(a):
    from os import system
    while True:
        a = input('Digite seu nome completo: ')
        if not ' ' in a:
            system('cls')
            print('Digite seu nome completo.')
            continue
        else:
            system('cls')
            break
    return a

def get_email():
    from os import system
    from email_validator import validate_email, EmailNotValidError
    while True:
        print('Digite seu e-mail abaixo. Certifique-se de que o e-mail está correto, ou o bot não funcionará!')
        email = input('')
        system('cls')
        try:
            validate_email(email)
            return email
        except EmailNotValidError as e:
            print('Digite um e-mail válido.')
            continue
    
def get_telefone():
    from os import system
    while True:
        telefone = input('Digite seu telefone (apenas números): ')
        if not telefone.isnumeric():
            system('cls')
            print('Digite números, sem letras ou espaços vazios.')
            continue
        if len(telefone) != 11:
            system('cls')
            print('Digite o DDD e o número do telefone.')
            continue
        else:
            system('cls')
            telefone = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
            break
    return telefone

def get_sexo():
    from os import system
    while True:
        sexo = input('Digite seu sexo (m/f): ')
        if sexo.lower() == 'm':
            system('cls')
            sexo = 'Masculino'
            break
        elif sexo.lower() == 'f':
            system('cls')
            sexo = 'Feminino'
            break
        else:
            system('cls')
            print('Sexo inválido.')
            continue
    return sexo