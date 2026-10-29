import requests
import sys
import threading
from functools import partial 
from concurrent.futures import ThreadPoolExecutor
def load_wordlist(wordlist):
    with open(wordlist, "r") as f:
        for line in f:
            yield line.strip()
def check_url(url, word):
    url = url + f"/{word}"
    try:
        if requests.get(url).status_code == 200:
            return url
        return None
    except requests.exceptions.RequestException:
        return None
def run_bruteforce(url, wordlist):
    result = set()
    brute_with_url = partial(check_url, url)
    with ThreadPoolExecutor(max_workers=100) as executor:
        for r in executor.map(brute_with_url, load_wordlist(wordlist)):
            if r is not None:
                result.add(r)
        return result
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 web_dir_bruteforce.py <url> <wordlist>")
        sys.exit(1)
    result = run_bruteforce(sys.argv[1], sys.argv[2])
    if  result:
        for r in result:
            print(f"'{r}' is found")
    else:
        print("no findings")