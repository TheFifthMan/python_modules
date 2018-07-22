
if __name__ =='__main__':
    url = "https://www.google.com/searchbyimage/upload"
    filename = {'files':('1.jpeg',open('1.jpeg','rb'),'image/jpeg')}
    proxies = {
        "http": "http://127.0.0.1:1080",
        "https": "https://127.0.0.1:1080",
        "socket5":"127.0.0.1:1080",
    }
    import requests
    r  = requests.post(url,files=filename)
    print(r.text)