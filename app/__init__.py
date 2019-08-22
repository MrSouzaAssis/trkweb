from flask import Flask
app = Flask(__name__)

# import time
# import paho.mqtt.client as paho
# broker="postman.cloudmqtt.com"
# #define callback
# def on_message(client, userdata, message):
#     time.sleep(1)
#     print("received message =",str(message.payload.decode("utf-8")))



# client= paho.Client("client-py001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
# ######Bind function to callback
# client.username_pw_set(username="umszfjyq",password="ZQcRUlqMSUZA")
# client.on_message=on_message
# #####
# print("connecting to broker ",broker)
# client.connect(broker,10926)#connect
# client.loop_start() #start loop to process received messages
# print("subscribing ")
# client.subscribe("sensors/testsensor")#subscribe
# time.sleep(2)
# print("publishing ")
# client.publish("sensors/testsensor","luquinha eu sou um app em python")#publish
# # client.disconnect() #disconnect
# # client.loop_stop() #stop loop

import time
import paho.mqtt.client as paho
broker="soldier.cloudmqtt.com"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))



client= paho.Client("client-py001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.username_pw_set(username="xoudbsxb",password="dt9e-nGjqgdS")
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker,18508)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("festa")#subscribe
time.sleep(2)
print("publishing ")
client.publish("festa","Opa fala js, aqui é o python")#publish
# client.disconnect() #disconnect
# client.loop_stop() #stop loop



from app import views, models