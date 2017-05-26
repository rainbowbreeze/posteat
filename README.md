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