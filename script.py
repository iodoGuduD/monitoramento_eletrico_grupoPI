# Lista chamada circuitos, onde cada item é outra lista representando um circuito elétrico
# Cada circuito contém: [nome, tipo, tensão (V), corrente (I), fator de potência (fp), frequência (Hz), data]
circuitos = [
    ["Circuito 1", "iluminacao", 220.0, 8.5, 0.95, 60.0, "05/11/2025"],
    ["Motor Bomba", "motor", 220.0, 14.0, 0.78, 60.0, "05/11/2025"],
]

# Loop que percorre cada circuito dentro da lista 'circuitos'
for c in circuitos:
    # Imprime algumas informações formatadas sobre cada circuito
    print("Nome:", c[0], "| Tipo:", c[1], "| V:", c[2], "| I:", c[3], "| fp:", c[4])

# Dicionário 'limites' que define parâmetros máximos e mínimos
# para cada tipo de circuito: corrente máxima, fator de potência mínimo
# e tensão nominal esperada.
limites = {
    "iluminacao": {"i_max": 10.0, "fp_min": 0.9, "tensao_nom": 220},
    "motor": {"i_max": 20.0, "fp_min": 0.75, "tensao_nom": 220},
    "tomada": {"i_max": 15.0, "fp_min": 0.8, "tensao_nom": 127},
    "alimentador": {"i_max": 40.0, "fp_min": 0.92, "tensao_nom": 220},
}

# Tolerância percentual permitida para a tensão nominal (±10%)
tolerancia_tensao = 0.10  # 10%

# Função que verifica se um circuito está dentro dos limites definidos
def dentro_da_faixa(circuito):
    # Desempacota os valores da lista do circuito
    nome, tipo, v, i, fp, f, data = circuito

    # Obtém as regras correspondentes ao tipo do circuito
    regra = limites.get(tipo, None)

    # Se não houver regra definida para esse tipo, considera como dentro da faixa
    if not regra:
        return True

    # Verifica se a tensão está dentro da faixa permitida considerando a tolerância
    if not (regra["tensao_nom"] * (1 - tolerancia_tensao) <= v <= regra["tensao_nom"] * (1 + tolerancia_tensao)):
        return False

    # Verifica se a corrente não ultrapassa o valor máximo
    if i > regra["i_max"]:
        return False

    # Verifica se o fator de potência está acima do mínimo
    if fp < regra["fp_min"]:
        return False

    # Se passou por todos os testes, o circuito está dentro da faixa
    return True

# Percorre todos os circuitos da lista e imprime se estão dentro da faixa
for c in circuitos:
    print(c[0], "está dentro da faixa?", dentro_da_faixa(c))

# Função que recebe uma linha de texto com medições separadas por ponto e vírgula
def registrar_medicao(linha):
    # Divide a linha em partes usando ';'
    partes = linha.split(";")

    # O primeiro elemento é o nome do circuito
    nome = partes[0].strip()

    # Dicionário para guardar as medições extraídas (v, i, fp, f)
    medidas = {}

    # Percorre as demais partes para buscar pares no formato chave=valor
    for pedaco in partes[1:]:
        pedaco = pedaco.strip()
        if "=" in pedaco:
            # Separa chave e valor
            k, v = pedaco.split("=")
            medidas[k.strip().lower()] = v.strip()  # salva no dicionário em minúsculas

    # Procura o circuito correspondente pelo nome dentro da lista 'circuitos'
    for c in circuitos:
        if c[0] == nome:
            # Atualiza os valores que estiverem presentes na string de medição
            if "v" in medidas:
                c[2] = float(medidas["v"])
            if "i" in medidas:
                c[3] = float(medidas["i"])
            if "fp" in medidas:
                c[4] = float(medidas["fp"])
            if "f" in medidas:
                c[5] = float(medidas["f"])
            break  # termina após encontrar o circuito certo

# Chamada da função com uma linha de medição real
registrar_medicao("Circuito 1; V=213; I=11.2; fp=0.82; f=60")

# Imprime todos os circuitos após a atualização
for c in circuitos:
    print(c)

def salvar_circuitos(nome_arquivo="circuitos.txt"):
    # Abre o arquivo no modo escrita "w"
    with open(nome_arquivo, "w") as arq:
        # Percorre todos os circuitos da lista
        for c in circuitos:
            # Monta a linha no formato separado por ponto e vírgula
            linha = f"{c[0]};{c[1]};{c[2]};{c[3]};{c[4]};{c[5]};{c[6]}\n"
            arq.write(linha)
    print("Circuitos salvos em", nome_arquivo)

def gerar_relatorio_nao_conforme(nome_arquivo="relatorio_nao_conforme.txt"):
    # Abre o arquivo no modo escrita
    with open(nome_arquivo, "w") as arq:
        arq.write("RELATÓRIO DE NÃO CONFORMIDADE\n\n")

def resumo_eletrico():
    # Encontra o circuito com o menor fator de potência (índice 4)
    menor_fp = min(circuitos, key=lambda x: x[4])

    # Cria uma lista com todos os circuitos que não estão dentro da faixa
    fora = [c for c in circuitos if not dentro_da_faixa(c)]

    # mostra na tela o circuito com o pior fator de potência
    print("Circuito com menor fator de potência:", menor_fp[0], "-", menor_fp[4])

    # mostra na tela quantos circuitos estão fora dos limites estabelecidos
    print("Total de circuitos fora da faixa:", len(fora))

# Chama a função para exibir o resumo
resumo_eletrico()

def modulo_extra(arquivo_nome="comp_utfpr\monitoramento_eletrico\Alimentador.txt"):
    # balanceamento de fases
    # lê o arquivo "alimentador.txt"
    with open(arquivo_nome, "r") as file:
      txt = file.read()
      # divide as correntes do arquivo em forma de lista
      parametro = txt.split(";")
      nome = parametro[0]
      # criação do dict das correntes do alimentador
      correntes = {}
      # divide cada parte da linha e salva-a em uma variável dentro de um dict
      for i in parametro[1:]:
        i = i.strip()
        vl, var = i.split("=")
        correntes[vl.strip().lower()] = var.strip()

    # quantas fases há (número necessário para o cálculo de balanceamento)
    n_fases = int(input("Digite o número de fases do circuito: "))
    potencias = []
    for i in range(n_fases):
      p = int(input(f"Digite o valor da potência da fase {i+1}: "))
      potencias.append(p)

    #realiza o cálculo do balanceamento de fases
    desvios_p = []
    p_total = 0
    for pot in potencias:
      p_total += pot
      p_med = p_total / len(potencias)
      desvios_p.append(abs(pot - p_med))

    p_med_max = max(desvios_p)
    dpc = (p_med_max / p_med) * 100

    # se o desequilíbrio for maior ou igual que 10%, gera aviso ao usuário
    if dpc >= 10:
      print("O circuito está desequilibrado! Cuidado!")
    else:
      print("O circuito está equilibrado. Ufa!")

    print(f"DPC = {dpc:.2f}")

# exemplo de teste:
#modulo_extra("alimentador.txt")

def main():
    print("=== Sistema de Monitoramento Elétrico ===")
    print("1 - Registrar medição")
    print("2 - Salvar circuitos")
    print("3 - Gerar relatório de não conformidade")
    print("4 - Resumo elétrico")
    print("5 - Realizar balanceamento de fases")
    opc = input("Escolha: ") # Lê a opção digitada pelo usuário

    # Verifica qual opção foi selecionada e executa a ação correspondente
    if opc == "1":
    # Solicita uma linha no formato esperado e registra a medição
        linha = input("Digite: Nome; V=...; I=...; fp=...; f=...\n")
        registrar_medicao(linha)
    elif opc == "2":
        salvar_circuitos()
    # Gera o relatório de circuitos fora da faixa permitida
    elif opc == "3":
        gerar_relatorio_nao_conforme()
    # Gera o relatório de circuitos fora da faixa permitida
    elif opc == "4":
        resumo_eletrico()
    # Encerra a execução retornando False
    elif opc == "5":
        #name = input("Digite o nome do arquivo das fases: ")
        modulo_extra()
    # Chama um módulo extra (deve estar definido no programa)
    elif opc == "0":
        return False
    # Encerra a execução retornando False

    else:
        print("Opção inválida")
    # Caso a opção não exista

# chama o menu
if __name__ == "__main__":
     main()