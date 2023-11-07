# Script criado para fins educativos por Marcelo Rocha (Zombyh) do grupo V10L3T34M

import os


def menu():
    while True:
        print("\nMenu:")
        print("1. Realizar brute force de arquivos com GOBUSTER")
        print("2. Realizar quebra de senha hash com HASHCAT")
        print("3. Realizar mapeamento de portas com NMAP")
        print("4. Realizar teste de SQL Injection com SQLMAP")
        print("5. Realizar verificação de Firewall com WAFWOOF")
        print("6. Realizar analise das tecnologias de um site com WHATWEB")
        print("0. Encerrar o programa")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            url_gobuster = input("Insira a URL a ser usada: ")
            wordlist = input("Insira o caminho completo da Wordlist a ser usada: ")
            os.system(f"gobuster dir -t 200 -e -r --no-error -o Gobuster_saida.txt -u {url_gobuster} -w {wordlist} -x php,txt,html,bkp,old,xml")
            print("Você selecionou a Opção 1")
        elif escolha == '2':
            os.system("python3 H4SHK1LL3R.py")
            print("Você selecionou a Opção 2")
        elif escolha == '3':
            url_nmap = input("Insira a URL a ser usada: ")
            os.system(f"nmap -D RND:20 -sS -p- -T4 --open -oN Nmap_saida.txt {url_nmap}")
            print("Você selecionou a Opção 3")
        elif escolha == '4':
            url_sqlmap = input("Insira a URL a ser usada: ")
            os.system(f"python3 SQLBR34K3R.py")
            print("Você selecionou a Opção 4")
        elif escolha == '5':
            url_wafwoof = input("Insira a URL a ser usada: ")
            os.system(f"wafw00f -v -o Wafwoof_saida -f txt {url_wafwoof}")
            print("Você selecionou a Opção 5")
         elif escolha == '6':
            url_whatweb = input("Insira a URL a ser usada: ")
            os.system(f"whatweb {url_whatweb}")
            print("Você selecionou a Opção 6")
        elif escolha == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
