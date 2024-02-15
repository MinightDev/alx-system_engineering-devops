
#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code == 200:
        try:
            response_json = sub_info.json()
            posts = response_json.get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        except Exception as e:
            print("Error parsing JSON response:", e)
    elif sub_info.status_code >= 300:
        print("None")
    else:
        print("An unexpected error occurred")

