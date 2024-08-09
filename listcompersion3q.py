names_and_ages = [("Alice", 20), ("Bob", 30), ("Eve", 28), ("Frank", 35), ("Gene", 22)]
 
filtered_names = [name for name, age in names_and_ages if age > 25 and 'e' not in name.lower()]
 
print(filtered_names)
