📊 Wikipedia Word Frequency Analyzer

This Python script analyzes the most frequent non-stopwords in a live Wikipedia article and exports the results to a CSV file.
🚀 Features

    Scrapes and parses a live Wikipedia page

    Cleans and tokenizes article text

    Filters out common English stopwords

    Counts and ranks word frequency

    Exports results to a .csv file

    Fully command-line customizable

📦 Requirements

    Python 3.x

    requests

    beautifulsoup4

Install requirements:

pip install requests beautifulsoup4

🧠 Usage

python word_frequency.py --url "https://en.wikipedia.org/wiki/Python_(programming_language)" --top 15 --output python_words.csv

Arguments:
Flag	Description	Required	Default
--url	URL of the Wikipedia page to analyze	✅	—
--top	Number of top words to display	❌	10
--output	Filename for the output CSV	❌	word_freq.csv
📁 Output

Creates a CSV file with the most common words and their frequencies:

Word,Frequency
python,42
language,30
programming,25
...

✨ Example

python word_frequency.py --url "https://en.wikipedia.org/wiki/Artificial_intelligence" --top 20

Outputs:

    Top 20 words printed in the terminal (optional)

    CSV saved to word_freq.csv
