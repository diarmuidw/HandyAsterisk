
'''
 A handy script to get the useragents for registered extensions
 It uses nothing fancy and may need tweaking on individual servers
'''
import subprocess
output = subprocess.check_output(["asterisk", "-rx", "sip show peers"])
lines = output.split('\n')

def cleanupuua(ua):
    #  Useragent    : Linksys/SPA2102-3.3.6,
    data = ua.replace('  Useragent    : ','')
    return data

fo = open('/tmp/useragent.txt', 'w')
for l in lines[:50]:
    username = l[:25]
    phone = username.split('/')[0]
    phone = phone.rstrip()
    host = l[26:40]
    longstatus = l[94:105]
    if longstatus.find('OK') >-1:
        status = 'OK'
    else:
        status = longstatus
    #print(username, host, status, phone )
    peeroutput = subprocess.check_output(["asterisk", "-rx", "sip show peer %s"%phone])
    for lo in peeroutput.split('\n'):
        if lo.find('Useragent') > -1:
            ua = cleanupuua(lo)
            s = '%s,%s,%s,%s\n'%(phone, host, ua, status)
            print(s)
            fo.write(s)
fo.close()


~~~
