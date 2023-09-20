"""
This is a Flask server for the Emotion Detector application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")
"""Set app Name and Starts Flask"""

@app.route("/emotionDetector")
def emot_detector():
    """Starts request and retuen response"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    result = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness']
    }
    str_result = str(result).replace('{', '').replace('}', '')
    emotion = response['dominant_emotion']
    r_string = "For the given statement, the system response is {}. The dominant emotion is {}."
    return r_string.format(str_result, emotion)

@app.route("/")
def render_index_page():
    """Render Index"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
