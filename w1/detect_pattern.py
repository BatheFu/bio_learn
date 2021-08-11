from collections import defaultdict

def detect(text,pattern):
    """two args:
        1. text: a string
        2. pattern: a string to be detected, allowing overlapping"""

    count = 0
    for i in range(len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count +=1
    print(count)
    return count

def detect2(text,k):
    """Find the most freq k-mer,
    args: 1.text, a string
        2. k, a integer
    output: a list of most freq k-mers
    """
    pass
def freq_table(text,k):
    freq_map=defaultdict()
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        if pattern in freq_map.keys():
            freq_map[pattern] +=1
        else:
            freq_map[pattern]=1
    return freq_map

def better_freq_words(text,k):
    freq_patterns = []
    freqMap = freq_table(text,k)
    max_v = max(freqMap.values())
    for key,val in zip(freqMap.keys(),freqMap.values()):
        if freqMap[key] == max_v:
            freq_patterns.append({str(key):val})
    return freq_patterns

def detect_all_kmers(text,limit=10):
    kmer_d = defaultdict()
    for k in range(3,limit):
        kmer_d[str(k)] = better_freq_words(text,k)
        #print(kmer_l[str(k)])
    return kmer_d

def print_all_kmers(kmer_d):
    for k,v in kmer_d.items():
        print("Length = {}\tK-mer = {}".format(k,v))

