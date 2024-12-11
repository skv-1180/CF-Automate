# cf-helper Library

A Python library for interacting with the Codeforces API, allowing you to fetch user information, ratings, problems, contests, and more.

---

## Table of Contents
- [Installation](#installation)
- [API Key Setup (Optional)](#api-key-setup-optional)
- [Usage](#usage)
  - [Importing the Library](#importing-the-library)
  - [Examples](#examples)
- [Functions](#functions)
- [Limitations](#limitations)
- [License](#license)

---

## Installation

To use `cf-helper`, you need to install the library. Ensure you have `pip` installed on your system.

```bash
pip install cf-helper
```

---

## API Key Setup (Optional)

To access private data via the Codeforces API, you'll need to generate an API key:

1. **Go to Codeforces**: Visit [Codeforces API Settings](https://codeforces.com/settings/api).
2. **Create a New API Key**: Provide a name for the key. Codeforces will generate:
   - **Key**: The public part of the API key.
   - **Secret**: A private part used for signing requests.
3. **Store the Key and Secret**:
   - Add your `key` and `secret` to a `.env` file in your project directory:
     ```
     key="your_api_key"
     secret="your_api_secret"
     ```

---

## Usage

### Importing the Library

The library provides utilities for easy interaction with the Codeforces API. Simplify your imports using the `cf_helper` package.

```python
from cf_helper import *
# No need to do below steps if only public functions are used
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("key")
secret = os.getenv("secret")
```

---

### Examples

Below are examples of various functions provided by the library.

#### Fetch User Information
```python
handle = "CodeLegendX"
print_user_info(handle)
```

#### Fetch User Status
```python
print_user_status(handle, noOfEntries=2)
```

#### Fetch User Friends
```python
print_user_friends(handle, key, secret, noOfFriends=2)
```

#### Fetch Problems
```python
print_problems(noOfEntries=2, tags="dp", rating=1900)
```

#### Fetch Contest Rating Changes
```python
print_rating_changes(contest_id=2040, noOfEntries=2)
```

#### Fetch User Contest Rating Change
```python
print_user_rating_change(contest_id=2040, handle="CodeLegendX")
```

#### Fetch Accepted Submission
```python
print_submission_link(handle, contestId=2040, index='C')
```

#### Fetch Contest Standings
```python
print_contest_standings(contestId=2040, from_index=1, count=5, showUnofficial=True)
```

#### Fetch User Standing in Contest
```python
print_user_standing(contestId=2006, handles="tourist;jiangly", showUnofficial=True)
```

---

## Functions
- `print_user_info(handle)`: Display user information in a readable format.
- `print_user_status(handle, noOfEntries)`: Display user submission status.
- `print_user_friends(handle, key, secret, noOfFriends, only_online)`: Display user friends.
- `print_problems(noOfEntries, tags, rating)`: Display problems.
- `print_rating_changes(contest_id, noOfEntries)`: Display contest rating changes.
- `print_user_rating_change(contest_id, handle):`: Display user contest rating change.
- `print_submission_link(handle, contestId, index)`: Display accepted submission link.
- `print_contest_standings(contestId, from_index, count, showUnofficial)`: Display contest standings.
- `print_user_standing(contestId, handles, showUnofficial)`: Display standings for specific handles in a contest.

---

## Limitations

- **Public Data Only**: Without an API key, only public data is accessible.
- **Rate Limits**: The Codeforces API has rate limits. Avoid excessive requests.
---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

