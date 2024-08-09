def pythagorean_triples(sides):
    triples = [(a, b, c) for a in sides for b in sides for c in sides if a <= b <= c]
    pythagorean_triples = list(filter(lambda x: x[0]**2 + x[1]**2 == x[2]**2, triples))
    unique_triples = list(map(tuple, set(map(lambda x: tuple(sorted(x)), pythagorean_triples))))
    return unique_triples
 
sides = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]
result = pythagorean_triples(sides)
print(result)  
has context menu
