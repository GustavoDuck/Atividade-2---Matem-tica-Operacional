def entrada_numero_float(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "!s":
            print("Programa encerrado. Agradecemos pela utilização.")
            exit()
        try:
            return float(user_input)
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

def calcular_razao_bissetriz(lados, tipo):
    lado_a, lado_b, lado_c = lados
    if tipo == "interna":
        return lado_b / (lado_a + lado_b)
    elif tipo == "externa":
        if lado_a - lado_b == 0:
            return None  # Retorna None para indicar erro de divisão por zero
        return lado_b / (lado_a - lado_b)

def solicitar_lados():
    lados = []
    for i in range(1, 4):
        lado = entrada_numero_float(f"Digite o valor do lado {i}: ")
        lados.append(lado)
    return lados

def main():
    while True:
        escolha = input("Você deseja calcular a bissetriz interna ou externa? (interna, externa) ou '!s' para sair: ").lower()
        if escolha == "!s":
            print("Programa encerrado. Agradecemos pela utilização.")
            return
        elif escolha in ["interna", "externa"]:
            lados = solicitar_lados()
            resultado = calcular_razao_bissetriz(lados, escolha)
            
            if escolha == "interna":
                print(f"Proporção da Bissetriz Interna: {resultado:.2f}")
            elif escolha == "externa":
                if resultado is None:
                    print("Erro: Divisão por zero na bissetriz externa.")
                else:
                    print(f"Proporção da Bissetriz Externa: {resultado:.2f}")
        else:
            print("Opção não reconhecida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
