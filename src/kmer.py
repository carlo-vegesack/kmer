import doctest
import pprint


def kmer(x: str, k: int):
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']
    """
    result = []
    for i in range(0,len(x)-k+1):
        substring = x[i:i+k]
        result.append(substring)
    return result    
    ... 


def unique_kmers(x: str, k: int):
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('tatatgtf',3)
    ['tat', 'ata', 'atg', 'tgt', 'gtf']
    """
    result = {}
    for i in range(0,len(x)-k+1):
        substring = x[i:i+k]
        result[substring] = None
    result_uniq = list(result.keys())
    return result_uniq
    ...

def count_kmers(x: str, k: int):
    """
    Computer all k-mers of x and count how often they appear.
    >>> count_kmers('agtagtcg', 3)
    {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}
    """
    result = {}
    for i in range(0,len(x)-k+1):
        substring = x[i:i+k]
        if substring in result:
            result[substring] += 1
        else:
            result[substring] = 1
    return result
    ...
