from TinyStatistician import TinyStatistician

tstat = TinyStatistician()

a = [1, 42, 300, 10, 59]
b = [1, 42, 300, 10, 59, 37]

print('Media -> ' + str(tstat.mean(a)) + ' <- expected: 82.4')

print('Mediana -> ' + str(tstat.median(a)) + ' <- expected: 42')
print('Mediana -> ' + str(tstat.median(b)) + ' <- expected: 39.5')

print('Quartiles -> ' + str(tstat.quartiles(a)) + ' <- expected: 5.5 & 179.5')
print('Quartiles -> ' + str(tstat.quartiles(b)) + ' <- expected: 10.0 & 59.0')

print('Varianza -> ' + str(tstat.var(a)) + ' <- expected: 12279.439999999999')

print('Desviacion estandar -> ' + str(tstat.std(a)) + ' <- expected: 110.81263465868862')