import os, sys
try:
    __import__("dxx").menu()
except Exception as e:
    exit(str(e))
