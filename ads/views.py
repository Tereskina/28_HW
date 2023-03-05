import json

from django.http import JsonResponse, Http404

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Categories



def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    def get(self, request):

        ads = Ads.objects.all()

        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price
            })

        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ads()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.description = ad_data["description"]
        ad.is_published = ad_data["is_published"]

        ad.save()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published
        })


class AdDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()

        except Http404 as error:
            return JsonResponse({'error': error.args}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published
        })


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):
    def get(self, request):

        categories = Categories.objects.all()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Categories()
        category.name = category_data["name"]

        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()

        except Http404 as error:
            return JsonResponse({'error': error.args}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })
