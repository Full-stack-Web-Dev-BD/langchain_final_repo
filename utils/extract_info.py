def get_session_id(req):
    if not "sessionInfo" in req.keys():
        return ""
    if not "session" in req["sessionInfo"].keys():
        return ""
    return req["sessionInfo"]["session"][-25:]

def get_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['name']['name']
    if "person" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['person']['name']
    return ""

def get_name_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['name']['original']
    if "person" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['person']['original']
    return ""

def get_callertype(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "persontype" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["persontype"]
    else:
        return ""

def get_phone_number(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "telefono" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['telefono']
    if "tel_cr" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['tel_cr']
    if "phone-number" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['phone-number']
    return ""

def get_relacion(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "relacion" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['relacion']
    return ""

def get_eta_phone(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "eta_phone" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['eta_phone']
    return ""

def get_eta_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "eta_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['eta_name']['name']
    return ""

def get_eta_name_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "eta_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['eta_name']['original']
    return ""

def get_geo_city(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "geo-city" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['geo-city']
    return ""

def get_relationship(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "personrelationship" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['personrelationship']
    return ""

def get_msg_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "msg_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['msg_name']["name"]
    return ""

def get_msg_name_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "msg_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['msg_name']["original"]
    return ""

def get_personorg(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "personorganization" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["personorganization"]
    return ""

def get_facility_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "facility_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["facility_name"]
    return ""

def get_firstname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "difunto_nombre" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['difunto_nombre']['name']
    return ""

def get_firstname_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "difunto_nombre" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['difunto_nombre']['original']
    return ""

def get_lastname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "dlast_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['dlast_name']["name"]
    else:
        return ""
    
def get_lastname_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "dlast_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['dlast_name']["original"]
    else:
        return ""

def get_dob(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if not "dob" in req['sessionInfo']['parameters'].keys():
        return ""
    return (str(int(req['sessionInfo']['parameters']['dob']['month'])) + "/" + str(int(req['sessionInfo']['parameters']['dob']['day'])) + "/" + str(int(req['sessionInfo']['parameters']['dob']['year'])))

def get_facility_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "facility_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['facility_name']
    return ""

def get_location_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    return req['sessionInfo']['parameters']['location_name']

def get_location_addr(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "location_addr" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["location_addr"]
    return ""

def get_topic(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "topic" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["topic"]
    else:
        return ""

def get_subtopic(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "subtopic" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["subtopic"]
    else:
        return ""

def get_nurse_phone_extension(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nurse_phone_extension" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nurse_phone_extension"]
    else:
        return ""

def get_tel_cr(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "telefono" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["telefono"]
    if "tel_cr" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['tel_cr']
    if "phone-number" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']['phone-number']
    else:
        return ""

def get_location_type(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "type" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["type"]
    else:
        return ""

def get_tag(req):
    return req["fulfillmentInfo"]["tag"]

def get_speech(req):
    if 'transcript' in req.keys():
        return str(req["transcript"])
    elif 'text' in req.keys():
        return str(req['text'])
    else:
        return ''

def get_nd_fname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_fname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_fname"]["name"]
    else:
        return ""

def get_nd_fname_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_fname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_fname"]["original"]
    else:
        return ""

def get_spell_fname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "spell_fname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["spell_fname"]
    else:
        return ""
    
def get_nd_lname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_lname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_lname"]["name"]
    else:
        return ""

def get_nd_lname_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_lname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_lname"]["original"]
    else:
        return ""

def get_certifier_fname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "certifier_fname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["certifier_fname"]["name"]
    else:
        return ""

def get_certifier_fname_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "certifier_fname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["certifier_fname"]["original"]
    else:
        return ""

def get_certifier_lname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "certifier_lname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["certifier_lname"]["name"]
    else:
        return ""

def get_certifier_lname_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "certifier_lname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["certifier_lname"]["original"]
    else:
        return ""

def get_hcertifier_phone(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "certifier_phone" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["certifier_phone"]
    else:
        return ""

def get_spell_lname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "spell_lname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["spell_lname"]
    else:
        return ""
    
def get_spell_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "spell_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["spell_name"]
    else:
        return ""

def get_nd_weight(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_weight" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_weight"]
    else:
        return ""

def get_nd_gender(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_gender" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_gender"]
    else:
        return ""

def get_nd_dob(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_dob" in req['sessionInfo']['parameters'].keys():
        return (str(int(req['sessionInfo']['parameters']['nd_dob']['month'])) + "/" + str(int(req['sessionInfo']['parameters']['nd_dob']['day'])) + "/" + str(int(req['sessionInfo']['parameters']['nd_dob']['year'])))
    else:
        return ""

def get_date_time(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "date-time" in req['sessionInfo']['parameters'].keys():
        return (str(int(req['sessionInfo']['parameters']['date-time']['month'])) + "/" + str(int(req['sessionInfo']['parameters']['date-time']['day'])))
    else:
        return ""

def get_nd_dod(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_dod" in req['sessionInfo']['parameters'].keys():
        return (str(int(req['sessionInfo']['parameters']['nd_dod']['month'])) + "/" + str(int(req['sessionInfo']['parameters']['nd_dod']['day'])))
    else:
        return ""

def get_nd_diseases(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_diseases" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_diseases"]
    else:
        return ""

def get_nd_location_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_location_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_location_name"]
    else:
        return ""

def get_nd_location_addr(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_location_addr" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_location_addr"]
    else:
        return ""

def get_nd_type_death_place(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_type_death_place" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_type_death_place"]
    else:
        return ""

def get_nd_room_number(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_room_number" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_room_number"]
    else:
        return ""

def get_nd_stairs(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_stairs" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_stairs"]
    else:
        return ""

def get_nd_lnk_fname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_lnk_fname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_lnk_fname"]["name"]
    else:
        return ""

def get_nd_lnk_fname_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_lnk_fname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_lnk_fname"]["original"]
    else:
        return ""

def get_nd_lnk_lname(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_lnk_lname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_lnk_lname"]["name"]
    else:
        return ""

def get_nd_lnk_lname_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_lnk_lname" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_lnk_lname"]["original"]
    else:
        return ""

def get_nd_lnk_rel(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_lnk_rel" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_lnk_rel"]
    else:
        return ""

def get_nd_lnk_phone(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "nd_lnk_phone" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["nd_lnk_phone"]
    else:
        return ""

def get_certifier_name(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "certifier_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["certifier_name"]["name"]
    else:
        return ""

def get_certifier_name_origin(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "certifier_name" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["certifier_name"]["original"]
    else:
        return ""

def get_certifier_phone(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "certifier_phone" in req['sessionInfo']['parameters'].keys():
        return req['sessionInfo']['parameters']["certifier_phone"]
    else:
        return ""

def get_phone_extension(req):
    if not "parameters" in req['sessionInfo'].keys():
        return ""
    if "number" in req['sessionInfo']['parameters'].keys():
        return int(req['sessionInfo']['parameters']["number"])
    else:
        return ""