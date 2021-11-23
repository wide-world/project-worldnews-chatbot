from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })

@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    
    # 뉴스 스크래핑 txt 파일 읽어오기
    bbc_path = '/home/ubuntu/main/news_app/bbc.txt'
    bbc_fp = open(bbc_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in bbc_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    bbc_list = list(tmp_str.split('\n'))
    bbc_fp.close()
    
    euro_path = '/home/ubuntu/main/news_app/euro.txt'
    euro_fp = open(euro_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in euro_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    euro_list = list(tmp_str.split('\n'))
    euro_fp.close()
    
    alj_path = '/home/ubuntu/main/news_app/alj.txt'
    alj_fp = open(alj_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in alj_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    alj_list = list(tmp_str.split('\n'))
    alj_fp.close()
    
    nhk_path = '/home/ubuntu/main/news_app/nhk.txt'
    nhk_fp = open(nhk_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in nhk_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    nhk_list = list(tmp_str.split('\n'))
    nhk_fp.close()
    
    cnn_path = '/home/ubuntu/main/news_app/cnn.txt'
    cnn_fp = open(cnn_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in cnn_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    cnn_list = list(tmp_str.split('\n'))
    cnn_fp.close()

    busi_path = '/home/ubuntu/main/news_app/busi.txt'
    busi_fp = open(busi_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in busi_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    busi_list = list(tmp_str.split('\n'))
    busi_fp.close()

    cli_path = '/home/ubuntu/main/news_app/cli.txt'
    cli_fp = open(cli_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in cli_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    cli_list = list(tmp_str.split('\n'))
    cli_fp.close()

    cor_path = '/home/ubuntu/main/news_app/cor.txt'
    cor_fp = open(cor_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in cor_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    cor_list = list(tmp_str.split('\n'))
    cor_fp.close()

    sci_path = '/home/ubuntu/main/news_app/sci.txt'
    sci_fp = open(sci_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in sci_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    sci_list = list(tmp_str.split('\n'))
    sci_fp.close()

    tech_path = '/home/ubuntu/main/news_app/tech.txt'
    tech_fp = open(tech_path, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in tech_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    tech_list = list(tmp_str.split('\n'))
    tech_fp.close()

    # 사용자의 발화에 따라 카카오에 출력
    if return_str == 'bbc' or return_str == 'BBC' or return_str == 'Bbc' or return_str == '비비씨' or return_str == '비비시':
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
                                "title": bbc_list[0],
                                #"description": "",
                                "imageUrl": bbc_list[20],
                                "link": {
                                    "web": bbc_list[1]
                                }
                            },
                            {
                                "title": bbc_list[2],
                                #"description": "",
                                "imageUrl": bbc_list[21],
                                "link": {
                                    "web": bbc_list[3]
                                }
                            },
                            {
                                "title": bbc_list[4],
                                #"description": "",
                                "imageUrl": bbc_list[22],
                                "link": {
                                    "web": bbc_list[5]
                                }
                            },
                            {
                                "title": bbc_list[6],
                                #"description": "",
                                "imageUrl": bbc_list[23],
                                "link": {
                                    "web": bbc_list[7]
                                }
                            },
                            {
                                "title": bbc_list[8],
                                #"description": "",
                                "imageUrl": bbc_list[24],
                                "link": {
                                    "web": bbc_list[9]
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
                'quickReplies': [
                    {
                        'label': '초기 화면',
                        'action': 'message',
                        'messageText': '초기 화면'
                    },
                    {
                        'label': '초기',
                        'action': 'message',
                        'messageText': '초기'
                    },
                    {
                        'label': '초기 화면',
                        'action': 'message',
                        'messageText': '초기 화면'
                    },  
                ]
            }
        })
     
    if return_str == 'cnn' or return_str == 'CNN' or return_str == 'cnn news' or return_str == 'CNN News' or return_str == 'Cnn':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "CNN News Most Read"
                        },
                        "items": [
                            {
                                "title": cnn_list[0],
                                #"description": "",
                                "imageUrl": cnn_list[8],
                                "link": {
                                    "web": cnn_list[1]
                                }
                            },
                            {
                                "title": cnn_list[2],
                                #"description": "",
                                "imageUrl": cnn_list[9],
                                "link": {
                                    "web": cnn_list[3]
                                }
                            },
                            {
                                "title": cnn_list[4],
                                #"description": "",
                                "imageUrl": cnn_list[10],
                                "link": {
                                    "web": cnn_list[5]
                                }
                            },
                            {
                                "title": cnn_list[6],
                                #"description": "",
                                "imageUrl": cnn_list[11],
                                "link": {
                                    "web": cnn_list[7]
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://edition.cnn.com/"
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

    if return_str == 'euro' or return_str == 'EURO' or return_str == 'Euro' or return_str == 'Euronews' or return_str == 'Euro-news' or return_str == 'euronews' or return_str == 'euro-news':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "Euro News Most Read"
                        },
                        "items": [
                            {
                                "title": euro_list[0],
                                #"description": "",
                                "imageUrl": euro_list[10],
                                "link": {
                                    "web": euro_list[1]
                                }
                            },
                            {
                                "title": euro_list[2],
                                #"description": "",
                                "imageUrl": euro_list[11],
                                "link": {
                                    "web": euro_list[3]
                                }
                            },
                            {
                                "title": euro_list[4],
                                #"description": "",
                                "imageUrl": euro_list[12],
                                "link": {
                                    "web": euro_list[5]
                                }
                            },
                            {
                                "title": euro_list[6],
                                #"description": "",
                                "imageUrl": euro_list[13],
                                "link": {
                                    "web": euro_list[7]
                                }
                            },
                            {
                                "title": euro_list[8],
                                #"description": "",
                                "imageUrl": euro_list[14],
                                "link": {
                                    "web": euro_list[9]
                                }
                            },
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www.euronews.com/news/international"
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
    
    if return_str == 'Aljazeera' or return_str == 'aljazeera' or return_str == 'ALJAZEERA' or return_str == 'alj' or return_str == 'ALJ' or return_str == 'Alj' or return_str == '알자지라':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "Aljazeera News Most Read"
                        },
                        "items": [
                            {
                                "title": alj_list[0],
                                #"description": "",
                                "imageUrl": alj_list[10],
                                "link": {
                                    "web": alj_list[1]
                                }
                            },
                            {
                                "title": alj_list[2],
                                #"description": "",
                                "imageUrl": alj_list[11],
                                "link": {
                                    "web": alj_list[3]
                                }
                            },
                            {
                                "title": alj_list[4],
                                #"description": "",
                                "imageUrl": alj_list[12],
                                "link": {
                                    "web": alj_list[5]
                                }
                            },
                            {
                                "title": alj_list[6],
                                #"description": "",
                                "imageUrl": alj_list[13],
                                "link": {
                                    "web": alj_list[7]
                                }
                            },
                            {
                                "title": alj_list[8],
                                #"description": "",
                                "imageUrl": alj_list[14],
                                "link": {
                                    "web": alj_list[9]
                                }
                            },
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www.aljazeera.com/"
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
    
    if return_str == 'nhk' or return_str == 'NHK' or return_str == 'Nhk' or return_str == 'nhk japan' or return_str == 'japan' or return_str == 'JAPAN':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "NHK World Japan Most Read"
                        },
                        "items": [
                            {
                                "title": nhk_list[0],
                                #"description": "",
                                "imageUrl": nhk_list[10],
                                "link": {
                                    "web": nhk_list[1]
                                }
                            },
                            {
                                "title": nhk_list[2],
                                #"description": "",
                                "imageUrl": nhk_list[11],
                                "link": {
                                    "web": nhk_list[3]
                                }
                            },
                            {
                                "title": nhk_list[4],
                                #"description": "",
                                "imageUrl": nhk_list[12],
                                "link": {
                                    "web": nhk_list[5]
                                }
                            },
                            {
                                "title": nhk_list[6],
                                #"description": "",
                                "imageUrl": nhk_list[13],
                                "link": {
                                    "web": nhk_list[7]
                                }
                            },
                            {
                                "title": nhk_list[8],
                                #"description": "",
                                "imageUrl": nhk_list[14],
                                "link": {
                                    "web": nhk_list[9]
                                }
                            },
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www3.nhk.or.jp/nhkworld/en/news/"
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
        
    if return_str == 'COVID19' or return_str == 'COVID-19' or return_str == '코로나' or return_str == '코로나바이러스' or return_str == 'Coronavirus' or return_str == 'coronavirus':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "Corona Virus News"
                        },
                        "items": [
                            {
                                "title": cor_list[0],
                                #"description": "",
                                "imageUrl": cor_list[2],
                                "link": {
                                    "web": cor_list[1]
                                }
                            },
                            {
                                "title": cor_list[3],
                                #"description": "",
                                "imageUrl": cor_list[5],
                                "link": {
                                    "web": cor_list[4]
                                }
                            },
                            {
                                "title": cor_list[6],
                                #"description": "",
                                "imageUrl": cor_list[8],
                                "link": {
                                    "web": cor_list[7]
                                }
                            },
                            {
                                "title": cor_list[9],
                                #"description": "",
                                "imageUrl": cor_list[11],
                                "link": {
                                    "web": cor_list[10]
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www.bbc.com/news/coronavirus"
                            }
                        ]
                    }
                }],
                'quickReplies': [
                    {
                        'label': '초기 화면',
                        'action': 'message',
                        'messageText': '초기 화면'
                    }
                ]
            }
        })

    if return_str == 'Climate' or return_str == 'climate' or return_str == '기후' or return_str == '환경' or return_str == '날씨':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "Climate News"
                        },
                        "items": [
                            {
                                "title": cli_list[0],
                                #"description": "",
                                "imageUrl": cli_list[2],
                                "link": {
                                    "web": cli_list[1]
                                }
                            },
                            {
                                "title": cli_list[3],
                                #"description": "",
                                "imageUrl": cli_list[5],
                                "link": {
                                    "web": cli_list[4]
                                }
                            },
                            {
                                "title": cli_list[6],
                                #"description": "",
                                "imageUrl": cli_list[8],
                                "link": {
                                    "web": cli_list[7]
                                }
                            },
                            {
                                "title": cli_list[9],
                                #"description": "",
                                "imageUrl": cli_list[11],
                                "link": {
                                    "web": cli_list[10]
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www.bbc.com/news/science-environment-56837908"
                            }
                        ]
                    }
                }],
                'quickReplies': [
                    {
                        'label': '초기 화면',
                        'action': 'message',
                        'messageText': '초기 화면'
                    }
                ]
            }
        })

    if return_str == 'Business' or return_str == 'business' or return_str == '경제' or return_str == '경영' or return_str == '비즈니스':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "Business News"
                        },
                        "items": [
                            {
                                "title": busi_list[0],
                                #"description": "",
                                "imageUrl": busi_list[2],
                                "link": {
                                    "web": busi_list[1]
                                }
                            },
                            {
                                "title": busi_list[3],
                                #"description": "",
                                "imageUrl": busi_list[5],
                                "link": {
                                    "web": busi_list[4]
                                }
                            },
                            {
                                "title": busi_list[6],
                                #"description": "",
                                "imageUrl": busi_list[8],
                                "link": {
                                    "web": busi_list[7]
                                }
                            },
                            {
                                "title": busi_list[9],
                                #"description": "",
                                "imageUrl": busi_list[11],
                                "link": {
                                    "web": busi_list[10]
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www.bbc.com/news/business"
                            }
                        ]
                    }
                }],
                'quickReplies': [
                    {
                        'label': '초기 화면',
                        'action': 'message',
                        'messageText': '초기 화면'
                    }
                ]
            }
        })

    if return_str == 'Science' or return_str == 'science' or return_str == '과학' or return_str == '연구':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "Science News"
                        },
                        "items": [
                            {
                                "title": sci_list[0],
                                #"description": "",
                                "imageUrl": sci_list[2],
                                "link": {
                                    "web": sci_list[1]
                                }
                            },
                            {
                                "title": sci_list[3],
                                #"description": "",
                                "imageUrl": sci_list[5],
                                "link": {
                                    "web": sci_list[4]
                                }
                            },
                            {
                                "title": sci_list[6],
                                #"description": "",
                                "imageUrl": sci_list[8],
                                "link": {
                                    "web": sci_list[7]
                                }
                            },
                            {
                                "title": sci_list[9],
                                #"description": "",
                                "imageUrl": sci_list[11],
                                "link": {
                                    "web": sci_list[10]
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www.bbc.com/news/science_and_environment"
                            }
                        ]
                    }
                }],
                'quickReplies': [
                    {
                        'label': '초기 화면',
                        'action': 'message',
                        'messageText': '초기 화면'
                    }
                ]
            }
        })

    if return_str == 'Tech' or return_str == 'tech' or return_str == '기술' or return_str == '공학':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    "listCard": {
                        "header": {
                            "title": "Tech News"
                        },
                        "items": [
                            {
                                "title": tech_list[0],
                                #"description": "",
                                "imageUrl": tech_list[2],
                                "link": {
                                    "web": tech_list[1]
                                }
                            },
                            {
                                "title": tech_list[3],
                                #"description": "",
                                "imageUrl": tech_list[5],
                                "link": {
                                    "web": tech_list[4]
                                }
                            },
                            {
                                "title": tech_list[6],
                                #"description": "",
                                "imageUrl": tech_list[8],
                                "link": {
                                    "web": tech_list[7]
                                }
                            },
                            {
                                "title": tech_list[9],
                                #"description": "",
                                "imageUrl": tech_list[11],
                                "link": {
                                    "web": tech_list[10]
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "홈페이지",
                                "action": "webLink",
                                "webLinkUrl": "https://www.bbc.com/news/technology"
                            }
                        ]
                    }
                }],
                'quickReplies': [
                    {
                        'label': '초기 화면',
                        'action': 'message',
                        'messageText': '초기 화면'
                    }
                ]
            }
        })

