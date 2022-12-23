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

### Step 1: Preprocessing

- Filter for leading actors and add column for gender

We filter for leading actors based on imdb's principals data which contains for each movie the most important people (i. e. actors, actress, directors etc.). The importance is given by imdb and stored in the 'ordering' column



- Add column for age of actor during start of movie

- Add column for imdb ratings

- Add column for number of movies an actor has been in before start of respective movie


- Filter out movies from unwanted movie genres = ["Animation", "Biography", "Documentary","Short"]
    - Animation - Only voice actors meanning that casting is heavily dictated by voice and language
    - Biography, Documentary - Heavily dependent on the subject
    - Short - We aim to study larger scale movies
- Study the genre density of the movie dataset
- Calculate the experience of actors per genre at the time of each movie release

### Step 2: Genre Analysis
- Feature engineering

- Genre pattern evaluation.

- Correlation matrix of the background of actors (i.e., experience in each genre) to the genre of the movie he was filming.



### Step 3: Analysis of the actor's features over time



A confounder to consider: Actor experience and audience preference

- The preferences of moviegoers can change over time. What may have been popular in one era may not be as popular in another. It’s important to consider how audience preferences may have changed over the different time periods we are analyzing. So let's see what we can find. We will divide our data into subgroups that depend on time periods (think baby boomer era vs gen Z era for example) to reduce the impact of the previously considered confounders; movies in the same time-period are much more likely to be made using similar technology and during comparable economic conditions. We can see how audience preference shifts through time by seeing how the top movies genres vary through time and which genres did actors gain most experience in

      Greatest Generation (born circa 1901 to 1924)
      Silent Generation (circa 1925 to 1945)
      Baby Boomers (circa 1946 to 1964)
      Generation X (circa 1965 to 1985)
      Millennial Generation (circa 1985 to 1996)
      Gen Z (post-Millennial) (circa 1997 to 2012)


- Visualise actor feature change over generations for each genre

    Since weighting the average with any success metrics does not really matter, we are not considering a movie success metric for the following visuals. This means that we cannot say that those are the profiles of successfull actors.

- Find average actor movie experience over the years

- Do more experienced actors/actresses tend to star in certain genres more frequently?

- We generate the per genre movie experience distribution of the top 1000 actors per generation in 3 different cases:
    - Only look at male actors
    - Only look at female actors
    - Combine both




### Step 4: Do Popular Actors stick to their best genres in the recent scenario?

From here one we only look at the latest generation (which concerns us)

- calculate the diversity in an Actor's genre background from past movies using entropy
  - Using shannons entropy H which returns 0 if an actor has only been part of 1 genre, and highest value = 2.32 (log_2(5)) for a uniform distriubiton. [ Since we are using 5 major genres to construct the major genre vector]

- Use the number of votes to decide the IMDB rating of their past movies as a metric of popularity



## Organization within the team
Arvind: datastory,

... (5 lines left)

Collapse
message.txt6 KB
﻿

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

### Step 1

- Filter for leading actors and add column for gender

We filter for leading actors based on imdb's principals data which contains for each movie the most important people (i. e. actors, actress, directors etc.). The importance is given by imdb and stored in the 'ordering' column



- Add column for age of actor during start of movie

- Add column for imdb ratings

- Add column for number of movies an actor has been in before start of respective movie


- Filter out movies from unwanted movie genres = ["Animation", "Biography", "Documentary","Short"]
    - Animation - Only voice actors meanning that casting is heavily dictated by voice and language
    - Biography, Documentary - Heavily dependent on the subject
    - Short - We aim to study larger scale movies
- Study the genre density of the movie dataset
- Calculate the experience of actors per genre at the time of each movie release

### Step 2
- Feature engineering

- Genre pattern evaluation.

- Correlation matrix of the background of actors (i.e., experience in each genre) to the genre of the movie he was filming.



### Step 3: Analysis of the actor's features over time



A confounder to consider: Actor experience and audience preference

- The preferences of moviegoers can change over time. What may have been popular in one era may not be as popular in another. It’s important to consider how audience preferences may have changed over the different time periods we are analyzing. So let's see what we can find. We will divide our data into subgroups that depend on time periods (think baby boomer era vs gen Z era for example) to reduce the impact of the previously considered confounders; movies in the same time-period are much more likely to be made using similar technology and during comparable economic conditions. We can see how audience preference shifts through time by seeing how the top movies genres vary through time and which genres did actors gain most experience in

      Greatest Generation (born circa 1901 to 1924)
      Silent Generation (circa 1925 to 1945)
      Baby Boomers (circa 1946 to 1964)
      Generation X (circa 1965 to 1985)
      Millennial Generation (circa 1985 to 1996)
      Gen Z (post-Millennial) (circa 1997 to 2012)


- Visualise actor feature change over generations for each genre

    Since weighting the average with any success metrics does not really matter, we are not considering a movie success metric for the following visuals. This means that we cannot say that those are the profiles of successfull actors.

- Find average actor movie experience over the years

- Do more experienced actors/actresses tend to star in certain genres more frequently?

- We generate the per genre movie experience distribution of the top 1000 actors per generation in 3 different cases:
    - Only look at male actors
    - Only look at female actors
    - Combine both




### Step 4: Do Popular Actors stick to their best genres in the recent scenario?

From here one we only look at the latest generation (which concerns us)

- calculate the diversity in an Actor's genre background from past movies using entropy
  - Using shannons entropy H which returns 0 if an actor has only been part of 1 genre, and highest value = 2.32 (log_2(5)) for a uniform distriubiton. [ Since we are using 5 major genres to construct the major genre vector]

- Use the number of votes to decide the IMDB rating of their past movies as a metric of popularity



## Organization within the team
Arvind: datastory,

Johnny: exploratory data analysis, finding trends inter- and intra-generations.

Sid: trends through time,

Hao: correlation analysis,
