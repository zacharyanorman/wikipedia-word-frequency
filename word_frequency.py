from bs4.element import AttributeValueWithCharsetSubstitution
import requests
from bs4 import BeautifulSoup
import argparse
import csv


def save_to_csv(word_list, filename="word_freq.csv"):
  with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Word", "Frequency"])
    for word, count in word_list:
      writer.writerow([word, count])


def top_n_words(str, n):
  clean_str = str.lower()
  word_list = clean_str.split()
  clean_word_list = []
  words_dict = {}
  stopwords = {
      "a", "about", "above", "after", "again", "against", "all", "am", "an",
      "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
      "before", "being", "below", "between", "both", "but", "by", "can",
      "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does",
      "doesn't", "doing", "don't", "down", "during", "each", "few", "for",
      "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't",
      "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers",
      "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll",
      "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its",
      "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no",
      "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought",
      "our", "ours", "ourselves", "out", "over", "own", "same", "shan't",
      "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some",
      "such", "than", "that", "that's", "the", "their", "theirs", "them",
      "themselves", "then", "there", "there's", "these", "they", "they'd",
      "they'll", "they're", "they've", "this", "those", "through", "to", "too",
      "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
      "we're", "we've", "were", "weren't", "what", "what's", "when", "when's",
      "where", "where's", "which", "while", "who", "who's", "whom", "why",
      "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll",
      "you're", "you've", "your", "yours", "yourself", "yourselves"
  }

  for i in word_list:
    strip_word = i.strip('!-_=+,.?').lower()
    clean_word_list.append(strip_word)
  for word in clean_word_list:
    if word not in stopwords:
      counts = clean_word_list.count(word)
      words_dict[word] = counts
  sorted_items = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
  return sorted_items[0:n]


def main():
  parser = argparse.ArgumentParser(
      description="Analyze word frequency from a Wikipedia page")
  parser.add_argument('--url', type=str, required=True, help='URL to analyze')
  parser.add_argument('--top',
                      type=int,
                      default=10,
                      help='Number of top words to display (default: 10)')
  parser.add_argument('--output',
                      type=str,
                      default="word_freq.csv",
                      help='Output CSV file name (default: word_freq.csv)')
  args = parser.parse_args()

  response = requests.get(args.url)
  soup = BeautifulSoup(response.text, 'html.parser')
  paragraphs = soup.find_all('p')
  article_text = " ".join([p.get_text() for p in paragraphs])

  top_words = top_n_words(article_text, args.top)
  save_to_csv(top_words, filename=args.output)
  print("Results saved to word_freq.csv")


if __name__ == "__main__":
  main()
