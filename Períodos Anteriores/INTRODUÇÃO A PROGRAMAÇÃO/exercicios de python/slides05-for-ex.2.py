#calcula o fatorial de um n�mero menor ou igual a 20
x = int(input("Digite o n�mero para calcular o fatorial: "))
if x <= 20:
    i = 2
    resultado = 1
    while i <= x:
        resultado *= i
        i+= 1
    print "O fatorial de",x,"�:",resultado
    print "O fatorial de %d �: %d"%(x, resultado)
else:
    print "S� posso calcular o fatorial de n�emros at� 20"