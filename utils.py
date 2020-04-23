"""
コピペして使えるutil系を集めたファイル
"""

##########
### input系
##########
n = int(input())
a, b = map(int, input().split(' '))

##########
### データ型
##########
s = set()
s.add()

##########
### よく使う関数
##########
# 商と余り
q, mod = divmod(10, 3)
# nCr
from operator import mul
from functools import reduce
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under
# 組み合わせを列挙
import itertools
for v in itertools.combinations([1,2,3], 2):
    # vはタプル
    # もとのlistの順番は崩れない
    print(v)
# デカルト積
import itertools
for v in itertools.product([1,2,3], [1,2,3]):
    # vはタプル
    print(v)
# 約数を列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
