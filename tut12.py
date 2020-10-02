#for loops
#
# l1 = ["jack", "jill", "mark", "paul"]
#
# for name in l1:
#     print(name)


# l1 = [["jack", 1], ["jill", 2], ["mark", 7], ["paul", 9]]
#
# for name, wife in l1:
#     print(name, "number of wives", wife)
#
# d1 = dict(l1)
# for name in d1:
#     print(name)
# for name, wives in d1.items():
#     print(name, "number of wives", wives)

l1 = [1, 2, "jack", "jill", 7, 11]

for item in l1:
    if str(item).isnumeric() and item > 6:
        print(item)


