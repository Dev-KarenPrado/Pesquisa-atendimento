# Programa de Pesquisa de Atendimento ao Cliente

def realizar_pesquisa(num_entrevistados=50):
    excelente = 0
    bom = 0
    ruim = 0

    print(f"--- Início da Pesquisa de Atendimento ({num_entrevistados} entrevistados) ---")

    for i in range(1, num_entrevistados + 1):
        print(f"\nEntrevistado nº {i}:")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        
        while True:
            print("Opinião sobre o atendimento:")
            print("1: EXCELENTE")
            print("2: BOM")
            print("3: RUIM")
            
            try:
                opiniao = int(input("Escolha uma opção (1, 2 ou 3): "))
                
                if opiniao == 1:
                    excelente += 1
                    break
                elif opiniao == 2:
                    bom += 1
                    break
                elif opiniao == 3:
                    ruim += 1
                    break
                else:
                    print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número (1, 2 ou 3).")

    print("\n" + "="*30)
    print("RESULTADO FINAL DA PESQUISA")
    print("="*30)
    print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
    print(f"b) Quantidade de respostas 'RUIM': {ruim}")
    print(f"Quantidade de respostas 'BOM': {bom}")
    print("="*30)

if __name__ == "__main__":
  
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        realizar_pesquisa(10)
    else:
        realizar_pesquisa(50)
