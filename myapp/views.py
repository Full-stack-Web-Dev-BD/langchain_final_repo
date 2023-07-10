from __future__ import print_function
from json import loads
from logging import getLogger
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os.path
import os
from dotenv import load_dotenv
from django.conf import settings
from django.templatetags.static import static

from django.shortcuts import render
from .forms import ChatForm
# from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
import openai
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.llms import OpenAI
from langchain.memory import ConversationEntityMemory

from langchain.chains import ConversationChain
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from pydantic import BaseModel
from typing import List, Dict, Any

llm = OpenAI(temperature=0)
memory = ConversationEntityMemory(llm=llm)

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = os.getenv("MODEL_ENGINE")
index = None

current_path = os.path.dirname(os.path.abspath(__file__))

def initialize_loader(URL):
    relative_path = ".." + URL
    loader = PyPDFLoader(os.path.abspath(os.path.join(current_path, relative_path)))
    global index 
    index = VectorstoreIndexCreator().from_loaders([loader])
    print(index)

def home(request):
    # sendEmail('Test email sending Django Backend');
    return render(request,'index.html')


def check_answer(s):
    sign = ".!?"
    if sign.find(s[-1]) == -1:
        p1 = s.rfind(".")
        p3 = s.rfind("!")
        p4 = s.rfind("?")
        p = max(p1, p3, p4)
        s = s[: p + 1]

    return s



def upload(request):
    context = {}
    if request.method == "POST" and request.FILES["file"]:
        myfile = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        initialize_loader(uploaded_file_url)
        context['url'] = uploaded_file_url
        return render(
            request, "chatPDF.html", context
        )
    return render(request, "chatPDF.html")

def oldUpload(request):
    context = {}
    if request.method == "POST" and request.FILES["file"]:
        myfile = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        initialize_loader(uploaded_file_url)
        context['url'] = uploaded_file_url
        return render(
            request, "upload.html", context
        )
    return render(request, "upload.html")




def chatPDF(request):
    context = {}
    if request.method == "POST" and request.FILES["file"]:
        myfile = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        initialize_loader(uploaded_file_url)
        context['url'] = uploaded_file_url
        print("context is ", context)
        return JsonResponse(context)
    return JsonResponse({})

def chatbot_response(user_input):

    model = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model,
        prompt=user_input,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Print the response
    response = completion.choices[0].text
    id = response.find("\n\n")
    if id == -1:
        return response
    else:
        return response[id + 2 :]


def google_search(input):
    search = SerpAPIWrapper()
    google = search.run(input)

    return google


def chatGPT(input):
    conversation = ConversationChain(
        llm=llm, verbose=True, prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE, memory=memory
    )

    prediction = conversation.predict(input=input)

    return prediction


def search_database(input):
    text = index.query(input)
    return text


def testimonial_test(input):
    template = "You are a virtual assistant to transfer the input text into a keyword."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = """{text} is input text. If the input text is mentioning about Google Search, you just say one word "Google.".
    If the input text is mentioning about ChatGPT, you just say one word "ChatGPT.". 
    Customer: "I am sorry, you can try using Google Search"
    You: "Google."
    Customer: "I am sorry, you can try using ChatGPT"
    You: "ChatGPT."
    Customer: "I am sorry, you can try using Google Search to find out the name of the person"
    You: "Google."
    Customer: "I am sorry, you can try using ChatGPT to generate a funny story"
    You: "ChatGPT."
    Customer: {text}
    You: 
    """
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )
    chat = ChatOpenAI(temperature=1)

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    testimonial = chain.run(text=input)

    return testimonial


def chatbot_response_fine_tuned(user_input):
    bot_response = search_database(user_input)

    bot_response_testimonial = testimonial_test(bot_response).split(":")[-1].strip()

    if bot_response_testimonial == "Google.":
        it1 = str(user_input).rfind("Customer:")
        it2 = str(user_input).rfind("You:")
        tmp = str(user_input)[it1 + 9 : it2 - 2]
        print("Googling...")
        response = google_search(tmp)

    elif bot_response_testimonial == "ChatGPT.":
        print("ChatGPT...")
        response = chatGPT(user_input)

    else:
        response = bot_response
    return response

def chattingView(request):
    form = ChatForm()

    return render(request, "chatting.html", {"form": form})


@api_view(("POST",))
def chatting(request):
    print("text chat ")
    try:
        msg = request.POST.get("msg")
        if msg == None or msg == "":
            resp = dict(err="Not Found")
            return Response(resp, status=400)
        reply = chatbot_response(msg)
        resp = dict(reply=reply)
        if reply.find("ยง") == -1:
            return Response(resp, status=200)
        else:
            return Response(resp, status=500)
    except:
        resp = dict(err="Server Error")
        return Response(resp, status=500)

@api_view(("POST",))
def chatting_tuned(request):
    try:
        msg = request.POST.get("msg")
        if msg == None or msg == "":
            resp = dict(err="Not Found")
            return Response(resp, status=400)
        reply = chatbot_response_fine_tuned(msg)
        resp = dict(reply=reply)
        if reply.find("ยง") == -1:
            return Response(resp, status=200)
        else:
            return Response(resp, status=500)
    except:
        resp = dict(err="Server Error")
        return Response(resp, status=500)


def chatting_tunedView(request):
    form = ChatForm()

    return render(request, "chatting_tuned.html", {"form": form})

@csrf_exempt
def webhook(request):
    return 0


def check_availability(request):
    return 0


@api_view(("GET",))
def set_caller_id(request):
    return 0


@api_view(("GET",))
def get_SessionId(request):
    return 0


@api_view(("GET",))
def get_SessionId_Suc(request):
    return 0