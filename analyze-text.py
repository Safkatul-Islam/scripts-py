def analyze_text(text):
    sentence_count = sum(1 for ch in text if ch in ".!?")

    cleaned_text = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in text.lower())
    words = cleaned_text.split()

    freq = {}
    longest_word = ""
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        if len(word) > len(longest_word):
            longest_word = word

    return {
        "word_count": len(words),
        "unique_words": len(freq),
        "most_frequent": max(freq, key=freq.get),
        "longest_word": longest_word,
        "sentence_count": sentence_count
    }


# Test
python_text = """Python is a beautiful language. It is simple, yet powerful!
Do you agree that Python is the best language for beginners?
Many experts say Python is great for data science and machine learning."""

result = analyze_text(python_text)
print(result)