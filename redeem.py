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
        final_response = {'status': True, 'response': ["Please enter the coupon code to redeem."] , 'user_details':{"language_code":preferred_language}}
    elif preferred_language == 'mar':
        final_response = {'status': True, 'response': ["कृपया पूर्तता करण्यासाठी कूपन कोड टाइप करा."],'user_details':{"language_code":'mr'}}
    elif preferred_language == 'hi':
        final_response = {'status': True, 'response': ["कृपया रिडीम करने के लिए कूपन कोड दर्ज करें"],'user_details':{"language_code":'hi'}}
    
    response = {'statusCode': 200, 'body': json.dumps(final_response), 'headers': {'Content-Type': 'application/json'}}
    return response