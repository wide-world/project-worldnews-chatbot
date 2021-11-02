from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })


@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    bbc_path = '/home/ubuntu/main/news_app/bbc.txt'
    bbc_fp = open(bbc_path,'r', encoding='utf-8')

    tmp_str=''
    for line in bbc_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')

    news_list = list(tmp_str.split('\n'))
    bbc_fp.close()

    news=''
    news = "\n".join(news_list)
    news.rstrip()

    if return_str == 'bbc' or return_str == 'BBC':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "BBC World News Most Read"
                        },
                        "items": [
                            {
                                "title": news_list[0],
                                #"description": "",
                                #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                "link": {
                                    "web": news_list[1]
                                }
                            },
                            {
                                "title": news_list[2],
                                #"description": "",
                                #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                "link": {
                                    "web": news_list[3]
                                }
                            },
                            {
                                "title": news_list[4],
                                #"description": "",
                                #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                "link": {
                                    "web": news_list[5]
                                }
                            },
                            {
                                "title": news_list[6],
                                #"description": "",
                                #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                "link": {
                                    "web": news_list[7]
                                }
                            },
                            {
                                "title": news_list[8],
                                #"description": "",
                                #"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                "link": {
                                    "web": news_list[9]
                                }
                            },
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www.bbc.com/news"
                            }
                        ]
                    }
                }],
                'quickReplies': [{
                    'label': '초기 화면',
                    'action': 'message',
                    'messageText': '초기 화면'
                }]
            }
        })
    if return_str == 'cnn' or return_str == 'CNN':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "테스트 성공입니다!"
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })

