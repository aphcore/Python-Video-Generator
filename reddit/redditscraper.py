import requests
import re
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
def getWordsInText(text):
    return len(re.findall(r'\S+', text))
def fetchThread(thread):
    if thread.endswith('/'):
        thread = thread[:-1]
    thread += '.json'
    response = requests.get(thread,headers=headers)
    if response.status_code == 200:
        data = response.json()  # Convert JSON response to Python dict
    else:
        raise Exception(f"Critical error when fetching reddit thread!! Error: {response.status_code} Thread: {thread}")
    title = data[0]['data']['children'][0]['data']['title']
    replies = []
    for reply in data[1]['data']['children']:
        replyParsed = reply['data']
        if not "ups" in replyParsed:
            continue
        if replyParsed['downs'] == 0:
            replyParsed['downs'] = 1
        words = getWordsInText(replyParsed['body'])
        if filtered(words):
            continue
        replies.append((replyParsed["ups"]/replyParsed["downs"],words,replyParsed["body"]))
    return (title,replies)

def filtered(text):
    swears = ['bullshit','ass', 'shit', 'fuck', "bitch", 'retard', 'lgbtq', 'lgbtq+', 'lgb','queer','motherfucker','fucker','bitchass','shitass','headass','horseshit','gay','lesbian','trans','transgender','hookup','sex','nsfw','18+','dick','pussy','cum','masturbate','damn','hell','piss','cock','cunt','prick','twat','asshole']
    pattern = r'\b(?:' + '|'.join(map(re.escape, swears)) + r')\b'
    if re.search(pattern, text, flags=re.IGNORECASE):
        print("[FLAG] Swear")
        return True
    return False

def getRedditData(thread):
    return fetchThread(thread)