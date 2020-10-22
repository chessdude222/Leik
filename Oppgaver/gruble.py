L_1 = [27, 19, 20, 90]
L_2 = [0, 1, 1, 0]
#new_list = [L_1[i]*L_2[i] for i in range(len(L_1))]
new_list = []
for i in range(len(L_1)):
    if L_2[i] == 1:
        new_list.append(L_1[i])
    else:
        new_list.append(L_1[i]*0)
print(new_list)
