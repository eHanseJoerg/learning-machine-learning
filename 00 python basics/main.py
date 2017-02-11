import tuny
import random
import urllib.request

tuny.fish()

x = random.randrange(1,1000)

print(x)

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + '.png'
    urllib.request.urlretrieve(url, full_name)


download_web_image('https://thenewboston.com/photos/users/2/resized/8aa8647e9d0606074a04bfb6ee64fa70.png')
