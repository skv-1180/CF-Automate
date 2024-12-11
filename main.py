from cf_helper.utility import *
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("key")
secret = os.getenv("secret")

if __name__ == "__main__":
    handle = "CodeLegendX"
    
    user_info = get_user_info(handle)
    print("\nUser Info:")
    print(user_info)
    
    user_status = get_user_status(handle)
    print("\nUser Status (limited to 2 entries):")
    for status in user_status[:2]:
        print(status)
    
    user_friends = get_user_friends(handle, key, secret)
    print("\nUser Friends (limited to 2 entries):")
    for friend in user_friends[:2]:
        print(friend)
    
    problems, problem_statistics = get_problemset_problems(tags="dp", rating=1900)
    print("\nProblems (limited to 2 entries):")
    for problem in problems[:2]:
        print(problem)
    
    print("\nProblem Statistics (limited to 2 entries):")
    for stat in problem_statistics[:2]:
        print(stat)
    
    rating_changes = get_contest_rating_changes(contest_id=566)
    print("\nRating Changes (limited to 2 entries):")
    for change in rating_changes[:2]:
        print(change)
    
    submission_link = get_accepted_submission(handle, contestId=2040, index='C')
    print("\nSubmission Link:")
    print(submission_link)


