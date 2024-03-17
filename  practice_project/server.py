"""
Sentiment Analysis Server
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analysis_func
app = Flask("Sentiment Analysis")

@app.route("/sentimentAnalysis")
def sentiment_analysis_function():
    ''' This function calls the application
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analysis_func(text_to_analyze)
    if len(response[2]) == 0:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, 'polarity': {response[0]:.2f}, 'subjectivity': {response[1]:.2f}."

    return response_text

@app.route("/")
def render_index_page():
    ''' This is the function to render the html interface
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)