from rest_framework.response import Response
from rest_framework.views import APIView

from apitest.models import Person
from apitest.serializers import PersonSerializers, PersonCreateSerializers
from rest_framework import status

from django.utils import timezone


class PersonListApiView(APIView):
    """
    Получаем список всех зарегистрированных пользователей.
    Запрос с параметром id возвращает выбранного пользователя
    """
    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()
        serializer = PersonSerializers(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonCreateApiView(APIView):
    """
    Создает нового пользователя
    После создания в БД возвращаем id
    """
    def post(self, request, *args, **kwargs):
        data = {
            'phone': request.data.get('phone'),
            'login': request.data.get('login'),
            'password': request.data.get('password'),
            'name': request.data.get('name'),
            'birth': request.data.get('birth'),
            'tg': request.data.get('tg'),
            'email': request.data.get('email')
        }
        serializer = PersonCreateSerializers(data=data)
        now = timezone.now().year
        """
        Проверяем валидность полученных данных.
        Делаем проверку на возраст 18+
        """
        if serializer.is_valid():
            birth_date = serializer.validated_data.get('birth')
            age = (now - birth_date.year)
            # print('age= ', age)
            if age > 18:
                serializer.save()
                return Response(serializer.data.get('id'), status=status.HTTP_201_CREATED)

            else:
                return Response(
                    {
                        'res': "Рано ещё заносить в базу"
                    }
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonLoginApiView(APIView):
    """
    Проверяем наличие пользователя в БД по логину и паролю.
    При наличии его в БД, возвращаем id
    """
    def post(self, request):
        try:
            person = Person.objects.get(login=request.data['login'], password=request.data['password'])
            return Response({"person": person.id}, status=status.HTTP_200_OK)
        except Person.DoesNotExist:
            return Response(
                {"res": "такого объекта не существует"},
                status=status.HTTP_400_BAD_REQUEST
            )
