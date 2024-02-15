import os
from dotenv import load_dotenv
from twilio.rest import Client



def sms(numbers_personal):
    load_dotenv()

    api =  os.getenv('API')
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    TWILIO_PHONE_NUMBER = '+16592157357'
    numbers = numbers_personal

    data =  """
    Este es un mensaje de prueba elaborado por: Luis
        
        Salario segunda quincena de Enero 2023: 
            C$2000
        Giras extras de Enero 2023: 
            C$1000
        Viaticos segunda Quincena de Enero 2023: 
            C$1000
        Domingos: 21 28: 
            C$200
        Viajes: 
            C$1000
        Bono productivo: 
            C$300
        Total ingresos: 
            C$10000
    """
        

    message = client.messages.create(
                                    body= data,
                                    from_=TWILIO_PHONE_NUMBER,
                                    to= numbers
                                )
    
    print(message.sid)
