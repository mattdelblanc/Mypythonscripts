import json
import requests
import urllib.parse as urlparse 
from urllib.parse import parse_qs
import dateutil.tz
import datetime


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
    user_data = body.get('user')
    conversation_details = body.get('conversation_details')

    booking_status = book_appointment(entities)
    response = {'statusCode': 200, 'body': json.dumps(booking_status), 'headers': {'Content-Type': 'application/json'}}
    return response


def book_appointment(entities):
    booking_status = {'status': False}
    fetch_entity = Entities(entities)
    base_url = "https://provider.kareo.com/patient-engagement-ui/api/AppointmentSchedule/providerShortName/"

    # appointment entities
    provider_short_name = fetch_entity.get('doctor_chinngyn_preference')
    if not provider_short_name:
        return booking_status
    service_location_guid = fetch_entity.get('appointment_preference')
    chinn_gyn_visit = fetch_entity.get('chinn_gyn_visit')

    appointment_dates = fetch_entity.get('webview_picker_chinngyn', '').replace("!", ":").upper()
    TIMEZONE_PACIFIC = dateutil.tz.gettz('US/Pacific')
    start_time, end_time = appointment_dates.split('|')
    start_time = start_time.rsplit("-", 1)[0].upper()
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S").replace(
        tzinfo=dateutil.tz.gettz('US/Pacific')).astimezone(
        datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')
    end_time = end_time.rsplit("-", 1)[0].upper()
    end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S").replace(
        tzinfo=dateutil.tz.gettz('US/Pacific')).astimezone(
        datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')

    # patient entities
    dob = fetch_entity.get('dob_chinn_gyn')
    dob = datetime.datetime(year=dob['yy'], month=dob['mm'], day=dob['dd'], hour=18, minute=30,
                            tzinfo=datetime.timezone.utc)
    name = fetch_entity.get('person_name')
    email = fetch_entity.get('email')
    phone_number = fetch_entity.get('phone_number_chinn_gynn')
    phone_number = "".join(e for e in phone_number if e.isnumeric())
    reason = fetch_entity.get('reason_visit_chinn_gyn')
    
    # Source
    utm_source = None
    page_url = fetch_entity.get('chinngyn_user_source')
    try:
        if page_url:
            page_url = page_url.replace("[colon]",":") 
            parsed = urlparse.urlparse(page_url)
            utm_source = parse_qs(parsed.query).get('utm_source',[""])[0]
    except Exception as e:
        print(f"URL parsing failed due to {e}")
        

    first_visit = fetch_entity.get('chinn_gyn_visit')
    reason += "    " + "Is this the first time you are visiting Chinn GYN-" + first_visit
    if utm_source:
        reason += " Source-"+utm_source
    reason = ''.join(e for e in reason if e.isalnum() or e in ["-", ",", "_", " "])
    # gender = fetch_entity.get('gender_chinn_gynn')
    appointment = {
        "reason": reason,
        "startTime": start_time,
        "endTime": end_time,
        "serviceLocationUUID": service_location_guid,
        "recareReminderEncryptedId": ""
    }
    insurance = {
        "companyName": "",
        "payerId": "",
        "policyNumber": "",
        "insuranceMode": 2
    }

    patient = {
        "genderId": 2,
        "insuranceMode": 2,
        "firstName": name.get('first_name', ''),
        "lastName": name.get('last_name', 'NA') if name.get('last_name') else 'NA',
        "phoneNumber": phone_number,
        "email": email,
        "dob": dob.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        "contactByText": True,
        "contactByPhone": True,
        "dateOfBirth": int(dob.timestamp() * 1000)
    }
    data = {
        'providerShortName': provider_short_name,
        'insurance': insurance,
        'appointment': appointment,
        'patient': patient,
    }
    headers = {
        'Content-Type': 'application/json'
    }
    booking_url = base_url + provider_short_name
    booking_url = "https://webhook.site/7342f6d8-98e0-413b-a078-9a528bfccc2e"
    response = requests.post(url=booking_url, json=data, headers=headers)
    print(data)
    if response.status_code == 204:
        booking_status['status'] = True
    elif response.status_code == 400:
        print("*****************")
        print(response.json())
        booking_status['status'] = False
        booking_status['message'] = response.json().get('message')
    else:
        booking_status['status'] = False
        # Uncomment after removing mock
        #print(response.json())
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    # REMOVE IF REMOVING MOCK URLS!!!!!!!
    booking_status['status'] = True
    return booking_status


class Entities:
    def __init__(self, entities):
        self.entities = entities

    def get(self, key, default=''):
        entity = self.entities.get(key, [])[0].get('entity_value', default)
        if entity is not None and 'value' in entity:
            entity = entity['value']
        return entity
