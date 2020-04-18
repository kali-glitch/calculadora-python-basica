print("""[ 0 ] soma\n [ 1 ] subtrair\n [ 2 ] mutiplicar\n [ 3 ] dividir\n [ 4 ]expoente\n [ 5 ] parar [ 6 ] raiz """)
o = int(input('opção: '))
if o == 0:
    n = float(input('valor um: '))
    n1 = float(input('valor dois: '))
    print(f'{n} + {n1} = {n+n1}')
if o == 1:
    n2 = float(input('valor um: '))
    n12 = float(input('valor dois: '))
    print(f'{n2} - {n12} = {n2 - n12}')
if o == 2:
    n3 = float(input('valor um: '))
    n13 = float(input('valor dois: '))
    print(f'{n3} x {n13} = {n3 * n13}')
if o == 3:
    n4 = float(input('valor um: '))
    n14 = float(input('valor dois: '))
    print(f'{n4} : {n14} = {n4 / n14}')
if o == 4:
    n111 = float(input('valor um: '))
    n11 = float(input('valor expoente: '))
    print(f'{n111} elevado a {n11} = {n111 ** n11}')
if o == 5:
    print("finalizando")
if o == 6:
    n6 = float(input('valor um: '))
    n16 = float(input('valor da raiz: '))
    print(f'{n6} a  {n16} raiz = {n6 ** (1/n16)}')
