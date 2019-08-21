#! python3
#pw.py - a password locker program.

PASSWORDS = {'chefsh': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'shcqupc': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             '18980805002': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    
