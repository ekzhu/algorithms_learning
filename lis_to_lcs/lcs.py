'''
The LCS can be reduced to LIS. See proof in the book by Guesfield:
Algoirhtm on Strings, Trees, and Sequences (12.6). Sketch for the proof:

1. `I`, any increasing subsequence in the list `pi` has at most 1 element from
each of the decreasing subsequences (segements). Thus, `I` does not repeats
elements in s1. The decreasing subsequences are arranged left to right in the
same order as in s1, thus `I` must map to a subsequence of s1.
2. Also, since the numbers in `I` are strictly increasing and represent the
positions in s2, it must map to a subsequence of s2.
'''
from lis import lis, greedy_cover

def lcs(s1, s2):
    '''The longest common subsequence algorithm by reduction to the longest
    increasing subsequence problem.'''
    pi = []
    for x in s1:
        pos = []
        for i, y in enumerate(s2):
            if x == y:
                pos.append(i)
        pi += pos
    return [s2[i] for i in lis(pi, greedy_cover)]

if __name__ == "__main__":
    import random, string
    alphabets = string.lowercase
    s1 = [alphabets[random.randint(0,len(alphabets)-1)] for _ in range(26)]
    s2 = [alphabets[random.randint(0,len(alphabets)-1)] for _ in range(26)]
    print "S1:", ''.join(s1)
    print "S2:", ''.join(s2)
    print "LCS", ''.join(lcs(s1, s2))
