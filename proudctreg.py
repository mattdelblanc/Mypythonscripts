
import  json
import requests

def main(event, context):
    """
   event['body'] is a string dict with the following keys:
   node, event, user, entities.
   Currently, we pass user_id, user_name, full_name, device_platform and language_code in the user dictionary.
   Args:
       event (dict): Data corresponding to this event
       context
   Returns
       (dict): response with statusCode and the response for the User
   """
    body = json.loads(event['body'])
    entities = body.get('entities')
    # print(entities)
    person_name = entities["person_name"][0]['original_text']
    date_of_purchase  = entities["date_of_purchase"][0]['original_text']
    order_id = entities["order_id_registration"][0]['entity_value']['value']
    product_id = entities["product_id_registration"][0]['entity_value']['value']
    address = entities["address_registration"][0]['entity_value']['value']
    print(person_name)
    print(date_of_purchase)
    print(order_id)
    print(product_id)
    print(address)
    registration_id = product_registration(person_name, date_of_purchase, order_id, address, product_id)
    user_data = body.get('user')
    conversation_details = body.get('conversation_details')
    final_response = {
        'status': True, 
        'entities':entities, 
        'user_full_name': user_data.get("full_name"),
        'user_device_platform': user_data.get("device_platform"),
        'conversation_details':conversation_details,
        'registration_id': registration_id
    }
    response = {'statusCode': 200, 'body': json.dumps(final_response), 'headers': {'Content-Type': 'application/json'}}
    return response
    
    
def product_registration(person_name, date_of_purchase, order_id,address, product_id):
    params = {'person_name': person_name, 'date_of_purchase': date_of_purchase, 'order_id': order_id, 'address': address, 'product_id': product_id}
    url = 'https://run.mocky.io/v3/83580f87-541f-468a-854c-1b2d8f78a56f'
    #url = 'https://webhook.site/b3ed6545-dc3d-40be-a31d-ffc37eead3d4'
    response = requests.post(url,json=params)
    data = response.json()

    return data['registration id']
    #return 'Thank You'
    