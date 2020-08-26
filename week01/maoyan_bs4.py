import requests
from bs4 import BeautifulSoup as bs
import pandas 

movielist = {'Name':[],'Type':[],'Release Date':[]}

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'

myurl = 'https://maoyan.com/films?showType=3'

cookie = '__mta=210532266.1597856646388.1597856709219.1597857662901.12; uuid_n_v=v1; uuid=F50E50E0E23D11EA9E4093FE693252837CA0C6EB724249F5B2111828D7A1B702; _csrf=985048b5e3059160ef776c933c08512465d19b9070cf587b9c5768f5a4ddc007; _lxsdk_cuid=17407ad819cc8-0e8bad765cfc1b-3323767-384000-17407ad819cc8; _lxsdk=F50E50E0E23D11EA9E4093FE693252837CA0C6EB724249F5B2111828D7A1B702; mojo-uuid=05bca89a7fafaed21a6f70d22cb566ff; mojo-session-id={"id":"42f0a7841796018ad3658f182a68b1b6","time":1597856646270}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597856646,1597856696,1597856709; __mta=210532266.1597856646388.1597856707790.1597856709219.11; mojo-trace-id=16; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597857662; _lxsdk_s=17407ad819d-908-03e-960%7C%7C29'

header = {'user-agent':user_agent,'cookie':cookie}

response = requests.get(myurl,headers=header)

#print(response.text)



bs_info = bs(response.text, 'html.parser')

movie_tags = bs_info.find_all('div', attrs={'class': 'movie-hover-info'})
for tag in movie_tags[:10]:
    movie_info = tag.find_all('div',attrs={'class': 'movie-hover-title'})
    movie_name = movie_info[0].find('span',attrs={'class': 'name'}).text
    #print(movie_name)
    movie_type = movie_info[1].text.split(':')[1].strip()
    #print(movie_type)
    movie_release_date = movie_info[3].text.split(':')[1].strip()
    #print(movie_release_date)
    movielist['Name'].append(movie_name)
    movielist['Type'].append(movie_type)
    movielist['Release Date'].append(movie_release_date)


#print(movielist)
            
movies = pandas.DataFrame(data=movielist)
movies.to_csv('./moive.csv',encoding='utf8',index=False)           


