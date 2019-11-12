info = {
    'host': 'wsl',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}
item='version'
if item in info: #validate the key
    info[item]=2.5 #update

info['architecture']='x86_64' #add

info.pop('desc') #delete

print(info['host']) #lookup

print(info)

print(info.keys())
print(info.values())
print(info.items())

for key,value in info.items(): #iterate
    print(key,'->',value)



