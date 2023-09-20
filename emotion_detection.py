import requests
import json

def higherValue(old_value,new_value):
    if(old_value < new_value):
        old_value = new_value

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_predictions, key=lambda k: emotion_predictions[k])
    result = {
        'anger': emotion_predictions['anger'],
        'disgust': emotion_predictions['disgust'],
        'fear': emotion_predictions['fear'],
        'joy': emotion_predictions['joy'],
        'sadness': emotion_predictions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return result