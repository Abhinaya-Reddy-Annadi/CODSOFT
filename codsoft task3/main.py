import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
from surprise.model_selection import cross_validate

# Load the MovieLens dataset
data_path = "/Users/adarshreddy/Downloads/ml-32m/ratings.csv"  # Update this with your file path

# Load the dataset into a pandas DataFrame
ratings_df = pd.read_csv(data_path)

# Inspect the dataset
print(ratings_df.head())

# Use the Reader class from surprise to define the rating scale
reader = Reader(rating_scale=(1, 5))

# Load the dataset into surprise's format
data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)

# Split the dataset into train and test sets
trainset, testset = train_test_split(data, test_size=0.25)

# Use the SVD algorithm (Singular Value Decomposition) for collaborative filtering
algo = SVD()

# Train the algorithm on the trainset
algo.fit(trainset)

# Test the algorithm on the testset
predictions = algo.test(testset)

# Evaluate the performance (Root Mean Squared Error)
accuracy.rmse(predictions)

# Function to get movie recommendations for a user
def get_movie_recommendations(user_id, top_n=10):
    # Get all movie ids
    movie_ids = ratings_df['movieId'].unique()

    # Get the list of movies the user has already rated
    rated_movies = ratings_df[ratings_df['userId'] == user_id]['movieId']

    # Predict ratings for all movies the user hasn't rated yet
    recommendations = []
    for movie_id in movie_ids:
        if movie_id not in rated_movies.values:
            prediction = algo.predict(user_id, movie_id)
            recommendations.append((movie_id, prediction.est))
    
    # Sort the predictions by the estimated rating in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    # Get the top N recommendations
    top_recommendations = recommendations[:top_n]
    
    # Return the movie ids and predicted ratings
    return top_recommendations

# Example: Get top 5 movie recommendations for user with user_id 1
user_id = 1
recommended_movies = get_movie_recommendations(user_id, top_n=5)
print("Top 5 recommended movies for user {}: {}".format(user_id, recommended_movies))
