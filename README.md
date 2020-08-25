# cbb-nlp
## NLP project based on College Basketball media coverage

#### Introduction

This post was inspired by a paper called “Tie-breaker: Using language models to quantify gender bias in sports journalism” which used a data-driven approach to quantify gender discrepancies in tennis press-conferences. Before that paper, scholarship on gender bias in sports has found that commentators relied on a “focus on personalities as opposed to athletic abilities” when covering women’s sports (Higgs & Weiller, 1994), and an analysis of sportscasting on major networks and newspapers found a “very high degree of embedded favoritism” towards men’s sports (Eastman & Billings, 2000). However, these investigations did not rely on data-driven approaches to quantifying the gender bias found. In this post, a similar language-model-based approach to the one used in “Tie-breaker” is used. Gender bias is quantified with respect to a language model based on game commentary. 

#### Dataset Description

College basketball press-conference transcripts are collected from ASAP Sport’s website (http://asapsports.com/). For this study, post-game and pregame interviews are collected for games played between 2016 and 2020. This gives a dataset of a total of 17085 question snippets, 8669 of which are posed to men’s basketball players/coaches and 8416 of which are posed to women’s basketball players/coaches. To land on this number, I collected all questions from all available postseason tournaments between 2016 and 2020, while making sure there was not a significant difference between the size of the two groups. 
	
To model basketball game-specific language, commentary transcripts are collected from YouTube’s automatic transcription service (http://youtube.com/). Each commentary transcript contains a full game’s worth of commentary. Here is a sample, taken from the Oregon-Baylor women’s Final Four matchup (https://www.youtube.com/watch?v=MqIGIGnHS4E). 

>*“...remember in women's college basketball we have the time out advance so there's gonna be a lot of time for Oregon **the** draw plays and certainly with the plethora of three-point shooters on their roster the Ducks aren't out of this one”*

Bolded is an error made by the automatic transcription service. The word “the” was actually spoken as the word “to”. Using an automatic transcription service will result in errors like this; however, due to the lack of basketball commentary transcripts publicly available, the automatic transcription was the only option. For the game-specific language model, a gender-balanced set of commentary transcripts is collected for 14 games played. The low amount of games used is due to a lack of availability of full games on YouTube. 

#### Exploratory Data Analysis

As exploratory data analysis, a word-level analysis is applied to quantify differences in word usage between journalists’ interviews of men’s and women’s basketball players/coaches. For each word w, the usage count is considered within men’s and women’s basketball players/coaches. Words with the greatest difference in usage between men’s and women’s players/coaches are considered. Preliminary analysis of word usage differences does not show a difference in game-relatedness between men’s and women’s players/coaches. The words with the highest differences in usage are listed below in descending order of usage difference: 

**Men’s:** second, half, tournament, zone, coach, and, like, zone

**Women’s:** game, third, said, really, fourth, how, final, four

#### Methodology

The gender-balanced set of commentary transcripts is used to train a bigram language model using KenLM. KenLM uses the modified Kneser-Ney smoothing method. This model will be used to quantify how game-related a question is. 
For a question q, its perplexity is measured with respect to the game-specific language model Pcommentary. This perplexity measure shows how game-related a question is: a higher perplexity measure suggest the question is less game-related. Perplexity is a standard measure of language-model fit. For an n-word sequence w1w2 … wn perplexity is calculated as follows:

Sample questions of low-perplexity and high-perplexity values are provided:

Perplexity: Low
Score: 76.83
Question: *FDU is one of the best three-point shooting teams in the country. What was your game plan to stop their three-point shooting?*

Perplexity: High
Score: 940.03
Question: *What is your background as far as your mother played sports here?*

#### Results

Perplexities for each question are computed and then grouped by the gender of the athletes: male coaches of women’s basketball teams fall under the women’s category. The Mann-Whitney U statistical significance test is used. After testing perplexity values between the two groups, it is found that the mean perplexity of questions posed to women’s basketball players/coaches is significantly larger (p-value = 0.0299) than the mean perplexity of questions posed to men’s basketball players/coaches. These findings suggest that the questions posed to men’s basketball players/coaches are more game-related than the questions posed to women’s basketball players/coaches. 

##### Works Cited: 

###### Teh, Y. W. (2006). A Bayesian Interpretation of Interpolated Kneser-Ney NUS School of Computing Technical Report TRA2/06. National University of Singapore.

###### Higgs, C. T., & Weiller, K. H. (1994). GENDER BIAS AND THE 1992 SUMMER OLYMPIC GAMES: AN ANALYSIS OF TELEVISION COVERAGE. Journal of Sport and Social Issues, 18(3), 234–246. doi: 10.1177/019372394018003004 

###### Eastman, S. T., & Billings, A. C. (2000). Sportscasting and Sports Reporting: The Power of Gender Bias. Journal of Sport and Social Issues, 24(2), 192–213. doi: 10.1177/0193723500242006

###### Fu, L., Danescu-Niculescu-Mizil, C., & Lee, L. (2016). Tie-breaker: Using language models to quantify gender bias in sports journalism. arXiv preprint arXiv:1607.03895.
