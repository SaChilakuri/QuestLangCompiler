import regex as re
pattern = r"\"[^\"]*\""

print(re.findall(pattern,"\"asdf\"asdf\""))
