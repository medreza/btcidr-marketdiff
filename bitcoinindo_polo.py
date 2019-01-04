import urllib2
from bs4 import BeautifulSoup

alamat = "https://coinmarketcap.com/exchanges/indodax"
page = urllib2.urlopen(alamat)
soup = BeautifulSoup(page, "html.parser")
a_tabel = soup.find_all('table')[0].find('a', string="BTC/IDR").parent.parent
btcindo = float(a_tabel.find("span", {"class":"price"})['data-native'])

alamat = "https://coinmarketcap.com/exchanges/poloniex/"
page = urllib2.urlopen(alamat)
soup = BeautifulSoup(page, "html.parser")
a_tabel = soup.find_all('table')[0].find('a', string="BTC/USDT").parent.parent
btcpolo_usdt = float(a_tabel.find("span", {"class":"price"})['data-native'])

alamat = "https://coinmarketcap.com/exchanges/poloniex/"
page = urllib2.urlopen(alamat)
soup = BeautifulSoup(page, "html.parser")
currencyrate = round(float(soup.find(id="currency-exchange-rates")['data-idr']), 8)

btcpolo = btcpolo_usdt/currencyrate

print "Harga 1 BTC dalam rupiah"
print "Bitcoin Indo :"+str(btcindo)
print "Poloniex     :"+str(btcpolo)
selisih = ((btcindo-btcpolo)/btcpolo)*100
print "Selisih      :"+str(selisih)+" %"
print ""
print "Withdrawal Fee Bitcoin Indo (0.0005 BTC): Rp" + str(btcindo*0.0005)
print "Withdrawal Fee Poloniex     (0.001 BTC) : Rp" + str(btcpolo*0.001)
