# The acting industry through the ages: Comparing successful actor profiles from different generations

## Data Story

Please visit our website [here!](https://arvind6599.github.io/datastory/)

## Abstract

All actors and movie directors have their own motivation to work hard and achieve success. Gaining valuable insight into factors that contribute to a movie's success and an actor's career skyrocketing can thus aid people in the industry to make casting decisions.
We will explore the relationship between actor/actress experience and movie success/popularity with goals of forming a descriptive analysis of actor-feature data to summarize and compare successful actor profiles from different generations. We will also be looking at potential trends through time and extract meaningful information.

## Tackled research question

- What are the main factors that guide the audience towards making a binary decision regarding movies?
  - We look at the movie genre
  - And the leading actors that make up the cast

## Datasets
We use the IMDB movie and actor datasets which can be found [here](https://datasets.imdbws.com/). Make sure to create and place them in your `data/` folder if you wish to rerun the code. We also supplement it with some additional data from [Kaggle](https://www.kaggle.com/datasets/PromptCloudHQ/imdb-data?resource=download).


## Methodology

### Step 1: Data Preprocessing
The initial datasets are quite substantial but were chopped up into pieces (one only contained movie ratings, another just actor information, and another just movie names and genres). So we first had to merge them together (all datasets with movie information were merged into one, and those with actor information into one).
The next step was to clean up all invalid rows, being those which had missing important information, such as the release date or genre of the movie, or the birth date of the actor.
We could now finally combine our movie and actor dataset into one, where each row was a combination of a movie and a leading actor that played in it. This netted us about 1 million rows

### Step 2: Data Exploration




## Organization within the team
Arvind: datastory,

Johnny: exploratory data analysis, finding trends inter- and intra-generations.

Sid: trends through time,

Hao: correlation analysis,