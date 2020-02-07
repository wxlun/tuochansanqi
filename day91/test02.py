import requests
session = requests.Session()

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
         'Host':'www.chouti.com'
         }
response0 = session.get(
    url='https://dig.chouti.com/'
                        )

post_dict = {
    'phone':'8613716330941',
    'password':'wxl123456',
    'oneMonth':1
}
response1 = session.post(
    url='https://dig.chouti.com/login' ,
    data = post_dict,
    headers =headers,
)

# response2 = session.post(
#     url='https://dig.chouti.com/link/vote?linksId=25888026' ,
#     headers =headers,
# )
print(response1.text)