def remove_fourth_character(word: str) -> str:
    if len(word)>4:
        bef_four=word[:3]
        af_four=word[4:]
        new=bef_four+af_four
        return new

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
