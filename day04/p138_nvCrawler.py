import urllib.request
import datetime
import json

cliendId = ""
clientSecret = ""

# 사이트 url에 연결할 객체


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", cliendId)
    req.add_header("X-Naver-Client-Secret", clientSecret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Succes " % datetime.datetime.now())
        return response.read().decode('utf-8')
    except:
        return None


print("-------------------------------------------------------")

# json 형태의 데이터를 받아오기 위한 함수


def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/news.json"
    # 쿼리공백이 들어가면 안댄다
    parameters = "?query=%s&start=%s&display=%s" % (
        urllib.parse.quote(srcText), start, display)
    url = base+node+parameters
    print(url)

    responseDecode = getRequestUrl(url)
    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)
# 함수만들기


# 딕객체에 담아서 계속 append시킴
def getPostDsta(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = post['pubDate']

    jsonResult.append({'cnt': cnt, 'title': title, 'description': description,
                      'org_link': org_link, 'link': link, 'pDate': pDate})


# 여기가 메인
node = 'news'
srcText = '선거'
cnt = 0
jsonResult = []

jsonResponse = getNaverSearch(node, srcText, 1, 100)
total = jsonResponse['total']

while((jsonResponse != None) and (jsonResponse['display'] != 0)):
    for post in jsonResponse['items']:
        cnt += 1
        getPostDsta(post, jsonResult, cnt)
    start = jsonResponse['start']+jsonResponse['display']
    jsonResponse = getNaverSearch(node, srcText, start, 10)

print('전체 검색 : %d건' % total)

with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf=8') as outfile:
    jsonFile = json.dumps(jsonResult, indent=4,
                          sort_keys=True, ensure_ascii=False)
    outfile.write(jsonFile)

print('가져온 데이터 : %d 건' % cnt)
print('%s_naver_%s.json Saved' % (srcText, node))
