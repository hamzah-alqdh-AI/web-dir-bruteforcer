# Web Directory Bruteforce
A multithreaded tool that discovers directories and files on a web server by testing path from a wordlist against http response codes.
## Requirements 
- Python 3.7+
- requests
## Installation
```bash
git clone http://github.com/hamzah-alqdh-AI/web-dir-bruteforcer.git
cd web-dir-bruteforcer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```
## Usage

```bash
python3 web_dir_bruteforcer.py <url> <wordlist>
```

Example:

```bash
python3 web_dir_bruteforcer.py http://localhost:8000 wordlist.txt
```
## Limitations
- Assumes valid inputs: the tool does not handle a missing wordlist file or an unreachable URL gracefully, and will exit with an error in those cases.
- Duplicate wordlist entries still trigger duplicate http requests, though duplicate results are removed from the output.
- Fixed to HTTP GET requests and status code 200 as the "found" signal. 
