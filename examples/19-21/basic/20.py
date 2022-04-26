# https://inf-ege.sdamgia.ru/problem?id=28243
from functools import lru_cache


def moves(s):
	return s + 1, s * 5

@lru_cache(None)
def f(s):
	if s > 100:
		return "W"

	if any(f(m) == "W" for m in moves(s)):
		return "P1"
	if all(f(m) == "P1" for m in moves(s)):
		return "B1"
	if any(f(m) == "B1" for m in moves(s)):
		return "P2"
	if all(f(m) == "P1" or f(m) == "P2" for m in moves(s)):
		return "B1/2"

for s in range(1, 100+1):
	if f(s) == "P2":
		print(s)