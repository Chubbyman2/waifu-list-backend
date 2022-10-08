# waifu-list-backend
This is essentially an upgrade of my <a href="https://github.com/Chubbyman2/waifu-list-api">previous waifu list REST API</a>. There are numerous differences in this project, which will be highlighted in the **Built With** section. That being said, may I present the new and improved <a href="http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/">Waifu List REST API</a>!

## Getting Started
To get started locally, clone the repo and install the necessary dependencies. Then:
1. Go to settings.py, set DEBUG=False for local deployment
2. cd waifu_list
3. python manage.py runserver

### Prerequisites
```
python==3.8.0
Django==4.1.2
djangorestframework==3.14.0
Pillow==9.2.0
psycopg2==2.9.4
python-dotenv==0.21.0
supabase==0.6.0
```

## REST API Documentation

### GET
Given a waifu ID or name, return the waifu entry.
- Endpoint: http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/api
- "id" and/or "name" required
```py
BASE = "http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/"
query = {
    "name": "Makise Kurisu",
    "anime": "Steins;Gate",
}
response = requests.get(BASE + "api", json=query)
print(response.json())
# {'id': 1, 'name': 'Lynn Wiles', 'anime': 'Pulse', 'rank': 1, 'description': 'My ideal girl', 'image': 'lynn_wiles.png', 'created_at': '2022-10-08T17:31:32.100908Z', 'updated_at': '2022-10-08T17:31:32.100908Z'}
```

### POST
Given all necessary fields, create a new waifu entry.
- Endpoint: http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/api
- "name", "anime", "rank", "description", "image" required
```py
BASE = "http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/"
query = {
    "name": "Makise Kurisu",
    "anime": "Steins;Gate",
    "rank": 2,
    "description": "The assistant",
    "image": "makise_kurisu.png"
}
response = requests.post(BASE + "api", json=query)
print(response.json())
# {'id': 2, 'name': 'Makise Kurisu', 'anime': 'Steins;Gate', 'rank': 2, 'description': 'The assistant', 'image': 'makise_kurisu.png', 'created_at': '2022-10-08T20:30:22.072971Z', 'updated_at': '2022-10-08T22:17:17.188822Z'}
```

### PUT
Given a waifu ID or name, along with the fields to be changed, update the waifu entry.
- Endpoint: http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/api
- "id" and/or "name" required
```py
BASE = "http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/"
query = {
    "name": "Makise Kurisu",
    "description": "Zombie girl"
}
response = requests.put(BASE + "api", json=query)
print(response.json())
# {'id': 2, 'name': 'Makise Kurisu', 'anime': 'Steins;Gate', 'rank': 2, 'description': 'Zombie girl', 'image': 'makise_kurisu.png', 'created_at': '2022-10-08T20:30:22.072971Z', 'updated_at': '2022-10-08T22:17:17.188822Z'}
```

### DELETE
Given a waifu ID or name, delete the waifu entry.
- Endpoint: http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/api
- "id" and/or "name" required
```py
BASE = "http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/"
query = {
    "name": "Makise Kurisu",
    "description": "Zombie girl"
}
response = requests.delete(BASE + "api", json=query)
print(response.json())
# {'message': 'Waifu successfully deleted.'}
```

### GET ALL
Returns all waifus in the database. No fields required.
- Endpoint: http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/api/all
```py
BASE = "http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/"
response = requests.get(BASE + "api/all", json=query)
print(response.json())
# [{'id': 1, 'name': 'Lynn Wiles', 'anime': 'Pulse', 'rank': 1, 'description': 'My ideal girl', 'image': 'lynn_wiles.png', 'created_at': '2022-10-08T17:31:32.100908Z', 'updated_at': '2022-10-08T17:31:32.100908Z'}, {'id': 2, 'name': 'Makise Kurisu', 'anime': 'Steins;Gate', 'rank': 2, 'description': 'Zombie girl', 'image': 'makise_kurisu.png', 'created_at': '2022-10-08T20:30:22.072971Z', 'updated_at': '2022-10-08T20:30:22.072971Z'}]
```

### DELETE ALL
Deletes all waifus in the database. No fields required.
- Endpoint: http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/api/all
```py
BASE = "http://waifu-list.eba-wprwgyza.us-east-1.elasticbeanstalk.com/"
response = requests.delete(BASE + "api/all", json=query)
print(response.json())
# {'message': 'All waifus successfully deleted.'}
```

## Built With
### Django
I switched from using Flask to Django as I got the hang of REST APIs and back end development. I was absolutely blown away with how beautifully Django handles database integrations, caching, and authentication. Django, along with its beautiful integration with Supabase, form the foundation of the back end. Tables that would usually be stored in a local SQLite database are now directly integrated with Supabase, which includes Django's authentication, saved models, permissions, logs, etc.

### Supabase (PostgreSQL)
I upgraded from a locally-hosted SQLite database to using a cloud-based PostgreSQL database provider, known as Supabase. I learned how to use Supabase during my summer internship at Content Turbine, and decided to use it as they allow for easy integration of migrations from Django.

### AWS Elastic Beanstalk
Previously, I used Heroku to host all my projects, including my previous REST API. However, due to Salesforce removing all free-tier plans, it was time for an upgrade. 

## To Do
### Authentication
Once the front end is up and running, and an authentication page is available, I will add a check for authorized users in the endpoints. Supabase and Django make this super easy.

### Caching w/ Redis
Django also has Redis integration, which I will look into in the future. This will help in case I get famous one day and lots of people check out my waifu list xD

## License
This project is licensed under the MIT License - see the <a href="https://github.com/Chubbyman2/waifu-database/blob/main/LICENSE">LICENSE</a> file for details.
