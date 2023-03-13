#Criar uma lista de grupos para apresentação
from random import shuffle
first_student = input("Qual o nome do primeiro aluno? ")
second_student = input("Who's the name to the second student? ")
third_student = input("who's the third student? ")
fourth_student = input("Who's the fourth student? ")
group = [first_student, second_student, third_student, fourth_student]
shuffle(group)
print(f"Ther order of the groups are: {group} ")

