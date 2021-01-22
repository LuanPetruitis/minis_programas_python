n1 = float(input('quanto você tirou  '))
n2 = float(input('quanto você tirou  '))
m = (n1 + n2) / 2
if m < 5 :
    print('\033[7;30;mREPROVADO\033[m')
elif 5 <= m <= 6.9:
    print('\033[7;30;mRECUPERAÇÃO\033[m')
else:
    print('\033[7;30;mAPROVADO\033[m')

input("Precione enter para finalizar o programa")
