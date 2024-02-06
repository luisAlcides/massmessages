from pysendpulse.pysendpulse import PySendPulse

REST_API_ID = '4c9cef5b00c1ef5e291a1a490f27a3fe'
REST_API_SECRET = '22d70c466e6f99e7d7ef181db6e6cf1a'
GRANT_TYPE = 'client_credentials'
TOKEN_STORAGE = 'memcached'
MEMCACHED_HOST = '127.0.0.1:11211'
ADDRESSBOOK_ID = '50587460295'
SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE, GRANT_TYPE, memcached_host=MEMCACHED_HOST)

SPApiProxy.add_sender('almacenamiento09nube@gmail.com', 'Luis')
print(SPApiProxy.get_list_of_senders())
SPApiProxy.sms_add_phones(ADDRESSBOOK_ID, ['+50587460295'])
SPApiProxy.sms_add_campaign_by_phones('Luis', '+50587460295', 'Este es el cuerpo del mensaje SMS', 'test')
