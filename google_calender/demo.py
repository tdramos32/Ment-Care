# from django.db import models
from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime
# from doctor.models import Appointment
import os

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION,SCOPES)

request_body = {
        'summary' : 'Mentcare'
}
page_token = None
calendar_exists = False
# calender_id = ''
while True:
    calendar_list = service.calendarList().list(pageToken=page_token).execute()
    #loops through the list of all calendars
    for calendar_list_entry in calendar_list['items']:
        pprint(calendar_list_entry['summary'])
        # if we find the calendar exists, then we skip making it, and go straight to creating event
        if 'Mentcare' == calendar_list_entry['summary']:
            calendar_exists = True
            calender_id = calendar_list_entry['id']
            print("The calender id: ",calender_id)
            pprint('mentcare is already in here man!!!')
            break
    if calendar_exists == False:
        pprint("The calendar DOESNT exist")
        response = service.calendars().insert(body=request_body).execute()
        calender_id = response['id']
        pprint("The calender id: ",calender_id)
    # create an event using the date froma doctor model appointment 
    hour_adjustment = 5 # adjustment for New York timezone
    event_request_body = {
        'start' : {
            'dateTime': convert_to_RFC_datetime(2023, 8, 1, 12 + hour_adjustment),
            'timeZone': 'New York'
            },
        'end' : {
            'dateTime': convert_to_RFC_datetime(2023, 8, 1, 12 + hour_adjustment),
            'timeZone': 'New York'
            },
        'summary': 'Mentcare Doctor Appointment',
        'description': 'Coming into NJIT hospital for a psychiatrist visit.',
        'colorId': 3,
        'status': 'confirmed',
        'transparency': 'opaque',
        'visibility': 'private',
        'location': 'Newark, NJ',
    } 
    maxAttendees = 2
    sendNotification = True
    sendUpdate = 'none'
    supportsAttachments = False
    calender_id = str(calender_id)
    response = service.events().insert(
            calenderId=calender_id,
            max_Attendees=maxAttendees,
            send_notification=sendNotification,
            send_update=sendUpdate,
            supports_attachments=supportsAttachments,
            body=event_request_body,
            ).execute()
    pprint(response)
    page_token = calendar_list.get('nextPageToken')
    if not page_token:
        break
