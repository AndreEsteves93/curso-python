#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Mais um, por favor: '))
'''if n1 > n2 > n3:
    print('O maior número é o {} e o menor {}.'.format(n1, n3))
if n1 > n3 > n2:
    print('O maior número é o {} e o menor {}.'.format(n1, n2))
if n2 > n1 > n3:
    print('O maior número é {} e o menor {}.'.format(n2, n3))
if n2 > n3 > n1:
    print('O maior número é {} e o menor {}.'.format(n2, n1))
if n3 > n1 > n2:
    print('O maior número é {} e o menor {}.'.format(n3, n2))
if n3 > n2 > n1:
    print('O maior número é {} e o menor {}.'.format(n3, n1))'''

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}. \nO maior valor digitado foi {}.'.format(menor, maior))
