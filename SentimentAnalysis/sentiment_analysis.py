# Import necessary packages
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

def sentiment_analysis_func(text_to_analyse):
    # create a spaCy model
    nlp = spacy.load("en_core_web_sm")
    # add to the pipeline
    nlp.add_pipe("spacytextblob")
    # analyze the sentiment of the text
    sentiment = nlp(text_to_analyse)
    score = sentiment._.blob.sentiment_assessments.assessments
    # The polarity of the document. The polarity score is a float within the range [-1.0, 1.0]
    polarity = sentiment._.blob.polarity
    # The subjectivity of the document. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    sujectivity = sentiment._.blob.subjectivity
    # print(polarity)
    # print(sujectivity)
    # print(score)
    return polarity, sujectivity, score

# print('Start running the code')
# if __name__ == "__main__": 
#     sentiment_analysis_func("I am glad this happened")
