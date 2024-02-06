import os
from twilio.rest import Client



api =  ' SKfad5a8956b33b595d1afae8b04bd2b0c'
account_sid = 'AC178dba80c9e2fe34ee9825f66ff64848'
auth_token = '586ffd76d3a6aa4a7739ba527a302f07'
client = Client(account_sid, auth_token)
numbers = ['+50587460295']

data =  """
    - Salario segunda quincena de Enero 2023: C$2000,
    - Giras extras de Enero 2023: C$1000,
    - Viaticos segunda Quincena de Enero 2023: C$1000,
    - Domingos: 21 28: C$200,
    - Viajes: C$1000,
    - Bono productivo: C$300,
    - Total ingresos: C$10000
"""
    

message = client.messages.create(
                                body= data,
                                from_='+16592157357',
                                to= numbers
                            )

print(message.sid)