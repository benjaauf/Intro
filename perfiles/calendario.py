from pprint import pprint
from .Google import Create_Service

CLIENT_SECRET_FILE = 'perfiles/client_secret_602736779324-6l2qrovkouvotof8cjv6pdtd1rbgjhk2.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']

def crear_calendario():
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION, SCOPES)
    calendar = {
    'summary': 'Prueba',
    'timeZone': 'America/Santiago'
    }
    created_calendar = service.calendars().insert(body=calendar).execute()
    return created_calendar






# print (created_calendar['id'])

# calendar = service.calendars().get(calendarId='primary').execute()

# print calendar['summary']

