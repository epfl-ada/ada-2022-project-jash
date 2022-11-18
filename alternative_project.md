# Analysing the impact of actors' features on the success of movies
## Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
- Project Goals
    1. Interactive tool for predicting influence of any actor's age, gender, height and nationality on the success of a movie (considering different success metrics; e. g. revenue, imdb votes etc.) in order to minimize risk for movie producers and investors. This tool will tell you, if you would be a good actor - or at least one that brings in the cash.
    2.  --> give recommendation to actors based on their personal features: age, gender, height, nationality and acting experience (= {beginner, intermediate, expert})
        1. which category is best for them based on their personal features
        2. which age is best to start in general and considering the movie category?
        3. which character type is best for actor (character type based on latent persona research)? 
        4. Do gender or ethnicity are hurdles or advantages for actors in the movie industry?

        - note: best means for an actor that he or she gets picked. An actors is only picked when they add value to the movie and said movie will have high return

## Research Questions: A list of research questions you would like to address during the project.
1. Do the features of actors (age, gender, height, nationality and acting experience) influence the success of a movie?
2. How do actors' features (e. g. age, gender, height, nationality) change over-time for each movie category? And why so?
2. What are the features of the cast of the top 10 successful movies per year or decade? (success = highest grossing or highest rated on imdb)
3. What are the most common features of actors per movie category?


4. Which features (e. g. gender) make it harder to get into films? Is any movie category sexist (= only favouring one gender)?

## Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
1. wikidata scraping to get the missing nationality(~= ethnicity) of some actors 
2. imdb scraping to get the missing height values of some actors

## Methods
1. analyse and visualise how ever feature of an actor changes over-time in generel and per movie category
    - is there are significant change --> 
2. 

1. Potential methods to predict success of movie based on actor's features: linear regression, ....???
2. time series analysis
3. basic stats to summarize data
4. test theory to insure statisitcal significance of analysis results

## Proposed timeline
1. get all required/missing data about actors from wikipedia and imdb (to ideally extend the list of features)
2. get imdb movie ratings as another metric for success
3. check dependency of each feature of actors on success of movie
4. built ML model predicting success of movie based on actor's features
5. make interactive UI for ML model
6. tell data story with stats and appealingvisulisations
7. bring interactive ML model and data story together

## Organization within the team: A list of internal milestones up until project Milestone P3.
- parallelize 4.-5. and 6. of timeline

## Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
