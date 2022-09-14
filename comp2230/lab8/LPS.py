# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def computeLPSArray(pat, lps):
    ln = 0
    i = 1

    while i < len(pat):
        if pat[i] == pat[ln]:
            ln += 1
            lps[i] = ln
            i += 1

        elif ln != 0:
            ln = lps[ln-1]

        else:
            lps[i] = 0
            i += 1


pat = "pappar"
lps = [0] * len(pat)

computeLPSArray(pat, lps)
print(lps)

pat = "ababbcabab"
lps = [0] * len(pat)

computeLPSArray(pat, lps)
print(lps)
