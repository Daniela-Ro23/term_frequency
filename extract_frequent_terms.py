import tkinter as tk
from tkinter import filedialog
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist

# Download necessary NTLK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Open file explorer for the user to select a .txt file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

# Read the text from the selected file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Ask the user for the language of the text and the number of common words to extract
language = input("Enter the language of the text (e.g., 'english', 'french', 'spanish'): ")
num_words = int(input("Enter the number of common words to extract: "))

# Tokenize the text
tokens = word_tokenize(text.lower())

# Filter out non-alphabetic words
filtered_tokens = [w for w in tokens if w.isalpha()]

# Remove stopwords
stop_words = set(stopwords.words(language))
filtered_tokens = [w for w in filtered_tokens if not w in stop_words]

# Get the frequency distribution
freq_dist = FreqDist(filtered_tokens)

# Get the most common words
common_words = dict(freq_dist.most_common(num_words))

# Filter out non-alphabetic words from the common words
common_words = {word: freq for word, freq in common_words.items() if word.isalpha()}

# Write the common words to a new .txt file (saved in same directory as input .txt)
output_file_path = file_path.rsplit('.', 1)[0] + '_common_terms.txt'
with open(output_file_path, 'w') as file:
    for word, freq in common_words.items():
        file.write(f"{word}: {freq}\n")

# Print the most common words
print("The most common words have been written to", output_file_path)
for word, freq in common_words.items():
    print(f"{word}: {freq}")