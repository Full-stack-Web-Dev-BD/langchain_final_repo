from voximplant.apiclient import VoximplantAPI, VoximplantException
import pytz
import datetime
import requests

if __name__ == "__main__":
    api = VoximplantAPI("credentials.json")

    # Get the first call session history record from the 2012-01-01 00:00:00 UTC to the 2014-01-01 00:00:00 UTC

    now = datetime.datetime.now()
    FROM_DATE = datetime.datetime(2022, 12, 28, 16, 14, 27)
    TO_DATE = datetime.datetime(2022, 12, 28, 16, 15, 30)
    COUNT = 60
    
    res = api.get_call_history(FROM_DATE, TO_DATE, count=COUNT)
    url = res['result'][-1]['log_file_url']

    auth_header = api.build_auth_header()
    response = requests.get(url, headers={"Authorization": auth_header})
    log = response.text

    idx = log.find('callerid')
    print(log[idx + 11 : idx + 22])
