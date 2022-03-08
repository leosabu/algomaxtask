
import os.path

from django.shortcuts import render
from rest_framework import views,response
from pathlib import Path
import json
import requests


def ratioFunction(num1, num2):
    import math
    x = num1
    y = num2
    a=str(int(round(x / (math.gcd(num1,num2)), 0)))
    b=str(int(round(y / (math.gcd(num1, num2)), 0)))
    ratio={"w":a,"m":b}
    print("ratio",a,b)
    return ratio

BASE_DIR = Path(__file__).resolve().parent.parent

class Resources(views.APIView):
    def get(self,request,*args,**kwargs):
        # path="static\\"+"senate.json"
        path="C:\\Users\\Lenovo\\PycharmProjects\\algomax task\\senate\\api\\static\\senate.json"

        try:
            with open(path,encoding="utf8") as file:
                data=json.load(file)
                gender_list = list(map(lambda dat: dat["person"]["gender"], data))
                male_count = gender_list.count("male")
                female_count = gender_list.count("female")
                print(male_count)
                print(female_count)

                result=ratioFunction(male_count, female_count)
                # print("here")
                # print(file)
            return response.Response({"ratio":result})
        except Exception as e:
            return response.Response({"error":"file not found"})


class senatelist(views.APIView):
    def get(self, request, *args, **kwargs):
        path = "C:\\Users\\Lenovo\\PycharmProjects\\algomax task\\senate\\api\\static\\senate.json"
        with open(path, encoding="utf8") as file:
            data = json.load(file)
        # return response.Response({"result":data})
        return render(request,'index.html',{"result":data})

class senate(views.APIView):  # class based view is created for get and post method
    def get(self, request, *args, **kwargs):
        # path="static\\"+"senate.json"
        path = "C:\\Users\\Lenovo\\PycharmProjects\\algomax task\\senate\\api\\static\\senate.json"

        try:
            with open(path, encoding="utf8") as file:
                data = json.load(file)
                return response.Response({"data": data})

        except Exception as e:
            return response.Response({"error": "file not found"})




