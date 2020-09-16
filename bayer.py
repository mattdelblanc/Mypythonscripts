import  json
def main(event, context):
    body = json.loads(event['body'])
    entities = body['entities']
    user_data = body['user']
    if len(entities["select_language_new"])>0:
        preferred_language = entities["select_language_new"][0]["entity_value"]
    else:
        preferred_language = 'en'

    if preferred_language == 'en':
        final_response = {'status': True, 'response': ["Please type your *6 digit pincode* below so I can help you with the best products for your crop"] , 'user_details':{"language_code":preferred_language}}
    elif preferred_language == 'mar':
        final_response = {'status': True, 'response': ["आपल्या पिकासाठी उत्तम उत्पादने निवडण्यासाठी कृपया तुमचा ६ अंकी पिनकोड मला सांगा."],'user_details':{"language_code":'mr'}}
    elif preferred_language == 'hi':
        final_response = {'status': True, 'response': ["अपनी फसल के लिए सर्वोत्तम उत्पाद चुनने के लिए कृपया मुझे अपना 6 अंकों का पिन कोड बताएं."],'user_details':{"language_code":'hi'}}
    elif preferred_language == 'te':
        final_response = {'status':True, 'response':["దయచేసి మీ పంటకు ఉత్తమమైన ఉత్పత్తులతో మీకు సహాయం చేయడానికి 6 అంకెల పిన్‌కోడ్‌తో నాకు సహాయం చేయండి"],'user_details':{"language_code":'te'}}
    response = {'statusCode': 200, 'body': json.dumps(final_response), 'headers': {'Content-Type': 'application/json'}}
    return response