import pandas
import matplotlib.pyplot as plt

#reading csv
df_first_emotions_csv = pandas.read_csv('./dataset/goemotions_1.csv')

#verifying data structure
print(df_first_emotions_csv.head())

#checking how many columns have null values
print(df_first_emotions_csv.isnull().sum())

emotion_columns = [
    'admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion',
    'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment',
    'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism',
    'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral'
]
emotion_counts = (df_first_emotions_csv[emotion_columns] == True).sum()

# Plot the bar chart
plt.figure(figsize=(10,6))
emotion_counts.plot(kind='bar', color='skyblue')
plt.title('Emotion Distribution in Dataset')
plt.xlabel('Emotion')
plt.ylabel('Count (Occurrences of Emotion = 1)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# Show the plot
plt.show()

regex_pattern = r"[!?]|\.\.\." 
emotion_punctuation = df_first_emotions_csv[df_first_emotions_csv['text'].str.contains(regex_pattern, regex=True)].sum()
plt.figure(figsize=(10,6))
emotion_punctuation.loc[emotion_columns].plot(kind='bar', color='skyblue')
plt.title('Emotion Distribution in Text With Punctuation ("?","!","...")')
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()

#Comparing emotion in text with punctuation x general
plt.figure(figsize=(12, 6))
emotion_counts.plot(kind='bar', width=0.4, position=1, color='skyblue', label='All Texts')
emotion_punctuation.loc[emotion_columns].plot(kind='bar', width=0.4, position=0, color='salmon', label='Texts with Punctuation')
plt.xlabel("Emotions")
plt.ylabel("Count")
plt.title("Comparison of Emotion Distribution in All Texts vs Texts with Punctuation")
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend()

# Show the plot
plt.show()