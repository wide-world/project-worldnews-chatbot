import os
import sys
import urllib.request

def run():
    fp = open('summary/eurosummary.txt', 'r', encoding = 'utf-8')
    f = open('translation/eurotranslation.txt', 'w', encoding = 'utf-8')
    string = ''

    while True :
        line = fp.readline()
        string += line
        if not line :
            break

    client_id = "WevlXrNV1ROE_Ko5ACh9"
    client_secret = "rvutTJWAJq"
    encText = urllib.parse.quote(string)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read().decode('utf-8')
        start_index = response_body.find('"translatedText":"') + 18
        end_index = response_body.find('"engineType"') - 2
        tmp = response_body[start_index:end_index]
        tmp = ''.join(tmp.split('\\'))
        tmp = '\n'.join(tmp.split('n'))
        tmp = ''.join(tmp.split('t'))
        tmp = ''.join(tmp.split('b'))
        f.write(tmp)
    else:
        print("Error Code:" + rescode)
    f.close()
    fp.close()
