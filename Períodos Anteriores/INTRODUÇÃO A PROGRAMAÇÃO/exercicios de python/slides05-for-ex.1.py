altura = 1000
quantidade = 0

while altura != 0:
    altura = float(input("Digite a altura do aluno: "))
    if altura == 0:
        break
    idade = int(input("Digite a idade do aluno: "))

    if altura < 1.5 and idade > 13:
        quantidade += 1

print "H� %d aluno(s) com idade maior que 13 anos e altura menor que 1.5m"%(quantidade)