from __future__ import print_function

class Bloom:
    def __init__(self, m):
        self.__m = m
        self.__array = [False] * m
        self.__hashes = [\
                lambda x: 10317898*len(x),\
                ]

    def __str__(self):
        s = ''
        for b in self.__array:
            s += '1' if b else '0'
        s += '\n({}/{} bits set)'.format(self.__array.count(True), self.__m)
        return s

    def __get_bit(self, hash_value):
        return self.__array[hash_value % self.__m]
    def __set_bit(self, hash_value):
        self.__array[hash_value % self.__m] = True

    def add(self, x):
        pass

    def contains(self, x):
        return False

def main():
    with open('../data/example_text.txt') as f:
        example_text = f.readline()
    example_words = example_text.split(' ')

    random_strings = []
    with open('../data/random_strings.txt') as f:
        for line in f:
            random_strings.append(line.strip())

    b = Bloom(16)
    for w in example_words:
        b.add(w)

    def grade(value, should_be):
        if value and not should_be:
            return 'False positive'
        if not value and should_be:
            return 'False negative'
        return 'Correct'

    final_result = {'Correct': 0, 'False positive': 0, 'False negative': 0}
    test_case = ['Lorem', 'ipsum', 'dolor', 'sit', 'commodo', 'Excepteur', 'Sed', 'put', 'perspiciatis', 'unde', 'omnis', 'iste', 'natus', 'error', 'sit'] + random_strings
    for w in test_case:
        result = grade(b.contains(w), w in example_words)
        print('contains({}): {} ({})'.format(w, b.contains(w), result))
        final_result[result] += 1

    print()
    print('The Bloom filter:')
    print(b)
    for fr in final_result:
        print('{}: {}/{} ({:.2f}%)'.format(fr, final_result[fr], len(test_case), 100. * final_result[fr] / len(test_case)))

if __name__ == '__main__':
    main()

