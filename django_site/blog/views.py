from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    return HttpResponse('<html><body>Post List</body></html>')
