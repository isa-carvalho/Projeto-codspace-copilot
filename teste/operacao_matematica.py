numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite utro numero: "))

operacao = input("Digite qual operacao deseja realizar  +, -,*,/: ")

if operacao == '+':
    print (numero1 + numero2)
elif operacao == '-':
    print(abs(numero1 - numero2))
elif operacao == '*':
    print(numero1 * numero2)
elif operacao ==  '/':
    print(numero1 / numero2)
else :
    print("operacao invalida ")