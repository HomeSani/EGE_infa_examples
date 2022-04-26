# https://inf-ege.sdamgia.ru/problem?id=3791

results = [0] * 1000

results[1] = 1

for i in range(1, 32+1):
	results[i+1] += results[i]
	results[i*4] += results[i]

print(results[32])