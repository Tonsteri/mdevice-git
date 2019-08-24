

import RPi.GPIO as GPIO
#import time



#Import libraries ADXL i2c
import time         #sleep()
import board            #fast pinlayout
import busio            #for handling several serial protovols
import adafruit_adxl34x     #for reading sensor

#led blink
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)
print ("LED on")
GPIO.output(13,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(13,GPIO.LOW)


#prepare i2c connection SCL SDA
i2c = busio.I2C(board.SCL, board.SDA)   

#print (i2c)

#accelerometer object to read etc.
accelerometer = adafruit_adxl34x.ADXL345(i2c)   


#Print sensor values
while True:
    print("%f %f %f"%accelerometer.acceleration)    #printataan objectin arvo
    
#tiedostoon kirjoitus
    dataAsInt = (accelerometer.acceleration)
    dataAsString = str(dataAsInt)

    fb = open('/home/pi/mdevice/Data/acctest1','a+')
    fb.write(dataAsString) 
    fb.write('\n')
    fb.close()
    
    time.sleep(1)                 #delay
