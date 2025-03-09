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


    # TEMP
    # TEMP
    # TEMP
    # filteredReplies = filteredReplies[0]
    print(Fore.RED+f"Found {len(filteredReplies)} Suitable Comments")
    for filteredReply in filteredReplies:
        print(Fore.GREEN + "Compiling Video")
        compileVideo(title,filteredReply)
        print(Fore.YELLOW + "Success!")


    # print(Fore.GREEN + "Compiling Video")
    # compileVideo(title,filteredReplies[0])
    # print(Fore.YELLOW + "Success!")

    # put on top of background

    # TTS & subtitles

    return


threads = [
    # "https://www.reddit.com/r/AskReddit/comments/1j58taz/people_who_knew_a_killer_did_you_ever_suspect/",
    # "https://www.reddit.com/r/AskReddit/comments/1j29dcb/serious_people_who_grew_up_in_a_small_town_what/",
    # "https://www.reddit.com/r/AskReddit/comments/1j1e24y/whats_a_scam_so_good_that_people_dont_even/",
    # "https://www.reddit.com/r/AskReddit/comments/1j5ejd2/those_of_you_who_grew_up_poor_what_was_your/",
    "https://www.reddit.com/r/AskReddit/comments/1j3bba5/whats_the_most_terrifying_we_need_to_leave_now/",
    # "https://www.reddit.com/r/AskReddit/comments/1j2llnm/whats_a_universally_loved_food_that_you_secretly/",
    # "https://www.reddit.com/r/AskReddit/comments/1j4o19p/people_who_unsubscribed_from_their_once_favorite/",
    # "https://www.reddit.com/r/AskReddit/comments/1j20m7s/what_is_the_disturbing_backstory_behind_something/",
    # "https://www.reddit.com/r/AskReddit/comments/1j6kzax/whats_a_sign_that_someone_is_way_smarter_than/",
    # "https://www.reddit.com/r/AskReddit/comments/1j6ktip/whats_that_one_alcoholic_drink_that_you_once_had/",
    # "https://www.reddit.com/r/AskReddit/comments/1j6hbgz/if_body_language_roughly_accounts_for_7080_of/"
]

if __name__ == "__main__":
    for thread in threads:
        createVideo(thread)