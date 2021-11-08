from requests_html import HTMLSession
import os

s = HTMLSession()

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}


def page(x):
    cur_dir = os.getcwd()
    pdf = cur_dir + f'/{query}'
    if not os.path.exists(pdf):
        os.mkdir(pdf)

    url = f'https://www.flaticon.com/search/{x}?word={query}&type=icon'
    r = s.get(url, headers=header)
    image = r.html.find('.icon--holder')
    for urls in image:
        imgtag = urls.find('img', first=True).attrs['data-src']
        title = urls.find('img', first=True).attrs['data-src'].split('/')[-1]
        if imgtag.endswith('.png'):
            img = imgtag

            with open(pdf + '/' + title, 'wb') as f:
                res = s.get(img, stream=True)
                f.write(res.content)

    return 
   



query = input('Enter keyword here:')
endpage = int(input('Enter endpage:'))
for x in range(1, endpage):
    page(x)


