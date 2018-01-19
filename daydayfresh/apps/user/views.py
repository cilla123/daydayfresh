
from random import choice

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from utils.yunpian import YunPian

from .serializers import SmsSerializer, UserRegSerializer
from .models import VerifyCode
from daydayfresh.settings import APIKEY

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return e

class SmsCodeViewset(CreateModelMixin, GenericViewSet):
    '''
    发送短信验证码
    '''
    serializer_class = SmsSerializer

    def generate_code(self):
        '''
        生成四位数字的验证码
        :return:
        '''
        seeds = "1234567890"
        ramdom_str = []
        for i in range(4):
            ramdom_str.append(choice(seeds))

        return "".join(ramdom_str)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]

        code_record = VerifyCode(code="1234", mobile=mobile)
        code_record.save()
        return Response({
            "mobile": mobile
        }, status=status.HTTP_201_CREATED)


        # yun_pian = YunPian(APIKEY)
        #
        # code = self.generate_code()
        #
        # sms_status = yun_pian.send_sms(code=code, mobile=mobile)
        #
        # if sms_status["code"] != 0:
        #     return Response({
        #         "mobile": sms_status["msg"]
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     code_record = VerifyCode(code=code, mobile=mobile)
        #     code_record.save()
        #     return Response({
        #         "mobile": mobile
        #     }, status=status.HTTP_201_CREATED)

class UserViewSet(CreateModelMixin, viewsets.GenericViewSet):
    '''
    用户
    '''
    serializer_class = UserRegSerializer