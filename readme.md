# Usage

#### This program allows you to generate multiple videos off of a single reddit thread.
#### The video will be 60 seconds long and cropped for mobile devices. Perfect for platforms such as Youtube Shorts or TikTok.
#### Examples: https://www.youtube.com/@aphinqq/shorts

## Setting up:
 - Create a folder in the root directory named 'output'
 - Create a folder in /video named 'background_footage'
 - Find some background footage for the video and place it in the folder from the previous step. The program automatically crops it.
 - Name your video(s) "worker[number].mp4" starting at 0. For example, worker0.mp4 & worker1.mp4

## Changing settings:
 - Change the screenshot features: /screenshot/screenshot.py
 - Changing video settings: /video/compileVideo.py
 - Changing the lower and upper bounds for word count: /reddit/redditscraper.py

## Running
 - Input a reddit thread into the 'threads' array in main.py
 - Install dependencies
 - Run main.py