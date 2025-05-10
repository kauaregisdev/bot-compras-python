from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

def iniciar(): # inicia o bot
    print('Iniciando o bot. Aguarde enquanto a compra é feita...')
    driver_path = r"C:\Users\kauar\OneDrive\Documentos\GitHub\bot-compras-python\bot_compras_site\bot\scripts\chromedriver.exe" # caminho do chromedriver
    driver = webdriver.Chrome(service=Service(driver_path), options=webdriver.ChromeOptions()) # criando o objeto do webdriver
    return driver

def abrir_site(driver): # abrindo um site no chromium
    driver.get('https://gsuplementos.com.br') # abre o site da Growth
    driver.maximize_window() # maximiza a janela do navegador
    sleep(5) # espera 5 segundos para carregar a página

def barra_pesquisa(driver, pesquisa): # usando a barra de pesquisa
    search_bar = driver.find_element(By.ID, 'busca-principal-topo') # localizar barra de pesquisa
    search_bar.click() # clica na barra de pesquisa
    sleep(1)
    search_bar.send_keys(pesquisa) # digita o que o usuário quer comprar
    sleep(1)
    search_bar.send_keys(Keys.ENTER) # pressiona enter para pesquisar
    sleep(5)

def localizar_produto(driver): # localizando e escolhendo o produto
    produto = driver.find_element(By.CLASS_NAME, 'cardProd-topo') # encontra o produto pesquisado
    produto.click()
    sleep(10) # espera 10 segundos para carregar a página do produto

def localizar_sabor(driver, sabor): # localizando e escolhendo o sabor do produto, caso necessário
    lista_sabores = driver.find_element(By.ID, 'attrSimples') # localiza o botão de sabor
    lista_sabores.click()
    sleep(1)
    botao_escolher_sabor = driver.find_element(By.XPATH, sabor) # localiza o botão de sabor desejado (erro no XPATH)
    botao_escolher_sabor.click()
    sleep(1)

def adicionar_carrinho(driver): # adicionando ao carrinho
    botao_add_carrinho = driver.find_element(By.ID, 'btComprar') # localiza o botão de adicionar ao carrinho
    driver.execute_script("arguments[0].click();", botao_add_carrinho) # usa JavaScript para clicar no botão
    sleep(1)

def ir_carrinho(driver): # indo para o carrinho
    botao_ir_carrinho = driver.find_element(By.ID, 'externo-carrinhoLateral-carrinho') # localiza o botão para 
    botao_ir_carrinho.click()
    sleep(1)

def calcular_frete(driver, cep): # calculando o frete
    botao_cep = driver.find_element(By.NAME, 'cep') # localiza o campo de CEP
    botao_cep.click() # clica no campo de CEP
    sleep(1)
    botao_cep.send_keys(cep) # digita o CEP
    sleep(1)
    botao_cep.send_keys(Keys.ENTER)
    sleep(5)

def preencher_cupom(driver, cupom): # preenchendo o cupom de desconto, se houver
    botao_cupom = driver.find_element(By.NAME, 'cupom') # localiza o campo de cupom
    botao_cupom.click()
    sleep(1)
    botao_cupom.send_keys(cupom) # digita o cupom
    sleep(1)
    botao_cupom.send_keys(Keys.ENTER)
    sleep(5)

def ir_pagina_final(driver): # indo pra página de finalização de compra
    botao_finalizar = driver.find_element(By.CLASS_NAME, 'resumoPedidoBotoes-finalizar') # localiza o botão de fechar pedido
    botao_finalizar.click() # clica no botão de fechar pedido
    sleep(5)

def preencher_cpf(driver, cpf): # preenchendo os dados pessoais
    campo_cpf = driver.find_element(By.NAME, 'email') # localiza o campo de preenchimento com e-mail ou CPF (nesse caso usei CPF)
    campo_cpf.click() # clica no campo de CPF
    sleep(1)
    campo_cpf.send_keys(cpf) # digita o CPF
    sleep(1)
    campo_cpf.send_keys(Keys.ENTER) # pressiona enter para validar o CPF
    sleep(5)

def inserir_senha(driver, senha): # entrando na conta do usuário
    campo_senha = driver.find_element(By.NAME, 'senha') # localiza o campo de senha
    campo_senha.send_keys(senha) # digita a senha
    sleep(1)
    campo_senha.send_keys(Keys.ENTER) # pressiona enter para validar a senha
    sleep(10)

def inserir_nome(driver, nome): # criando uma conta para o usuário
    campo_nome = driver.find_element(By.ID, 'nome-cadastro')
    campo_nome.click()
    sleep(1)
    campo_nome.send_keys(nome)
    campo_nome.send_keys(Keys.ENTER)
    sleep(1)

def inserir_email(driver, email): # insere email no campo de texto
    campo_email = driver.find_element(By.ID, 'email-cadastro')
    campo_email.click()
    sleep(1)
    campo_email.send_keys(email)
    campo_email.send_keys(Keys.ENTER)
    sleep(1)

def inserir_telefone(driver, tel): # insere telefone no campo de texto
    campo_telefone = driver.find_element(By.ID, 'celular-cadastro')
    campo_telefone.click()
    sleep(1)
    campo_telefone.send_keys(tel)
    campo_telefone.send_keys(Keys.ENTER)
    sleep(1)

def inserir_sexo(driver, sexo): # aperta o botão informando qual o sexo do usuário
    campo_sexo = driver.find_element(By.ID, 'masc') if sexo in ['m', 'M'] else driver.find_element(By.ID, 'fem')
    campo_sexo.click()
    sleep(1)
    campo_sexo.send_keys(Keys.ENTER)
    sleep(1)

def criar_senha(driver, senha): # cria senha para a conta do usuário
    campo_senha = driver.find_element(By.ID, 'senha-cadastro')
    campo_senha.click()
    sleep(1)
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.ENTER)
    sleep(10)

def cadastrar_endereco(driver, num_residencia): # preenchendo os dados de endereço, caso necessário
    campo_num_casa = driver.find_element(By.NAME, 'numeroRapido') # localiza o campo de número da casa
    driver.execute_script("arguments[0].click();", campo_num_casa) # clica no campo de número da casa
    sleep(1)
    campo_num_casa.send_keys(num_residencia)
    sleep(1)
    botao_cadastrar_endereco = driver.find_element(By.NAME, 'btnEnviar') # localiza o botão de cadastrar endereço
    botao_cadastrar_endereco.click() # clica no botão de cadastrar endereço
    sleep(1)

def ir_pagamento(driver): # indo para a aba de pagamento
    botao_ir_pagamento = driver.find_element(By.ID, 'btnEnderecoIrPagamento') # localiza o botão de ir para a aba de pagamento
    botao_ir_pagamento.click() # clica no botão de ir para a aba de pagamento
    sleep(5)

def localizar_metodo_pag(driver, metodo_pag): # preenchendo os dados de pagamento
    botao_metodo = driver.find_element(By.XPATH, metodo_pag) # localiza o botão do método escolhido
    botao_metodo.click() # clica no botão do método escolhido

def inserir_num_cartao(driver, num_cartao): # insere o número do cartão de crédito
    sleep(5)
    campo_num_cartao = driver.find_element(By.ID, 'cardNumber') # localiza o campo de número do cartão
    campo_num_cartao.click()
    sleep(1)
    campo_num_cartao.send_keys(num_cartao)
    sleep(1)

def inserir_nome_titular(driver, nome_titular): # insere o nome do titular do cartão
    campo_nome_cartao = driver.find_element(By.ID, 'cardholderName') # localiza o campo de nome do titular
    campo_nome_cartao.click()
    sleep(1)
    campo_nome_cartao.send_keys(nome_titular)
    sleep(1)

def inserir_cpf_titular(driver, cpf_titular): # insere o CPF do titular
    campo_cpf_titular = driver.find_element(By.ID, 'docNumber') # localiza o campo de CPF do titular
    campo_cpf_titular.click()
    sleep(1)
    campo_cpf_titular.send_keys(cpf_titular)
    sleep(1)

def inserir_mes_validade(driver, mes): # seleciona o mês de validade do cartão
    from selenium.webdriver.support.ui import Select
    campo_select_mes = driver.find_element(By.ID, 'cardExpirationMonth')
    campo_select_mes.click()
    sleep(1)
    campo_mes_val = Select(campo_select_mes)
    campo_mes_val.select_by_value(mes)
    sleep(1)

def inserir_ano_validade(driver, ano): # seleciona o ano de validade do cartão
    from selenium.webdriver.support.ui import Select
    campo_select_ano = driver.find_element(By.ID, 'cardExpirationYear')
    campo_select_ano.click()
    sleep(1)
    campo_ano_val = Select(campo_select_ano)
    campo_ano_val.select_by_value(ano)
    sleep(1)

def inserir_cod_seg(driver, cod_seg): # localiza o campo de código de segurança
    campo_cod_seg = driver.find_element(By.ID, 'securityCode')
    campo_cod_seg.click()
    sleep(1)
    campo_cod_seg.send_keys(cod_seg)
    sleep(1)

def inserir_campo_parcelas(driver, parcelas): # seleciona o número de parcelas  
    from selenium.webdriver.support.ui import Select
    campo_parcelas = driver.find_element(By.ID, 'parcelasCartaoMercadoPago')
    campo_parcelas.click()
    sleep(1)
    campo_select_parcelas = Select(campo_parcelas)
    campo_select_parcelas.select_by_value(parcelas)

def finalizar_compra(driver): # finaliza compra
    sleep(5)
    botao_finalizar_compra = driver.find_element(By.ID, 'finalizarPedido') # localiza o botão de finalizar compra
    botao_finalizar_compra.click() # aperta no botão de finalizar compra
    sleep(10)

def finalizar(driver): # encerra o bot
    driver.quit()