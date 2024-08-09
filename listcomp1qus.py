words = ["apple", "banana", "cherry", "date", "fig", "grape","kiwi"]


lengths_without_e = [len(word) for word in words if 'e' not in word]


print(lengths_without_e)
