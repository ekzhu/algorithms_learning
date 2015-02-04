'''
A sketch of the proof for LIS algorithm:

Definition: Let `pi` be a list of n integers, not necessarily distinct. An
increasing subsequence of `pi` is a subsequence of `pi` whose values strictly
increase from left to right.

Definition: A decreasing subsequence of `pi` is a subsequence of `pi` where the
numbers are non-increasing from left to right.

Definition: A cover of `pi` is a set of decreasing subsequences of `pi` that
contain all the numbers of `pi`. For example:
{5,3,2,1}; {4,}; {9, 6}; {8,7}; {10,} is a cover of `pi` = 5,3,4,9,6,2,1,8,7,10.

Definition: The size of the cover is the number of decreasing subsequences in it,
and a smallest cover is a cover with minimum size among all covers.

Lemma 1: If `I` is an increasing subsequence of `pi` with length equal to the
size of a cover of `pi`, call it `C`, then `I` is a longest increasing
subsquence of `pi` and `C` is a smallest cover of `pi`.

Proof: No increasing subsequence of `pi` can contain more than one number
contained in any decreasing subsequence of `pi`, since the numbers in an
increasing subsequence strictly increase from left to right, whereas the numbers
in a decreasing subsequence are non-increasing left to right. Hence no
increasing subsequence of `pi` can have lenght greater than the size of any
cover of `pi`. Now assume the length of `I` is equal to the size of `C`. This
implies that `I` is a longest increasing subsequence of `pi` because no other
increasing subsequence can be longet than the size of `C`. Conversely, `C` must
be a smallest cover of `pi`, for if there were a smaller cover `C'`, than `I`
would be longer than the size of `C`, which is impossible. Hence the proof.

Lemma 2: There is an increasing subsequence `I` of `pi` containing exactly one
number from each decreasing subsequence in the greedy cover `C`. Hence `I` is
the longest possible and `C` is the smallest possible.

Proof: For an arbitrary number `x` in a decreasing subsequence `i` and `i` > 0,
there must be a smaller number `y` in decreasing subsquence `i-1`,
since when `x` is placed in `i` by the greedy cover algorithm, it could not be
placed in `i-1` because `x`>`y` and `y` was the last element in `i-1`.

Repeat the argument till `i-1`=0, we can conclude there is an increasing
subsequence in `pi` containing one number from each of the first `i+1`
subsequences ending with `x`. Choose `x` to be any number in the last
decreasing subsequence proves the lemma.

This also shows that the greedy cover algorithm produces a smallest cover for
`pi`.
'''
import bisect

def naive_greedy_cover(pi):
    '''Given a sequence of integer `pi`, find a cover of non-increasing
    subsequences for `pi`. Return the cover as a list of subsequences.'''
    cover = []
    for x in pi:
        subsqs = filter(lambda sq : True if sq[-1] >= x else False, cover)
        if len(subsqs) == 0:
            cover.append([x,])
        else:
            subsqs[0].append(x)
    return cover

def greedy_cover(pi):
    '''Given a sequence of integer `pi`, find a cover of non-increasing
    subsequences for `pi`. Return the cover as a list of subsequences.'''
    cover = []
    L = []
    for x in pi:
        # Use binary search to find the left-most non-increasing subsequence
        # that can be extended by x
        i = bisect.bisect_left(L, x)
        if i == len(L):
            cover.append([x,])
            L.append(x)
        else:
            cover[i].append(x)
            L[i] = x
    return cover


def lis(pi, cover_algo):
    '''The longest increasing subsquence algorithm.'''
    if len(pi) == 0:
        return []
    cover = cover_algo(pi)
    x = cover[-1][0]
    sq = [x,]
    i = len(cover) - 2
    while i >= 0:
        for y in cover[i]:
            if y < x:
                break
        x = y
        i -= 1
        sq = [x,] + sq
    return sq


def profile(pi, cover_algo):
    import time
    N = 100
    durs = [0 for _ in range(N)]
    for i in range(N):
        start = time.time()
        lis(pi, cover_algo)
        durs[i] = time.time() - start
    return min(durs)

if __name__ == "__main__":
    import random
    pi = [random.randint(1, 100) for _ in range(12)]
    print "Pi:", pi
    print "Cover:", naive_greedy_cover(pi)
    print "LIS using naive greedy cover algo:", lis(pi, naive_greedy_cover)
    print "LIS using greedy cover algo:", lis(pi, greedy_cover)

    # Profiling
    import time
    print "Profiling..."
    pi = [random.randint(1, 1000) for _ in xrange(1000)]
    t1 = profile(pi, naive_greedy_cover)
    print "LIS using naive greedy cover took %s" % str(t1)
    t2 = profile(pi, greedy_cover)
    print "LIS using binary search greedy cover took %s" % str(t2)
    print "Using binary search greedy is %.2f times faster than the naive approach" % (t1 / t2)
