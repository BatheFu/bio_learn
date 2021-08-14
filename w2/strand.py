def dna_rv_complement(pattern):
    """return the reverse complement"""
    project_d = {'A': 'T', 'C': 'G'}
    project_d.update({v: k for k, v in project_d.items()})
    rv_pattern = ''
    for i in range(-1, -len(pattern)-1, -1):
        rv_pattern = rv_pattern + project_d[pattern[i]]
    return rv_pattern

def count_c_g_diff(text,loc=0):
    """find skew i, return the score of index i of the text"""
    if loc == 0:
        return 0
    elif text[loc-1] == "C":
        return count_c_g_diff(text,loc-1) - 1
    elif text[loc-1] == "G":
        return count_c_g_diff(text,loc-1) + 1
    elif text[loc-1] == "A" or "T":
        return count_c_g_diff(text,loc-1)

def skew(text,loc):
    """ find skew i, return the score of index i of the text
        a better ver without recursion"""
    if loc == 0:
        return 0
    score = 0
    for i in range(loc):
        if text[i] == "C":
            score -= 1
        elif text[i] == "G":
            score += 1
    return score
def find_min_skew(text):
    """find the minimum score, return the index, maybe more than one"""
    res_lst =  [skew(text,i) for i in range(len(text))]
    res_dct = {} # mapping score:index
    for i,p in enumerate(res_lst):
        if not res_dct.__contains__(p):
            res_dct[p] = [i]
        else:
            res_dct[p].append(i)
    min_score = min(res_dct.keys())
    return res_dct[min_score]

def hamming_dist(p,q):
    """count the diff neucleutide of two strings"""
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

def match_approx_patterns(pattern,text,d):
    """
    Input: Strings Pattern and Text along with an integer d.
    Output: All starting positions where Pattern appears as a\
    substring of Text with at most d mismatches."""
    index = []
    for i in range(len(text)-len(pattern)+1):
        temp = text[i:i+len(pattern)]
        if hamming_dist(pattern,temp) <= d:
            index.append(i)
    return index

def count_pattern_with_mismatch(text,pattern,d):
    return len(match_approx_patterns(pattern,text,d))

def neighbors(pattern,d):
    """return the neighbourhood set of mutated patterns
    output: a set"""
    if d == 0:
        return {}
    if len(pattern) == 1:
        return {'A','G','C','T'}
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:],d)
    for text in suffix_neighbors:
        if hamming_dist(pattern[1:],text) < d:
            for each in {'A','G','C','T'}:
                new_kmer = each + text
                neighborhood.add(new_kmer)
        else:
            new_kmer = pattern[0] + text
            neighborhood.add(new_kmer)
    return neighborhood
def freq_words_with_mistakes(text,k,d):
    """ A nice recursion algorithm of computing mismatches freq pattern"""
    patterns = []
    freq_map = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        neighbourhood = list(neighbors(pattern,d)) + list(neighbors(dna_rv_complement(pattern),d))
        for j in range(len(neighbourhood)):
            neighbor = neighbourhood[j]
            if not freq_map.__contains__(neighbor):
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] = freq_map[neighbor] + 1
    max_count = max(freq_map.values())
    print(max_count)
    for key in freq_map.keys():
        if freq_map[key] == max_count:
            patterns.append(key)
    print(*patterns)
    return patterns


if __name__ =="__main__":
    s = "TATATATATCTATCGTGTTCCGCTACGCGTGTCGCGTACACTCTATAGTTAACTCTCACTCTACGCTATCACCGCGTACCGCCGCCGCTCACTCACGTACTAGTTCACACGTTCTATATATCCGCTCCGCTCGTTATACGCTCACTCTCTCTCGTTCTCGTCGCTCTCACGTTCGTCGCTAGTCGCCGCGTCGCTCGTTATACGC"
    freq_words_with_mistakes(s,6,3)