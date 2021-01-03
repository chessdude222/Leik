def find(text, args):

    result = {}

    for a in args:
        result[a] = 0
        for j in range(len(text)):
            if text[j:j+len(a)] == a:
                result[a] += 1
    return result

text = 'ababab'
args = ['ab', 'b', 'c']
print(find(text, args))
