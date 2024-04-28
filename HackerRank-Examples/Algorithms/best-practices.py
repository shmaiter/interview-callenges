import random
from timer import Timer
from collections import defaultdict, Counter
import string
import itertools

friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
numbers = [6, 5, 3, 7, 2, 4, 1]
animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5},
]
all_words = "all the worlds in the world".split()


def f_strings(name, age):
    print(f"My name is {name} and I'm {age / 10:.3f} decades old.")


def sorted_keys(key):
    print(sorted(animals, key=lambda animal: animal[key]))


def get_random_word():
    return random.choice(all_words)


def unique_values():
    unique_words = set()
    for _ in range(1000):
        unique_words.add(get_random_word())
    print(unique_words)


def memoryComplexity():
    # list comprehension
    # sum([i*i for i in range(1, 1000001)])
    # generators
    print(sum((i*i for i in range(1, 1000001))))


def defaultValues():
    cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}

    # if key exists return the value, otherwise default will be returned
    name = cowboy.get('name', 'The man with no name')

    # if key exists return the value, otherwise default is assigned to the new key and
    # then will be returned.
    name = cowboy.setdefault('name', 'Musa')
    print(name)


def defaultDict():
    student_grades = defaultdict(list)
    grades = [
        ('elliot', 91),
        ('neelam', 98),
        ('bianca', 81),
        ('elliot', 88),
    ]
    for name, grade in grades:
        student_grades[name].append(grade)

    print(student_grades)


def count_duplicates():
    words = "if there was there was but if there was not there was not".split()
    counts = Counter(words)
    print(counts.most_common(3))


def itertools_pc():
    # return "tuples", takes 2 parameters: an iterable and
    # a key "r=" for length of elements in every tuple

    # the order DOES matter
    # ('sam', 'devon') and ('devon', 'sam') represent different pairs,
    # BOTH of them would be included
    permutations = list(itertools.permutations(friends, r=2))

    # the order DOESN'T matter
    # ('sam', 'devon') and ('devon', 'sam') represent the same pair,
    # only ONE of them would be included
    combinations = list(itertools.combinations(friends, r=2))
    print(combinations)


if __name__ == '__main__':
    # 1.
    # f_strings('Alen', 31)
    # 2.
    # sorted_keys('type')
    # 3.
    # unique_values()
    # 4.
    # memoryComplexity()
    # 5.
    # defaultValues()
    # 6.
    # defaultDict()
    # 7.
    # count_duplicates()
    # 8.
    # print(string.ascii_letters)
    # print(string.punctuation)
    # 9.
    # itertools_pc()
    pass
