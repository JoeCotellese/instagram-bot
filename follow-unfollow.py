import sys
import yaml
from random import shuffle
from instapy import InstaPy, Settings
from instapy.util import smart_run

def config_bot(config):
    Settings.chromedriver_location = config['settings']['chromedriver_location']
    Settings.log_location = config['settings']['log_location']
    Settings.database_location = config['settings']['db_location']
    session = InstaPy(username=config['auth']['username'],
                    password=config['auth']['password'],
                    headless_browser=config['settings']['browser_headless'],
                    multi_logs=True,
                    want_check_browser=False)
    session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')

    return session
def run_newbot(session, config):
    """
    This template is written by @zackvega

    What does this quickstart script aim to do?
    - This is my simple but effective script.
"""
    # let's go! :>
    with smart_run(session):
        # general settings
        session.set_relationship_bounds(enabled=True,
                                        potency_ratio=None,
                                        delimit_by_numbers=True,
                                        max_followers=6000,
                                        max_following=3000,
                                        min_followers=30,
                                        min_following=30)
        # session.set_comments(
        #     [ 'Nice shot! @{}', 
        #       'I love your profile! @{}', 
        #       '@{} Love it!',
        #       '@{} :heart::heart:',
        #       'Where did you take this @{}?',
        #     'Love your posts @{}',
        #     'Looks awesome @{}',
        #     'Getting inspired by you @{}',
        #     ':raised_hands: Yes!',
        #     ':raising_hands: Love this @{}! What camera did you use?'
        #     '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
        #     media='Photo')
        # session.set_do_like(enabled=True, percentage=100)
        hashtag_list = config['hashtags']
        # session.set_smart_hashtags(hashtag_list, limit=3, sort='top', log_tags=True)
        # session.like_by_tags(amount=10, use_smart_hashtags=True)
        session.follow_by_tags(hashtag_list, amount=100, interact=False)

        # session.set_do_comment(enabled=True, percentage=5)


        # follow activity
        # amount_number = 100
        # follow_list = config['follow_followers']
        # session.follow_user_followers(follow_list,
        #                             amount=amount_number, randomize=False,
        #                             interact=True, sleep_delay=config['settings']["follow_delay"])

        """ Joining Engagement Pods...
        """
        # session.join_pods(topic='food', engagement_mode='no_comments')


def unfollow_bot(session, config):
    with smart_run(session):
        # unfollow activity
        session.unfollow_users(amount=127, nonFollowers=True, 
                            style="RANDOM",
                            unfollow_after=42 * 60 * 60, 
                            sleep_delay=config['settings']["unfollow_delay"])

def run_bot(session, config):    
    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background

    follow_delay = config['settings']['follow_delay']
    unfollow_delay = config['settings']['unfollow_delay']
    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        #max_followers=4590,
                                        min_followers=45,
                                        min_following=77)

        # activities
        follow_list = config['follow_followers']
        session.follow_user_followers(follow_list)
        # hashtag_list = config['hashtags']
        # session.follow_by_tags(hashtag_list, amount=50)
        
        # session.like_by_tags(hashtag_list)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print ("Missing config file name")
        sys.exit()
    config = yaml.load(open(sys.argv[1], 'r'))
    try:
        session = config_bot(config)
        run_newbot(session, config)
    except Exception as e:
        print (e)
    try:
        session = config_bot(config)
        unfollow_bot(session,config)
    except Exception as e:
        print (e)

