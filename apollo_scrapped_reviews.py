pip install google-play-scraper

import pandas as pd
from google_play_scraper import app, reviews_all

# Define the app ID
app_id = "com.apollo.patientapp"

# Retrieve the app information
app_info = app(app_id)

# Create an empty list to store the reviews
reviews_list = []

# Retrieve all reviews for the app
reviews = reviews_all(app_id)

# Iterate over each review and extract relevant information
for review in reviews:
    # Extract the review rating
    rating = review["score"]

    # Extract the review content
    content = review["content"]

    # Extract the username
    username = review["userName"]

    # Extract the review date
    date = review["at"]

    # Append the review information to the list
    reviews_list.append([rating, content, username, date])

# Create a DataFrame from the reviews list
df = pd.DataFrame(reviews_list, columns=["Rating", "Content", "Username", "Date"])

# Export the DataFrame to a CSV file
df.to_csv("apollo.csv", index=False)

