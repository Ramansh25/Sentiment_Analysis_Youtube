#!/usr/bin/env python
# coding: utf-8

# In[2]:



import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#from wordcloud 
import WordCloud

# Load the CSV file
csv_filename = 'YouTube_Comments_Sentiment_KsEoGDgKdwQ_20240701014137.csv'
df = pd.read_csv(csv_filename)


video_details = {
    'likes': 11005306,
    'views': 349562
}

# Basic Data Exploration
st.title('YouTube Comments Analysis Dashboard')

# Sidebar to display some information
st.sidebar.title('Dataset Information')
st.sidebar.info(f"Dataset shape: {df.shape}")

# Summary Statistics (if applicable)
st.subheader('Summary Statistics')
st.write(df.describe())

# Visualization: Sentiment Distribution (Bar Chart)
st.subheader('Sentiment Distribution of YouTube Comments')
sentiment_counts = df['Sentiment'].value_counts()
fig_bar = plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'gray', 'red'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.xticks(rotation=0)
st.pyplot(fig_bar)

# Visualization: Sentiment Distribution (Pie Chart)
st.subheader('Sentiment Distribution of YouTube Comments (Pie Chart)')
fig_pie, ax_pie = plt.subplots(figsize=(8, 6))
colors = ['green', 'gray', 'red']
labels = sentiment_counts.index
ax_pie.pie(sentiment_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
ax_pie.set_title('Sentiment Distribution (Pie Chart)')
ax_pie.axis('equal')
st.pyplot(fig_pie)

# Visualization: Word Cloud
st.subheader('Word Cloud of YouTube Comments')
df['Processed_Comment'] = df['Processed_Comment'].astype(str)
all_comments = ' '.join(df['Processed_Comment'].tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_comments)
fig_wordcloud = plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud')
st.pyplot(fig_wordcloud)

# Visualization: Comparison between Likes and Views (Pie Chart)
st.subheader('Comparison between Likes and Views')
fig_likes_views, ax_likes_views = plt.subplots(figsize=(8, 6))
sizes = [video_details['views'], video_details['likes']]
labels = ['likes', 'views']
ax_likes_views.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen'])
ax_likes_views.set_title('Distribution of Likes and Views for the Video')
ax_likes_views.axis('equal')
st.pyplot(fig_likes_views)



# Footer
st.text('')
st.text('')
st.markdown("---")
st.markdown("Created with Streamlit by Ramansh.")

# Run the app with `streamlit run dashboard.py`


# In[ ]:




