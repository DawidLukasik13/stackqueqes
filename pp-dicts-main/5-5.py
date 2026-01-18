paragraph = "cat dog mouse cat rat cat mouse"

counts = {}
for word in paragraph.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
