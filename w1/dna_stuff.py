from collections import Counter
from detect_pattern import *

def dna_complement(pattern):
    """return the reverse complement"""
    project_d = {'A':'T','C':'G'}
    project_d.update({v:k for k,v in project_d.items()})
    rv_pattern = ''
    for i in range(-1,-len(pattern)-1,-1):
        rv_pattern = rv_pattern + project_d[pattern[i]]
    return rv_pattern

def find_pattern_index(text,pattern):
    """return the index of the pattern"""
    index=""
    for i in range(len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            index = index + str(i) + " "
    print(index)
    return index

def find_clumps(text,k,L,t):
    """find a clump in a given window of length L
    L: searching window length
    k : length of kmers
    t : times
    """
    patterns = []
    n = len(text)
    for i in range(n-L+1):
        window = text[i:i+L]
        freqMap = freq_table(window,k)
        for key in freqMap.keys():
            if freqMap[key] >=t:
                patterns.append(key)
    remove_dup = set(patterns)
    final_patterns = ""
    for _ in remove_dup:
        final_patterns = final_patterns + _ + " "
    print(final_patterns)
    return final_patterns

def better_find_clumps(text,k,L,t):
    """ kmer length = 9"""
    d = {}
    # kmer projection d
    for i in range(0,len(text)-k+1):
        kmer = text[i:i+k]
        d[kmer] = i
    print(d)
    print(len(d))
    count_d = Counter(d.keys())
    print(count_d)
    count_f={}
    count=0
    for key in count_d:
        if count_d[key] >=t:
            count_f[key] = d[key]
            indices = list(count_f.values())
            if max(indices)+k-min(indices) <=L:
                count+=1
    print(count)
    return count


