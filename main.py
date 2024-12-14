from cf_helper import *
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("key")
secret = os.getenv("secret")

if __name__ == "__main__":
    handle = "CodeLegendX"
    print_user_info(handle)
    print_user_status(handle, noOfEntries=2)
    print_user_friends(handle, key, secret,5, only_online=False)
    print_problems(noOfEntries=2, tags="dp", rating=1900)
    print_rating_changes(contest_id=566, noOfEntries=2)
    print_user_rating_change(contest_id=2040, handle="CodeLegendX")
    print_submission_link(handle, contestId=2040, index='G')
    print_contest_standings(contestId=2040, from_index=1, count=5, showUnofficial=True)
    print_user_standing(contestId=2006, handles="tourist;jiangly", showUnofficial=True)
    print_upcoming_contest()
    print_virtual_contests(handle, "Div. 3", noOfContest=10, chooseRandom=True)
    print_unattempted_problems(handle,tags="dp", rating=1900, noOfEntries=5,chooseRandom=True)


