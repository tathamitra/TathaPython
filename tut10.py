d2 = {"Tathagata": "chicken", "mark": "burger", "micheal": "pizza", "trotskey": "vodka", "khilji": "kebab"}

print(d2)
print(d2["micheal"])
print(d2.get("micheal"))

d2["420"] = "kebab"
d2.update({"leena": "toffee"})

print (d2)
del(d2["420"])


print(d2)
print(d2.keys())
print(d2.items())


d3=d2.copy()