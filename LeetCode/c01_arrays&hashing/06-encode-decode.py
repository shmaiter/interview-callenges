'''271. Encode and Decode Strings
    Given a list of strings encode it as single string and decode it into its original forms.
'''

# --------------------------------------------------------- Solution #1
# def encode(strs: list[str]) -> list[str]:
#     glue = "&*.*&".join(strs)
#     return decode(glue)


# def decode(strs: str) -> list[str]:
#     return strs.split("&*.*&")


# --------------------------------------------------------- Solution #2
def encode(strs: list[str]) -> list[str]:
    res = ""
    
    for s in strs:
        # res += f"{len(s)}#{s}"
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> list[str]:
    res, i = [], 0  # result of strings, and pointer

    while i < len(s):
        j = i
        if s[j] != "#":
            j += 1
        lenght = int(s[i:j])
        res.append(s[j + 1 : j + 1 + lenght])
        i = j + 1 + lenght
    return res


print(decode(encode(["sapo", "perro", "gato", "5#gallo"])))
