from TinyStatistician import TinyStatistician

tstat = TinyStatistician()

a = [1, 42, 300, 10, 59]
b = [1, 42, 300, 10, 59, 37]

print('Media -> ' + str(tstat.mean(a)) + ' <- expected: 82.4')

print('Mediana -> ' + str(tstat.median(a)) + ' <- expected: 42')
print('Mediana -> ' + str(tstat.median(b)) + ' <- expected: 39.5')

##tstat.quartile(a)
# Expected result: [10.0, 59.0]

##tstat.var(a)
# Expected result: 12279.439999999999

##tstat.std(a)
# Expected result: 110.81263465868862