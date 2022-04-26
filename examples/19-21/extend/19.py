# https://inf-ege.sdamgia.ru/problem?id=27794
# Когда в условии сказано "неудачного первого хода"
# меняем all на 18 строке на any !!!
from functools import lru_cache


def moves(h):
	a, b = h

	return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

@lru_cache(None)
def f(h):
	if sum(h) >= 50:
		return "W"
	if any(f(m) == "W" for m in moves(h)):
		return "P1"
	if any(f(m) == "P1" for m in moves(h)):
		return "B1"
	if any(f(m) == "B1" for m in moves(h)):
		return "P2"
	if all(f(m) == "P1" or f(m) == "P2" for m in moves(h)):
		return "B1/2"

for s in range(1, 41+1):
	if f((8, s)) == "B1":
		print(s)