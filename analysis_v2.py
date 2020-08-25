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

years = [2016, 2017, 2018, 2019, 2020]

mensWords = []
womensWords = []

mensQuestions = []
womensQuestions = []
mensPerplexity = []
womensPerplexity = []
for year in years:
    mensQuestionCount = 0
    womensQuestionCount = 0
    # mens words
    f = open("./data/%s/mens_ints2.txt" % str(year), "r")
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

    print(str(year) + " mens question count: " + str(mensQuestionCount))

    # womens words
    f = open("./data/%s/womens_ints2.txt" % year, "r")
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

    # sorted_words = sorted(womensWordCount.items(),
    #                       key=lambda x: x[1], reverse=True)

    # for i in sorted_words[0:20]:
    #     print(i[0] + ": " + str(i[1]))
    print(str(year) + " womens question count: " + str(womensQuestionCount))

    # totalPerplexity = 0
    # count = 0
    # mensPerplexities = []
    # womensPerplexities = []
    # model = kenlm.LanguageModel('yourLM.klm')

    # for question in womensQuestions[0:len(mensQuestions)]:
    #     totalPerplexity = totalPerplexity + model.perplexity(question)
    #     count = count + 1
    #     womensPerplexities.append(model.perplexity(question))

    # womensPerplexity.append(totalPerplexity/count)

    # totalPerplexity = 0
    # count = 0

    # for question in mensQuestions:
    #     totalPerplexity = totalPerplexity + model.perplexity(question)
    #     count = count + 1
    #     mensPerplexities.append(model.perplexity(question))

    # mensPerplexity.append(totalPerplexity/count)

    # statistic, pvalue = scipy.stats.mannwhitneyu(
    #     womensPerplexities, mensPerplexities, alternative='greater')
    # print(statistic)
    # print(pvalue)
    # if pvalue < 0.05:
    #     print("The p-value of " + str(pvalue) +
    #           " is statistically significant at p < .05.")

# plt.plot(years, womensPerplexity, label="Women's")
# plt.plot(years, mensPerplexity, alpha=0.5, label="Men's")
# plt.legend()
# plt.show()


totalPerplexity = 0
count1 = 0
mensPerplexities = []
womensPerplexities = []
model = kenlm.LanguageModel('yourLM.klm')

for question in womensQuestions:
    totalPerplexity = totalPerplexity + model.perplexity(question)
    count1 = count1 + 1
    womensPerplexities.append(model.perplexity(question))

womensPerplexity = (totalPerplexity/count1)

totalPerplexity = 0
count2 = 0

for question in mensQuestions:
    totalPerplexity = totalPerplexity + model.perplexity(question)
    count2 = count2 + 1
    mensPerplexities.append(model.perplexity(question))

print("Total womens question count: " + str(count1))
print("Total mens question count: " + str(count2))

mensPerplexity = (totalPerplexity/count2)
statistic, pvalue = scipy.stats.mannwhitneyu(
    womensPerplexities, mensPerplexities, alternative='greater')
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
