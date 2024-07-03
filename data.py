import googleapiclient.discovery
import pandas as pd
import findspark
findspark.init()
import pandas as pd
from pyspark.sql import SparkSession
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import nltk

def get_dataset(video_id):
    spark = SparkSession.builder \
        .appName("YouTubeCommentsSentimentAnalysis") \
        .config("spark.driver.maxResultSize", "4g") \
        .config("spark.network.timeout", "800s") \
        .config("spark.executor.heartbeatInterval", "60s") \
        .getOrCreate()
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyC_0RVqlHp4M5_LSBZNEo3GEkUa3PE-LiY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # Function to fetch comments
    def get_comments(video_id):
        comments = []
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100
        )

        while request:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comments.append([
                    comment['authorDisplayName'],
                    comment['likeCount'],
                    comment['textDisplay']
                ])
            request = youtube.commentThreads().list_next(request, response)

        return comments

    # Fetch comments for the given video ID
    #video_id = "vzLu82DvAWY"
    comments = get_comments(video_id)

    # Create a DataFrame
    df = pd.DataFrame(comments, columns=['author', 'like_count', 'text'])

    # Display the DataFrame
    #print(df)
    # Download VADER lexicon
    #nltk.download('vader_lexicon')

    # Assuming df is your pandas DataFrame containing the comments
    # df = pd.read_csv('your_comments_file.csv')  # Example to load from a CSV file

    # Initialize Spark session
    # # Convert pandas DataFrame to Spark DataFrame
    spark_df = spark.createDataFrame(df)

    # Initialize VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    def get_vader_sentiment(text):
        scores = sid.polarity_scores(text)
        compound_score = scores['compound']
        if compound_score > 0:
            return 'positive'
        elif compound_score == 0:
            return 'neutral'
        else:
            return 'negative'

    # Register the function as a UDF
    sentiment_udf = udf(get_vader_sentiment, StringType())

    # Apply the UDF to the Spark DataFrame
    spark_df_with_sentiment = spark_df.withColumn('sentiment', sentiment_udf(spark_df['text']))

    # Show the results
    spark_df_with_sentiment.show(truncate=False)

    new = spark_df_with_sentiment.collect()
    #len(new)
    column_names = new[0].asDict().keys()
    output_df = pd.DataFrame(new,columns=column_names)
    return output_df
