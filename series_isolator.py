from id_manager import IdManager as IDM
from series import Series 

def series_to_wiki_link(name):
    return f'https://gundam.fandom.com/wiki/{name.replace(" ","_")}'
    
def convert_to_series(name,id):
    return Series(id,name,series_to_wiki_link(name))

def isolate(kit_list,id_manager):
    series_list=[]
    for k in kit_list:
        series_name = k["info"]["series"]
        if series_name not in series_list:
            series = convert_to_series(series_name,id_manager.next_id())
            series_list.append(series)
    return series_list
