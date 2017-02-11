from urllib import request

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=11&b=24&c=2016&d=0&e=24&f=2017&g=d&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)   #Konvertierung zu String; Problem: jetzt ist es ein langer String
    lines = csv_str.split('\\n')

    'File kreieren und download-Daten reinschreiben'
    destination = r'goog.csv'    #r bedeutet raw string
    fx = open(destination, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()


download_stock_data(goog_url)
