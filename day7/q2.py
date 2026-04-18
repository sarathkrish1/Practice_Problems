colors = ['Red', 'Green', 'Pink', 'Blue', 'Black', 'Purple', 'Yellow', 'Magenta', 'Brown']

remove_idx = [0, 2, 5]
revised_colors = []

for i in range(len(colors)):
    if i not in remove_idx:
        revised_colors.append(colors[i])

print("Colors List :", colors)
print("List After Removing Particular Elements :", revised_colors)