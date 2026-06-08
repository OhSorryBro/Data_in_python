from operator import itemgetter
import requests

url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print(f"Status code: {r.status_code}")

submissions_ids = r.json()
submissions_dicts= []
for submission_id in submissions_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    submission_dict= {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts = sorted(submissions_dicts, key=itemgetter('comments'), reverse = True)

    for submission_dict in submission_dicts:
        print(f"\n Article name: {submission_dict['title']}")
        print(f"Link to discussion: {submission_dict['hn_link']}")
        print(f"Number of comments: {submission_dict['comments']}")