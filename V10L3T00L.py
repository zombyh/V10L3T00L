# Script criado para fins educativos por Marcelo Rocha (Zombyh) do grupo V10L3T34M

import os


def menu():
    while True:
        print("\nMenu:")
        print("1. Realizar brute force de diretótios com GOBUSTER")
        print("2. Realizar quebra de senha hash com HASHCAT")
        print("3. Realizar mapeamento de portas com NMAP")
        print("4. Realizar SQL Injection com SQLMAP")
        print("5. Realizar verificação de Firewall com WAFWOOF")
        print("0. Encerrar o programa")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            url_gobuster = input("Insira a URL a ser usada: ")
            wordlist = input("Insira o caminho completo da Wordlist a ser usada: ")
            os.system(f"gobuster dir -t 200 --no-error -o Gobuster -u {url_gobuster} -w {wordlist} -x php,txt,html")
            print("Você selecionou a Opção 1")
        elif escolha == '2':
            os.system("python3 H4SHK1LL3R.py")
            print("Você selecionou a Opção 2")
        elif escolha == '3':
            url_nmap = input("Insira a URL a ser usada: ")
            os.system(f"nmap -sS -p- -T4 --open -oN nmap.txt {url_nmap}")
            print("Você selecionou a Opção 3")
        elif escolha == '4':
            url_sqlmap = input("Insira a URL a ser usada: ")
            os.system(f"sqlmap -u {url_sqlmap} --random-agent")
            print("Você selecionou a Opção 4")
        elif escolha == '5':
            url_wafwoof = input("Insira a URL a ser usada: ")
            os.system(f"wafw00f -a -o Wafwoof_saida -f txt {url_wafwoof}")
            print("Você selecionou a Opção 5")
        elif escolha == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
