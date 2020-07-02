from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse , HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import  LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError ,LineBotApiError
from linebot.models import MessageEvent ,TextSendMessage , ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,TextMessage, PostbackEvent
from .module.func import *
from urllib.parse import parse_qsl
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
	if request.method == 'POST':
		signature = request.META['HTTP_X_LINE_SIGNATURE']
		body = request.body.decode('utf-8')
		# print(body)
		try:
			events = parser.parse(body, signature)
		except InvalidSignatureError:
			return HttpResponseForbidden()
		except LineBotApiError:
			return HttpResponseBadRequest()
		for event in events:
			if isinstance(event, MessageEvent):
				if isinstance(event.message, TextMessage):
					mtext = event.message.text
					if mtext == '@傳送花藝課程資訊':
					   sendCarousel(event)
					elif mtext == '@傳送七夕花禮資訊':
						sendCarouselImg(event)
					elif mtext == '@傳送花禮作品':
						sendCarouselImg2(event)
					elif mtext =="@傳送聯絡資訊":
						sendFlex(event)
					else:
						output = "抱歉本機器人尚未設置自訂言論!!!"
						line_bot_api.reply_message(event.reply_token,TextSendMessage(text = output))
			if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
				backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
				if backdata.get('action') == 'buy':
					sendBack_buy(event, backdata)                       
		return HttpResponse()
	else:
		#return HttpResponseBadRequest()
		return HttpResponse()
    
# def callback(request):
# 	if request.method =='POST':
# 		signature = request.META['HTTP_X_LINE_SIGNATURE']
# 		body = request.body.decode('utf-8')
		
# 		try:
# 			events = parser.parse(body,signature)
# 		except InvalidSignatureError:
# 			return HttpResponseForbidden()
# 		except LineBotApiError:
# 			return HttpResponseBadRequest()
# 		for event in events:		
# 			if isinstance(event , MessageEvent):
# 				mtext = event.message.text 
# 				if mtext =="@傳送文字":
# 					sendText(event)
# 				elif mtext =="@傳送圖片":
# 					sendImage(event)
# 				elif mtext =="@傳送貼圖":
# 					sendStick(event)
# 				elif mtext =="@多項傳送":
# 					sendMulti(event)
# 				elif mtext =="@傳送位置":
# 					sendPosition(event)
# 				elif mtext =="@快速選單":
# 					sendQuickreply(event)
# 				else:
# 					output = "RRRR 我聽不懂!!!"
# 					line_bot_api.reply_message(event.reply_token,TextSendMessage(text = output))
# 		return HttpResponse()
# 	else:
# 		return HttpResponseBadRequest()# Create your views here.
