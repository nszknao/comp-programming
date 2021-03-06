"""
コピペして使えるutil系を集めたファイル
"""

##########
### input系
##########
n = int(input())
a, b = map(int, input().split(' '))

##########
### 基本
##########
keys = [1,2,3]
dicts = {key:'1' for key in keys}

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
# 逆行列
l_2d = [[1,2], [3,4]]
l_2d_t = [list(x) for x in zip(*l_2d)]
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
    # [(1, 2), (1, 3), (2, 3)]
    # もとのlistの順番は崩れない
    print(v)
# 重複組み合わせを列挙
for v in itertools.combinations_with_replacement([1,2,3], 3):
    # [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]
    # もとのlistの順番は崩れない
    print(v)
# デカルト積
import itertools
for v in itertools.product([1,2,3], [1,2,3]):
    # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    print(v)
# 順列
import itertools
for v in itertools.permutations([1,2,3]):
    # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
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
# ビットカウント
def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f
# 二分探索
from bisect import bisect, bisect_left
# bisectは、値が存在したらその次のindexを返す
# bisect_leftは、値が存在したらその前のindexを返す
arr = [1,20,30,55]
bisect(arr, 20) # →2
bisect_left(arr, 20) # →1
# 二分探索(arrに存在しなかったら、Noneを返す)
def binary_search(arr, item):
    """
    arr: 昇順にソート済list
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    # 最終的にlowとhighは同じ値になる
    # 加えて、itemが間に挟まったらlow(=high)は右側(大きい値)に寄る
    return None
# 三分探索(凸関数f(x)の最適化に使えた)
left = 0
right = 100 # sampleケースでinputが最大のときの答えが90ちょいだから
def f(x):
    return 2**x
while right - left > 0.000000001:
    mid_left = right/3 + left*2/3
    mid_right = right*2/3 + left/3
    if f(mid_left) > f(mid_right):
        left = mid_left
    else:
        right = mid_right
print(f(right))
# 深さ優先探索(DFS)
n = 10
first_order = [-1] * n
last_order = [-1] * n
ptr = 1
seen = [False] * n
def dfs(g, seen, idx):
    global first_order, first_order, ptr
    first_order[idx] = ptr
    ptr += 1
    seen[idx] = True
    for i in g[idx]:
        # idxから行ける各頂点について
        if seen[i]: continue
        dfs(g, seen, i)
    last_order[idx] = ptr
    ptr += 1
