from id_manager import IdManager as IDM
from series import Series 

def series_to_wiki_link(name):
    return f'https://gundam.fandom.com/wiki/{name.replace(" ","_")}'
    

def isolate(kit_list):
    idm=IDM()
    series_list=[]
    for k in kit_list:
        series_name = k["series"]
        if series_name not in series_list:
            series = Series(idm.next_id(),series_name,series_to_wiki_link(series_name))
            series_list.insert(series)
    return series_list
