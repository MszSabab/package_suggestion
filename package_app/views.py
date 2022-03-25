import json

from rest_framework.response import Response
from rest_framework.views import APIView


class First(APIView):

    permission_classes = []
    # serializer_class = DisburseSerializer
    def post(self, request):

        self.request = request

        response = self.request
        print(response)
        yes = json.loads(self.request)
        if response.status_code == 200:
            return Response(yes, response.status_code)
        return None
