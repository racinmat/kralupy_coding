import test
import scripts


def is_palindrome(string):
    for k in range(int(len(string) / 2)):
        # (k) 0, 1, 2...
        # (-k) -0, -1, -2
        # (-k-1) -1, -2, -3
        left_char = string[k].lower()
        right_char = string[-k - 1].lower()
        if left_char != right_char:
            return False
    return True

if __name__ == '__main__':
    @test.describe('sample tests')
    def sample_tests():
        test.assert_equals(is_palindrome('a'), True)
        test.assert_equals(is_palindrome('aba'), True)
        test.assert_equals(is_palindrome('Abba'), True)
        test.assert_equals(is_palindrome('malam'), True)
        test.assert_equals(is_palindrome('walter'), False)
        test.assert_equals(is_palindrome('kodok'), True)
        test.assert_equals(is_palindrome('Kasue'), False)

    # assert is_palindrome('a')
    # assert is_palindrome('aba')
    # assert is_palindrome('Abba')
    # assert is_palindrome('malam')
    # assert not is_palindrome('walter')
    # assert is_palindrome('kodok')
    # assert not is_palindrome('Kasue')
    # print('vše funguje')
