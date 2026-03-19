word1 = "Ghananil"
word2 = "12344567876545"
joint_string = ""
lenth = max(len(word1), len(word2))

for i in range(lenth):
    if i < len(word1):
        joint_string += word1[i]
    else:
        joint_string += " "
    if i < len(word2):
        joint_string += word2[i]
    else:
        joint_string += " "

print(joint_string)