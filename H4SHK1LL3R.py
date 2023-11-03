# Script criado para fins educativos por Marcelo Rocha (Zombyh) do grupo V10L3T34M

import os


def quebra_hash(hash_type):
    hash_types = {
        '1': (22000, 'Hash'),
        '2': (0, 'MD5'),
        '3': (100, 'SHA-1'),
        '4': (1400, 'SHA-256'),
        '5': (1700, 'SHA-512'),
    }

    if hash_type in hash_types:
        dicionario = input('Insira aqui o caminho completo do dicionario a ser usado: ')
        codigo = input('Insira o codigo hash a ser utilizado: ')
        mode, hash_name = hash_types[hash_type]
        os.system(f"hashcat -m {mode} -a 0 -w 3 {codigo} {dicionario} -O")
        os.system(f"hashcat -m {mode} {codigo} {dicionario} --show >> decodificados_{codigo}.txt")
    else:
        print("Opção inválida.")


def main():
    while True:
        print("\nMenu:")
        print("1. Realizar quebra de senha Hash (Wi-Fi) com Hashcat.")
        print("2. Realizar quebra de senha MD5 com Hashcat.")
        print("3. Realizar quebra de senha SHA-1 com Hashcat.")
        print("4. Realizar quebra de senha SHA-256 com Hashcat.")
        print("5. Realizar quebra de senha SHA-512 com Hashcat.")
        print("0. Encerrar o programa")
        choice = input("Opção: ")

        if choice == '0':
            break
        quebra_hash(choice)


if __name__ == "__main__":
    main()
