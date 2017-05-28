# PostEat
Backend bot code for PostEat bot

## Setup steps
### Virtual environment
[venv in python 3.5](https://docs.python.org/3/tutorial/venv.html)  
$ python3 -m venv venv  
$ source venv/bin/activate  
$ pip install --upgrade pip  
Then, every time I install a new package, I run  
$ pip freeze > requirements.txt

### Directory structure
From py.test suggestion, there is a link to [a blogpost with structure](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) and a [package](https://github.com/ionelmc/cookiecutter-pylibrary) has been created to manage the initial structure (refers to travis.ci integration and other goodies). This [guide](https://hynek.me/articles/testing-packaging/) seems the most up-to-date  
Old articles, but full of info, in [jeffknupp guide](https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/) can help, although there are differences like "test" and not "tests" and the lack of "src" folder

### Testing
Selected py.test in alternative to nose  
Created folder tests (pytest [suggestion](http://pytest.readthedocs.io/en/latest/goodpractices.html)) and added \_\_init__.py to avoid common pitfalls with tox    
$ pip install -U pytest  
To run tests: py.test  
(pytest will run all files in the current directory and its subdirectories of the form test_*.py or *_test.py. More generally, it follows [standard test discovery rules](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery))

To test against several environment, useful for a package, installed tox via [guide](https://tox.readthedocs.io/en/latest/)  
$ pip install tox  
$ tox-quickstart  (to create tox.ini files, and specify py.test as command to run)

### setup.py
[docs](https://docs.python.org/3/distutils/setupscript.html)  
left empty, as I'm not writing a package, but an application

### Run locally
python src/posteat/mainfile.py

### Facebook
Interact with Graph API https://developers.facebook.com/docs/graph-api/overview/
I obtained ad access token from the Graph Explorer

curl -i -X GET \
   "https://graph.facebook.com/v2.9/me?fields=id%2Cname&access_token=EAACEdEose0cBALTqc1mZBuFRVHS7pzXgU5bv7siBEOvj8gaPYLpLyVvN47Lfhvg8QRCONN9FQsnwg5n8YZCZAnEYkluZBmMiRdGN079T79fLEEoijbWSQ6VNcPQNRtWdlJKGZAJ6VilksaVcWKMZAVKCCNDAkg8worIkYuYKFEZAcIecDmCZBAsG8R983pEHUGwZD"


=== Query
  curl -i -X GET \
   "https://graph.facebook.com/v2.9/me?fields=id%2Cname&access_token=<access token sanitized>"
=== Access Token Info
  {
    "perms": [
      "public_profile"
    ],
    "user_id": 132539590632798,
    "app_id": 145634995501895
  }
=== Parameters
- Query Parameters

  {
    "fields": "id,name"
  }
- POST Parameters

  {}
=== Response
  {
    "id": "132539590632798",
    "name": "Gino Pilotino",
    "__debug__": {}
  }
=== Debug Information from Graph API Explorer
- https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=me%3Ffields%3Did%2Cname&version=v2.9




{'posts': {'paging': {'previous': 'https://graph.facebook.com/v2.7/147172505469032/posts?limit=1&since=1495815720&access_token=ss&__paging_token=ss&__previous=1', 'next': 'https://graph.facebook.com/v2.7/147172505469032/posts?limit=1&access_token=ss&until=1495815720&__paging_token=ss'}, 'data': [{'message': 'Venerdì 9 Giugno 2017 - Cena di pesce con i vini Costaripa\n\nANTIPASTO\nCarpaccio di baccalà marinato all\'aneto abbinato ad un calice di un rosè "Rosamara"\n\nPRIMO\nCalamarata con gambero rosa, Julienne di zucchine e zafferano abbinato ad un calice di un lugana "Pievecroce"\n\nSECONDO \nFiletto di branzino su letto di vellutata di asparagi e pomodorino semi dry abbinato ad un calice di un lugana "Pievecroce"\n\nDOLCE \nBavarese ai frutti di bosco\n\n25 euro, acqua e caffè inclusi.  Prenotazioni: 3356302052', 'id': '147172505469032_547288368790775', 'created_time': '2017-05-26T16:22:00+0000'}]}, 'id': '147172505469032'}

{  
   'posts':{  
      'paging':{  
         'previous':'https://graph.facebook.com/v2.7/147172505469032/posts?limit=1&since=1495815720&access_token=ss&__paging_token=ss&__previous=1',
         'next':'https://graph.facebook.com/v2.7/147172505469032/posts?limit=1&access_token=ss&until=1495815720&__paging_token=ss'
      },
      'data':[  
         {  
            'message':'Venerdì 9 Giugno 2017 - Cena di pesce con i vini Costaripa\n\nANTIPASTO\nCarpaccio di baccalà marinato all\'aneto abbinato ad un calice di un rosè "Rosamara"\n\nPRIMO\nCalamarata con gambero rosa, Julienne di zucchine e zafferano abbinato ad un calice di un lugana "Pievecroce"\n\nSECONDO \nFiletto di branzino su letto di vellutata di asparagi e pomodorino semi dry abbinato ad un calice di un lugana "Pievecroce"\n\nDOLCE \nBavarese ai frutti di bosco\n\n25 euro, acqua e caffè inclusi.  Prenotazioni: 3356302052',
            'id':'147172505469032_547288368790775',
            'created_time':'2017-05-26T16:22:00+0000'
         }
      ]
   },
   'id':'147172505469032'
}


Create a developer account etc: https://developers.facebook.com/docs/apps
Created an app
used the app id and app secret to create the token, as explained here: https://developers.facebook.com/docs/facebook-login/access-tokens#apptokens


https://facebook-sdk.readthedocs.io/en/latest/  
$ pip install facebook-sdk  
To obtain access token, start at https://developers.facebook.com/docs/facebook-login/access-tokens  
Then, it's a webapp without Javascript, so https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow 


### Test facebook
https://github.com/tino/facebook2/blob/master/test/test_facebook.py

