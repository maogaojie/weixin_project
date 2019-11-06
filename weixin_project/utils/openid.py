import requests, json
from weixin_project import settings


def get_openid(code):
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
    settings.appid, settings.secret, code)
    res = requests.get(url)
    print(res)
    return json.loads(res.text)['openid']
