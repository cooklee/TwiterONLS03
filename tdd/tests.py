def test_prime_numbers():
    assert prime(1) == []
    assert prime(2) == [2]
    assert prime(3) == [3]
    assert prime(4) == [2, 2]
    assert prime(5) == [5]
    assert prime(6) == [2, 3]
    assert prime(7) == [7]
    assert prime(8) == [2, 2, 2]
    assert prime(9) == [3, 3]
    assert prime(2 * 2 * 3 * 3 * 5 * 7 * 11) == [2, 2, 3, 3, 5, 7, 11]


def prime(n):
    numbers = []
    devider = 2
    while n > 1:
        while n % devider == 0:
            numbers.append(devider)
            n //= devider
        devider += 1
    return numbers
