# ## 1、首先登陆任何页面，获取cookie
import requests
i1 = requests.get(url="https://dig.chouti.com/help/service")
i1_cookies = i1.cookies.get_dict()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
         'Host':'www.chouti.com'
         }

# ## 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2 = requests.post(
    url="https://dig.chouti.com/login",
    data={
        'phone': '8613716330941',
        'password': 'wxl123456',
        'oneMonth': "",
    },
    cookies=i1_cookies,
    headers = headers
)

print(i2.text)
