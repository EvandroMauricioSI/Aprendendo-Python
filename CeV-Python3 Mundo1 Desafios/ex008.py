# DESAFIO 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input('Valor em metros: '))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('{} metro(s) corresponde(m) a:' .format(metros))
print('{:>10}   km' .format(km))
print('{:>10}   hm' .format(hm))
print('{:>10}   dam' .format(dam))
print('{:>10}   dm' .format(dm))
print('{:>10}   cm' .format(cm))
print('{:>10}   mm' .format(mm))
