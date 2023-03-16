from time import sleep
import time

def ft_progress(lst):
	startTime = time.time()
	for id, i in enumerate(lst):
		timeNow = time.time() - startTime
		progress = id + 1
		percent = float((float(progress) / float(len(lst))) * 100.0)
		esTime = (timeNow * (len(lst) / progress)) - timeNow
		
		newInput = ('ETA: {eta:6.1f} [{per:3}%][{loading:55}] {here}/{to} | elapsed time {passed:.1f}s'
		.format(eta=esTime, per=int(percent), loading='>'.rjust(int((percent/10.0) * 5.5), '='), here=progress, to=len(lst), passed=timeNow))

		print(newInput, end='\r')
		yield i


listy = range(100)
ret = 0
for elem in ft_progress(listy):
	ret+=(elem+3) %5
	sleep(0.01)
print()
print(ret)