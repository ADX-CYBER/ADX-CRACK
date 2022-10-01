import os, sys
try:
    __import__("arch64").menu()
except Exception as e:
    exit(str(e))
