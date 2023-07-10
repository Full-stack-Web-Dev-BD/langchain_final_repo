from ssml_builder.core import Speech

def gen_rep(msg, url):
    return {
        'fulfillment_response': {
            'messages': [{
                    'play_audio': {
                        'audio_uri': url
                    }
                }]
        }
    }

def gen_target_page(page, msg):
    return {
        'fulfillment_response': {
            'messages': [{
                    'text': {
                        'text': [msg]
                    }
                }]
        },
        "target_page": page
    }

def gen_trans_rep(trans_number):
    return {
        'fulfillment_response': {
            'messages': [{
                    'liveAgentHandoff':{
                        "metadata":{
                            "center": "ASD",
                            "centerPhone": str(trans_number)
                        }
                    }
                }]
        }
    }

def gen_text_rep(msg):
    return {
        'fulfillment_response': {
            'messages': [{
                    'text': {
                        'text': [msg]
                    }
                }]
        }
    }


def gen_test(msg):
    speech = Speech()
    speech.add_text('I am Python Webhook.')
    speech.voice(value=msg, name="Kendra")
    generated_speech = speech.speak()
    return {
        'fulfillment_response': {
            'messages': [
                {
                    'text': {
                        'text': [msg]
                    }
                },
                {
                    'output_audio_text': {
                        'ssml': generated_speech
                    }
                }
            ]
        }
    }
