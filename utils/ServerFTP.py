from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import tkinter as tk
from tkinter import filedialog
import sys

if len(sys.argv) > 1:
	port = int(sys.argv[1])
else:
	port = 2121
if len(sys.argv) > 2 :
	credential = sys.argv[2]
else:
	credential = "user:user"
root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory()
name = credential.split(":")
authorizer = DummyAuthorizer()
authorizer.add_user(name[0],name[1], directory, perm="elradfmwMT")
authorizer.add_anonymous(directory)
handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", port), handler)
server.serve_forever()
