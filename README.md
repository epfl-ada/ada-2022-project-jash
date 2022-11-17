# Analysing and predicitng movie characters (= trope)
## Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
- Project Goals
    1. interactive tool for predicting movie character (= trope) based on features of actor
    2. data story in connection with prediction of trope: Analysing the usage of tropes in movies overt-time and each trope's influence on the successfulness of a movie (measured in revenue of movie)

## Research Questions: A list of research questions you would like to address during the project.

1. Which features of an actor (age, nationality, height etc.) influence the assignment to a trope class? By how much?
2. What are they keywords in movie summaries that are associated with each trope? Can some distribution/point cloud (per trope) be extracted?
3. Are movie stars necessarily the most successful in their trope? (movie stars A and B could belong to trope 1, star A can be much more successful than B in the movie industry, but can B be more successful when playing characters belonging to trope 1? Is this even possible? Can we vary this question if not?)
4. Determing "classic" statistics in our dataset is also a good idea; they can enhance our main story. Things like most successful movie stars, trend of movie genres/tropes over the years, average age of actors that made it big, most common actor backgrounds in movies, are there actors/directors that bring more value to movies on average (johnny's idea 2 in google doc) etc.

## Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
1. wikidata scraping to get the missing nationality(~= ethnicity) of some actors 
2. imdb scraping to get the missing height values of some actors

## Methods
1. Potential methods to build movie character classifier: linear regression, k-nearest neighbor, decision tree etc.
2. We could create clusters (1 per trope) and model some soft cluster classifier that outputs the distribution of belonging to each cluster (ex: Person A has 40% chance of belonging to "Sleeping Beauty" trope, 30% to "bully"... etc)
3. Another option would be to train a Neural Network that does the classification: we'd first have a Convolutional part where we extract the most meaningful features out of our dataset then we would input these into a Fully Connected NN to do the classification

## Proposed timeline
- At the start, group work: lay down together the basic and necessary foundations required to build whatever we will be building. Make sure everyone understands what has be done, why, and how to use it.
- Eventually, parallel work: one part of the team works on the data story, the other on the interactive ML classifier
  

## Organization within the team: A list of internal milestones up until project Milestone P3.
- First get all required/missing datasets
- Then divide work into two: half of the group will work on the data story (like the usage of movie tropes over time etc, to be better defined), the second half will work on the classifier

## Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
