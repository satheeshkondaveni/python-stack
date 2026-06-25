from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Dictionary where key = sorted letters, value = list of words
anagrams = defaultdict(list)
print('defaultdict', anagrams)

for word in words:
    key = ''.join(sorted(word))  # sort letters to form the key
    anagrams[key].append(word)

print('defaultdict==>', anagrams)
# Convert dictionary values to a list of lists
result = list(anagrams.values())

print(result)
