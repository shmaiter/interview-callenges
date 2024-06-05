# Encode and Decode Strings
from icecream import ic


def encode(strs: list[str]) -> str:
    hash = ''

    for word in strs:
        hash += str(len(word)) + "#" + word
    ic(hash)
    return hash


def decode(s: str) -> list[str]:
    res, i = [], 0  # result of strings, and pointer

    while i < len(s):
        j = i
        ic(j)
        while s[j] != "#":
            j += 1
        ic(j)
        lenght = int(s[i:j])
        word = s[j + 1 : j + 1 + lenght]
        res.append(word)
        i = j + 1 + lenght
        ic(lenght)
        ic(word)
    return res


# print(decode(encode(["neet", "code", "love", "you"])))
ic(decode(encode(["we", "say", ":", "yes", "!@#$%^&*()"])))
