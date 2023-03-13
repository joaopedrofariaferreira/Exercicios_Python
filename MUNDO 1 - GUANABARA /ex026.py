#um p[rograma que leia uma frase e mostre
#quatas vezes aparece a letra a
#em qual posiçao a letra a aparece na 1 vez
#em que posição ela aparece na ultima vez
frase = input('digite uma frase ')
#Quantas vezes a letra a apareceu
print(frase.count('a'))
#posiçao que A apareceu pela primeira vez
print(frase.find('a'))
#posiçao que apareceu pela ultima vez
print(frase.rfind('a'))