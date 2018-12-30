import yaml
from instapy import InstaPy, Settings
from instapy.util import smart_run

config = yaml.load(file('config.yaml', 'r'))
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
Settings.chromedriver_location = config['settings']['chromedriver_location']

session = InstaPy(username=config['auth']['username'],
                  password=config['auth']['password'],
                  headless_browser=False)


with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                     delimit_by_numbers=True,
                                      max_followers=4590,
                                      min_followers=45,
                                      min_following=77)

    #session.set_dont_include(["friend1", "friend2", "friend3"])
    #session.set_dont_like(["pizza", "#store"])


    # activities

    """ Massive Follow of users followers (I suggest to follow not less than 3500/4000 users for better results)...
    """
    session.follow_user_followers(['stalkfollowlove','lindos.rhodes.greece','suloinenjoutilaisuus'], amount=800, randomize=False, interact=False)

    """ First step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=12*60*60, sleep_delay=601)

    """ Second step of Massive Follow...
    """
    session.follow_user_followers(['reflectiongram','elponzophoto','briannamadia'], amount=800, randomize=False, interact=False)

    """ Second step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=12*60*60, sleep_delay=601)

    """ Clean all followed user - Unfollow all users followed by InstaPy...
    """
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=24*60*60, sleep_delay=601)
