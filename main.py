from colorama import Fore

from reddit.redditscraper import getRedditData
from screenshot.screenshot import getScreenshot
from video.compileVideo import compileVideo

subreddits = [
    "stories",
    "askreddit",
    "emotionalneglect",
    'confession',
    'entitledpeople'
]

def createVideo(thread):
    print(Fore.GREEN + "Fetching Data From Reddit Thread")
    title, replies = getRedditData(thread)
    print(Fore.GREEN + "Generating Initial Title Screenshot")
    getScreenshot(title)
    wordLowerBound = 200
    wordUpperBound = 300
    filteredReplies = []
    for reply in replies:
        upvotes, words, text = reply
        if words >= wordLowerBound and words < wordUpperBound:
            filteredReplies.append(text)


    print(Fore.RED+f"Found {len(filteredReplies)} Suitable Comments")
    for filteredReply in filteredReplies:
        print(Fore.GREEN + "Compiling Video")
        compileVideo(title,filteredReply)
        print(Fore.YELLOW + "Success!")


    return


threads = [
    "https://www.reddit.com/r/AskReddit/comments/1j58taz/people_who_knew_a_killer_did_you_ever_suspect/",
]

if __name__ == "__main__":
    for thread in threads:
        createVideo(thread)