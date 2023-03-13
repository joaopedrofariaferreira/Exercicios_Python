#aplicativo que mostre varios numeros e pare quando o usuario digitar o numero 999
numero = int(input(" Digite um numero qualquer: "))
while numero != 999:
    print(f" o nuimero digitado foi {numero}")
    second_number = int(input(" deseja digitar mais um numero? Se sim, digite 1, caso contrario digite 999"))
    if numero == 999:
        print("oBRIGADO POR JOGAR")