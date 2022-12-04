msg = '''
To connect a scanner on a Wi-Fi network, 
select Start > Settings > Devices > Printer & scanners. 
Select Add a printer or scanner. Wait for your PC to 
find nearby scanners, then choose the one you want to 
use and select Add device. If you want to remove the 
scanner later, just highlight it and select Remove.
'''

msg2 = msg.replace('a', 'o')
print(msg2)

msg3 = msg.replace('scanner','router')
print(msg3)

msg4 = msg.replace('scanner','router', 3)
print(msg4)

msg5 = msg.replace('th','rh')
print(msg5)

msg5 = msg.replace('t','i',3)
print(msg5)