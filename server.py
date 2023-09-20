from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid input ! Try again."
    else:
        result = {
            'anger': response['anger'],
            'disgust': response['disgust'],
            'fear': response['fear'],
            'joy': response['joy'],
            'sadness': response['sadness']
        }
        return "For the given statement, the system response is {}. The dominant emotion is {}.".format(str(result).replace('{', '').replace('}', ''), response['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

