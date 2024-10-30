# Verificação de Bissetriz em Triângulos

Este projeto implementa um programa em Python para calcular a proporção da bissetriz interna e externa de um triângulo, com base nos valores dos seus lados. O código permite ao usuário escolher entre calcular a bissetriz interna ou externa, além de lidar com entradas de forma robusta e amigável.

## Funcionalidades

- **Entrada de Dados:** O programa solicita ao usuário que insira os valores dos lados do triângulo.
- **Cálculo de Bissetriz:** Com base na escolha do usuário (bissetriz interna ou externa), o programa calcula e retorna a proporção da bissetriz.
- **Tratamento de Erros:** O programa garante que as entradas sejam números válidos e lida com erros de divisão por zero de forma adequada.

## Estrutura do Código

### Funções Principais

1. **`entrada_numero_float(prompt)`**
   - Solicita ao usuário um número em ponto flutuante.
   - Se o usuário inserir `!s`, o programa será encerrado.
   - Retorna um número válido ou repete a solicitação em caso de erro.

2. **`calcular_razao_bissetriz(lados, tipo)`**
   - Recebe uma lista com os lados do triângulo e o tipo de bissetriz (interna ou externa).
   - Calcula e retorna a proporção da bissetriz correspondente.
   - Se a bissetriz externa é selecionada e ocorre divisão por zero, retorna `None`.

3. **`solicitar_lados()`**
   - Coleta os valores dos três lados do triângulo a partir da entrada do usuário.
   - Retorna uma lista com os valores dos lados.

4. **`main()`**
   - Controla o fluxo principal do programa.
   - Solicita ao usuário escolher entre bissetriz interna ou externa.
   - Chama as funções necessárias para coletar dados e calcular as proporções.
   - Exibe o resultado ou mensagens de erro conforme apropriado.

## Como Usar

1. Execute o programa em um ambiente Python.
2. Siga as instruções no terminal para inserir os lados do triângulo.
3. Escolha se deseja calcular a bissetriz interna ou externa.
4. O resultado será exibido no formato desejado.

## Exemplo de Uso

```plaintext
Você deseja calcular a bissetriz interna ou externa? (interna, externa) ou '!s' para sair: interna
Digite o valor do lado 1: 5
Digite o valor do lado 2: 7
Digite o valor do lado 3: 9
Proporção da Bissetriz Interna: 0.58
