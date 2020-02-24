from telegram.ext import Updater
#updater = Updater('1085952720:AAFOdU5rcADlTlY4ll77BunsxbZC63PP7mU', use_context=False)
PROXY = {'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater("1085952720:AAFOdU5rcADlTlY4ll77BunsxbZC63PP7mU", request_kwargs=PROXY)
    mybot.start_polling()
    mybot.idle()
main()