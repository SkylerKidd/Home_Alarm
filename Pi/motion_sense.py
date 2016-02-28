import RPi.GPIO as GPIO
import time
import json, urllib2

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

config = {}
execfile('settings.conf', config)

data = {
    'title': 'Alarm Trip',
    'msgAlert': 'Alert!',
    password = config['password']
}

try:
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(2)
    print "Ready"

    while True:
        if GPIO.input(PIR_PIN):
            req = urllib2.Request('http://homealarm.herokuapp.com/alert')
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req, json.dumps(data))
            print "Motion Detected"
            print "Msg sent: " + str(data['msgAlert'])
            time.sleep(6)
        else:
            print "Motion Not Detected"
        time.sleep(1)
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
