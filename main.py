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

def createVideo():
    print(Fore.GREEN + "Fetching Data From Reddit Thread")
    title, replies = getRedditData("https://www.reddit.com/r/AskReddit/comments/1j58taz/people_who_knew_a_killer_did_you_ever_suspect/")
    print(Fore.GREEN + "Generating Initial Title Screenshot")
    getScreenshot(title)
    wordLowerBound = 200
    wordUpperBound = 350
    filteredReplies = []
    for reply in replies:
        upvotes, words, text = reply
        if words >= wordLowerBound and words < wordUpperBound:
            filteredReplies.append(text)


    # TEMP
    # TEMP
    # TEMP
    # filteredReplies = filteredReplies[0]
    # for filteredReply in filteredReplies:
    #     compileVideo(title,filteredReply)
    print(Fore.GREEN + "Compiling Video")
    compileVideo(title,filteredReplies[0])
    print(Fore.YELLOW + "Success!")

    # put on top of background

    # TTS & subtitles

    return

if __name__ == "__main__":
    createVideo()