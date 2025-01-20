print('\033[1;33m+\33[m' * 22)
print('\033[1;33mSimule seu empréstimo\33[m')
print('\033[1;33m+\33[m' * 22)
valor = float(input('Qual o valor do empréstimo? R$'))
sal = float(input('Qual é o seu salário? R$'))
prazo = int(input('Em quantos anos pretende pagar? '))
prestação = valor / (prazo * 12)
if prestação > sal * .30:
    print('\033[1;31mEmprestimo negado!\033[m \nO valor da prestação de R${:.2f} excede 30% do seu salário.'
          .format(prestação))
else:
    print('\033[1;32mEmprestimo aprovado!\033[m '
          '\nSeu emprestimo no valor de R${:.2f} terá parcelas mensais de R${:.2f} por um período de {} meses.'
          .format(valor, prestação, (prazo * 12)))
