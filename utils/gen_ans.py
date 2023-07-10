import random

def default_welcome():
    msg = ["Green Cremation Texas! This is Sam."]
    id = [492]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def question_getname():
    msg = ["Can I get your name, please?"]
    id = [91]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def not_match_default():
    msg = ['I missed what you said. What was that?', 'Sorry, can you say that again?']
    id = [94, 95]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def got_name(name):
    msg = ['How can I help you?', 'What can I do for you?']
    id = [82, 83]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def say_sorry():
    msg = ["Yes, I can help you with that and my condolences."]
    id = [293]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ask_num():
    return 'What is the best call back number for you?', 81

def ask_relationship():
    return "Can you tell us about your relationship with the deceased?", 2

def ans_faq_1():
    msg = ['Our most common questions are about cremation pricing, or death certificate pricing.']
    id = [54]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_2():
    msg = ["This usually takes 4-6 weeks, and they'll be mailed to you by the state of Texas. There are options to expedite the death certificates, the price for that is in our general price list if you are interested."]
    id = [273]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_3():
    msg = ["Each of our cremation packages come with at least 3 death certificates. But you can order more. We recommend that you order at least 10. You should get more than you think you'll need. It's better to have too many than not enough.",
           "Each of our cremation packages come with at least 3 death certificates, but you can easily add more."
           ]
    id = [274, 276]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_4():
    msg = ['We notify the social security administration on your behalf.', 
            'This is just part of the service that we provide you.',
            'There is nothing that you need to do to notify social security. We take care of that for you.'
            ]
    id = [23, 24, 25]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_5():
    msg = ["Well, I estimate that it takes roughly two weeks from when we have a loved one in our care for Cremation itself to take place. And as far as turnaround time to receive cremated remains, that's roughly three to four weeks total. This timeline could be sooner, but it does depend on the Doctor and the County."]
    id = [278]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_6():
    msg = ["I can do my best to answer your questions, but you’ll likely need to speak with our Funeral Director to get more specific pricing answers. The cost for a Cremation starts out at $995."]
    id = [480]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_7():
    msg = ["Yes, we offer an array of urns and keepsakes. They range in price from $20 to $600.",
           "Our cremation packages come with a default urn which is a white cardboard box, but you can easily change it to any of our available urns. They range in price from $20 to $600."
            ]
    id = [279, 280]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_8():
    return "We have three physical locations in the Austin area, but we service the entire state. Our primary location is in central Austin. Our two satellite locations are in South Austin and in Pflugerville.", 266

def ans_faq_9():
    return 'Our normal business hours are Monday through Friday 9am to 5pm. But, we are "open" 24/7. All of our locations are appointment only.', 38

def ans_faq_10():
    return 'We service the entire state, but our primary service area is 35 miles from our central Austin location. This means that the transportation cost for any cases outside of our primary service area there is a $3.50/mile fee.', 39

def ans_faq_11():
    msg = ['You can see our complete general price list on our website cremation.green.',
            'There are several factors that should be considered as far as location and conditions.'
    ]
    id = [282, 283]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_12():
    return "Our most common questions are about cremation pricing, or death certificate pricing.", 6

def ans_faq_13():
    return "Yes, it is cremation.green. That is Cremation, singular dot green like the color. Cremation.green.", 272

def ans_faq_14():
    return "We do not offer traditional chapel services or formal viewings, but there is the ability to witness the cremation. It is 15 minutes and 5 people maximum to be present at the time of cremation, this does allow families to say final goodbyes to their loved one. The cost for a witness cremation can vary from $500-900 depending on individual circumstances. Since we do not embalm or do cosmetics, the viewing ability is largely determined upon your loved one's physical condition.", 281

def ans_faq_15():
    msg = ["My name is Sam. I'm a virtual assistant for Green Cremation Texas. I'm here to help answer questions that you may have.",
            "I'm Sam a virtual assistant for Green Cremation Texas.",
            "I'm a virtual assistant for Green Cremation Texas. My name is Sam."
        ]
    id = [60, 61, 62]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_16():
    return "Yes, we have simplified the cremation process to 7 steps. We created a short video that is on our website that explains it in greater details. Essentially, the process starts with us picking up your loved one and bringing them into our care. We will send you information to get set up on our simple online system. There are several forms that we need signed by the Legal Next of Kin and/or the primary point of contact. We also need a doctor to sign off on the death certificate. Then, we will schedule cremation. Afterwards we will return the cremated remains to you.", 65

def ans_faq_17():
    return "At this point, I am not able to provide that information. But, I can assure you that our Funeral Director, Marlaena will communicate that information to you. You can also refer to your online dashboard to see the current status and estimated dates.", 66

def ans_faq_18():
    return "Ok, yes. I understand that you're wanting to start planning ahead. That is a very good idea. We have put together an excellent resource that will answer all of your questions. Just go to cremation.green/plan", 265

def ans_faq_19():
    return "I'm so sorry. We do not offer pet cremation.", 68

def ans_faq_20():
    return "The cost for a Cremation starts out at $995. All that you need to do to secure our services is to give the hospital or hospice our name and phone number. They will call us when the time comes, and we begin the arrangements from there.", 312

def ans_faq_21():
    msg = ["The Cost for water cremation starts at $1,995. Water cremation is not currently legal in Texas, so out of state transport is involved. The airfare cost is $700",
            "$1,995, not including extra costs like airfare to the water cremation facility, or additional choices like urns and death certificates."
        ]
    id = [451, 452]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_22():
    msg = ["Depending on how quickly it takes for the Doctor to sign off on the death certificates, we usually anticipate about 4 weeks before cremated remains are ready to be brought home"
        ]
    id = [453]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_23():
    msg = ["Water cremation is a process of cremation that uses water and alkaline solution to replace the flame of a traditional cremation. It is an environmentally friendly alternative to flame cremation. It is unfortunately not legal in Texas, but we offer this through out of state transport."
        ]
    id = [454]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_24():
    msg = ["You can certainly provide an urn, however there is a cost of $25 for us to fill the urn. Urn filling is only done at our Central location"]
    id = [455]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_25():
    msg = ["Absolutely, there is a cost of $25 per separation. The cost does not include an urn or keepsake."]
    id = [456]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_26():
    msg = ["If you need more death certificates, you are able to order copies through the state vital statistics department in person- or online at texas.gov."]
    id = [457]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_27():
    msg = ["The cost for natural burial starts at $2,585. This does not include: A casket, cemetery plot, or opening and closing of the grave."]
    id = [458]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_28():
    msg = ["We now offer third party payment plans through a partnership with PayPal credit. The details are on our website cremation.green/payment-options."]
    id = [459]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_29():
    msg = ["Our central Austin funeral home is located at 6448 East Highway 290"]
    id = [267]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_30():
    msg = ["Our South Austin funeral home is located at 10415 Old Manchaca Rd."]
    id = [270]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_31():
    msg = ["Our Pflugerville funeral home is located at 1019 S Heatherwilde Blvd."]
    id = [271]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq_32():
    msg = ["Yes, I’m happy to help. What would you like more information about? Our most common questions are about cremation pricing, or death certificate pricing. Other than that, we get more general questions about the cremation process and the types of urns that we offer."]
    id = [474]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def ans_faq(x):
    arr = [ans_faq_1, ans_faq_2, ans_faq_3, ans_faq_4, ans_faq_5, ans_faq_6, ans_faq_7, ans_faq_8, ans_faq_9, ans_faq_10, ans_faq_11, ans_faq_12, ans_faq_13, ans_faq_14, ans_faq_15, ans_faq_16, ans_faq_17, ans_faq_18, ans_faq_19, ans_faq_20, ans_faq_21, ans_faq_22, ans_faq_23, ans_faq_24, ans_faq_25, ans_faq_26, ans_faq_27, ans_faq_28, ans_faq_29, ans_faq_30, ans_faq_31, ans_faq_32]
    return arr[x - 1]()

def make_call_back():
    return "I'm sorry. Our Funeral Director, Marlaena, is not available at the moment. I'll take your name and number and have her call you back shortly.", 69

def ask_anything_else():
    msg = [' ']
    id = [242]   
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]

def greetings():
    msg = ['']
    id = [496]
    idx = random.randint(0, len(msg) - 1)
    return msg[idx], id[idx]