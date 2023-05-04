import openai
import time
import os
import json
openai.api_key="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"
def hoiGPT(cauhoi,tenfile):
    answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "Hãy giới thiệu " + cauhoi},
        ]
    )
    with open('data/'+tenfile+'.txt', 'w',encoding='utf-8') as f:
        f.write(str(answer["choices"][0]["message"]["content"]))
with open('listCauhoi.json', 'r',encoding='utf8') as f:
    data=json.loads(f.readline())
    for x in data:
        print('data/'+x["filename"]+'.txt')
        if not os.path.exists('data/'+x["filename"]+'.txt'):
            hoiGPT(x["name"],x["filename"])
            time.sleep(10)
