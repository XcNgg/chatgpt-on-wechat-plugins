import requests
from my_fake_useragent import UserAgent
import pprint

def get_data():
    """
    return
        from_who：作者
        hitokoto：诗词
        _from：诗词名称
    """
    headers =  {
        "User-Agent" : UserAgent().random()
    }
    url = "https://v1.hitokoto.cn/?c=i&encode=json"
    response = requests.get(url=url,headers=headers)
    result = response.json()
    from_who = result.get('from_who',"未知")
    hitokoto = result.get('hitokoto',"未知")
    _from = result.get('from',"未知")
    return from_who,hitokoto,_from







if __name__ == '__main__':
    from_who,hitokoto,_from = get_data()
    """
    {'commit_from': 'api',
     'created_at': '1586395379',
     'creator': 'a632079',
     'creator_uid': 1044,
     'from': '放言五首·其五',
     'from_who': '白居易',
     'hitokoto': '松树千年终是朽，槿花一日自为荣。',
     'id': 5761,
     'length': 16,
     'reviewer': 1044,
     'type': 'i',
     'uuid': 'e3854f83-cfb2-496f-803e-873981c4e699'}
     """
    response = f"{hitokoto} \n --{from_who} ·《{_from}》"
    print(response)