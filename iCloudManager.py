from pyicloud import PyiCloudService
import sys
import json

def getiCloudConfig():
    with open('config.json') as json_data:
        return json.load(json_data)['icloud']

class iCloud:
    def __init__(self):
        config = getiCloudConfig()
        self.acc = config['accountName']
        self.pw = config['accountPw']
        self.api = PyiCloudService(self.acc, self.pw)
        # self.check2fa()

    def check2fa(self):
        if self.api.requires_2sa:
            import click
            print "Two-step authentication required. Your trusted devices are:"

            devices = self.api.trusted_devices
            for i, device in enumerate(devices):
                print "  %s: %s" % (i, device.get('deviceName',
                    "SMS to %s" % device.get('phoneNumber')))
                device = click.prompt('Which device would you like to use?', default=0)
                device = devices[device]
                if not self.api.send_verification_code(device):
                    print "Failed to send verification code"
                    sys.exit(1)

                code = click.prompt('Please enter validation code')

                if not self.api.validate_verification_code(device, code):
                    print "Failed to verify verification code"
                    sys.exit(1)


