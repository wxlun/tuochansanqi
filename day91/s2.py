import requests
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36','Upgrade-Insecure-Requests': '1',
         'Host':'www.chouti.com'
         }
r1 = requests.get('https://dig.chouti.com/')
r1_cookies = r1.cookies.get_dict()
print(r1_cookies)
post_dict = {
    "phone":'8613716330941',
    "password":'wxl123456',
    'oneMonth':1

}

r2 = requests.post(
    url = "https://dig.chouti.com/login",
    headers =headers,
    data=post_dict,
    cookies=r1.cookies
)

# r3 = requests.post(
#     url = 'http://www.chouti.com/ctu_57777056742',
#     # cookies={'st_user_token': r2_cookies.get('st_user_token')}
#     cookies = {'gpsd':r1_cookies.get('gpsd')}
# )

print(r2.text)