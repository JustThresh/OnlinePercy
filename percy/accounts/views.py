from django.shortcuts import render
# Create your views here.
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import TestModel


class AddAccounts(APIView):
    permission_classes = permissions.AllowAny,

    # 获取登录者的ip -wf-18-11-19
    def get_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
        return ip

    def get(self, request):
        try:
            print(request)
            name = request.GET.get('name', None)
            print(1)
            TestModel.objects.create(
                name=name
            )
        except Exception as a:
            print(a)
        # new_data = TestModel()
        # print(2)
        # new_data.name = name
        # print(3)
        # try:
        #     new_data.save(update_fields=['name', 'id'])
        # except Exception as e:
        #     print(e)
        # print(4)
        ip = self.get_ip(request)
        return Response(ip, status=status.HTTP_200_OK)
