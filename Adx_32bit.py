import os, sys
try:
    __import__("arch32").menu()
except Exception as e:
    exit(str(e))
