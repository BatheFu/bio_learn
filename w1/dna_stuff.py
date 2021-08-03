from collections import Counter
from detect_pattern import *


def dna_complement(pattern):
    """return the reverse complement"""
    project_d = {'A': 'T', 'C': 'G'}
    project_d.update({v: k for k, v in project_d.items()})
    rv_pattern = ''
    for i in range(-1, -len(pattern)-1, -1):
        rv_pattern = rv_pattern + project_d[pattern[i]]
    return rv_pattern


def find_pattern_index(text, pattern):
    """return the index of the pattern"""
    index = ""
    for i in range(len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            index = index + str(i) + " "
    print(index)
    return index


def find_clumps(text, k, L, t):
    """find a clump in a given window of length L
    L: searching window length
    k : length of kmers
    t : times
    """
    patterns = []
    n = len(text)
    for i in range(n-L+1):
        window = text[i:i+L]
        freqMap = freq_table(window, k)
        for key in freqMap.keys():
            if freqMap[key] >= t:
                patterns.append(key)
    remove_dup = set(patterns)
    final_patterns = ""
    for _ in remove_dup:
        final_patterns = final_patterns + _ + " "
    print(final_patterns)
    return final_patterns


def better_find_clumps(text, k, L, t):
    index = [i for i in range(len(text) - k + 1)]
    kmer = [text[i:i+k] for i in index]
    d = {}
    for i in range(len(kmer)):
        km = kmer[i]
        if not d.__contains__(km):
            d[km] = [i]
        else:
            d[km].append(i)

    result = []
    for key,value in d.items():
        for i in range(len(value)-t+1):
            if value[i+t-1] -value[i] <= L-k:
                result.append(key)
                break
    print(len(result))


if __name__ == "__main__":
    better_find_clumps(
        "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4)
    e_coli = open("w1/E_coli.txt",'r').read()
    better_find_clumps(e_coli,9,500,3)
