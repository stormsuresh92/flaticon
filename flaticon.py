from requests_html import HTMLSession
import time

s = HTMLSession()

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

links = []
def page(x):
    
    url = f'https://www.flaticon.com/search/{x}?word={query}&type=icon&color=color&order_by=4'
    
    r = s.get(url, headers=header)
    
    image = r.html.find('.icon--holder')
    
    for url in image:
        
        link = url.find('img', first=True).attrs['data-src']
        
        title = url.find('img', first=True).attrs['alt'].replace(' free icon', '')
        
        links.append(link)
        
        for png in links:
            try:
                with open(title + '.png', 'wb') as f:
                    
                    r = s.get(png, stream=True)
                    
                    f.write(r.content)
            except:
                pass
            
        time.sleep(3)

query = input('Enter keyword here:')
endpage = int(input('Enter endpage:'))
for x in range(1, endpage):
    page(x)
