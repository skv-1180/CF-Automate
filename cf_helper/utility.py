import requests
import time
import hashlib
import random
import string
from bs4 import BeautifulSoup


def get_user_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['result'][0]
        else:
            print(f"Error: {data['comment']}")
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
            print(f"Error: {data['comment']}")
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
            print(f"Error: {data['comment']}")
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
            print(f"Error: {data['comment']}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_problemset_problems(tags=None, problemset_name=None, rating=None):
    method = "problemset.problems"
    url = f"https://codeforces.com/api/{method}"
    params = {}
    if tags:
        params["tags"] = tags
    if problemset_name:
        params["problemsetName"] = problemset_name
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
            print(f"Error: {data['comment']}")
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
            print(f"Error: {data['comment']}")
    else:
        print(f"HTTP Error: {response.status_code}")

def get_accepted_submission(handle, contestId, index):
    submissions = get_user_status(handle)
    if submissions:
        for submission in submissions:
            if submission['problem']['contestId'] == contestId and submission['problem']['index'] == index and submission['verdict'] == 'OK':
                sub_id = submission['id']
                return f"https://codeforces.com/contest/{contestId}/submission/{sub_id}"
    else:
        print("No submissions found or error occurred.")


