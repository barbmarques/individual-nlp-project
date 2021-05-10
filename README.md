<a name="top"></a>
![Natural Language Processing](https://github.com/barbmarques/individual-nlp-project/blob/main/NLP.jpeg, raw=True)



<a id='navigation'></a>

[[Project Summary](#project-summary)]
[[Project Planning](#pipeline)]
[[Key Findings](#key-findings)]
[[Data Dictionary](#data-dictionary)]
[[Project Replication](#replication)]

___
<a name="project-summary"></a><h1><img src=""/></h1>

#### Project Summary:

I was assigned the task of scraping data from GitHub repository README files. The goal was to build a model that can accurately predict what programming language is primarily used in a repository, given the text of the README file.

Data Source: GitHub Repositories

All files referenced in this presentation are available in the github repository for this project:   https://github.com/barbmarques/individual-nlp-project.


#### Project Goals/Deliverables:
- Build a model that 

#### Initial Questions: 
- Can the use of certain words in the text of a README file be used to accurately predict the primary language used in the repository?



<a name="pipeline"></a><h1><img src=""/></h1>


#### Progression through the Data Science Pipeline: 
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
- Created and called a function, ```prep_zillow```, as a reproducible component that cleans/prepares data for analysis by: renames columns, handling missing values, adjusts data types, handles any data integrity
- Created and called a function, ```train_validate_test_split```, that splits the data into train, validate and test sets.
- Numeric data was scaled using MinMax scaler.
- Created a module ```wrangle_zillow.py``` which stores code for functions that acquire and prepare data.

```Explore:```
- Visualize all combination of variables to explore relationships.
- Tested for independent variables that correlate with tax value.
- Created a module, ```explore.py```, which stores code for functions to explore data.
- Developed hypotheses and ran statistical tests: t-test and correlation, to accept or reject null hypotheses.
- Summarized takeaways and conclusions.

```Model:``` 
- Developed a baseline model.
- Developed a regression model that performs better than the baseline
- Documented algorithms and hyperparameters used.
- Plotted the residuals and documented evaluation metrics (SSE, RMSE, or MSE).

```Deliver:```
- Clearly documented all code in a reproducible Jupyter notebook called Zillow_Regression_Project.
- Created a Google slide presentation that can be shared with Zillow management.

<a name="key-findings"></a><h1><img src=""/></h1>


<a name="data-dictionary"></a><h1><img src=""/></h1>
#### Data Dictionary of Variables Used in Analysis

| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| **language**| The 2017 total tax assessed value of the parcel | object|
|repo| The name of the GitHub repository whose README file was scraped | object |
|readme_contents| The text of the readme file that was scraped from the GitHub repository| object |


<a name="replication"></a><h1><img src=""/></h1>




#### Recommendation & Takeaways:

- Recommend using a Polynomial Regression Model (degree of 2) to predict home values based on bathroom count, age of home, square footage and zip code.
- Note: Scatterplot visualization demonstrates that our model tends to under-value homes that exceed the median tax value of ~$408,000.
- Primary Drivers of Tax Value include: square footage, bedroom and bathroom count, age of home, and zip code in which home is located.

#### Given more Time and Resources, I would:

- Fine tune feature engineering, perhaps combining some features, to increase accuracy.
- Since there was little difference in the RMSE for mean and median, I would re-run models using median as baseline. 
- Reconfigure many of my explorations and modeling code into functions, to clean up notebook and increase reproducibility of results.






#### Instructions for Reproducing My Findings:

1.  Start by cloning the github repository on your From your terminal command line, type git clone git@github.com:barbmarques/zillow-regression-project.git

2.  Download the following files from https://github.com/barbmarques/zillow-regression-project to your working directory:  
 - Zillow_Regression Project.ipynb
 - wrangle_zillow.py
 - explore.py
  
3.  You will also need you a copy of your personal env file in your working directory:
 - This should contain your access information (host, user, password) to access Codeup's database in MySQL

4. Run the Jupyter notebook, Zillow_Regression_Project, cell by cell, to reproduce my analysis.

4. To access the property value predictions in a csv format, download ```property_value_predictions
.csv```. 


