from rest_framework import viewsets
from rest_framework.response import Response
from Apps.mixins import is_admin_registered, is_authenticated
from .models import Apps, AdminUser
from .serializers import AppsSerializer


class AppsApi(viewsets.ViewSet):
    def list(self, request):
        queryset = Apps.objects.all()
        serializer = AppsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if 'username' in request.data and 'password' in request.data:
           username = request.data.get('username', '')
           if username is not '':
               if is_admin_registered(user=username):
                   password = request.data.get('password', None)
                   if is_authenticated(user=username, password=password):
                        serializer = AppsSerializer(data=request.data)
                        if serializer.is_valid():
                            user = AdminUser.objects.get(admin_username=username)
                            serializer.save(admin_user=user)
                            return Response(serializer.data)
                        return Response(serializer.errors)
                   return Response({'msg': 'Invalid Password'})
               return Response({'msg': 'username is not registered'})
           return Response({'msg': 'Invalid Credentials'})
        return Response({'msg': 'Credentials are not provided'})

    def retrieve(self, request, pk):
        app = Apps.objects.get(id=pk)
        serializer = AppsSerializer(app)
        return Response(serializer.data)

    def update(self, request, pk):
        if 'username' in request.data and 'password' in request.data:
            username = request.data.get('username', '')
            if username is not '':
                if is_admin_registered(user=username):
                    password = request.data.get('password', None)
                    if is_authenticated(user=username, password=password):
                        app = Apps.objects.get(id=pk)
                        serializer = AppsSerializer(app, data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data)
                        return Response(serializer.errors)
                    return Response({'msg': 'Invalid Password'})
                return Response({'msg': 'username is not registered'})
            return Response({'msg': 'Invalid Credentials'})
        return Response({'msg': 'Credentials are not provided'})

    def partial_update(self, request, pk):
        if 'username' in request.data and 'password' in request.data:
            username = request.data.get('username', '')
            if username is not '':
                if is_admin_registered(user=username):
                    password = request.data.get('password', None)
                    if is_authenticated(user=username, password=password):
                        app = Apps.objects.get(id=pk)
                        serializer = AppsSerializer(app, data=request.data, partial=True)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data)
                        return Response(serializer.errors)
                    return Response({'msg': 'Invalid Password'})
                return Response({'msg': 'username is not registered'})
            return Response({'msg': 'Invalid Credentials'})
        return Response({'msg': 'Credentials are not provided'})

    def destroy(self, request, pk):
        if 'username' in request.data and 'password' in request.data:
            username = request.data.get('username', '')
            if username is not '':
                if is_admin_registered(user=username):
                    password = request.data.get('password', None)
                    if is_authenticated(user=username, password=password):
                        app = Apps.objects.get(id=pk)
                        status , deleted_app = app.delete()
                        if status == 1:
                            return Response({'msg': 'App Deleted Successfully'})
                        return Response({'msg': 'Unable to delete pls try again'})
                    return Response({'msg': 'Invalid Password'})
                return Response({'msg': 'username is not registered'})
            return Response({'msg': 'Invalid Credentials'})
        return Response({'msg': 'Credentials are not provided'})