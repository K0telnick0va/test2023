from requests import get, post

print(get('http://127.0.0.1:5000/api/jobs').json())
print(get('http://127.0.0.1:5000/api/jobs/1').json())
print(get('http://127.0.0.1:5000/api/jobs/100').json())
print(get('http://127.0.0.1:5000/api/jobs/wsedrftgyh').json())


print(post('http://127.0.0.1:5000/api/jobs',
           json={'id': 15, 'job': 'do smth', 'work_size': 100,
                 'collaborators': '1, 2, 3',
                 'is_finished': False,
                 'team_leader': 1}).json())

