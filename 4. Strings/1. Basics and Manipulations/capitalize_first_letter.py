string = "mo shayan ul haque"
words = string.split()
ans = []
for i in range(len(words)):
    ans.append(words[i].capitalize())
    if i < len(words)-1:
        ans.append(" ")
print("".join(ans))
