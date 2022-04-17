import requests
import json
import sys
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def request_user_info(name):
    return str(requests.get('https://pubg.op.gg/user/'+name, headers=headers).content)

def request_user_history(id_, page):  #this is valid
    return json.loads(requests.get('https://pubg.op.gg/api/users/'+id_+'/matches/recent?season=&server=na&queue_size=&mode=&after=', headers=headers).content)

def request_match_detail(id_):  #this is valid
    return json.loads(requests.get('https://pubg.op.gg/api/matches/'+id_, headers=headers).content)
    
def request_match_kill_detail(id_):  #this is valid
    return json.loads(requests.get('https://pubg.op.gg/api/matches/'+id_+'/deaths', headers=headers).content)

def request_match_history(id_):
    hist = []
    for page in range(0,1):
        feed = request_user_history(id_, page)
        if('matches' not in feed.keys()):
            break
        else:
            hist = hist + [x['match_id'] for x in feed['matches']['items']]
    return hist

def get_user_id(feed):
    return feed.split('data-user_id="')[1].split('"')[0] if 'data-user_id="' in feed else None


def mp_run(lst: list, function, processes: int):
    """Handles multiprocessing using ThreadPool; sends items from a list to a function and gets the results as a list"""
    # Define the number of processes, use less than or equal to the defined value
    count_threads = min(processes, len(lst))
    if count_threads == 0:
        return []
    pool = ThreadPool(count_threads)

    # Tell the user what is happening
    print(f"Scraping {len(lst)} items using {function} in {count_threads} processes.")

    # Calls function() and adds the filesize returned each call to an lst
    result = (pool.imap_unordered(function, lst))
    pool.close()

    # Display progress as the scraper runs its processes
    while (len(lst) > 1):
        completed = result._index

        # Break out of the loop if all tasks are done or if there is only one task
        if (completed == len(lst)):
            sys.stdout.flush()
            sys.stdout.write('\r' + "")
            sys.stdout.flush()
            break

         # Avoid a ZeroDivisionError
        if completed > 0:
            sys.stdout.flush()
            sys.stdout.write('\r' + f"{completed / len(lst) * 100:.0f}% done. {len(lst) - completed} left. ")
            sys.stdout.flush()
        sys.stdout.flush()
        sleep(1)

    pool.join()
    print("I HAVE COMPLETED!!!")
    return list(result)
