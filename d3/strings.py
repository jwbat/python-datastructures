import string

class String:
    vowels = 'aeiou'

    def count_vowels(self, s):
        return sum([1 for ltr in s.lower() if ltr in self.vowels])

    def reverse(self, s):
        def rev(s):
            if s == '':
                return ''
            else:
                return rev(s[1 : ]) + s[0]
        return rev(s)

    def reverse_words(self, sentence):
        lst = sentence.split()
        lst.reverse()
        return ' '.join(lst)

    def is_rotation(self, s1, s2):
        if not len(s1) or not len(s2):
            return False
        if s1 == s2:
            return True

        rotate = lambda s: s[-1] + s[ : -1]

        rotated = rotate(s1)
        while rotated != s1:
            if rotated == s2:
                return True
            rotated = rotate(rotated)
        return False

    def remove_duplicates(self, s):
        stringset = set()
        result = ''
        for char in s:
            if char not in stringset:
                result += char
            stringset.add(char)
        return result

    def most_repeated_char(self, s):
        d = {char : s.count(char) for char in set(s)}
        lst = [(count, char) for (char, count) in d.items()]
        return max(lst)[1]

    def capitalize_words(self, s):
        return string.capwords(s)

    def are_anagrams(self, s1, s2):
        f = lambda s: sorted(list(s.lower()))
        return f(s1) == f(s2)

    def is_palindrome(self, s):
        return s == self.reverse(s)

    def is_palindrome2(self, s):
        # faster than the 1st one
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left] == s[right]:
                return False
            left += 1
            right -= 1
        return True


def main():
    s = String()

    word = 'continue'
    another = 'fluffy'
    sentence = 'see spot run'
    string1, string2 = '', ''
    string1, string2 = 'ABCD', 'CDAB'
    stringA, stringB = 'ABCD', 'DCAB'
    word1, word2 = 'senator', 'treason'
    word3, word4 = 'food', 'fod'
    word5 = 'abba'
    word6 = 'kook'
    word7 = 'titer'

    print(f'\n\t count vowels in {word}: ', s.count_vowels(word))

    print(f'\t reverse "{word}": ', s.reverse(word))
    print(f'\t reverse "{sentence}": ', s.reverse_words(sentence))

    print(f'\t {string1} is a rotation of {string2}: ', s.is_rotation(string1, string2))
    print(f'\t {string1} is a rotation of {string1}: ', s.is_rotation(string1, string1))
    print(f'\t {stringA} is a rotation of {stringB}: ', s.is_rotation(stringA, stringB))

    print(f'\t "{word}" with duplicates removed: ', s.remove_duplicates(word))
    print(f'\t most repeated char in "{word}" : ', s.most_repeated_char(word))
    print(f'\t most repeated char in "{another}" : ', s.most_repeated_char(another))
    print(f'\t capitalize "{sentence}": ', s.capitalize_words(sentence))

    print(f'\t "{word1}" is an anagram of "{word2}": ', s.are_anagrams(word1, word2))
    print(f'\t "{word3}" is an anagram of "{word4}": ', s.are_anagrams(word3, word4))

    print(f'\t "{word5}" is a palindrome: ', s.is_palindrome(word5))
    print(f'\t "{word6}" is a palindrome: ', s.is_palindrome(word6))
    print(f'\t "{word7}" is a palindrome: ', s.is_palindrome(word7))

    print(f'\t "{word5}" is a palindrome (v2): ', s.is_palindrome2(word5))
    print(f'\t "{word6}" is a palindrome (v2): ', s.is_palindrome2(word6))
    print(f'\t "{word7}" is a palindrome (v2): ', s.is_palindrome2(word7))


if __name__ == '__main__':
    main()
