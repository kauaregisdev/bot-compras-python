import automation as a
import terminal as t
import validate as v
from time import sleep

t.exibir_boas_vindas() # apresenta o sistema
sleep(10)

while True: # recebe e valida a pesquisa
    produto = t.escolher_produto()
    pesquisa = v.validar_pesquisa(produto)
    if not pesquisa:
        print('Produto inválido!')
        continue
    else:
        break

if produto == '1': # escolhe o sabor do whey
    while True:
        sabor = t.escolher_sabor_whey()
        sabor = v.validar_sabor_whey(sabor)
        if not sabor:
            print('Sabor inválido!')
            continue
        else:
            break

if produto == '2': # escolhe o tipo de creatina
    while True:
        tipo = t.escolher_creatina()
        tipo = v.validar_creatina(tipo)
        if not tipo:
            print('Sabor inválido!')
            continue
        else:
            break

if produto == '3': # escolhe o sabor do pré-treino
    while True:
        sabor = t.escolher_sabor_pretreino()
        sabor = v.validar_sabor_pretreino(sabor)
        if not sabor:
            print('Sabor inválido!')
            continue
        else:
            break

while True:
    cpf = t.receber_cpf()
    cpf = v.check_cpf(cpf)
    if not cpf:
        print('CPF inválido!')
        continue
    else:
        break

while True:
    cep = t.receber_cep()
    cep = v.check_cep(cep)
    if not cep:
        print('CEP inválido!')
        continue
    else:
        break

while True:
    conta = t.informa_conta()
    conta = v.possui_conta(conta)
    if not conta:
        print('Input inválido!')
        continue
    else:
        break

if conta in ['n', 'N']:
    while True:
        nome = t.receber_nome()
        nome = v.check_nome(nome)
        if not nome:
            print('Nome inválido!')
            continue
        else:
            break

    while True:
        email = t.receber_email()
        email = v.check_email(email)
        if not email:
            print('E-mail inválido!')
            continue
        else:
            break

    while True:
        tel = t.receber_telefone()
        tel = v.check_telefone(tel)
        if not tel:
            print('Telefone inválido!')
            continue
        else:
            break

    while True:
        sexo = t.receber_sexo()
        sexo = v.check_sexo(sexo)
        if not sexo:
            print('Sexo inválido!')
            continue
        else:
            break

else:
    while True:
        endereco = t.receber_endereco()
        endereco = v.possui_endereco(endereco)
        if not endereco:
            print('Input inválido!')
            continue
        else:
            break

    if not endereco:
        while True:
            num_residencia = t.receber_num_residencia()
            num_residencia = v.validar_num_residencia(num_residencia)
            if not num_residencia:
                print('Número inválido!')
                continue
            else:
                break

while True:
    cupom = t.escolher_cupom()
    cupom = v.validar_cupom(cupom)
    if not cupom:
        print('Input inválido!')
        continue
    else:
        cupom = v.existe_cupom(cupom)
        break

while True:
    escolha_metodo = t.escolher_metodo_pag()
    metodo_pag = v.validar_metodo_pag(escolha_metodo)
    if not metodo_pag:
        print('Método inválido!')
        continue
    else:
        break

if escolha_metodo == '1':
    while True:
        ...

    while True:
        ...
    
    while True:
        ...

    while True:
        ...

    while True:
        ...

try: # executa o bot
    ...
finally: # fecha o navegador
    a.finalizar()