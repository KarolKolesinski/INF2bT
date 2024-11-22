def f(x):
    return x * x + 1

a = 0      
b = 2
E = 10000000

szer = (b - a) / E
calka = 0

for i in range(E):
    wys = f(a + i * szer)
    calka += szer * wys

print(calka)