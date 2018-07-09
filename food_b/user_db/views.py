# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from user_functions import *
from organization_chart.models import WizEmployee, WizCurrentPeopleRelation, WizGroups, WizGroupsPeopleRelation
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# Create your views here.

class fCreateUser(APIView):
    permission_classes = (IsAuthenticated, )
    authenticated_classes = (JSONWebTokenAuthentication, )

    def post(self, request, format=None):
        email = request.data.get('email')
        mobile_num = request.data.get('mobile_number')
        if not email or not mobile_num:
            return Response("Need both email and mobile number", status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(user=email)
        address = request.data.get('address', {})
        add_phone_and_address(user, mobile_num, address)



