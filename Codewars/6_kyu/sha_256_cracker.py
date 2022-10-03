import hashlib
import itertools


def sha256_cracker(hash_, chars):
    """
    When provided with a SHA-256 hash, return the value that was hashed
    Example arguments:
    '5694d08a2e53ffcae0c3103e5ad6f6076abd960eb1f8a56577040bc1028f702b',
    'cdeo'
    Correct output: 'code'
    """
    for x in itertools.permutations(chars):
        x = ''.join(x)
        if hashlib.sha256(x.encode('utf-8')).hexdigest() == hash_:
            return x
    return None


ht = 'b8c49d81cb795985c007d78379e98613a4dfc824381be472238dbd2f974e37ae'
ch = 'deGioOstu'
ht_2 = 'f58262c8005bb64b8f99ec6083faf050c502d099d9929ae37ffed2fe1bb954fb'
ch_2 = 'abc'
print(sha256_cracker(ht, ch))
print(sha256_cracker(ht_2, ch_2))
