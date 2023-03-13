#crie um programa que leia as duas medias de um aluno e calcule sua media, mostrando uma mensagem no final de acordo com a media atingida
#media abaixo de 5: REPROVADO
#MEDIA ACIMA DE 5 E 6.9 : VOCÊ ESTÁ DE RECUPERAÇÃO
# MEDIA 7 OU SUPERIOR: APROVADO
primeira_nota = float(input('Qual foi sua primeira prova? '))
segunbda_nota = float(input('Qual foi sua segunda nota? '))
media = (primeira_nota + segunbda_nota) / 2
if media < 5:
    print('Você está reprovado, procure a direção da escola!!')
elif media >= 7:
    print('Você foi aprovado, parabéns!')
elif media <= 6.9:
    print('Você está de recuperação, procure a direção!')

