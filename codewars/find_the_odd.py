import test
# https://www.codewars.com/kata/find-the-odd-int/train/python
# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    occurences = {}
    for i in seq:
        if i in occurences:
            occurences[i] += 1
        else:
            occurences[i] = 1

    for number, occurs in occurences.items():
        if occurs % 2 == 1:
            return number

    return None


if __name__ == '__main__':
    print('tohle se stane když to spustíš')
    test.describe("Example")
    test.assert_equals(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
