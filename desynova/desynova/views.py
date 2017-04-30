from django.shortcuts import render
import json
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
import random, string
from models import *
from desynova.settings import LIVE_URL
from Crypto.Cipher import AES
import base64
import requests


def landing_page(request):
    return render(request, "templates/landing_page.html")

def short_url(request):
	if request.method == "POST":
		params = json.loads(request.body)
		print params
		x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
		params['short_url_string'] = x
		ShortUrl.objects.create(**params)
		return JsonResponse({
			"message": "Url created successfully",
			"status": True
		})
	elif request.method == "GET":
		return JsonResponse({
			"short_url_list": [{"short_url_id": i.short_url_string, "display_short_url": LIVE_URL+i.short_url_string} for i in ShortUrl.objects.all()],
			"status": True
		})
	else:
		return JsonResponse({
			"message": "Request method not valid",
			"status": False
		})

def redirect_url(request, short_url_id=None):
	short_url_obj = ShortUrl.objects.get(short_url_string=short_url_id)
	print short_url_id, short_url_obj.original_url
	return HttpResponseRedirect(short_url_obj.original_url)

def paste_lockly(request, short_url_id=None):
	if request.method == "POST":
		params = json.loads(request.body)
		if len(params.get('secret_key')) not in [16,24,32]:
			return JsonResponse({
				"message": "Secret key length should be 16,24,32",
				"status": True
			})
		x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
		params['short_url_string'] = x
		cipher = AES.new(params.get('secret_key'),AES.MODE_ECB)
		params['content'] = base64.b64encode(cipher.encrypt(params.get('content').rjust(32)))
		PasteLockly.objects.create(**params)
		return JsonResponse({
			"message": "Content save successfully",
			"status": False
		})
	elif request.method == "GET":
		return JsonResponse({
			"share_url_list": [{"share_url_id": i.short_url_string, "secret_key": i.secret_key, "display_share_url": LIVE_URL+i.short_url_string} for i in PasteLockly.objects.all()],
			"status": True
		})

def decode_content(request, share_url_id=None):
    return render_to_response("templates/decode_content.html", {"share_url_id": share_url_id})

def get_decode_content(request):
	params = json.loads(request.body)
	paste_lockly = PasteLockly.objects.get(short_url_string=params.get('share_url_id'))
	if paste_lockly.secret_key != params.get('secret_key'):
		return JsonResponse({
			"message": "Invalid secret key",
			"status": False
		})
	cipher = AES.new(params.get('secret_key'),AES.MODE_ECB)
	content = cipher.decrypt(base64.b64decode(paste_lockly.content))
	return JsonResponse({
		"content": content,
		"status": True
	})

def get_neft_data(request):
	response = requests.get('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
	return JsonResponse({
		"data": json.loads(response.text)['data'],
		"status": True
	})