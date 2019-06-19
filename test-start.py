import requests
print("""
                         +-------------------+
                         | [~]CALL-PRANK[~]  |
                         +-------------------+
                          Auto Haws/Termux-Lab
""")
print('')
num_phone = input('[*]phone: ')
name = input("[*]name: ")
print('''
                  |  [!]Select prank  |')
[1] ~ Titan gel order?
[2] ~ Alo.. It`s Mvideo? //no work
[3] ~ WTF?               //no work
[4] ~ GOLD GOLD GOLD     //no work
''')
call = input('[*]Prank: ')
urls = [
'',
'https://titan-gel-official.ru/send.php',
'https://www.mvideo.ru/callback-checkout?_DARGS=/sitebuilder/blocks/help/callbackForm.jsp',
'https://mebelin-kazan.ru/callback.html',
'http://silver-kazan.ru/local/ajax/request_call.php'
]
post_name = [
'',
'name',
'clientName',
'client',
'NAME'
]
post_phone = [
'',
'phone',
'/com/mvideo/callback/CallbackFormHandler.contactPhone',
'phone',
'PHONE'
]
urls_call = len(urls)
start_call = 0
yn = input("[!*]Want to continue? [y/n]: ")
if(yn == 'y'):
    if(call > urls_call):
        print('''
+----------------+
[!]Select a number from the list!
+----------------+
             ''')
    else:
        requests.post(urls[call],
        data = {
        post_name[call]: name,
        post_phone[call]: num_phone},
        headers = {
        'Accept-Language':'en-US,en;q=0.5',
        'Connection':'keep-alive',
        'Host': urls[call],
        'origin': urls[call],
        'Referer': urls[call]})
        print('''
+----------------+
[!]Result - OK
+----------------+
         ''')
else:
    print('''
+----------------+
[!]Stopped!
+----------------+
         ''')
