"""
Sentiment Analysis Server
"""
# Import relevant libraries and functions
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analysis_func
# Flask library along with its render_template function (for deploying the HTML file) and 
# request function (to initiate the GET request from the web page).

# Initiate the Flask app by name
app = Flask("Sentiment Analysis")

# The function uses the Flask decorator @app.route("/sentimentAnalyzer") as referenced in the mywebscript.js file.
@app.route("/sentimentAnalysis")
def sentiment_analysis_function():
    ''' This function calls the application
    '''
    # First, send a GET request to the HTML interface to receive the input text.
    # Note that the GET request should reference textToAnalyze variable as defined in the mywebscript.js file.
    text_to_analyze = request.args.get('textToAnalyze')
    # Call function sentiment_analysis_func
    response = sentiment_analysis_func(text_to_analyze)
    # Incorporate Error handling
    if len(response[2]) == 0:
        response_text = "Invalid Input! Please try again."
    else:
        response_text = f"For the given statement, 'polarity': {response[0]:.2f}, 'subjectivity': {response[1]:.2f}."

    return response_text

# Render the HTML template using render_index_page
@app.route("/")
def render_index_page():
    ''' This is the function to render the html interface
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # Run the application host: 0.0.0.0 (or localhost) on port number 5000
    app.run(host = "0.0.0.0", port = 5000)