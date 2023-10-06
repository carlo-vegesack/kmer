import doctest


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """
    result = []
    for i in range(0,len(x)-k+1):
        substring = x[i:i+k]
        result.append(substring)
    return result


        
... 


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    FIXME: do you want more tests here?
    """
    # result = {}
    # for i in range(0,len(x)-k+1):
    #     substring = x[i:i+k]
    #     result[substring] = None
    # result_uniq = list(result.keys())
    # print (result_uniq)
    # return result_uniq
    ...
unique_kmers('tatatatatgtf',3)

def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    FIXME: do you want more tests here?
    """
    ...
