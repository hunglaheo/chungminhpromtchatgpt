import json
with open('listCauhoi.json', 'r',encoding='utf8') as f:
    data=json.loads(f.readline())
counter = {}
for item in data:
    hashable_dict = frozenset(item.items())
    if hashable_dict not in counter:
        counter[hashable_dict] = 1
    else:
        counter[hashable_dict] += 1

duplicates = [dict(item) for item in counter if counter[item] > 1]
print(duplicates) # Output: [{"id": 1, "name": "Alice"}]