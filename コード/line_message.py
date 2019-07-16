import requests
import socket
import xml.etree.ElementTree as ET

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 10500))

try:
    data = ''
    token = '(トークン)'  #取得したトークン
    
    while True:
        if '</RECOGOUT>\n.' in data:
            root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
            for whypo in root.findall('./SHYPO/WHYPO'):
                command = whypo.get('WORD')
                score = float(whypo.get('CM'))
                
                print(command)
                
                if score >= 0.9:
                    if command == u'会社休みます':
                        payload = {'message': '   会社休みます'}
                        url = 'https://notify-api.line.me/api/notify'
                        headers = {'Authorization': 'Bearer ' + token}

                        res = requests.post(url, data=payload, headers=headers)
                        print(res)
                
                    elif command == u'会議欠席します':
                        payload = {'message': '   会議欠席します'}
                        url = 'https://notify-api.line.me/api/notify'
                        headers = {'Authorization': 'Bearer ' + token}

                        res = requests.post(url, data=payload, headers=headers)
                        print(res)
                        
                        
                    elif command == u'熱があります':
                        payload = {'message': '   熱があります'}
                        url = 'https://notify-api.line.me/api/notify'
                        headers = {'Authorization': 'Bearer ' + token}

                        res = requests.post(url, data=payload, headers=headers)
                        print(res)
                        
                print('\n')
            data = ''
            
        else:
            data = data + client.recv(1024).decode('utf-8')

except KeyboardInterrupt:
    client.close()