"""
コピペして使えるutil系を集めたファイル
"""

##########
### input系
##########
n = int(input())
a, b = map(int, input().split(' '))

##########
### よく使う関数
##########
# 商と余り
q, mod = divmod(10, 3)
# 組み合わせを列挙
import itertools
for v in itertools.combinations([1,2,3], 2):
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
