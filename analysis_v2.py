# Title Comment
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import word_tokenize
import time
import math
import kenlm
import scipy

stop_words = set(stopwords.words('english'))

year = 2019
mensQuestionCount = 0
womensQuestionCount = 0
mensWords = []
womensWords = []
mensQuestions = []
womensQuestions = []

# mens words
f = open("./data/%s/mens_ints.txt" % year, "r")
questionsWithStopWords = []
for line in f:
    if(line[0] == "Q"):
        questionsWithStopWords.append(line)
        mensQuestions.append(line)
        mensQuestionCount = mensQuestionCount + 1
for question in questionsWithStopWords:
    word_tokens = word_tokenize(question)
    for w in word_tokens:
        if w not in stop_words and w != "Q" and w != "Q." and w != "'" and w != "," and w != "." and w != "?" and w != "'s" and w != "'ve" and w != "n't":
            mensWords.append(w)


mensWords.sort()
mensWordCount = {}
lastWord = mensWords[0]
count = 1

for word in mensWords:
    if lastWord == word:
        count = count+1
    else:
        mensWordCount.update({lastWord: count})
        count = 1
    lastWord = word

print("Mens question count: " + str(mensQuestionCount))

# womens words
f = open("./data/%s/womens_ints.txt" % year, "r")
questionsWithStopWords = []
for line in f:
    if(line[0] == "Q"):
        questionsWithStopWords.append(line)
        womensQuestions.append(line)
        womensQuestionCount = mensQuestionCount + 1
for question in questionsWithStopWords:
    word_tokens = word_tokenize(question)
    for w in word_tokens:
        if w not in stop_words and w != "Q" and w != "Q." and w != "'" and w != "," and w != "." and w != "?" and w != "'s" and w != "'ve" and w != "n't":
            womensWords.append(w)


womensWords.sort()
womensWordCount = {}
lastWord = womensWords[0]
count = 1

for word in womensWords:
    if lastWord == word:
        count = count+1
    else:
        womensWordCount.update({lastWord: count})
        count = 1
    lastWord = word


print("Womens question count: " + str(womensQuestionCount))


totalPerplexity = 0
count = 0
mensPerplexities = []
womensPerplexities = []
model = kenlm.LanguageModel('yourLM.klm')

for question in womensQuestions:
    totalPerplexity = totalPerplexity + model.perplexity(question)
    count = count + 1
    womensPerplexities.append(model.perplexity(question))

womensPerplexity = (totalPerplexity/count)

totalPerplexity = 0
count = 0

for question in mensQuestions:
    totalPerplexity = totalPerplexity + model.perplexity(question)
    count = count + 1
    mensPerplexities.append(model.perplexity(question))


mensPerplexity = (totalPerplexity/count)
statistic, pvalue = scipy.stats.mannwhitneyu(
    womensPerplexities, mensPerplexities)
print(statistic)
print(pvalue)
if pvalue < 0.05:
    print("The p-value of " + str(pvalue) +
          " is statistically significant at p < .05.")
sexes = ("Mens", "Womens")
y_pos = np.arange(len(sexes))
perplexities = [mensPerplexity, womensPerplexity]
print(perplexities)
plt.bar(y_pos, perplexities, align='center', alpha=0.5)
plt.xticks(y_pos, sexes)
plt.ylabel('Perplexity')
plt.title('Average Perplexity per Question')

plt.show()
