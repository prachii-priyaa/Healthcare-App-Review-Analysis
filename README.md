# Healthcare-App-Review-Analysis
This project focuses on analyzing healthcare app reviews **(Practo, Apollo, Tata 1mg, Mfine and Lybrate)** to gain insights into user sentiment, user profiling, trend analysis, comparative analysis, user satisfaction, and topic modeling. The goal is to extract meaningful information from a large dataset of healthcare app reviews and provide valuable insights for app developers, marketers, and stakeholders.

## Project Overview
In this project, we start by collecting healthcare app reviews from various sources and combine them into a single dataset. The dataset includes information such as the healthcare app name, username, review content, rating, and date.

Next, we perform data preprocessing tasks such as removing empty rows and columns from the dataset. We also add new columns for date and time to facilitate further analysis.

## Sentiment Analysis
We conduct sentiment analysis on the review content using two popular approaches: TextBlob and Vader. Sentiment scores and labels (positive, negative, neutral) are assigned to each review. The sentiment analysis results are saved in a new CSV file.

## User Profiling
To gain insights into user preferences and behavior, we apply user profiling techniques. First, we utilize TF-IDF vectorization to extract features from the review content. Then, we apply clustering algorithms (K-means) to group users based on their reviews. User clusters are assigned based on their similarity in review content. The clustering results are visualized using scatter plots and heatmap.

## Trend Analysis
We analyze the trend of sentiment scores over time to identify any patterns or changes in user sentiments. The average sentiment scores are calculated for each date, and a trend line is plotted to visualize the sentiment trend.

## Comparative Analysis and User Satisfaction
We calculate the average app ratings for each healthcare app to compare user satisfaction levels. The distribution of ratings is visualized using histograms. Additionally, we analyze the factors contributing to high or low user satisfaction by examining positive and negative reviews.

## Topic Modeling (LDA)
Topic modeling is performed using Latent Dirichlet Allocation (LDA). We apply TF-IDF vectorization to the review content and then apply LDA to extract topics. The top words for each topic are displayed to understand the main themes in the reviews.

## Requirements
To run this project, you need to have the following dependencies installed:

- scikit-learn
- nltk
- pandas
- numpy

## Acknowledgments
The project utilizes various Python libraries such as scikit-learn, nltk, pandas, and numpy for data analysis and visualization.
The project is inspired by the need to understand user sentiments and preferences in healthcare app reviews to improve user experience and satisfaction.
