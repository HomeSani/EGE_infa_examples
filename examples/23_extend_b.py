# https://inf-ege.sdamgia.ru/problem?id=25852

results = [0] * 1000

results[1] = 1

for i in range(1, 10+1):
	if i + 1 <= 10:
		results[i+1] += results[i]
	if i * 2 <= 10:
		results[i*2] += results[i]

for i in range(10, 22+1):
	if i + 1 != 15 and i * 2 != 15:
		results[i+1] += results[i]
		results[i*2] += results[i]

print(results[22])