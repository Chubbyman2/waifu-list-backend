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

## Built With
### Django
I switched from using Flask to Django as I got the hang of REST APIs and back end development. I was absolutely blown away with how beautifully Django handles database integrations, caching, and authentication. Django, along with its beautiful integration with Supabase, form the foundation of the back end. Tables that would usually be stored in a local SQLite database are now directly integrated with Supabase, which includes Django's authentication, saved models, permissions, logs, etc.

### Supabase (PostgreSQL)
I upgraded from a locally-hosted SQLite database to using a cloud-based PostgreSQL database provider, known as Supabase. I learned how to use Supabase during my summer internship at Content Turbine, and decided to use it as they allow for easy integration of migrations from Django.

### AWS Elastic Beanstalk
Previously, I used Heroku to host all my projects, including my previous REST API. However, due to Salesforce removing all free-tier plans, it was time for an upgrade. 

## License
This project is licensed under the MIT License - see the <a href="https://github.com/Chubbyman2/waifu-database/blob/main/LICENSE">LICENSE</a> file for details.
