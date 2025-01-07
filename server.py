"""
Server for Emotion Detection Application using Flask.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Emotion detection endpoint.

    Returns:
        json: JSON response containing the formatted result or an error message.
    """
    text_to_analyze = request.json.get('text', '')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again."
    else:
        response_text = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. The dominant emotion is "
            f"{result['dominant_emotion']}."
        )

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
