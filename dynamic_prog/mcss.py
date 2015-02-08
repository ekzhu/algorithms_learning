'''
Maximum Contiguous Subsequence Sum Problem.
Solved using dynamic programming.
'''

def mcss(pi):
    b = 0
    ans = 0
    for a in pi:
        b = max(b + a, a)
        ans = max(b, ans)
    return ans

if __name__ == "__main__":
    import random
    pi = [random.randint(-12,12) for _ in range(12)]
    print pi
    print mcss(pi)
