import os, sys
try:
    __import__("dx").menu()
except Exception as e:
    exit(str(e))
