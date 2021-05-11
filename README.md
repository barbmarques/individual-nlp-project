<a name="top"></a>![Natural Language Processing](https://github.com/barbmarques/individual-nlp-project/blob/main/nlpbanner.png?raw=true)

***
[[Project Summary](#project-summary)]
[[Project Deliverables](#deliverables)]
[[Initial Questions](#hypotheses)]
[[Project Plan](#plan)]
[[Findings & Takeaways](#findings)]
[[Data Dictionary](#dd)]
[[Reproduce My Findings](#reproduce)]
___
## <a name="project-summary"></a>
#### <font color = 'darkblue'>Project Summary:

I was tasked with scraping data from GitHub repository README files in repositories that reference cybersecurity. The goal was to understand what programming languages are being actively used by those working in cybersecurity positions. I built a model to predict which programming language is primarily used in a repository, given the text of the README file.

Data Source: 470 GitHub Repositories that reference cybersecurity in their title.

All files referenced in this presentation are available in the github repository for this project:   https://github.com/barbmarques/individual-nlp-project.

## <a name="deliverables"></a>
#### <font color = 'darkblue'>Project Deliverables:
- A model to predict which programming language is primarily used in a repository, given the text of the README file.
- A slide deck presentation that demonstrates the model and my findings based on same.

## <a name="hypotheses"></a>
#### <font color = 'darkblue'>Initial Questions: 
- Can the use of certain words in the text of a README file be used to accurately predict the primary language used in the repository?
- Which programming languages are most commonly used in GitHubs of users in the Cybersecurity field?
- What words are the most commonly used to describe projects for the various programming languages?

## <a name="plan"></a>
#### <font color = 'darkblue'>Project Plan: 
``` PLAN -> ACQUIRE -> PREPARE -> EXPLORE -> MODEL -> DELIVER ```

Each step in the process is recorded and staged on a Trello board at: https://trello.com/b/aiTU7TYX

```Plan:```
- Set up GitHub repo, readme, env.
- Brainstorm a list of questions and form hypotheses about how variables might impact one another. 

```Acquire:```
- Create function to scrape readme text from GitHub Repositories.

```Prepare:```
- Carefully reviewed data, identifying any missing, erroneous, or invalid values. 
- Explored value counts of the dataframe and visualized distribution of univariate data 

```Explore:```
- Visualize all combination of variables to explore relationships.
- Tested for independent variables that correlate with tax value.
- Created a module, ```explore.py```, which stores code for functions to explore data.
- Developed hypotheses and ran statistical tests: t-test and correlation, to accept or reject null hypotheses.
- Summarized takeaways and conclusions.

```Model:``` 
- Developed a baseline model.
- Developed three classification models, identifying the one model that performs better against the baseline using the train and validation data.
- Evaluate the test data set on the best performing model
- Documented evaluation metrics and takeaways.

```Deliver:```
- Document evaluation and takeaways.
- Deliver slide deck for presentation and Jupyter Notebook containing all preparation, exploration and modeling.
     
## <a name="findings"></a>
#### <font color = 'darkblue'>Findings & Takeaways:
- Of the 240 GitHub README files that were analyzed, I found the majority used Python as the primary language (followed by Jupyter Notebook and then HTML). 
- Using a K-Nearest Neighbors model on out-of-sample test data, I was able to predict the primary language of a repository with an accuracy of 49%.
- This beats baseline performance of 42%.

## <a name="dd"></a>
#### <font color = 'darkblue'>Data Dictionary of Variables Used in Analysis

| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| **language**| The primary programming language that is represented in the given repository. This value was scraped from each repositories GitHub page. For modeling purposes, only the top six languages were considered. (Python, Jupyter Notebook, HTML, Java, Shell and JavaScript. | object|
|repo| The name of the GitHub repository whose README text was analyzed. | object |
|readme_contents| The text of the readme file that was scraped from the GitHub repository| object |

## <a name="reproduce"></a>
#### <font color = 'darkblue'>Instructions for Reproducing My Findings:

1.  Start by cloning the github repository on your From your terminal command line, type git clone git@github.com:barbmarques/individual-nlp-project.git

2.  You will also need you a copy of your personal env file in your working directory. This should contain your GitHub access information (host, user, password) 

3. Run the Jupyter notebook, Final_Notebook, cell by cell, to reproduce my analysis.
