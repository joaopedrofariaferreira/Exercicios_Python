#crie um programa que leia uma frase qualqauer e diga se ela é ujm palindromo. desconsiderando os espaços
f = input('Digite uma frase para saber se ela é um PALINDROMO: ').upper().strip()
palavras = f.split()
juntas = ''.join(palavras)
inverso = ''
for letra in range(len(juntas) -1, -1, -1):
    inverso += juntas[letra]
if inverso == juntas:
    print('Essa palavra é um Palindromo! ')
else:
    print('A frase não é um palindromo!')