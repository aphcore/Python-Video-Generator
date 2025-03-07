import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

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
    for reply in data:
        replyParsed = reply["data"]["children"][0]['data']
        if "selftext" in replyParsed:
            continue
        if replyParsed['downs'] == 0:
            replyParsed['downs'] = 1
        print(replyParsed)
        replies.append((replyParsed["ups"]/replyParsed["downs"],replyParsed["body"]))
    # print(data[0]['data']['children'])
    return (title,replies)

def sanitize(text):
    return text #in the future this function should remove all instances of when:
    # people do "EDIT: blah blah blah"
    # people putting links or other things the AI cannot say well

def getRedditData(thread):
    title, replies = fetchThread(thread)
    print(title)
    for reply in replies:
        score_ratio, text = reply
        print(str(score_ratio)+" "+str(text))

getRedditData("https://www.reddit.com/r/redditdev/comments/1j5coup/fetching_comments_for_rall_has_stopped_working/")