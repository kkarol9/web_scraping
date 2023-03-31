import json
data = []
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
data.append({
    'title': a,
    'details': b,
    'surname': c,
    'first_name': d,
    'results': e,
    'score' : f 
 })

q = data

data2 = []
data2.append({
    'title': a,
    'details': b,
    'surname': data,

 })
print(data2)


with open('cwiczenie_slownik.json', 'w') as f:
    json.dump(data2, f)
