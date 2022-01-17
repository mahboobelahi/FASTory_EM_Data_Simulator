import requests, csv, time
import configurations as CONFIG

def sub_or_Unsubscribe_DataSource(ASYNCH_URL,DEVICE_ID,subs=False):
    
    if subs:
        req= requests.get(f'{ASYNCH_URL}/unsubscribe',
                params={"externalId":DEVICE_ID,"topicType":'multi' })
        print(f'Subscribing to Data Source: {DEVICE_ID}....')
        req= requests.get(f'{ASYNCH_URL}/subscribe',
                        params={"externalId":DEVICE_ID,"topicType":'multi' })
        if req.status_code ==200:
                print(f'Subscrption Status: {req.status_code} {req.reason}')
        else:
            print(f'Subscrption Status: {req.status_code} {req.reason}')
    else:
        req= requests.get(f'{ASYNCH_URL}/unsubscribe',
                        params={"externalId":DEVICE_ID,"topic":'multi' })

        if req.status_code ==200:
            print(f'Unsubscrption Status: {req.status_code} {req.reason}')
        else:
            print(f'Unsubscrption Status: {req.status_code} {req.reason}')

def publish_measurements(external_ID,url):
    with open(CONFIG.FILE_NAME, 'r') as file: #with open('N_Measurements9.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            time.sleep(1)
            req_V=requests.post(url=f'{CONFIG.SYNCH_URL}/sendMeasurement?externalId={external_ID}&fragment=CurrentMeasurement&value={row["RMS Current (A)"]}&unit=A')
            req_A=requests.post(url=f'{CONFIG.SYNCH_URL}/sendMeasurement?externalId={external_ID}&fragment=VoltageMeasurement&value={row["RMS Voltage (V)"]}&unit=V')

            req_P=requests.post(url=f'{CONFIG.SYNCH_URL}/sendMeasurement?externalId={external_ID}&fragment=PowerMeasurement&value={row["Power (W)"]}&unit=W' )
            print( f'{req_A}, {req_V} ,{req_P.status_code}, {external_ID}')
            # print(row['RMS_Current(A)'],
            #       row['RMS_Voltage(V)'],
            #       row['Power(W)'])
        url=url+'/simulate'
        req= requests.get(url)
 