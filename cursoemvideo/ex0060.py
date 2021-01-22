n = int(input('Digite um numero inteiro;  '))
f = n
while not n == 1:
    f = f * (n - 1)
    n -= 1
print(f)
