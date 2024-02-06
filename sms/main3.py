

# Set your API key

import requests

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjdhMGFlOTIwZDM4YTE1YTY2NzgxMjYwZjEzNmI2MDdiNWU4ZmE2ZmJhYmE1YzFlOWRhMjVkOTIyODI5NmYxMTkzMzIyMjM2YjIzOTNiNzgyIn0.eyJhdWQiOiI0YzljZWY1YjAwYzFlZjVlMjkxYTFhNDkwZjI3YTNmZSIsImp0aSI6IjdhMGFlOTIwZDM4YTE1YTY2NzgxMjYwZjEzNmI2MDdiNWU4ZmE2ZmJhYmE1YzFlOWRhMjVkOTIyODI5NmYxMTkzMzIyMjM2YjIzOTNiNzgyIiwiaWF0IjoxNzA2NzI4ODA2LCJuYmYiOjE3MDY3Mjg4MDYsImV4cCI6MTcwNjczMjQwNiwic3ViIjoiIiwic2NvcGVzIjpbXSwidXNlciI6eyJpZCI6ODU3MTMwMCwiZ3JvdXBfaWQiOm51bGwsInBhcmVudF9pZCI6bnVsbCwiY29udGV4dCI6eyJhY2NsaW0iOiIwIn0sImFyZWEiOiJyZXN0In19.bBPgpCF-kUObQpKuAj6SGiU3EdcIOw7pCW31Ic2Ztm-LXgOKYDu3F_Nm5_WkySVxdVdAVz-VryUuxJfALhpg5M3644xiFxOmyKA5QElAOhLCnStRXi2HkRwsSSbAnBRNFYDQUgF13AiYovQ6hY-ubc-kYAJK6BpfSDT7ABbmr2cuBKV2SInJyOsfrO4Rc1r5p-zwM6gp91-RXguCVzRnnKzcC-VZnaPn7c4OO9-GvayJCF4Zimzx2wMZypQFUQbedhOr-k01vKzOSj5ALs5n1V-_w0iVNcutHKDibdgMktQeQB0FKrF5pzgllSRFnUO_hHuE8bU7p7M4FZy5pbA7vg'


# Define la URL de la solicitud
url = 'https://api.sendpulse.com/sms/send'

# Define los parámetros de la campaña
campaign_params = {
    "sender": "4c9cef5b00c1ef5e291a1a490f27a3fe",
    "phones": [
        "50587460295",
    ],
    "body": "Este es el cuerpo del mensaje SMS",
    "route": {
        "UA": "international"
    },
    "emulate": False,
    "date": "2024-07-07 10:00:00",
    "stat_link_tracking": True,
    "stat_link_need_protocol": True
}

# Envía la solicitud POST para crear la campaña
response = requests.post(url, json=campaign_params)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Parsea la respuesta JSON
    response_data = response.json()
    if response_data["result"]:
        campaign_id = response_data["campaign_id"]
        print(f"Campaña creada exitosamente. ID de campaña: {campaign_id}")
    else:
        print("Error al crear la campaña.")
else:
    print(f"Fallo al crear la campaña. Código de estado: {response.status_code}, Respuesta: {response.text}")
