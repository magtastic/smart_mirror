import json
import os
import requests
from requests_cloudkit import CloudKitAuth


def getiCloudConfig():
    with open('config.json') as json_data:
        return json.load(json_data)['icloud']


class iCloud:
    def __init__(self):
        config = getiCloudConfig()
        filePath = '{currDir}/{relativeFilePath}'.format(
            currDir=os.getcwd(),
            relativeFilePath=config['key_file_path']
        )

        self.baseUrl = 'https://api.apple-cloudkit.com/database'
        self.version = 1
        self.container = 'iCloud.Magtastic.SmartMirror'
        self.environment = 'development'

        print(filePath)
        self.auth = CloudKitAuth(
            key_id=config['key_id'],
            key_file_name=filePath
        )

        self.getSomething()

    def getUrl(self, subPath):
        return '{baseUrl}/{version}/{container}/{environment}/{subPath}'.format(
            baseUrl=self.baseUrl,
            version=self.version,
            container=self.container,
            environment=self.environment,
            subPath=subPath
        )

    def getSomething(self):
        url = self.getUrl('public/users/caller')
        r = requests.get(
            url,
            auth=self.auth
        )
        print(r.status_code)
        print(r.json())
