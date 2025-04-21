# 🚀 Advanced Word Counter Mini Project

# 👉 Create a simple Python program that takes a paragraph or sentence from the user, and tells how many words are in it.

# ✅ Step 1: Take input from the user
text = input("Enter your paragraph or sentence: ")

# ✅ Step 2: Split the text into words
words = text.split()
word_count = len(words)

# Step 3: Character count
char_with_spaces = len(text)
char_without_spaces = len(text.replace(" ", ""))

# Step 4: Sentence count (splitting using '.', '!', '?')
import re
sentence = re.split(r'[.!?]+', text)
sentence = [s.strip() for s in sentence if s.strip() != '']
sentence_count = len(sentence)

# Step 5: Average words per sentence
average_words = word_count / sentence_count if sentence_count != 0 else 0

# Step 6: Most frequent word (optional bonus)
from collections import Counter
word_frequency = Counter(words)
most_common = word_frequency.most_common(1)[0] # Gives (word, count)

# Step 7: Unique words
unique_words = set(words)

# Step 8: Final output
print("\n📊 TEXT ANALYSIS")
print(f'total words: {word_count}')
print(f'🔠 Characters (with spaces): {char_with_spaces}')
print(f'🔡 Characters (without spaces): {char_without_spaces}')
print(f'📙 Total Sentences: {sentence_count}')
print(f'📏 Average Words per Sentence: {average_words:.2f}')
print(f"🔥 Most Frequent Word: '{most_common[0]}' (used {most_common[1]} times)")
print(f"🧠 Unique Words: {', '.join(unique_words)}")

