# term_frequency

A simple script that extracts the most common terms from a .txt file, excluding stopwords, based on the language specified by the user. It utilizes natural language processing techniques to tokenize the text, remove stopwords, and calculate the frequency of the remaining words. It outputs a list of the most frequent terms and their counts to a new .txt file.

## Requirements

- Python 3
- tkinter library (for file dialog and user interaction)
- nltk library (for text processing)
    * punkt and punkt_tab (for tokenizing the text)
    * stopwords (for filtering out common stopwords)

## Usage

Run extract_frequent_terms.py

A file dialog will open where the input .txt is selected.

The script will ask in the console for the language of the text and the number of terms to be extracted and counted.

After processing, a new .txt file is created with a list of the terms and their frequencies.
