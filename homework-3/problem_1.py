from collections import Counter


def generate_phrase(characters, phrase):
    return Counter(characters) == Counter(phrase)


print(generate_phrase("aabbccc", "cbacba")) #should be false
print(generate_phrase("abc def ghi jkl", "abcdefg   hijkl")) #should be True
print(generate_phrase("cfg is fun", "funcgf is ")) #should be True
print(generate_phrase("   ", "  ")) #3 white spaces vs 2 white spaces
print(generate_phrase("   ", "   ")) #3 white spaces vs 3 white spaces