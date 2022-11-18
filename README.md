# What type of actor are you?
## Analysing the impact of actors' features on the success of movies
### Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
- Project Motivation:
  
    As avid media consumers and wanna-be movie stars, we kept wondering whether there existed some hidden elements that spring an actor’s career into a success. Could we also make it big? And if so, would we be Bruce Lee? Or Cinderella?
 
    In light of our noble cause, we will use data to break down genres and character profiles to better communicate what is the recipe for success for a good movie and a prolific actor career.
 
- Project Goal:

    We wish to study the relationship between actor profiles and movie genres and specifically study the progression of gender inclusivity for various genres. We propose to make an interactive tool that allows users to filter according to movie genre and display descriptive statistics to perform prescriptive analysis on what makes an ideal actor profile.
    Our analysis aims to break down the data pertaining to each movie genre to showcase its relation to actor features and subsequently compute an ideal actor profile for that specific genre. We start by computing statistics for each genre such as: 
    - Minimum and maximum values for age and height to convey the youngest, oldest, shortest and tallest actors
    - The count of male and female actors for each genre
    - Average movie revenue to signify the scale/popularity of the genre
 
    We then compute the ideal profile for an actor which validates the general audience's expectations and also considers reward with monetary success. We will be using a weighted mean on the continuous actor features to compute the ideal value of a feature along with its standard deviation. These weights will depend on success metrics such as movie revenue(scaled to account for inflation) and movie ratings based on availability.
 
    As a final component, we will try to create some interactive figures that will assign every combination of feature inputs to a certain character type. A user would select what features describe him best and would observe a distribution of the most likely character tropes he might belong to as an actor.
 
 
### Research Questions: A list of research questions you would like to address during the project.
1. Based on specific actor features values, are we able to determine the most likely TVTrope persona that the actor will fall into? We are thinking of some kind of soft clustering.

2. Do some features (e. g. gender) make it harder to get into specific film genres? Is any movie category dominated by a certain actor category?

3. What are the features of the cast of the top 10 successful movies per year or decade? (success = highest grossing or highest rated on IMDb)

4. How do actors’ ideal features (e. g. age, gender, height, nationality) change over time for each movie category? And why so?

5. What would the ideal actor look like (features-wise) per movie genre and/or character trope?
 
 
### Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
1. We wish to find the nationality of every actor; this allows us to more accurately define actor profiles. We scrape wikidata to get the missing nationality of some actors. It is simple to do so by following the `pywiki` library documentation.
   
2. Same idea as above, but this time with regard to height. We scrape IMDb to get the missing height values of some actors. As there are no nice libraries to do this, we rely on good old HTML scraping.
 
3. (Optional) Wikidata scraping to obtain movie budgets. It could help give a new dimension to movie profitability.
 
### Methods
Step 1: Data scraping, dataset preparation and pre-processing
- Scraping wikidata to get the missing nationality, height and movie budget data.
- Incorporate additional data into the existing dataset.
- Implement data cleansing and compute necessary features.

Step 2: General preliminary analysis using the CMU Corpus dataset.
- Compute Basic stats (min, max, mean, median etc.) for every feature per genre. Investigate the significance of every feature per genre and determine whether particular features that dominate the actor or movie category exists.

Step 3: To find the so-called ideal profile, we base ourselves on movie revenue and ratings and design a metric that balances the influence of movie revenue and ratings (upon availability).

Step 4: Implement correlation analysis. Study the relationship between the movie revenue/rating and actor features and use confidence interval and T-test to ensure statistical significance.

Step 5: Use clustering methods to determine what ideal actors may look like in each movie genre.

Step 6: Build the GitHub site and redact the data story.

 
 
### Proposed timeline
- Week 1: get all required/missing data about actors from Wikipedia and IMDb. Same for movie ratings.

- Week 2: design and code the metric that will define actor profiles

- Week 3: finish all correlation analysis and tabulate actor profiles results 

- Week 4: implement the user interactive tool that maps a set of features to a character trope

 
 
### Organization within the team: A list of internal milestones up until project Milestone P3.
Everyone got together to brainstorm the main ideas and discuss what makes more sense. Individually, we did or are currently doing the following:
- John: Scraping of Wikipedia e. g. for nationality
- Arvind: Identifying the ideal actor profile per genre
- Sid: Scraping of IMDb for height
- Hao: Help to write the proposal
