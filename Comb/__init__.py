if __name__ == '__main__':
    from Comb import factorial
    from Comb import permutation
    from Comb import combination
else:
    from Comb.Comb import factorial
    from Comb.Comb import combination
    from Comb.Comb import permutation


def test(comments=False):
    assert permutation(4) == 24
    if comments:
        print('premutation test completed')
    assert combination(5,3) == 10
    if comments:
        print('combination test completed')

if __name__ == '__main__':
    test()



