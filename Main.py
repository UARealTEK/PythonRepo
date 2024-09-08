def reverse(lst):
    index = len(lst) -1
    out = list()

    while index >= 0:
        out.append(lst[index])
        index -= 1
    return out

test = [1,2,3]
print(reverse(test))