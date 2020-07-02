from linebot.models import MessageEvent ,TextSendMessage , ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction, URITemplateAction, PostbackTemplateAction,ImagemapSendMessage,BaseSize,MessageImagemapAction,ImagemapArea,URIImagemapAction,CarouselColumn,CarouselTemplate,ImageCarouselColumn,ImageCarouselTemplate,BubbleContainer, ImageComponent, BoxComponent, TextComponent, IconComponent, ButtonComponent, SeparatorComponent, FlexSendMessage, URIAction
from linebot import  LineBotApi,WebhookParser
from linebot.exceptions import InvalidSignatureError ,LineBotApiError
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse , HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


def sendText(event):
	try:
		message = TextSendMessage(
			text = "因為今年疫情緣故，豆干節詳細舉辦日期尚未得知，以下為去年活動懶人包供參考：\n 網址：https://jfsblog.com/blog/post/daxi-bean-curd-festival"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))
def sendText2(event):
	try:
		message = TextSendMessage(
			text = "因為今年疫情緣故，活動延期，詳細舉辦日期尚未得知，以下為去年活動懶人包供參考：\n 網址：https://jfsblog.com/blog/post/taoyuan-balloon-festival"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))

def sendImage(event):
	try:
		message = ImageSendMessage(
			original_content_url="https://i.imgur.com/FutqcMi.jpg",
			preview_image_url="https://i.imgur.com/FutqcMi.jpg"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendImage2(event):
	try:
		message = ImageSendMessage(
			original_content_url="https://i.imgur.com/dazZhFz.jpg",
			preview_image_url="https://i.imgur.com/dazZhFz.jpg"
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendStick(event):
	try:
		message = StickerSendMessage(
			package_id='1',
			sticker_id='2'
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendMulti(event):
	try:
		message = [
				TextSendMessage(text="【金師獎】中原資管105級謝師宴 🎉 \n:::::::::::::::::::::::::::::::::::::::::::::::\n活動時間：109/6/17(三) 晚上17:30 報到進場 ； 18:00 開始\n活動地點：南方莊園渡假飯店 (桃園市中壢區樹籽路8號) 中原過去交通約20-25分鐘，備免費停車場\n價格：750-850 / 人（將於統計人數後公告確定金額於各班群組）\n繳費方式與時間待金額確定會一併公告，請同學務必注意！！\n用餐內容：自助Buffet\n🎁當天有抽獎活動哦！獎品豐富!\n之後會再讓大家安排座位跟自己的好朋友同一桌!!\n快來參加謝師宴、吃大餐、抽好禮\n\n報名截止時間：6/3(三)11:59分"),
				TextSendMessage(text="※ 本次謝師宴主題為【金師獎】\n※ 服裝方面，請著「正式服裝」出席\n⚠️ 請勿穿著拖鞋入場\n❗️ 此表單填寫完畢即視為確定出席\n \n※ 待統計完人數確定每人繳付金額後，無論晚到還是缺席都需要負擔「完整出席餐費」！\n\n甲班負責人聯絡電話：蔡宜真 0926-108-965\n乙班負責人聯絡電話：涂益誠 0934-258-528\n\n有任何疑問都歡迎直接聯繫負責人\n感謝配合 !! ")
		]
		
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))
def sendPosition(event):
	try:
		message = [
			LocationSendMessage(title='桃園市大溪區',address='335桃園市大溪區',latitude='24.8709613',longitude='121.2306069'),
			TextSendMessage(text="大溪區爲中華民國桃園市的一個市轄區，境內有大漢溪，因而得名。大溪區原為復興區的木材輸出門戶，以大漢溪爲河運管道。雖然現在河運已經不再，但當地昔日的渡船頭仍然保存，大溪爲北橫公路的入口端，因擁有豐富的觀光資源，桃園市政府持續推展生態休閒遊憩東都心之重點發展區。")
		]
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))
def sendQuickreply(event):
	try:
		message = TextSendMessage(
			text = "選擇你最愛的程式語言吧",
			quick_reply=QuickReply(
				items=[
					QuickReplyButton(
						action=MessageAction(label="Python",text="Python")
					),
					QuickReplyButton(
						action=MessageAction(label="Java",text="Java")
					),
					QuickReplyButton(
						action=MessageAction(label="C#",text="C#")
					),
					QuickReplyButton(
						action=MessageAction(label="Basic",text="Basic")
					),
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "發生錯誤！"))
def sendButton(event):  #按鈕樣版
    # try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ButtonsTemplate(
                thumbnail_image_url='https://lh3.googleusercontent.com/proxy/mAPV6VIFrXqWaX4uzwu-qfk2QSg4g7LkE2hhEU7SGW_tbJJ-k1gTb9B4YYcYGQk9yNLOwn560yrLiTMLhBRoKQm_voje3g',  #顯示的圖片
                title='大溪近期經典活動',  #主標題
                text='請點選選項以獲取更多資訊：',  #副標題
                actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='2020大溪豆干節(延期)',
                        text='@傳送大溪豆乾活動'
                    ),
                    MessageTemplateAction(  #開啟網頁
                        label='2020石門水庫熱氣球嘉年華(延期)',
                        text='@傳送石門水庫熱氣球活動'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    # except:
    #     line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPizza(event):
    try:
        message = TextSendMessage(
            text = '感謝您購買披薩。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_buy(event, backdata):  #處理Postback
    try:
        text1 = '感謝您購買披薩，'
        text1 += '我們將盡快為您製作。'
        message = TextSendMessage(  #傳送文字
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendImgmap(event):
	#try:
		image_url = 'https://i.imgur.com/Yz2yzve.jpg'
		imgwidth = 1040
		imgheight = 300
		message = ImagemapSendMessage(
			base_url=image_url,
			alt_text= "圖片地圖範例",
			base_size=BaseSize(height=imgheight, width=imgwidth),
			actions=[
				MessageImagemapAction(
					text="你點選了紅色區域!",
					area=ImagemapArea(
						x=0,
						y=0,
						width=imgwidth*0.25,
						height=imgheight
					)
				),
				URIImagemapAction(
					link_url='https://www1.cycu.edu.tw/',
					area=ImagemapArea(
						x=imgwidth*0.75,
						y=0,
						width=imgwidth*0.25,
						height=imgheight
					)
				),
			]
		)
		line_bot_api.reply_message(event.reply_token, message)
	#except:
	#	line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendCarousel(event):
	try:
		message = TemplateSendMessage(
			alt_text='轉盤樣板',
			template=CarouselTemplate(
				columns=[
					CarouselColumn(
						thumbnail_image_url='https://i.imgur.com/nw20uTZ.jpg',
						title='花藝課程資訊',
						text='往後滑動→\n觀看歷史活動紀錄！',
						actions=[
							URITemplateAction(
								label='前往官方網站查看更多',
								uri='https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://scontent.ftpe4-2.fna.fbcdn.net/v/t1.0-9/83595928_2629590977119079_4877398284773097472_n.jpg?_nc_cat=100&_nc_sid=0debeb&_nc_ohc=3ZkXpMXCLeAAX_WJgzD&_nc_ht=scontent.ftpe4-2.fna&oh=0e4e6cc0085c0eb7b98588cb347d0387&oe=5F20CBB7',
						title='2020年 年花課程',
						text='1/21~1/22',
						actions=[
							URITemplateAction(
								label='前往觀看活動相片',
								uri='https://www.facebook.com/193614007383467/photos/a.2629573170454193/2629590973785746'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://scontent.ftpe4-1.fna.fbcdn.net/v/t1.0-9/28378946_1585021301576057_2777316159554010739_n.jpg?_nc_cat=108&_nc_sid=cdbe9c&_nc_ohc=5f9Skl3x7YMAX8A-4n1&_nc_ht=scontent.ftpe4-1.fna&oh=f015a5cc57f8a905b019f54577b91d8b&oe=5F2027D1',
						title='2018年 樹屋年花單堂課',
						text='2/11下午場，2/12下午&晚上場',
						actions=[
							URITemplateAction(
								label='前往觀看活動相片',
								uri='https://www.facebook.com/media/set/?vanity=193614007383467&set=a.1585021004909420'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://scontent.ftpe4-1.fna.fbcdn.net/v/t1.0-9/25348528_1517277188350469_4496425193584292466_n.jpg?_nc_cat=107&_nc_sid=0debeb&_nc_ohc=yDGyQom23f0AX_eOQZF&_nc_ht=scontent.ftpe4-1.fna&oh=d3c9bbe185351a0d3450e479f6a71ef2&oe=5F23B7E4',
						title='2017年 聖誕節單堂手作課',
						text='12/16',
						actions=[
							URITemplateAction(
								label='前往觀看活動相片',
								uri='https://www.facebook.com/media/set/?vanity=193614007383467&set=a.1517274651684056'
							)
						]
					),
					CarouselColumn(
						thumbnail_image_url='https://scontent.ftpe4-2.fna.fbcdn.net/v/t31.0-8/17310385_1267893303288860_5561151591450420887_o.jpg?_nc_cat=104&_nc_sid=cdbe9c&_nc_ohc=ave_PC7CEy8AX8iNtNl&_nc_ht=scontent.ftpe4-2.fna&oh=134321caba072597e606abd5b539b93e&oe=5F227A4D',
						title='2017年 年花課',
						text='1/25',
						actions=[
							URITemplateAction(
								label='前往觀看活動相片',
								uri='https://www.facebook.com/193614007383467/photos/a.1267892846622239/1267895486621975'
							)
						]
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,message)
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendCarouselImg(event):
	#try:
		message = TemplateSendMessage(
			alt_text='七夕節慶花禮',
			template=ImageCarouselTemplate(
				columns=[
					ImageCarouselColumn(
						image_url='https://scontent.ftpe4-2.fna.fbcdn.net/v/t1.0-9/67299993_2260768084001372_3451101592084807680_n.jpg?_nc_cat=100&_nc_sid=0debeb&_nc_ohc=vJWl2bkosSYAX-tBBX9&_nc_ht=scontent.ftpe4-2.fna&oh=e16b11102648b089e1c81691ea2fe29d&oe=5F201FFB',
						action=URITemplateAction(
								label='情人節花束',
								uri='https://www.facebook.com/permalink.php?story_fbid=2260769327334581&id=193614007383467'
						)
					),
					ImageCarouselColumn(
						image_url='https://scontent.ftpe4-2.fna.fbcdn.net/v/t1.0-9/67201666_2260771107334403_2385870353156014080_n.jpg?_nc_cat=104&_nc_sid=0debeb&_nc_ohc=3uFtashVnmoAX_3svyt&_nc_ht=scontent.ftpe4-2.fna&oh=a005091f15ab8e0583abf71e46855db1&oe=5F226A57',
						action=URITemplateAction(
								label='情人節花束',
								uri='https://www.facebook.com/permalink.php?story_fbid=2260771784001002&id=193614007383467'
						)
					),
					ImageCarouselColumn(
						image_url='https://scontent.ftpe4-2.fna.fbcdn.net/v/t1.0-9/20664043_1406627942748728_8455519672773317811_n.jpg?_nc_cat=104&_nc_sid=8bfeb9&_nc_ohc=DJpgE2e07XEAX_i__OU&_nc_ht=scontent.ftpe4-2.fna&oh=9fce94bd012b9c3933ffcaaad064a68e&oe=5F225B23',
						action=URITemplateAction(
								label='情人節花束',
								uri='https://www.facebook.com/permalink.php?story_fbid=1419633931448129&id=193614007383467'
						)
					),
					ImageCarouselColumn(
						image_url='https://scontent.ftpe4-1.fna.fbcdn.net/v/t1.0-9/13880355_1062116740533185_4130157721522038996_n.jpg?_nc_cat=105&_nc_sid=8bfeb9&_nc_ohc=ienoRfsrlhEAX-gPVYk&_nc_ht=scontent.ftpe4-1.fna&oh=2aa34c53e13e74e8269a9117e140c672&oe=5F23F4E8',
						action=URITemplateAction(
								label='情人節提籃花',
								uri='https://www.facebook.com/permalink.php?story_fbid=1062117130533146&id=193614007383467'
						)
					),
					ImageCarouselColumn(
						image_url='https://scontent.ftpe4-2.fna.fbcdn.net/v/t1.0-9/20664043_1406627942748728_8455519672773317811_n.jpg?_nc_cat=104&_nc_sid=8bfeb9&_nc_ohc=DJpgE2e07XEAX_i__OU&_nc_ht=scontent.ftpe4-2.fna&oh=9fce94bd012b9c3933ffcaaad064a68e&oe=5F225B23',
						action=URITemplateAction(
								label='情人節花束',
								uri='https://www.facebook.com/permalink.php?story_fbid=1419633931448129&id=193614007383467'
						)
					)
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,message)
def sendCarouselImg2(event):
	#try:
		message = TemplateSendMessage(
			alt_text='各式花禮作品',
			template=ImageCarouselTemplate(
				columns=[
					ImageCarouselColumn(
						image_url='https://i.imgur.com/i8M7sme.jpg',
						action=URITemplateAction(
								label='提籃花',
								uri='https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/'
						)
					),
					ImageCarouselColumn(
						image_url='https://imgur.com/DJ1Buef.jpg',
						action=URITemplateAction(
								label='花束',
								uri='https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/'
						)
					),
					ImageCarouselColumn(
						image_url='https://imgur.com/wGCAsMH.jpg',
						action=URITemplateAction(
								label='永生花',
								uri='https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/'
						)
					),
					ImageCarouselColumn(
						image_url='https://imgur.com/FQaXKug.jpg',
						action=URITemplateAction(
								label='蘭花',
								uri='https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/'
						)
					),
					ImageCarouselColumn(
						image_url='https://imgur.com/ag3ubZN.jpg',
						action=URITemplateAction(
								label='提籃花',
								uri='https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/'
						)
					),
					ImageCarouselColumn(
						image_url='https://imgur.com/5Yro8Ym.jpg',
						action=URITemplateAction(
								label='盆花',
								uri='https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/'
						)
					),
					ImageCarouselColumn(
						image_url='https://i.imgur.com/PquESwg.jpg',
						action=URITemplateAction(
								label='提籃花',
								uri='https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/'
						)
					),
				]
			)
		)
		line_bot_api.reply_message(event.reply_token,message)
	#except:
	#	line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))
def sendFlex(event):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            header=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='紫盒子花禮設計', color='#381E4C', weight='bold', size='xxl'),
                ]
            ),
            hero=ImageComponent(
                url='https://scontent.ftpe4-2.fna.fbcdn.net/v/t31.0-8/13055946_999120876832772_2044881262332591773_o.jpg?_nc_cat=100&_nc_sid=e3f864&_nc_ohc=gCBdBiAdm6UAX9JxTw0&_nc_ht=scontent.ftpe4-2.fna&oh=e9a94af719cb33c68959d34b6f4590a1&oe=5F20EAC2',
                size='full',
                aspect_ratio='792:555',
                aspect_mode='cover',
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業地址:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text='新北市林口區文化二路一段', color='#666666', size='sm', flex=5)
                                ],
                            ),
							BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='⚘⚘⚘⚘⚘⚘', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text='354號', color='#666666', size='sm', flex=5)
                                ],
                            ),
                            SeparatorComponent(color='#0000FF'),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業時間:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text="09:00 - 21:00", color='#666666', size='sm', flex=5),
                                ],
                            ),
                        ],
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=URIAction(label='電話聯絡', uri='tel:0919273609'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=URIAction(label='查看網頁', uri="https://www.facebook.com/%E7%B4%AB%E7%9B%92%E5%AD%90%E8%8A%B1%E7%A6%AE%E8%A8%AD%E8%A8%88-193614007383467/")
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='copyright@purpleBox 2020', color='#888888', size='sm', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="聯絡資訊", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))