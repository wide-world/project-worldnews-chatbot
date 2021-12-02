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

    bbc_summary = '/home/ubuntu/main/news_app/contents/summary/bbcsummary.txt'
    bbcs_fp = open(bbc_summary, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in bbcs_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    bbc_s_list = list(tmp_str.split('\n'))
    bbcs_fp.close()
    
    cnn_summary = '/home/ubuntu/main/news_app/contents/summary/cnnsummary.txt'
    cnns_fp = open(cnn_summary, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in cnns_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    cnn_s_list = list(tmp_str.split('\n'))
    cnns_fp.close()

    alj_summary = '/home/ubuntu/main/news_app/contents/summary/aljsummary.txt'
    aljs_fp = open(alj_summary, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in aljs_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    alj_s_list = list(tmp_str.split('\n'))
    aljs_fp.close()

    nhk_summary = '/home/ubuntu/main/news_app/contents/summary/nhksummary.txt'
    nhks_fp = open(nhk_summary, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in nhks_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    nhk_s_list = list(tmp_str.split('\n'))
    nhks_fp.close()

    euro_summary = '/home/ubuntu/main/news_app/contents/summary/eurosummary.txt'
    euros_fp = open(euro_summary, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in euros_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    euro_s_list = list(tmp_str.split('\n'))
    euros_fp.close()

    bbc_translation = '/home/ubuntu/main/news_app/contents/translation/bbctranslation.txt'
    bbct_fp = open(bbc_translation, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in bbct_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    bbc_t_list = list(tmp_str.split('\n'))
    bbct_fp.close()
    
    cnn_translation = '/home/ubuntu/main/news_app/contents/translation/cnntranslation.txt'
    cnnt_fp = open(cnn_translation, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in cnnt_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    cnn_t_list = list(tmp_str.split('\n'))
    cnnt_fp.close()
    
    alj_translation = '/home/ubuntu/main/news_app/contents/translation/aljtranslation.txt'
    aljt_fp = open(alj_translation, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in aljt_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    alj_t_list = list(tmp_str.split('\n'))
    aljt_fp.close()
    
    nhk_translation = '/home/ubuntu/main/news_app/contents/translation/nhktranslation.txt'
    nhkt_fp = open(nhk_translation, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in nhkt_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    nhk_t_list = list(tmp_str.split('\n'))
    nhkt_fp.close()
    
    euro_translation = '/home/ubuntu/main/news_app/contents/translation/eurotranslation.txt'
    eurot_fp = open(euro_translation, 'r', encoding = 'utf-8')
    tmp_str=''
    for line in eurot_fp.readlines():
        tmp_str += line
    tmp_str = tmp_str.strip('\n')
    euro_t_list = list(tmp_str.split('\n'))
    eurot_fp.close()
    
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
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC요약1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약1"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC요약2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약2"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC요약3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약3"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC요약4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약4"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC요약5",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약5"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC번역1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역1"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC번역2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역2"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC번역3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역3"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC번역4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역4"
                    },
                    {
                        "action": "block",
                        "messageText": "BBC번역5",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역5"
                    },
                ],
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
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    },
                    {
                        "action": "block",
                        "messageText": "CNN요약1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약1"
                    },
                    {
                        "action": "block",
                        "messageText": "CNN요약2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약2"
                    },
                    {
                        "action": "block",
                        "messageText": "CNN요약3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약3"
                    },
                    {
                        "action": "block",
                        "messageText": "CNN요약4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약4"
                    },
                    {
                        "action": "block",
                        "messageText": "CNN번역1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역1"
                    },
                    {
                        "action": "block",
                        "messageText": "CNN번역2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역2"
                    },
                    {
                        "action": "block",
                        "messageText": "CNN번역3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역3"
                    },
                    {
                        "action": "block",
                        "messageText": "CNN번역4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역4"
                    },
                ]
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
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    },
                    { 
                        "action": "block",
                        "messageText": "EURO요약1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약1"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO요약2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약2"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO요약3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약3"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO요약4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약4"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO요약5",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약5"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO번역1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역1"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO번역2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역2"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO번역3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역3"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO번역4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역4"
                    },
                    {
                        "action": "block",
                        "messageText": "EURO번역5",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역5"
                    },
                ]
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
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    },
                    {   "action": "block",
                        "messageText": "ALJ요약1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약1"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ요약2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약2"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ요약3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약3"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ요약4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약4"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ요약5",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약5"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ번역1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역1"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ번역2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역2"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ번역3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역3"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ번역4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역4"
                    },
                    {
                        "action": "block",
                        "messageText": "ALJ번역5",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역5"
                    },
                ]
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
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    },
                    {   "action": "block",
                        "messageText": "NHK요약1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약1"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK요약2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약2"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK요약3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약3"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK요약4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약4"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK요약5",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "요약5"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK번역1",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역1"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK번역2",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역2"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK번역3",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역3"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK번역4",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역4"
                    },
                    {
                        "action": "block",
                        "messageText": "NHK번역5",
                        "blockId": "61682be94687a505ab3be73a",
                        "label": "번역5"
                    },
                ]
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
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
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
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
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
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    },
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
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
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
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC요약1' or return_str == 'bbc요약1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_s_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC요약2' or return_str == 'bbc요약2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_s_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC요약3' or return_str == 'bbc요약3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_s_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC요약4' or return_str == 'bbc요약4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_s_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC요약5' or return_str == 'bbc요약5':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_s_list[4]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'CNN요약1' or return_str == 'cnn요약1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cnn_s_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'CNN요약2' or return_str == 'cnn요약2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cnn_s_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'CNN요약3' or return_str == 'cnn요약3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cnn_s_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })    

    if return_str == 'CNN요약4' or return_str == 'cnn요약4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cnn_s_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ요약1' or return_str == 'alj요약1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_s_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })
    
    if return_str == 'ALJ요약2' or return_str == 'alj요약2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_s_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ요약3' or return_str == 'alj요약3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_s_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ요약4' or return_str == 'alj요약4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_s_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ요약5' or return_str == 'alj요약5':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_s_list[4]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK요약1' or return_str == 'nhk요약1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_s_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK요약2' or return_str == 'nhk요약2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_s_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK요약3' or return_str == 'nhk요약3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_s_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK요약4' or return_str == 'nhk요약4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_s_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK요약5' or return_str == 'mhk요약5':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_s_list[4]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO요약1' or return_str == 'euro요약1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_s_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO요약2' or return_str == 'euro요약2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_s_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO요약3' or return_str == 'euro요약3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_s_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO요약4' or return_str == 'euro요약4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_s_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO요약5' or return_str == 'euro요약5':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_s_list[4]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC번역1' or return_str == 'bbc번역1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_t_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC번역2' or return_str == 'bbc번역2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_t_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC번역3' or return_str == 'bbc번역3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_t_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC번역4' or return_str == 'bbc번역4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_t_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'BBC번역5' or return_str == 'bbc번역5':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": bbc_t_list[4]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'CNN번역1' or return_str == 'cnn번역1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cnn_t_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'CNN번역2' or return_str == 'cnn번역2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cnn_t_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'CNN번역3' or return_str == 'cnn번역3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cnn_t_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'CNN번역4' or return_str == 'cnn번역4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": cnn_t_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ번역1' or return_str == 'alj번역1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_t_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ번역2' or return_str == 'alj번역2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_t_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ번역3' or return_str == 'alj번역3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_t_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ번역4' or return_str == 'alj번역4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_t_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'ALJ번역5' or return_str == 'alj번역5':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": alj_t_list[4]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK번역1' or return_str == 'nhk번역1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_t_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK번역2' or return_str == 'nhk번역2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_t_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK번역3' or return_str == 'nhk번역3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_t_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK번역4' or return_str == 'nhk번역4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_t_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'NHK번역5' or return_str == 'mhk번역5':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": nhk_t_list[4]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO번역1' or return_str == 'euro번역1':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_t_list[0]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO번역2' or return_str == 'euro번역2':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_t_list[1]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO번역3' or return_str == 'euro번역3':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_t_list[2]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO번역4' or return_str == 'euro번역4':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_t_list[3]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })

    if return_str == 'EURO번역5' or return_str == 'euro번역5':
        return JsonResponse({
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": euro_t_list[4]
                        }
                    }
                ],
                'quickReplies': [
                    {
                        "action": "block",
                        "blockId": "616291e7c78e3769ca9a029e",
                        "label": "홈"
                    }
                ]
            }
        })     
