import requests
import sys
from rich import print as rprint
from rich import print_json
import time
import xml.dom.minidom


match len(sys.argv):

    case 2:
        path = sys.argv[1]
        typ  = "get"
        formats = "*/*"
        save = None
    case 3:
        path = sys.argv[1]
        typ  = sys.argv[2]
        formats = "*/*"
        save = None
    case 4:
        path = sys.argv[1]
        typ  = sys.argv[2]
        formats = sys.argv[3]
        save = None
    case 5:
        path = sys.argv[1]
        typ  = sys.argv[2]
        formats = sys.argv[3]
        save = sys.argv[4]
    case _:
        path = "/"
        typ  = "get"
        formats = "*/*"
        save = None
        
file = {"file":open("vehicule.json","rb")}
data = {
    "username":"",
    "password":"",
    "email":"",
    "host":"",
    "port":"21",
    "name":""
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0."
}

headers["accept"] = formats
headers['key'] = "01b7c26ada1bbc0d3d9792ddceedc3666c14a336781465bf94f98892141ab8a1"
headers['user'] = "user"
headers['pass'] = "12345"
#headers['Content-Type']= "application/x-www-form-urlencoded"
url = "http://localhost:8080/"+path
rprint("[blue]===============================[REQUETE]=========================")
rprint("[green]url :"+url)
rprint("Request type : "+typ.upper())
rprint("Header content : ",end="")
rprint(headers)
start = time.time()
match typ:
    case "put":
        response = requests.put(url, headers=headers,data=data)
    case "post":
        rprint("POST data : ",end="")
        rprint(data)
        response = requests.post(url,files=file, headers=headers,data=data)
        #response = requests.post(url, headers=headers,data=data)
    case "get":
        response = requests.get(url, headers=headers)
    case "delete":
        response = requests.delete(url, headers=headers)
    
end = time.time()
rprint(f"[blue]==============================[REPONSE][{round(end-start,3)} s]=========================")
rprint("Code Retour : "+str(response.status_code))
rprint("Header : ",end="")
rprint(response.headers)
rprint("Content : ",end="")
if (response.status_code == 200):
    if "json" in response.headers.get("Content-Type") and not "xml" in formats :
        if (response.text != ""):
            print_json(response.text)
    elif "xml" in response.headers.get("Content-Type") or "xml" in formats:
        dom =  xml.dom.minidom.parseString(response.text)
        pretty_xml_as_string = dom.toprettyxml()
        if save is not None:
            with open(save,"wb") as f:
                      f.write(response.content)
        else:
            rprint(pretty_xml_as_string)
    else:
        if save is not None:
            with open(save,"wb") as f:
                f.write(response.content)
        else:
            rprint(response.text)
else:
    if save is not None:
        with open(save,"wb") as f:
            f.write(response.content)
    else:
        rprint(response.text)

