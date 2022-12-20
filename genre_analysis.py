pd.options.mode.chained_assignment = None  # default='warn'

# for the sake of diversity - not taking crime and adventure reduces significantly after animation is removed
genres_major = ['Drama', "Action", "Romance","Comedy"]

# remove genres which do not have a relation to actor features
genres_remove = ["Animation", "Biography", "Documentary","Short"]


# function removes certain genres and makes additional columns for each major genre marking which category the movie belongs to 

def extract_genres(dataset, genres_major=genres_major, genres_remove=genres_remove):

    dataset.dropna(inplace=True)

    x = []
    a = []


    # filter genres that we are not considering = [short, documentary, biography, animation]
    dataset_filtered = dataset[~dataset['genres'].str.contains('|'.join(genres_remove))]

    # to store only movies and actors that have worked in the major genres
    movies_major = dataset_filtered[dataset_filtered['genres'].str.contains('|'.join(genres_major))]

    for i in genres_major:

        movies_major[i] = movies_major['genres'].apply(lambda x: 1 if i in x else 0)

    movies_major.sort_values(by ='startYear', ascending=True)

    for y in movies_major['genres']:

        if type(y) == str:
            x+= y.split(",")

    genres_all, counts = np.unique(x, return_counts=True)

    genre_df = pd.DataFrame(list(zip(genres_all, counts)), columns=["genre", "count"])

        
    genre_df.sort_values('count',inplace=True, ascending = False)
    genre_df.reset_index(drop=True,inplace=True)
    genre_df.set_index('genre').plot(kind='bar', figsize=(13,4))

    return genres_all, counts, movies_major