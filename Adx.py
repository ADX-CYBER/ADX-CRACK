import os, sys
try:os.system('termux-setup-storage')
except:pass
try:
    __import__("arch64").menu()
except Exception as e:
    exit(str(e))
