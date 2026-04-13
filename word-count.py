def word_count(text):
    cleaned = text.lower().translate(str.maketrans("", "", ".,!?;:"))
    words = cleaned.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts

text = "The cat sat on the mat. The cat sat down on the mat!"
count= word_count(text)

sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
for word, count in sorted_items:
    print(f"{word}: {count}")

# -----------------------------------------------------------------------------------

# Literal way

def word_count(text):
    text = text.lower().replace('.', '').replace('!', '').replace(',', '')
    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

python_text = "The cat sat on the mat. The cat sat down on the mat!"
result = word_count(python_text)
for word, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}")