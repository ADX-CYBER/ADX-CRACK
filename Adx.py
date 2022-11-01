import os, sys
try:os.system('termux-setup-storage')
except:pass
try:
    __import__("adx101").menu()
except Exception as e:
    exit(str(e))
