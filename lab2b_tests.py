# lab2b_tests.py

import nose
from lab2b import *

def test_make_random_code():
    for i in range(100):
        code = make_random_code()
        assert len(code) == 4
        for char in code:
            assert char in 'RGBYOW'

def make_random_codes(n):
    codes = []
    for _ in range(n):
        # We assume that make_random_code() works.
        codes.append(make_random_code())
    return codes

def test_count_exact_matches():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        assert 0 <= count_exact_matches(c1, c2) <= 4

    # Check specific answers.
    assert count_exact_matches('RGBY', 'RGBY') == 4
    assert count_exact_matches('RGBY', 'GBYR') == 0
    assert count_exact_matches('RGBY', 'RGOO') == 2
    assert count_exact_matches('RGBY', 'RWBW') == 2
    assert count_exact_matches('RGBY', 'WOWO') == 0 
 

def test_count_letter_matches():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        assert 0 <= count_letter_matches(c1, c2) <= 4

    # Check specific answers.
    assert count_exact_matches('RGBY', 'RGBY') == 4
    assert count_letter_matches('RGBY', 'RGBY') == 4
    assert count_letter_matches('RGBY', 'GBYR') == 4
    assert count_letter_matches('ROGO', 'RRGG') == 2
    assert count_letter_matches('RGBY', 'OROG') == 2
    assert count_letter_matches('RGBY', 'BWBR') == 2
    assert count_letter_matches('RBBY', 'GRBO') == 2 
    assert count_letter_matches('RGBY', 'WOWO') == 0 

def test_compare_codes():
    # Check basic invariants.
    codes1 = make_random_codes(1000)
    codes2 = make_random_codes(1000)
    for (c1, c2) in zip(codes1, codes2):
        comp = compare_codes(c1, c2)
        assert len(comp) == 4
        for char in comp:
           assert char in 'bw-'

    # Check specific answers.
    assert compare_codes('RGBY', 'RGBY') == 'bbbb'
    assert compare_codes('RGBY', 'GBYR') == 'wwww'
    assert compare_codes('RGBY', 'OROG') == 'ww--'
    assert compare_codes('RGBY', 'BWBR') == 'bw--'
    assert compare_codes('RGBY', 'WOWO') == '----'

if __name__ == '__main__':
    nose.runmodule()



