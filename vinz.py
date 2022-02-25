import requests
import json
import time
from os import system
#By Vinz (Don't Remove This WM !)



# SETTINGS PANEL #

LicenseKey = "VinzCloud2K21"
AppType = "application/json"
imvinz_server = "https://wa.iamvinz.com"
vinz_server_cadangan = "https://server.iamvinz.com"

# SETTINGS PANEL ENDED

####################################################
#Scroll Kebawah Jika Diperlukan
#Silahkan Recode, Jika Error ditanggung sendiri !
###################################################



























#By Vinz (Don't Remove This WM !)
# Color
cyan  = '\x1b[36m'
white = '\x1b[37m'
kuning = '\x1b[33m'
red = '\x1b[31m'
greennd= '\x1b[32m'
def vinz_banner_utama():
    system('cls||clear')
    vinz_banner_dash = """
{}_  _  _ _______     ______ _______ _______ _______ _  _  _ _______ __   __
{} |  |  | |_____|  _ |  ____ |_____|    |    |______ |  |  | |_____|   \_/  
{} |__|__| |     |    |_____| |     |    |    |______ |__|__| |     |    |                                                                               
\n 
             {}> By Vinz Development <\n\n
{}=================================
{}[SERVER] : {}VinzCloud - ID
{}[STATUS] : {}ONLINE 
{}=================================
    \n""".format(cyan, kuning, cyan, kuning, white, kuning, greennd, kuning, greennd, white)
    print(vinz_banner_dash)
def vinz_banner_end():
    system('cls||clear')
    vinz_banner_ended = """
{}_  _  _ _______     ______ _______ _______ _______ _  _  _ _______ __   __
{} |  |  | |_____|  _ |  ____ |_____|    |    |______ |  |  | |_____|   \_/  
{} |__|__| |     |    |_____| |     |    |    |______ |__|__| |     |    |                                                                               
\n 
{}Get Device Key On https://wa.iamvinz.com,
Thanks For Using our services\n\n
{}================================
====== ( CONTACT CENTER ) ======

{}[WA]    : {}50371717170
{}[EMAIL] : {}support@iamvinz.com

{}================================
""".format(cyan, kuning, cyan, kuning, white, kuning, greennd, kuning, greennd, white)
    print(vinz_banner_ended)
imvinz_pathNet = "/index.php/api/sendMessageText"
url =  imvinz_server + imvinz_pathNet
vinz_banner_utama()
DeviceKey = str(input('{}[{}?{}] {}Device ID :'.format(cyan, white, cyan, white)))
vinz_no = str(input('{}[{}?{}] {}Nomor (62xxx) :'.format(cyan, white, cyan, white)))
vinz_chat = str(input('{}[{}?{}] {}Chatnya : '.format(cyan, white, cyan, white)))
vinz_send_range = int(input('{}[{}?{}] {}Jumlah Kirim  : '.format(cyan, white, cyan, white)))
print('\n{}Creating Request...'.format(greennd))
payload = json.dumps({
  "instance_key": DeviceKey,
  "jid": vinz_no,
  "message": vinz_chat
})
headers = { 'Content-Type': AppType, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
def res():
    requests.request("GET", url, headers=headers, data=payload)
for x in range(0, vinz_send_range):
    res()
    system('cls||clear')
    print('{}\n\nVinzCloud -- Whatsapp Gateway\nSending Message #{}'.format(cyan, greennd)+ str(x+1))
    totalsend = str(x+1)
time.sleep(1)
system('cls||clear')  
print("\nLoading...") 
time.sleep(1)
system('cls||clear')  
vinz_banner_end()
print("{}</> {}RECENT CHAT {}</>{}".format(red, kuning, red, cyan))
print("\nSend To :"+ vinz_no)
print("Jumlah :"+ totalsend)
print("\nCHAT :"+ vinz_chat)
print("\n{}===={}===={}===={}===={}===={}===={}===={}====".format(red, cyan, greennd, red, cyan, greennd, red, greennd))

