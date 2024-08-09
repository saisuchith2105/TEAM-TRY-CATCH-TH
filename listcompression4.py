import re
from collections import defaultdict
 
merge_similar_keys = lambda d: {
    k: [item for key, value in d.items() if re.sub(r'\W+', '', key) == k for item in value]
    for k in set(re.sub(r'\W+', '', k) for k in d.keys())
}
d = {'hello-world': [1, 2, 3], 'hello_universe': [4, 5, 6], 'foo-bar': [7, 8, 9], 'foo_baz': [10, 11, 12]}
result = merge_similar_keys(d)
print(result)
