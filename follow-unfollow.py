import sys
import yaml
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
                    headless_browser=False)


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
        for follow in follow_list:
            """ Massive Follow of users followers (I suggest to follow not less than 3500/4000 users for better results)...
            """
            session.follow_user_followers(follow, amount=100, randomize=True, interact=False)

            """ First step of Unfollow action - Unfollow not follower users...
            """
            session.unfollow_users(amount=50, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=12*60*60, sleep_delay=601)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print ("Missing config file name")
        sys.exit()
    config = yaml.load(open(filename, 'r'))
    run_bot(config)

