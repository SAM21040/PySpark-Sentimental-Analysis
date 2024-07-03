from data import get_dataset
import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter

st.title('YouTube Comments Sentiment Analysis Dashboard')

# Input box for video ID
video_id = st.text_input('Enter YouTube Video ID', '')

def generate_wordcloud(text):
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='rgba(255, 255, 255, 0)', mode='RGBA').generate(text)
    return wordcloud

if video_id:
    df = get_dataset(video_id)
    
    st.write('### Data Preview')
    st.dataframe(df.head())

    st.write('### Number of Comments Fetched :' + str(len(df)))

    st.write('### Sentiment Distribution')
    sentiment_count = df['sentiment'].value_counts().reset_index()
    sentiment_count.columns = ['Sentiment', 'Count']
    fig1 = px.bar(sentiment_count, x='Sentiment', y='Count', color='Sentiment', title='Sentiment Distribution')
    st.plotly_chart(fig1)

    st.write('### Most Liked Comments')
    most_liked_comments = df.nlargest(10, 'like_count')
    st.dataframe(most_liked_comments[['author', 'like_count', 'text', 'sentiment']])

    st.write('### Word Cloud')
    all_text = ' '.join(df['text'].tolist())
    wordcloud = generate_wordcloud(all_text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    # Top Words by Sentiment
    st.write('### Top Words by Sentiment')
    sentiments = df['sentiment'].unique()
    for sentiment in sentiments:
        st.write(f"#### {sentiment.capitalize()} Comments")
        sentiment_text = ' '.join(df[df['sentiment'] == sentiment]['text'].tolist())
        sentiment_words = [word for word in sentiment_text.split() if word.lower() not in STOPWORDS]
        sentiment_word_freq = Counter(sentiment_words)
        sentiment_most_common_words = pd.DataFrame(sentiment_word_freq.most_common(10), columns=['Word', 'Frequency'])
        fig_top_words = px.bar(sentiment_most_common_words, x='Word', y='Frequency', title=f'Top Words in {sentiment.capitalize()} Comments')
        st.plotly_chart(fig_top_words)

    # Sentiment by Like Count
    st.write('### Sentiment by Like Count')
    fig_comment_likes = px.box(df, x='sentiment', y='like_count', color='sentiment', title='Sentiment by Like Count', labels={'like_count': 'Like Count'})
    st.plotly_chart(fig_comment_likes)

    author_filter = st.text_input('Filter by Author', '')
    if author_filter:
        filtered_df = df[df['author'].str.contains(author_filter, case=False)]
        st.write(f'### Comments by {author_filter}')
        st.dataframe(filtered_df)
    else:
        st.write('Enter an author name to filter the comments')

if __name__ == '__main__':
    st.write('Streamlit app is running...')
