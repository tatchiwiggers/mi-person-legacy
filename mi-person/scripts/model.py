# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):

	# Create a SentimentIntensityAnalyzer object.
	sid_obj = SentimentIntensityAnalyzer()

	# polarity_scores method of SentimentIntensityAnalyzer
	# object gives a sentiment dictionary.
	# which contains pos, neg, neu, and compound scores.
	sentiment_dict = sid_obj.polarity_scores(sentence)
	
	print("Overall sentiment: ", sentiment_dict)
	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

	print("\nSentence overall rated as", end = " ",)

	# decide sentiment as positive, negative and neutral
	# sentence = input("Enter a sentence to be analyzed: ")

	# sentiment_scores(sentence)
	if sentiment_dict['compound'] >= 0.05 :
		return "Positive, say something nice back :)"

	elif sentiment_dict['compound'] <= - 0.05 :
		return "Negative, try to chill a bit before answering..."

	else :
		return "Neutral, so no problem here ;)"

