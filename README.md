# monitoramento_eletrico_grupoPI
**MONITOR ELÉTRICO - Grupo π**
- O seguinte programa visa auxiliar o cálculo de fatores elétricos, presentes por exemplo em uma instalação elétrica.
Dado a sua natureza, é particularmente útil para um engenheiro eletricista. O programa conta com 5 funções, cada uma
correspondente a um número que o usuário digita e escolhe. Além disso ele utiliza diversos conceitos de programação em Python
como: variáveis, loops, listas, listas de listas, dicionários e arquivos.

- **Como Executar o programa**:
  - Para executar o programa, basta executar script.py em uma IDE(integrated development enviroment), como o Pycharm, VSCode ou Google
    Colab.

- **Funcionalidades**:
  
  - **Primeira função - Registrar Medições:**
    Essa função, correspondente ao número 1, registra um circuito, com seu nome e características. As informações registradas
    são: nome, tensão elétrica, corrente elétrica, fator de potência e frequência. O usuário deve digitar as características 
    nessa ordem e separados por ponto e vírgula.
  
  - **Segunda função - Salvar Circuitos:**
    Essa função, correspondente ao número 2, escreve em  um arquivo os dados de um circuito elétrico. As informações presentes são:
    Nome, tipo, tensão elétrica, corrente elétrica, fator de potência, frequência e data da medição; nessa ordem.
  
  - **Terceira função - Gerar Relatório de Não Conformidade:**
    Essa função, correspondente ao número 3, escreve em um arquivo os dados dos circuitos registrados que não estão em conformidade, ou seja, que
    estão com características anormais. As informações são escritas no arquivo relatorio_nao_conforme.txt.
  
  - **Quarta função - Resumo Elétrico:**
    Essa função, corresponde ao número 4, exibe no console o circuito com o menor fator de potência, com seu respectivo fator de potência
    e o número de circuitos que não estão em uma faixa de conjunto de valores.
  
  - **Quinta função - Módulo Extra - Balanceamento de Fases:**
    O balanceamento de fases é essencial para circuitos de corrente alternada, pois quando as fases estão desbalanceadas pode ocorrer sobretensões e carregamento
    do neutro, que podem causar danos físicos aos dispositivos ligados na rede. Esse módulo visa balancear as N fases de um circuito qualquer. O módulo lê o arquivo
    Alimentador.txt, pede o número de fases do circuito, e as potências e realiza os balanceamentos das N fases presentes nesse circuito, no final o programa avisa
    se o circuito está desbalanceado.


  

