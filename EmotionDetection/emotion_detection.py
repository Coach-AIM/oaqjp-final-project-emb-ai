"""
Emotion Detection Module using Watson NLP Library with dominant emotion calculation.
"""
import json
import requests


def emotion_detector(text_to_analyze):
    """Sends a POST request to Watson NLP EmotionPredict service, extracts emotion

    scores, determines the dominant emotion, and returns them in a dictionary.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        'grpc-metadata-mm-model-id': (
            'emotion_aggregated-workflow_lang_en_stock'
        )
    }
    payload = {'raw_document': {'text': text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers)
    formatted_response = json.loads(response.text)

    # Extract the nested emotion dictionary
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Store scores in a dictionary
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    # Logic to find the key with the highest numerical value
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Append the dominant emotion to the final dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores