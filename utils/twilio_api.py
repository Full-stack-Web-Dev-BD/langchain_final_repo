from twilio.rest import Client

def send_sms(account_sid, auth_token, to_id, msg):
    client = Client(account_sid, auth_token)
    client.messages.create(to = to_id, from_ = "+15129420750", body = msg)
    return
