def leiadinheiro(txt):
    while True:
        p = str(input(txt)).strip().replace(',', '.')
        if p.isalpha() or p == '':
            print(f'\033[0;31mERRO: \"{p}\" é um preço inválido!\033[m')
        else:
            return float(p)
