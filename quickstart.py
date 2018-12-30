import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy, Settings

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'
Settings.chromedriver_location = '/usr/local/bin/chromedriver'
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-1.21,
				  delimit_by_numbers=True,
				   max_followers=4590,
				    max_following=5555,
				     min_followers=45,
				      min_following=77)
    session.set_do_comment(True, percentage=10)
    session.set_comments(['Great photo!', 'Sweet!!', 'This is great!', "Love this!"])
    #session.set_dont_include(['friend1', 'friend2', 'friend3'])
    session.set_dont_like(['pizza', 'girl'])
    session.set_user_interact(amount=4,
				 percentage=50,
                  randomize=True,
                   media='Photo')
    session.set_use_clarifai(enabled=True, api_key='a6ae1a497caa4003855968941dbdf041')
    #                                        ^

    # uses the clarifai api to check if the image contains nsfw content
    # Check out their homepage to see which tags there are -> won't comment on image
    # (you won't do this on every single image or the 5000 free checks are wasted very fast)
    session.clarifai_check_img_for(['nsfw'], comment=False)  # !if no tags are set, use_clarifai will be False

    # actions
    
    #session.like_by_feed()
    session.like_by_tags(['#instadaily', '#tbt', '#quotes', '#picoftheday'], amount=10)
    session.follow_by_tags(tags=['#photography'], amount=50)
    session.unfollow_users(amount=100, onlyNotFollowMe=True, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=600, unfollow_after=4*24*60*60)

except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
