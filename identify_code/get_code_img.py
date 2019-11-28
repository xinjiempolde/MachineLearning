import requests
url = 'http://mathe.neu.edu.cn/code.action'
for i in range(1400):
    img_name = './RawImg/' + str(i) + '.jpg'
    response = requests.get(url)
    print(str(i) + '\n')
    with open(img_name, 'wb') as f:
        f.write(response.content)
f.close()