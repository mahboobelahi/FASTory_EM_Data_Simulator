# Import libraries
import threading, time, requests,json,csv,Utility_FUNC
from flask import Flask, request
import configurations as CONFIG


app = Flask(__name__)

@app.route('/')
def welcom():

    return f"<h1>Hello from {CONFIG.DEVICE_NAME}, listening at {CONFIG.LocIP}:{CONFIG.LocPort}<h1>"

@app.route('/simulate', methods= ['GET'])
def simulateData():
    id= CONFIG.DEVICE_ID
    url= '127.0.0.1'
    thread = threading.Timer(.1, Utility_FUNC.publish_measurements,args=(id,url))
    thread.daemon=True
    thread.start()
    return 'OK'



if __name__ == "__main__":

    threading.Timer(2, Utility_FUNC.sub_or_Unsubscribe_DataSource,
                args=(CONFIG.ASYNCH_URL, CONFIG.DEVICE_ID, True)
                ).start()

    threading.Timer(4, Utility_FUNC.publish_measurements,
            args=('127.0.0.1', CONFIG.DEVICE_ID, True)
            ).start()
    
    app.run(host=CONFIG.LocIP, port=CONFIG.LocPort)
