from .utility import *

def print_user_info(handle):
    user_info = get_user_info(handle)
    print("\nUser Info:")
    print(f"Handle: {user_info['handle']}")
    print(f"Name: {user_info.get('firstName', '')} {user_info.get('lastName', '')}")
    print(f"Rank: {user_info.get('rank', 'N/A')}")
    print(f"Rating: {user_info.get('rating', 'N/A')}")
    print(f"Max Rating: {user_info.get('maxRating', 'N/A')}")
    print(f"Country: {user_info.get('country', 'N/A')}")
    print(f"City: {user_info.get('city', 'N/A')}")
    print(f"Organization: {user_info.get('organization', 'N/A')}")

def print_user_status(handle, noOfEntries=5):
    user_status = get_user_status(handle)
    print("\nUser Status")
    for status in user_status[:noOfEntries]:
        print(f"Contest ID: {status['contestId']}, Index: {status['problem']['index']}, Verdict: {status['verdict']}")

def print_user_friends(handle, key, secret,noOfFriends = 5, only_online=False):
    user_friends = get_user_friends(handle, key, secret,only_online)
    print("\nUser Friends")
    for friend in user_friends[:noOfFriends]:
        print(friend)

def print_problems(noOfEntries=5, tags=None, rating=None):
    result = get_problemset_problems(tags, rating)
    if result is None:
        print("\nProblems: No data available")
        return
    problems, _ = result
    print("\nProblems")
    for problem in problems[:noOfEntries]:
        print(f"Name: {problem['name']}, Contest ID: {problem['contestId']}, Index: {problem['index']}")

def print_problem_statistics(noOfEntries=5, tags=None, rating=None):
    result = get_problemset_problems(tags, rating)
    if result is None:
        print("\nProblem Statistics: No data available")
        return
    _, problem_statistics = result
    print("\nProblem Statistics")
    for stat in problem_statistics[:noOfEntries]:
        print(stat)

def print_rating_changes(contest_id,noOfEntries=5):
    rating_changes = get_contest_rating_changes(contest_id)
    print("\nRating Changes")
    for change in rating_changes[:noOfEntries]:
        print(f"Handle: {change['handle']}, Rank: {change['rank']}, Old Rating: {change['oldRating']}, New Rating: {change['newRating']}")

def print_user_rating_change(contest_id, handle):
    rating_changes = get_user_rating_change(contest_id, handle)
    print(f"\nRating Changes for {handle}")
    for change in rating_changes:
        print(f"Rank: {change['rank']}, Old Rating: {change['oldRating']}, New Rating: {change['newRating']}")

def print_submission_link(handle, contestId, index):
    submission_link = get_accepted_submission(handle, contestId, index)
    print("\nSubmission Link:")
    print(submission_link)

def print_contest_standings(contestId, from_index=1, count=5, showUnofficial=False):
    standings = get_contest_standings(contestId, from_index, count, showUnofficial)
    if standings is None:
        print("\nContest Standings: No data available")
        return
    contest = standings['contest']
    problems = standings['problems']
    rows = standings['rows']
    
    print(f"\nContest: {contest['name']}")
    
    print("Standings:")
    for row in rows:
        print(f"  Rank: {row['rank']}, Handle: {row['party']['members'][0]['handle']}, ParticipantType: {row['party']['participantType']}")

def print_user_standing(contestId, handles, showUnofficial=False):
    standings = get_user_standing(contestId, handles, showUnofficial)
    if standings is None:
        print("\nContest Standings: No data available")
        return
    contest = standings['contest']
    rows = standings['rows']
    
    print(f"\nContest: {contest['name']}")
    
    print("Standings:")
    for row in rows:
        print(f"  Rank: {row['rank']}, Handle: {row['party']['members'][0]['handle']}, ParticipantType: {row['party']['participantType']}")

def print_upcoming_contest():
    contests = get_contest_list(gym=False)
    print("\nUpcoming Contest List:")
    upcoming_contests = [contest for contest in contests if contest['phase'] == 'BEFORE']
    for contest in upcoming_contests:
        duration_hours = contest['durationSeconds'] // 3600
        duration_minutes = (contest['durationSeconds'] % 3600) // 60
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(contest['startTimeSeconds']))
        print(f"Contest ID: {contest['id']}, Name: {contest['name']}, Duration: {duration_hours}h {duration_minutes}m, Start Time: {start_time}")

def print_virtual_contests(handle, contest_type, noOfContest=5, chooseRandom=False):
    virtual_contests = get_virtual_contests(handle, contest_type, noOfContest, chooseRandom)
    if virtual_contests:
        print("\nVirtual Contests:")
        for contest in virtual_contests:
            print(f"Name: {contest['name']}")
            print(f"Link: {contest['link']}")
            print(f"Duration: {contest['duration']}")
            print()
    else:
        print("No suitable virtual contests found.")

def print_unattempted_problems(handle, tags=None, rating=None, noOfEntries=5, chooseRandom=False):
    unattempted_problems = get_unattempted_problems(handle, tags, rating, chooseRandom)
    print("\nUnattempted Problems:")
    for problem in unattempted_problems[:noOfEntries]:
        problem_link = f"https://codeforces.com/contest/{problem['contestId']}/problem/{problem['index']}"
        print(f"Name: {problem['name']}, Contest ID: {problem['contestId']}, Index: {problem['index']}, Rating: {problem.get('rating', 'N/A')}, Link: {problem_link}")


