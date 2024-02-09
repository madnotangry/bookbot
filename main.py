#!/usr/bin/python3

def get_book_text(book_path):
  with open(book_path) as f:
    text = f.read()
    return text

def word_count(text):
  words = text.split()
  return len(words)

def char_count(text):
  letters = {}
  for letter in text:
    if letter.isalpha():
      letter = letter.lower()
      if letter in letters:
        letters[letter] += 1
      else:
        letters[letter] = 1
  return letters

def sort_on(dict):
  return dict["num"]

def main():
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  # print(text)

  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count(text)} words found in the document\n")

  chars = char_count(text)
  sorted_chars = sorted(chars.items(), key=lambda x:x[1], reverse=True)
  for char_num in sorted_chars:
    print(f"The '{char_num[0]}' character was found {char_num[1]} times")

  print("--- End report ---")
main()
