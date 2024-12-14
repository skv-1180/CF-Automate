import requests
import time
import hashlib
import random
import string

def get_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK' and data['result']:
            return data['result'][0]
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_user_rating(handle):
    url = f"https://codeforces.com/api/user.rating?handle={handle}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result']
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_user_status(handle, from_index=1, count=10):
    url = f"https://codeforces.com/api/user.status?handle={handle}&from={from_index}&count={count}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result']
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def generate_api_sig(method, params, secret):
    rand = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    params_str = '&'.join([f"{k}={v}" for k, v in sorted(params.items())])
    sig_base = f"{rand}/{method}?{params_str}#{secret}"
    api_sig = rand + hashlib.sha512(sig_base.encode('utf-8')).hexdigest()
    return api_sig

def get_user_friends(handle, key, secret, only_online=False):
    method = "user.friends"
    url = f"https://codeforces.com/api/{method}"
    current_time = int(time.time())
    params = {
        "apiKey": key,
        "time": current_time,
        "onlyOnline": str(only_online).lower()
    }
    api_sig = generate_api_sig(method, params, secret)
    params["apiSig"] = api_sig
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result']
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_problemset_problems(tags=None, rating=None):
    method = "problemset.problems"
    url = f"https://codeforces.com/api/{method}"
    params = {}
    if tags:
        params["tags"] = tags
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            problems = data['result']['problems']
            problem_statistics = data['result']['problemStatistics']
            if rating is not None:
                problems = [problem for problem in problems if problem.get('rating') == rating]
            return problems, problem_statistics
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_contest_rating_changes(contest_id):
    method = "contest.ratingChanges"
    url = f"https://codeforces.com/api/{method}"
    params = {
        "contestId": contest_id
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result']
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_user_rating_change(contest_id, handle):
    rating_changes = get_contest_rating_changes(contest_id)
    return list(filter(lambda change: change['handle'] == handle, rating_changes))

def get_accepted_submission(handle, contestId, index):
    submissions = get_user_status(handle)
    if submissions:
        for submission in submissions:
            if submission['problem']['contestId'] == contestId and submission['problem']['index'] == index and submission['verdict'] == 'OK':
                sub_id = submission['id']
                return f"https://codeforces.com/contest/{contestId}/submission/{sub_id}"
    else:
        print("No submissions found or error occurred.")

def get_contest_standings(contestId, from_index=1, count=5, showUnofficial=False):
    url = f"https://codeforces.com/api/contest.standings?contestId={contestId}&from={from_index}&count={count}&showUnofficial={str(showUnofficial).lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result']
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_user_standing(contestId, handles, showUnofficial=False):
    url = f"https://codeforces.com/api/contest.standings?contestId={contestId}&showUnofficial={str(showUnofficial).lower()}"
    if isinstance(handles, str):
        handles = [handles]
    url += f"&handles={';'.join(handles)}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result']
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_contest_list(gym=False):
    method = "contest.list"
    url = f"https://codeforces.com/api/{method}"
    params = {
        "gym": str(gym).lower()
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result']
        else:
            print(f"Error: {data.get('comment', 'Unknown error')}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_virtual_contests(handle, contest_type, noOfEntries=5, chooseRandom=False):
    valid_types = ["Div. 1", "Div. 2", "Div. 3", "Div. 4", "Div. 1 + Div. 2", "Educational"]
    if contest_type not in valid_types:
        print("Invalid contest type. Valid types are: Div. 1, Div. 2, Div. 3, Div. 4, Div. 1 + Div. 2, Educational")
        return []
    
    contests = get_contest_list(gym=False)
    user_status = get_user_status(handle, from_index=1, count=10000)
    attempted_contests = {status['contestId'] for status in user_status}
    
    virtual_contests = []
    for contest in contests:
        if contest['phase'] == 'FINISHED' and contest['id'] not in attempted_contests:
            if contest_type == "Div. 1 + Div. 2" and "Div. 1 + Div. 2" in contest['name']:
                duration_hours = contest['durationSeconds'] // 3600
                duration_minutes = (contest['durationSeconds'] % 3600) // 60
                contest_link = f"https://codeforces.com/contest/{contest['id']}"
                virtual_contests.append({
                    "link": contest_link,
                    "duration": f"{duration_hours}h {duration_minutes}m",
                    "name": contest['name']
                })
            elif contest_type in contest['name'] and "Div. 1 + Div. 2" not in contest['name']:
                duration_hours = contest['durationSeconds'] // 3600
                duration_minutes = (contest['durationSeconds'] % 3600) // 60
                contest_link = f"https://codeforces.com/contest/{contest['id']}"
                virtual_contests.append({
                    "link": contest_link,
                    "duration": f"{duration_hours}h {duration_minutes}m",
                    "name": contest['name']
                })
    
    if chooseRandom:
        random.shuffle(virtual_contests)
    
    return virtual_contests[:noOfEntries]

def get_unattempted_problems(handle, tags=None, rating=None, chooseRandom=False):
    problems, _ = get_problemset_problems(tags, rating)
    submissions = get_user_status(handle, from_index=1, count=10000)
    attempted_problems = {(submission['problem']['contestId'], submission['problem']['index']) for submission in submissions}
    
    unattempted_problems = []
    for problem in problems:
        if (problem['contestId'], problem['index']) not in attempted_problems:
            unattempted_problems.append(problem)
    
    if chooseRandom:
        random.shuffle(unattempted_problems)
    
    return unattempted_problems



