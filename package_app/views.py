
from django.shortcuts import render
from rest_framework.views import APIView

from package_app.models.service import Service
from .forms import Form


class First(APIView):

    permission_classes = []

    def post(self, request):
        gt = 0
        db_name = []

        price_dict = {"domain": 900,
                      "internet": 800,
                      "hosting": 1000,
                      "online bill pay": 100,
                      "real IP": 200,
                      "24/7 support": 400
                      }

        if request.method == "POST":
            form = Form(request.POST)
            if form.is_valid():
                service = form.cleaned_data['service']
                addon = form.cleaned_data["addon"]
                print("package: 100 taka less for more than one service >>>>>>>>>>>>>>>>>")
                for s in service:
                    db_name.append(s)
                    price = price_dict[s]
                    gt = gt+price
                    print("package:", s, "price", price)
                print("addon: >>>>>>>>>>>>>>>>>")
                if addon:
                    for a in addon:
                        db_name.append(a)
                        addon_price = price_dict[a]
                        gt = gt + addon_price
                        print("addon:", a, "price", addon_price)
                else:
                    addon_price = 0
                    gt = gt + addon_price
                if len(service) > 1:
                    gt = gt - 100
                print("total:", gt)
        db = Service.objects.create(names=db_name, total_price=gt)
        db.save()
        context = {"form": Form}
        return render(request, 'form.html', context)
