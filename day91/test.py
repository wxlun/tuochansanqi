import requests
post_dict = {
    'phone':'8613716330941',
    'password':'wxl123456',
    'oneMonth':1
}
# 伪装成浏览器，不然会遇到防火墙
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

response = requests.post(
    url='https://dig.chouti.com/login',
    headers =headers,
    data = post_dict
)

print(response.text)
cookise_dict = response.cookies.get_dict()
print(cookise_dict)