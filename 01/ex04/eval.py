

class Evaluator:


	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			print('-1')
			return
		result = 0
		for i1, i2 in zip(coefs, words):
			result += i1 * len(i2)
		print(result)


	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			print('-1')
			return
		result = 0
		coefis = list(enumerate(coefs))
		for i, value in coefis:
			result += value * float(len(words[i]))
		print(result)

if __name__ == "__main__":
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.2, 0.5]
	Evaluator.zip_evaluate(coefs, words)
	Evaluator.enumerate_evaluate(coefs, words)


	words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
	coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
	Evaluator.zip_evaluate(coefs, words)
	Evaluator.enumerate_evaluate(coefs, words)