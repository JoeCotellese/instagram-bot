import sys
import yaml
from random import shuffle
from instapy import InstaPy, Settings
from instapy.util import smart_run


def run_bot(config):    
    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
    Settings.chromedriver_location = config['settings']['chromedriver_location']
    Settings.log_location = config['settings']['log_location']
    Settings.database_location = config['settings']['db_location']
    session = InstaPy(username=config['auth']['username'],
                    password=config['auth']['password'],
                    headless_browser=True,
                    multi_logs=True)

    follow_delay = config['settings']['follow_delay']
    unfollow_delay = config['settings']['unfollow_delay']
    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=4590,
                                        min_followers=45,
                                        min_following=77)

        # activities
        follow_list = config['follow_followers']
        shuffle(follow_list)
        for follow in follow_list:
            """ Massive Follow of users followers (I suggest to follow not less than 3500/4000 users for better results)...
            """
            session.follow_user_followers(follow, amount=800, randomize=True, interact=False, sleep_delay=follow_delay)

            """ First step of Unfollow action - Unfollow not follower users...
            """
            session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=12*60*60, sleep_delay=unfollow_delay)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print ("Missing config file name")
        sys.exit()
    config = yaml.load(open(sys.argv[1], 'r'))
    run_bot(config)

