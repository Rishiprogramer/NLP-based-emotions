# NLP-based-emotions

Sentiment Analysis Classifier
Overview
This Natural Language Processing (NLP) model is designed to analyze and classify the underlying sentiment of text data. By processing textual input, the model identifies the emotional tone and categorizes it into distinct sentiments, enabling automated text analysis for applications like customer feedback review, social media monitoring, and user experience research.

Key Features

Analyzes raw text to predict the primary emotional sentiment.

Preprocesses data through tokenization, stop-word removal, and text normalization to improve prediction accuracy.

Known Issues & Limitations

Sentiment Overlap (Sadness misclassified as Joy): The model currently experiences occasional difficulties distinguishing between sadness and joy. This misclassification often happens when text contains complex phrasing, sarcasm, or ambiguous vocabulary (such as "tears" which can belong to both "tears of joy" and "crying tears").


#Test Accuracy: 0.89

#Train Accuracy: 0.966171875
