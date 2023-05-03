from hospital.Google import Create_Service, convert_to_RFC_datetime
import re
# from Google import Create_Service, convert_to_RFC_datetime

def make_event(app_date, app_time):
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
    calender_id = ''
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        #loops through the list of all calendars
        for calendar_list_entry in calendar_list['items']:
            # if we find the calendar exists, then we skip making it, and go straight to creating event
            if 'Mentcare' == calendar_list_entry['summary']:
                calendar_exists = True
                calender_id = calendar_list_entry['id']
                break
        if calendar_exists == False:
            response = service.calendars().insert(body=request_body).execute()
            calender_id = response['id']
        # create an event using the date froma doctor model appointment 
        hour_adjustment = 4 # adjustment for New York timezone
        months = {
                'January':1,
                'February':2,
                'March':3,
                'April':4,
                'May':5,
                'June':6,
                'July':7,
                'August':8,
                'September':9,
                'October':10,
                'November':11,
                'December':12
                }
        date_of_appointment = str(app_date).split() #index vals - 0:Month 1:Day w/ a comma 2: Year
        date_of_appointment[0] = months[date_of_appointment[0]]
        date_of_appointment[1] = date_of_appointment[1][:len(date_of_appointment[1])-1]
        time_of_appointment = re.split(r'[\s:]',app_time) #expected to see ex. "6:12", so ind 0 is 6 and ind 1 is 12
        for i in range(len(date_of_appointment)):
            date_of_appointment[i] = int(date_of_appointment[i])
        for i in range(len(time_of_appointment) - 1):
            time_of_appointment[i] = int(time_of_appointment[i])
        if time_of_appointment[2] == 'am' and time_of_appointment[0] == 12:
            time_of_appointment[0] = 0
        print(time_of_appointment[0])
        event_request_body = {
            'start' : {
                'dateTime': convert_to_RFC_datetime(date_of_appointment[2], 
                                                    date_of_appointment[0], 
                                                    date_of_appointment[1], 
                                                    time_of_appointment[0]+ hour_adjustment, 
                                                    time_of_appointment[1]),
                'timeZone':'America/New_York'
                },
            'end' : {
                #added 45 to time so the appointment lasts 45 minutes

                'dateTime': convert_to_RFC_datetime(date_of_appointment[2], 
                                                    date_of_appointment[0], 
                                                    date_of_appointment[1], 
                                                    time_of_appointment[0] + hour_adjustment + 1, 
                                                    time_of_appointment[1]),
                'timeZone':'America/New_York'
                },
            'summary': 'Mentcare Doctor Appointment',
            'description': 'Coming into NJIT hospital for a psychiatrist visit.',
            'colorId': 3,
            'status': 'confirmed',
            'transparency': 'opaque',
            'visibility': 'private',
            'location': 'Newark, NJ',
        } 
        max_Attendees = 2
        send_notification = True
        sendUpdate = 'none'
        supports_attachments = False
        calender_id = str(calender_id)
        response = service.events().insert(
                calendarId=calender_id,
                maxAttendees=max_Attendees,
                sendNotifications=send_notification,
                sendUpdates=sendUpdate,
                supportsAttachments=supports_attachments,
                body=event_request_body,
                ).execute()
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break

if __name__ == "__main__":
    make_event("May 2, 2023", "6:12") # just a test



