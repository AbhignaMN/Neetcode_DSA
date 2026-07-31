def concatenate(s1: str, s2: str) -> str:
    s=s1+s2
    if len(s)>10:
        return "Too long!"
    return s




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
