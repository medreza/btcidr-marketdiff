import urllib2
import csv
from bs4 import BeautifulSoup

alamat = "https://coinmarketcap.com/exchanges/indodax/"
page = urllib2.urlopen(alamat)
soup = BeautifulSoup(page, "html.parser")
a_tabel = soup.find_all('table')[0].find('a', string="BTC/IDR").parent.parent
btcindo = float(a_tabel.find("span", {"class":"price"})['data-native'])

alamat = "https://coinmarketcap.com/exchanges/quoine/"
page = urllib2.urlopen(alamat)
soup = BeautifulSoup(page, "html.parser")
a_tabel = soup.find_all('table')[0].find('a', string="BTC/IDR").parent.parent
btcquo = float(a_tabel.find("span", {"class":"price"})['data-native'])

print "Harga 1 BTC dalam rupiah"
print "Bitcoin Indo :"+str(btcindo)
print "Quoinex      :"+str(btcquo)
selisih = ((btcindo-btcquo)/btcquo)*100
print "Selisih      :"+str(selisih)+" %"
