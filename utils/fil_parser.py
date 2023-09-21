import requests
from bs4 import BeautifulSoup
from rich import print as rprint
import urllib3
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
import webbrowser
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
}

def extract_link(url:str)->dict:
    rprint(f"[yellow]Requesting {url} ...")
    res_dict =  dict()
    try :
        page = requests.get(url, headers=header,verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        with open("test.html","w") as f:
            f.write(str(page.content))
        data = soup.find_all('a')
        for link in data :
            if link.has_attr('href'):
                if link['href'][0:9] == "index.php":
                    res_dict[link.text] = link["href"].split("index.php?")[1]
                    # res_dict.update(url+"?"+extract_link((link['href'].split("?")[1])))
    except Exception as e:
        # rprint(f"[red] Error {e}")
        pass
    return res_dict



def create_content(cpt:int,key:str)->str :
    return  f"[b]{cpt}[/b]\n[green]{key}"

def display_res(res:dict)->dict:
    cpt = 0
    keys = dict()
    data = []
    for key in res.keys():
        # rprint(f"[green] {cpt}=> {key} : {res[key]}")
        data.append(Panel(create_content(cpt,key)))
        keys[cpt] = key
        cpt += 1
    rprint(Columns(data))
    return keys


def filter_dict(dict1:dict, seen:list)->dict:
    res = dict()
    for key in dict1.keys():
        if not key in seen:
            res[key] = dict1[key]
    return res

def clear_seen(seen:list,res:list)->list:
    for key in res:
        seen.remove(key)
    return seen


cmd_list = [
    "/q",
    "/b",
    "/h",
    "/d",
    "/o"
    "/c"
]
if __name__ == "__main__" :
    url = "https://www.fil.univ-lille.fr/portail/index.php"
    res = extract_link(url)
    keys = display_res(res)
    rprint(f"[yellow] Enter the number of the page you want to go to : ")
    cmd = ""
    index = 0
    history = dict()
    history[index] = {"url":url,"res":res.keys()}
    megaMeme = {}
    seen = list()
    seen += res.keys()
    while cmd != "/q":
        try :
            cmd = input("Enter command : ")
            code = int(cmd)
            if code in keys.keys():
                index += 1
                theUrl = url+"?"+res[keys[code]]
                res = filter_dict(extract_link(theUrl),seen)
                history[index] = {"url": theUrl,"res":res.keys()}
                megaMeme[theUrl.split('portail/')[1]] =res
                seen += res.keys()
                keys = display_res(res)
            else:
                rprint("Command not found")
        except ValueError :
            if not cmd in cmd_list:
                rprint("[red] Error : Enter a number")
        if cmd == "/b":
            if index >0:
                del history[index]
                index -= 1
                seen = clear_seen(seen,res.keys()) # Clear seen of this link
                seen = clear_seen(seen,history[index]['res']) # and the seen of the previews link
                res = filter_dict(extract_link(history[index]["url"]),seen)
                seen += res.keys()
                keys = display_res(res)
            else:
                rprint("[red] Error : You can't go back")
        elif cmd == "/h":
            rprint(history)
        elif cmd == "/q":
            rprint("[green] Bye !")
        elif cmd == "/d":
            display_res(res)
        elif cmd == "/o":
            rprint("[green] Opening the page ...")
            webbrowser.open(history[index]["url"])
        elif cmd == "/c":
            rprint(megaMeme)
        