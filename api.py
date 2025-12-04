#import requests
#url="https://jsonplaceholder.typicode.com/users/2"
#response=requests.get(url)
#data=(response.json())
#print("NAME:",data["name"])
#print("EMAIL:",data["email"])
#print("CITY:",data["address"]["city"])

#import requests
#url="https://jsonplaceholder.typicode.com/comments?postId=1"
#response=requests.get(url)
#comments=(response.json())
#if len(comments)>0:
#    print(f"First Comment:{comments}")
#    print(f"Total comments:",{len(comments)})
#else:
#    print("No comments found")


#import requests
#url="https://jsonplaceholder.typicode.com/posts"
#payload={
 #   "title":"Automation testing",
#    "body":"this is a POST request created by me",
#    "id1":99
#}
#response=requests.post(url,json=payload)
#print(response.status_code)
#print(response.json())

import requests
url="https://jsonplaceholder.typicode.com/posts/1"
payload={
  "id": 1,
  "title": "Updated full post",
  "body": "Updated body using PUT request",
  "userId": 1
    }
response=requests.put(url,json=payload)
put_json=response.json()
print(f"Updated title:",put_json["title"])
print(f"Updated body:",put_json["body"])


