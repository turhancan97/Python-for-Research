#Introduction to Language Processing
#Counting Words

text = "This is my test text. We're keeping this text short to test"

def count_word(text):
    text = text.lower()
    word_counts = {}
    skips = [".",",",":",";","'",'"']
    for ch in skips:
        text =text.replace(ch,"")
    for word in text.split(" "):
        #known word
        if word in word_counts:
            word_counts[word] += 1
        #unknown word
        else:
            word_counts[word]=1
    return word_counts

from collections import Counter

def count_word_fast(text):
    text = text.lower()
    word_counts = {}
    skips = [".",",",":",";","'",'"']
    for ch in skips:
        text =text.replace(ch,"")
    word_counts = Counter(text.split(" "))
    return word_counts

print(count_word(text)==count_word_fast(text))

#Reading in a Book
def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path,"r",encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

text = read_book(".\Books_EngFr\English\shakespeare\Romeo and Juliet.txt")
print(len(text))
ind = text.find("What's in a name")
print(ind)
sample_text = text[ind: ind+100]
print(sample_text)

#Computing Word Frequency Statistics
def word_stats(word_counts):
     """
     Return number of unique words and word frequency
     """
     num_unique = len(word_counts)
     counts = word_counts.values()
     return (num_unique,counts)
 
text = read_book(".\Books_EngFr\English\shakespeare\Romeo and Juliet.txt")
word_counts = count_word(text)
(num_unique,counts) = word_stats(word_counts)
print(num_unique)
print(sum(counts))

text = read_book(".\Books_GerPort\German\shakespeare\Romeo und Julia.txt")
word_counts = count_word(text)
(num_unique,counts) = word_stats(word_counts)
print(num_unique)
print(sum(counts))

#Reading Multiple Files

import os
book_dir = "./Books_EngFr"
import pandas as pd
stats = pd.DataFrame(columns = ("language","author","title","length","unique"))
title_num = 1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language ):
        for title in os.listdir(book_dir + "/" + language + "/" + author ):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique,counts) = word_stats(count_word(text))
            stats.loc[title_num] = language,author.capitalize(),title.replace(".txt",""),sum(counts),num_unique
            title_num += 1
            
print(stats)
stats.head()
stats.tail()

# Plotting Book Statistics
import matplotlib.pyplot as plt
plt.plot(stats.length,stats.unique,"bo")
plt.loglog(stats.length,stats.unique,"bo")
plt.figure(figsize = (10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length,subset.unique,"o",label="English",color="crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length,subset.unique,"o",label="French",color="forestgreen")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
