# desenvolva um programa que leia o primeiro termo e a razao de uma pa (progressao aritmetica). No final
#mostre os 10 primeiros termos dessa progressao
n1 = int(input('qual o termo inicial da pa? '))
r = int(input('Agora qual o numero da razão da pa? '))
decimo = n1 + (10 - 1) * r
for p in range(n1, decimo, r):
   print(f' {p}')
print('Acabou')
