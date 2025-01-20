frase = '  Curso em Vídeo Python  '
print(frase[3:13:2])

print("""Nessa aula, vamos aprender operações com String no 
Python. As principais operações que vamos aprender são 
o Fatiamento de String, Análise com len(), count(), 
find(), transformações com replace(), upper(), lower(), 
capitalize(), title(), strip(), junção com join().""")

print(frase.count('O'))
print(frase.upper().count('O'))

print(len(frase))
print(len(frase.strip()))

print(frase.replace('Python', 'Android'))
#frase = frase.replace('Python' , 'Android') fazendo uma nova atribuição

print('Curso' in frase) # para saber se existe na lista
print(frase.find('Curso')) # para achar em qual posição está
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
