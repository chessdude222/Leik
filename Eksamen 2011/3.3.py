def dict2list(colors):
    list = []
    for key in colors:
        for n in range(colors[key]):
            list.append(key)
    return list

colors = {'red': 3, 'yellow': 1, 'purple': 2}
print(dict2list(colors))
