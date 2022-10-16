import requests
import os
import json
import re
import os
from google.cloud import language_v1
import numpy as np

bearer_token = "my token"

search_url = "https://api.twitter.com/2/tweets/search/recent"

#query_params = {'query': '(from:elonmusk -is:reply)', 'tweet.fields': 'author_id'}
query_params = {'query': 'pepsi'}


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    textlist = []
    json_response = connect_to_endpoint(search_url, query_params)
    jsondata = json.dumps(json_response, indent=4, sort_keys=True)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    dictdata = json.loads(jsondata)
    for i in dictdata['data']:
        textlist.append(i['text'])
    print(textlist)

# Where list1 is textlist

if __name__ == "__main__":
    main()

list1 = ['RT @Varsha_Voicing: Last year, people said #TejRan R trying to copy #SidNaaz\n\nThis year, alleging #PriyankaChaharChoudhary is copying #Rubi…', "@Pepsi_the_Cutie Again, you haven't touched on the fact that he's explicitly called male by himself and others multiple times in many different adaptations, and that the only times he's called female is when people confuse him for a girl", 'RT @TheCryptoDaddi: Pepsi might be putting “Project Proton” to use 🤷🏼\u200d♂️\n\nThis is the first of many self service situations that are arisin…', 'ME HE GASTADO 2 EUROS MÁS EN EL PEDIDO PARA INCLUIR UNA PEPSI CUANDO TENGO UNA BOTELLA DE COCACOLA EN LA NEVERA https://t.co/R8Xq0hZ0rW', '@Super70sSports Greatest marketing ploy ever for Classic Coke.  I think Pepsi was destroying them at the time.', 'RT @Taka_Radjiman: PEPSI パワー\n#Taka_live https://t.co/xhEWBhFPaa', 'RT @Naranjazos10: 🔥💥 BRUTAL!\n\nParecía difícil que Pepsi superara los anteriores mundiales...\n\nPero siempre es posible evolucionar\n\nDisfruta…', "Barış Manço'nun ölümü kesin suikasttı. Volkan Konak ise Pepsi reklamında oynamayı redettikten sonra ambargoyu yedi. Eskisi gibi televizyona çıkmasına izin vermiyorlar. https://t.co/FJ92FXgKQm", 'RT @KevMagnet: “No way wine is better than Pepsi”', '@Mir2Tasha Mm mm si! Conocí cuando trabajé para Pepsi en el Desafío contra Coca Cola. El depósito de dónde salían las cargas a los puestos estaba en Pompeya, yo pasaba ahí de 08 a 12 am. El desierto.']
# str = ''
# for i in list1:
#     str += i

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'my json'
client = language_v1.LanguageServiceClient()

rs = []
for i in list1:
    text = i
    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )


    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment
    rs.append(sentiment.score)

print('Average Sentiment Score:')
print(np.average(rs))

