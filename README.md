# cf_helper Library

A Python library for interacting with the Codeforces API, allowing you to fetch user information, ratings, problems, contests, and more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Key Setup](#api-key-setup)
- [Functions](#functions)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Installation
To use `cf_helper`, you need to install the library. Make sure you have `pip` installed on your system.

```bash
pip install cf-helper
```

## API Key Setup
To access private data via the Codeforces API, you'll need to generate an API key:

1. **Go to Codeforces**: Visit [https://codeforces.com/settings/api](https://codeforces.com/settings/api).
2. **Create a new API Key**: Provide a name for the key, and Codeforces will generate two parameters:
   - **Key**: The public part of the API key.
   - **Secret**: A private, secret part used for signing requests.
3. **Store the Key and Secret**:
   - Add your `key` and `secret` to an environment variable file (e.g., `.env`):
     ```
     key="your_api_key"
     secret="your_api_secret"
     ```

## Usage
1. **Importing Functions**
   ```python
   from cf_helper.utility import *
   from dotenv import load_dotenv
   import os

   load_dotenv()
   key = os.getenv("key")
   secret = os.getenv("secret")

   if __name__ == "__main__":
       handle = "CodeLegendX"
   ```

2. **Fetch User Information**
   ```python
   user_info = get_user_info(handle)
   print("\nUser Info:")
   print(user_info)
   ```

3. **Fetch User Status**
   ```python
   user_status = get_user_status(handle)
   print("\nUser Status:")
   for status in user_status[:2]:
       print(status)
   ```

4. **Fetch User Friends**
   ```python
   user_friends = get_user_friends(handle, key, secret)
   print("\nUser Friends:")
   for friend in user_friends[:2]:
       print(friend)
   ```

5. **Fetch Problems**
   ```python
   problems, problem_statistics = get_problemset_problems(tags="dp", rating=1900)
   print("\nProblems:")
   for problem in problems[:2]:
       print(problem)
   ```

6. **Fetch Problem Statistics**
   ```python
   print("\nProblem Statistics:")
   for stat in problem_statistics[:2]:
       print(stat)
   ```

7. **Fetch Contest Rating Changes**
   ```python
   rating_changes = get_contest_rating_changes(contest_id=566)
   print("\nRating Changes:")
   for change in rating_changes[:2]:
       print(change)
   ```

8. **Fetch Accepted Submission**
   ```python
   submission_link = get_accepted_submission(handle, contestId=2040, index='C')
   print("\nSubmission Link:")
   print(submission_link)
   ```

## Functions
- `get_user_info(handle)`: Fetches user information for a given Codeforces handle.
- `get_user_rating(handle)`: Fetches user rating history.
- `get_user_status(handle, from_index=1, count=10)`: Fetches user submissions.
- `generate_api_sig(method, params, secret)`: Generates an API signature for secure requests.
- `get_user_friends(handle, key, secret, only_online=False)`: Fetches friends list.
- `get_problemset_problems(tags=None, problemset_name=None, rating=None)`: Fetches problems from the problem set.
- `get_contest_rating_changes(contest_id)`: Fetches contest rating changes.
- `get_accepted_submission(handle, contestId, index)`: Fetches a link to an accepted submission.

## Limitations
- The library accesses only public data when the API key is not used.
- Private data (e.g., hacks during contests) requires a valid API key.
- The methods are rate-limited by the Codeforces API. Use responsibly.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

