import asyncio
import os

from pyppeteer import launch


def getScreenshot(text,awards=6,name='aphinqq',verified=True,likes="99+",comments="99+"):
    html_content = f"""
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}

            .post {{
                width: 400px;
                background: black;
                border-radius: 10px;
                padding: 15px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                display: flex;
                flex-direction: column;
            }}

            .user-info {{
                display: flex;
                align-items: center;
                margin-bottom: 10px;
            }}

            .profile-pic {{
                width: 40px;
                height: 40px;
                border-radius: 50%;
                margin-right: 10px;
            }}

            .user-details {{
                display: flex;
                flex-direction: column;
            }}

            .username {{
                font-weight: bold;
                display: flex;
                align-items: center;
                color: white
            }}

            .verified {{
                width: 16px;
                height: 16px;
                margin-left: 5px;
            }}

            .badges {{
                display: flex;
                gap: 5px;
                margin-top: 5px;
            }}

            .badge {{
                width: 20px;
                height: 20px;
            }}

            .post-text {{
                font-size: 18px;
                font-weight: bold;
                margin: 10px 0;
                color: white
            }}

            .post-footer {{
                display: flex;
                justify-content: space-between;
                font-size: 14px;
                color: white;
                margin-top: 10px;
            }}

            .left {{
                display: flex;
                align-items: center;
                gap: 10px;
            }}

            .icon {{
                width: 16px;
                height: 16px;
                margin-right: 5px;
            }}

            .right {{
                display: flex;
                align-items: center;
                gap: 5px;
            }}

            .share-icon {{
                width: 16px;
                height: 16px;
            }}

        </style>
    </head>
    <body>
        <div class="post">
            <div class="user-info">
                <img src="https://i.aphcore.io/image/8cJ6843" alt="Reddit Logo" class="profile-pic">
                <div class="user-details">
                    <div class="username">
                        {name}
                        {'<img src="https://i.aphcore.io/image/3n8H1373" alt="" class="verified">' if verified else ''}
                    </div>
                    <div class="badges">
                        {'<img src="https://i.aphcore.io/image/bJ0D1375" alt="Award 1" class="badge">' if awards > 0 else ''}
                        {'<img src="https://i.aphcore.io/image/HfhJ1374" alt="Award 2" class="badge">' if awards > 1 else ''}
                        {'<img src="https://i.aphcore.io/image/cqAB1376" alt="Award 3" class="badge">' if awards > 2 else ''}
                        {'<img src="https://i.aphcore.io/image/BG3n1377" alt="Award 4" class="badge">' if awards > 3 else ''}
                        {'<img src="https://i.aphcore.io/image/P9HE1378" alt="Award 5" class="badge">' if awards > 4 else ''}
                        {'<img src="https://i.aphcore.io/image/QaCG1379" alt="Award 6" class="badge">' if awards > 5 else ''}
                    </div>
                </div>
            </div>
            <div class="post-text">
                {text}
            </div>
            <div class="post-footer">
                <div class="left">
                    <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                    </svg>
                    <div style="margin-left:-0.6rem">{likes}</div>
                    <svg class="icon" width="16" height="16" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                        <path d="M21 6h-2V4c0-1.1-.9-2-2-2H7C5.9 2 5 2.9 5 4v2H3c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h4l5 4 5-4h4c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-8 13l-3.5-2.5H4V8h16v8h-5.5L13 19z"/>
                    </svg>
                    <div style="margin-left:-0.6rem">{comments}</div>
                </div>
                <div class="right">
                    <svg class="share-icon" width="16" height="16" viewBox="0 0 24 24" fill="white" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18 16.08c-.76 0-1.47.3-2 .77L8.91 12.7c.05-.23.09-.47.09-.7s-.04-.47-.09-.7L16 6.92c.53.48 1.24.78 2 .78 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .23.04.47.09.7L8 10.08c-.53-.48-1.24-.78-2-.78-1.66 0-3 1.34-3 3s1.34 3 3 3c.76 0 1.47-.3 2-.77l7.09 4.15c-.05.23-.09.47-.09.7 0 1.66 1.34 3 3 3s3-1.34 3-3-1.34-3-3-3z"/>
                    </svg>
                    Share
                </div>
            </div>
        </div>
    </body>
    </html>

    """

    async def _generate_image():
        browser = await launch()
        page = await browser.newPage()
        await page.setContent(html_content)
        await page.evaluate('document.body.style.background = "transparent"')

        await asyncio.sleep(3)
        element = await page.querySelector('.post')
        bounding_box = await element.boundingBox()

        fileDir = os.path.dirname(os.path.abspath(__file__))
        await page.screenshot({
            'path': os.path.join(fileDir, "reddit_screenshot.png"),
            'omitBackground': True,
            'clip': {
                'x': bounding_box['x'],
                'y': bounding_box['y'],
                'width': bounding_box['width'],
                'height': bounding_box['height']
            }
        })
        await browser.close()

    asyncio.run(_generate_image())