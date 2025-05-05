import functions as f
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pyautogui import write, press
from os import system
from time import sleep
sabor = None
senha = None
nome = None
email = None
telefone = None
sexo = None

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
sleep(20)
system('cls')

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
        sleep(15)
        system('cls')
        while True:
            sabor = input('Digite o dígito correspondente ao sabor desejado: ')
            if sabor == '1':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Natural ']"
                break
            elif sabor == '2':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Chocolate Milk Shake ']"
                break
            elif sabor == '3':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Morango ']"
                break
            elif sabor == '4':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Cookies and Cream ']"
                break
            elif sabor == '5':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Doce de leite ']"
                break
            else:
                system('cls')
                print('Sabor inválido.')
                continue
        pesquisa = 'whey protein concentrado 1kg'
        break

    elif pesquisa == '2':
        system('cls')
        print('Ótima escolha! Você tem direito a escolher as seguintes opções:' \
        '\n''1 - Creatina normal (64,90 à vista, 72,00 no cartão)' \
        '\n''2 - Creatina Creapure (109,90 à vista, 122,00 no cartão)')
        sleep(15)
        system('cls')
        while True:
            pesquisa = input('Digite o dígito correspondente à opção desejada: ')
            if pesquisa == '1':
                system('cls')
                pesquisa = 'creatina monohidratada 250g'
                break
            elif pesquisa == '2':
                system('cls')
                pesquisa = 'creatina creapure 250g'
                break
            else:
                system('cls')
                print('Opção inválida.')
                continue
        break

    elif pesquisa == '3':
        system('cls')
        print('Ótima escolha! Você tem direito a escolher os seguintes sabores:' \
        '\n''1 - Limão' \
        '\n''2 - Laranja' \
        '\n''3 - Melancia' \
        '\n''4 - Uva' \
        '\n''5 - Açaí com Guaraná' \
        '\n''6 - Tutti-Fruti')
        sleep(15)
        system('cls')
        while True:
            sabor = input('Digite o dígito correspondente ao sabor desejado: ')
            if sabor == '1':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Limão ']"
                break
            elif sabor == '2':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Laranja ']"
                break
            elif sabor == '3':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Melancia ']"
                break
            elif sabor == '4':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Uva ']"
                break
            elif sabor == '5':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Açaí com Guaraná ']"
                break
            elif sabor == '6':
                system('cls')
                sabor = "//div[@class='attrSimples_valores']//span[text()=' Tutti-Fruti ']"
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
    f.get_cpf(cpf) # chamando a função de validação de CPF
    if not f.get_cpf(cpf):
        system('cls')
        print('CPF inválido.')
        continue
    else:
        system('cls')
        break

# recebendo o CEP do usuário
while True:
    cep = input('Digite o seu CEP: ')
    f.get_cep(cep) # chamando a função de validação de CEP
    if not f.get_cep(cep):
        system('cls')
        print('CEP inválido.')
        continue
    else:
        system('cls')
        cep = cep[:5]+'-'+cep[5:] # inserindo o hífen no meio do CEP
        break

# recebendo o login do usuário, caso tenha
while True:
    login = input('Você já possui uma conta no site da Growth? (s/n): ')
    if not f.get_senha(login, senha): # chamando a função de validação de login
        system('cls')
        print('Opção inválida.')
        continue
    else:
        system('cls')
        break

if not login:
    f.get_nome() # chamando a função de validação de nome
    f.get_email() # chamando a função de validação de email
    f.get_telefone() # chamando a função de validação de telefone
    f.get_sexo() # chamando a função de validação de sexo

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
   
print('Aguarde enquanto o bot faz a compra...')

# caminho para o chrome e o chromedriver
chrome_path = r"C:\Users\kauar\Downloads\chrome-win64\chrome-win64\chrome.exe"  # caminho correto do chrome
driver_path = r"C:\Users\kauar\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # caminho correto do chromedriver
options = webdriver.ChromeOptions()
options.binary_location = chrome_path # local do chrome
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options) # verifica se o caminho do ChromeDriver está correto

try:
    # abrindo um site no chromium
    driver.get('https://gsuplementos.com.br') # abre o site da Growth
    sleep(5) # espera 5 segundos

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
    sleep(5) # espera 10 segundos para carregar a página do produto

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
    botao_cep.send_keys(Keys.ENTER) # pressiona enter para buscar o CEP
    sleep(3) # esperando o frete ser calculado

    # preenchendo o cupom de desconto, se houver
    if cupom:
        botao_cupom = driver.find_element(By.NAME, 'cupom') # localiza o campo de cupom
        botao_cupom.click()
        sleep(1)
        botao_cupom.send_keys(cupom) # digita o cupom
        sleep(1)
        botao_cupom.send_keys(Keys.ENTER) # pressiona enter para aplicar o cupom
        sleep(3) # esperando o cupom ser aplicado
    
    # indo pra página de finalização de compra
    botao_finalizar = driver.find_element(By.CLASS_NAME, 'resumoPedidoBotoes-finalizar') # localiza o botão de fechar pedido
    botao_finalizar.click() # clica no botão de fechar pedido
    sleep(5)
    
    # preenchendo os dados pessoais
    campo_cpf = driver.find_element(By.CLASS_NAME, 'mainBox-conteudo-form-input-validacao') # localiza o campo de CPF
    campo_cpf.click() # clica no campo de CPF
    sleep(1)
    driver.execute_script("arguments[0].value = arguments[1];", campo_cpf, cpf) # não está funcionando corretamente, ver depois
    sleep(1)
    press('enter') # pressiona enter para validar o CPF
    sleep(5)
    if login:
        write(senha)
        press('enter')
        sleep(5)
    else:
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
        campo_telefone.send_keys(telefone)
        campo_telefone.send_keys(Keys.ENTER)
        sleep(1)
        campo_sexo = driver.find_element(By.ID, 'masc') if sexo == 'Masculino' else driver.find_element(By.ID, 'fem')
        campo_sexo.click()
        sleep(1)
        campo_sexo.send_keys(Keys.ENTER)
        sleep(1)
        campo_senha = driver.find_element(By.ID, 'senha-cadastro')
        campo_senha.click()
        sleep(1)
        campo_senha.send_keys(senha)
        campo_senha.send_keys(Keys.ENTER)
        sleep(5)

    # preenchendo os dados de pagamento (incompleto)

finally:
    # fechando o navegador
    driver.quit()