# Ainda estou trabalhando nessa ferramenta

import os

def menu():
    while True:
        print("\nMenu:")
        print("1. Opção 1")
        print("2. Opção 2")
        print("3. Opção 3")
        print("4. Opção 4")
        print("5. Opção 5")
        print("6. Encerrar o programa")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            # código
            print("Você selecionou a Opção 1")
        elif escolha == '2':
            # código
            print("Você selecionou a Opção 2")
        elif escolha == '3':
            # código
            print("Você selecionou a Opção 3")
        elif escolha == '4':
            # código
            print("Você selecionou a Opção 4")
        elif escolha == '5':
            # código
            print("Você selecionou a Opção 5")
        elif escolha == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
