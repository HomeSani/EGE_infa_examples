# https://inf-ege.sdamgia.ru/problem?id=13525

results = [0] * 1000

results[1] = 1

for i in range(1, 8+1):
	if i + 1 <= 8:
		results[i+1] += results[i]
	if i + 3 <= 8:
		results[i+3] += results[i]

for i in range(8, 15+1):
	results[i+1] += results[i]
	results[i+3] += results[i]

print(results[15])