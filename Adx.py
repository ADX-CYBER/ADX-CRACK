import os, sys
try:
    __import__("adx").adx_()
except Exception as e:
    exit(str(e))
