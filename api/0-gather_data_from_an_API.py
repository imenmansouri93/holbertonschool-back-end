#!/usr/bin/python3
''''is this the real world'''
import requests
import sys
if __name__ == '__main__':
    identity = sys.argv[1]
    payload = {"userId": identity}
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(identity)).json()
    list = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=payload).json()

    completed = []
    for task in list:
        if task.get("completed") is True:
            completed.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(list)))
    for complete in completed:
        print("\t {}".format(complete))

