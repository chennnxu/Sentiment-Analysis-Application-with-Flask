// Function to run sentiment analysis when called
let RunSentimentAnalysis = ()=>{
    // Get the text to analyze from the input field with id "textToAnalyze"
    textToAnalyze = document.getElementById("textToAnalyze").value;
    // Create a new XMLHttpRequest object to make a request to the server
    let xhttp = new XMLHttpRequest();
    // Define a function to handle the response from the server
    xhttp.onreadystatechange = function() {
        // Check if the request is complete and the response is ready
        if (this.readyState == 4 && this.status == 200) {
            // Update the HTML content of an element with id "system_response" with the response text
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    // Open a GET request to the server with the specified endpoint and parameters
    xhttp.open("GET", "sentimentAnalysis?textToAnalyze"+"="+textToAnalyze, true);
    // Send the request to the server
    xhttp.send();
}
