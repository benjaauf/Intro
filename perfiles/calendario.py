from pprint import pprint
from .Google import Create_Service
from Test.models import *
from datetime import date, timedelta, tzinfo, datetime, time

CLIENT_SECRET_FILE = 'perfiles/client_secret_602736779324-6l2qrovkouvotof8cjv6pdtd1rbgjhk2.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events']



def crear_calendario():
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION, SCOPES)
    calendar = {
    'summary': 'Prueba',
    'timeZone': 'America/Santiago',
    }
    created_calendar = service.calendars().insert(body=calendar).execute()
    return created_calendar


class TZ(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=-3)

def crear_estudio(horarios,materias):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION, SCOPES)
    # 
    # Encontrar calendario 
    HORAS = {
        'b1': ('8:15','9:25'),
        'b2': ('9:35','10:45'),
        'b3': ('10:55','12:05'),
        'b4': ('12:15','13:25'),
        'b5': ('14:30','15:40'),
        'b6': ('15:50','17:00'),
        'b7': ('17:10','18:20'),
        'b8': ('18:30','19:40'),
        'b9': ('19:50','21:00'),
        'b10':('21:10','22:20'),
    }
    DAYS = {
        0:'Lunes',
        1:'Martes',
        2:'Miercoles',
        3:'Jueves',
        4:'Viernes',
        5:'Sabado',
        6:'Domingo'
    }
    result = service.calendarList().list().execute()
    for i in range(len(result['items'])):
        calendario = result['items'][i]['summary']
        if calendario == 'Prueba':
            id_calendario = result['items'][i]['id']
            break
    # Eliminar todos los eventos
    eventos_calendario = service.events().list(calendarId=id_calendario).execute()
    if len(eventos_calendario['items']) != 0:
        ids = []
        for i in range(len(eventos_calendario['items'])):
            id_evento = eventos_calendario['items'][i]['id']
            ids.append(id_evento)
        for i in range(len(ids)):
            id_evento = ids[i]
            service.events().delete(calendarId=id_calendario, eventId=id_evento).execute()
    # Encontrar bloques donde hacer los eventos
    for horario in horarios:
        dia_actual = date.today().weekday()
        dia_pedido= horario.day
        for i in DAYS:
            if DAYS[i] == dia_pedido:
                dia_pedido = i
                break
        td = timedelta(days=dia_pedido-dia_actual)
        dia_evento = date.today() + td
        bloques ={}
        bloques['b1'] = horario.b1
        bloques['b2'] = horario.b2
        bloques['b3'] = horario.b3
        bloques['b4'] = horario.b4
        bloques['b5'] = horario.b5
        bloques['b6'] = horario.b6
        bloques['b7'] = horario.b7
        bloques['b8'] = horario.b8
        bloques['b9'] = horario.b9
        bloques['b10'] = horario.b10
        # Descripcion de ramos
        ramos= ''
        for materia in materias:
            nombre = str(materia.ramo)
            dificultad = str(materia.get_dificultad_display())
            ramos = ramos + 'Dificultad de ' + nombre +': ' + dificultad + '\n'
        for bloque in bloques:
            if bloques[bloque] == 'Estudiar':
                hinicio , hfinal = HORAS[bloque] 
                hinicio = time(hour=int(hinicio[:-3]), minute= int(hinicio[-2:])) 
                hfinal = time(hour=int(hfinal[:-3]), minute= int(hfinal[-2:])) 
                inicio = datetime(year=dia_evento.year, month = dia_evento.month, day= dia_evento.day, hour=hinicio.hour, minute=hinicio.minute, tzinfo=TZ()).isoformat()
                final = datetime(year=dia_evento.year, month = dia_evento.month, day= dia_evento.day, hour=hfinal.hour, minute=hfinal.minute, tzinfo=TZ()).isoformat()
                event = {
                    'summary': 'Hora de estudio',
                    'description':  ramos,
                    'start': {
                        'dateTime': inicio,
                        'timeZone': 'America/Santiago',
                    },
                    'end': {
                        'dateTime':  final,
                        'timeZone': 'America/Santiago',
                    },
                    'reminders': {
                        'useDefault': False,
                        'overrides': [
                        {'method': 'popup', 'minutes': 10},
                        {'method': 'popup', 'minutes': 0},
                        ],
                        # agregar frecuencia semanal 
                    },
                    'recurrence': [
                        'RRULE:FREQ=WEEKLY;COUNT=4'
                    ],
                    'colorId': '1'
                }
                event = service.events().insert(calendarId=id_calendario, body=event).execute()
            elif bloques[bloque] == 'Ocupado':
                hinicio , hfinal = HORAS[bloque] 
                hinicio = time(hour=int(hinicio[:-3]), minute= int(hinicio[-2:])) 
                hfinal = time(hour=int(hfinal[:-3]), minute= int(hfinal[-2:])) 
                inicio = datetime(year=dia_evento.year, month = dia_evento.month, day= dia_evento.day, hour=hinicio.hour, minute=hinicio.minute, tzinfo=TZ()).isoformat()
                final = datetime(year=dia_evento.year, month = dia_evento.month, day= dia_evento.day, hour=hfinal.hour, minute=hfinal.minute, tzinfo=TZ()).isoformat()
    # descripcion = poner las dificultades lista de string
                event = {
                    'summary': 'Hora de clases',
                    'description':  'Tienes clases',
                    'start': {
                        'dateTime': inicio,
                        'timeZone': 'America/Santiago',
                    },
                    'end': {
                        'dateTime':  final,
                        'timeZone': 'America/Santiago',
                    },
                    'reminders': {
                        'useDefault': False,
                        'overrides': [
                        {'method': 'popup', 'minutes': 10},
                        ],
                        # agregar frecuencia semanal 
                    },
                    'recurrence': [
                        'RRULE:FREQ=WEEKLY;COUNT=4'
                    ],
                    'colorId':'10'
                }
                event = service.events().insert(calendarId=id_calendario, body=event).execute()
    return 0

def crear_certamen(certamenes):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION, SCOPES)
    HORAS = {
        'b1': ('8:15','9:25'),
        'b2': ('9:35','10:45'),
        'b3': ('10:55','12:05'),
        'b4': ('12:15','13:25'),
        'b5': ('14:30','15:40'),
        'b6': ('15:50','17:00'),
        'b7': ('17:10','18:20'),
        'b8': ('18:30','19:40'),
        'b9': ('19:50','21:00'),
        'b10':('21:10','22:20'),
    }
    result = service.calendarList().list().execute()
    for i in range(len(result['items'])):
        calendario = result['items'][i]['summary']
        if calendario == 'Prueba':
            id_calendario = result['items'][i]['id']
            break
    eventos_calendario = service.events().list(calendarId=id_calendario).execute()
    # if len(eventos_calendario['items']) != 0:
    #     ids = []
    #     for i in range(len(eventos_calendario['items'])):
    #         id_evento = eventos_calendario['items'][i]['id']
    #         ids.append(id_evento)
    #     for i in range(len(ids)):
    #         id_evento = ids[i]
    #         service.events().delete(calendarId=id_calendario, eventId=id_evento).execute()
    # user, ramo fecha , hora
    for certamen in certamenes:
        nombre = 'Certamen de ' + certamen.ramo.ramo
        fecha = date.fromisoformat(str(certamen.fecha))
        hora = certamen.hora
        hinicio,hfinal = HORAS[hora]
        hinicio = time(hour=int(hinicio[:-3]), minute= int(hinicio[-2:])) 
        hfinal = time(hour=int(hfinal[:-3]), minute= int(hfinal[-2:])) 
        inicio = datetime(year=fecha.year, month = fecha.month, day= fecha.day, hour=hinicio.hour, minute=hinicio.minute, tzinfo=TZ()).isoformat()
        final = datetime(year=fecha.year, month = fecha.month, day= fecha.day, hour=hfinal.hour, minute=hfinal.minute, tzinfo=TZ()).isoformat()
        event = {
                'summary': nombre,
                'description':  'Prueba de descripcion',
                'start': {
                    'dateTime': inicio,
                    'timeZone': 'America/Santiago',
                },
                'end': {
                    'dateTime':  final,
                    'timeZone': 'America/Santiago',
                },
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                    {'method': 'popup', 'minutes': 10},
                    ],
                },
                #cambiar color
                'colorId':'10'
            }
    event = service.events().insert(calendarId=id_calendario, body=event).execute()
    return 0
"""
print (created_calendar['id'])

calendar = service.calendars().get(calendarId='primary').execute()

print (calendar['summary'])


result = service.events().list(calendarId='fr81e51428p5ugtrho4cd3fdcc@group.calendar.google.com').execute()

"""


