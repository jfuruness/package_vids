# lib\_work\_login

This package is a very simple one I wrote in a half hour, so lower your expectations.

All this package does is run a set of commands to log you into work through a terminal.

This is because I have to go through several ssh gateways, move dirs, activiate tmux, type my password, and sometimes I need multiple terminals going. So this is a way to make it much faster.


* [lib\_work\_login](#lib\_work\_login)
* [Description](#package-description)
* [Usage](#usage)
* [Possible Future Improvements](#possible-future-improvements)
* [Installation](#installation)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [History](#history)
* [Credits](#credits)
* [Licence](#licence)
* [Todo and Possible Future Improvements](#todopossible-future-improvements)
* [FAQ](#faq)


## Package Description
* [lib\_work\_login](#lib\_work\_login)

This package is a really simple one I wrote, it just runs a set of commands to log you into work through a terminal. If you have not configured it yet, it will write to a config file for you the set of commands you typically run to log into work. Then it will type this config file, and log you into work.

### Usage
* [lib\_work\_login](#lib\_work\_login)

#### In a Script - purely for development
You really shouldn't ever need this, but whatevs.

Also note that you don't ever need to run the configure function.
Login will run that function for you.

```python
from lib_work_login import Work_Login
# default conf path is "~/.work_login.conf and does not need changing
work_login_instance = Work_Login(conf_path="/my_conf_path")
work_login_instance.configure()  # configures script, not neseccary
work_login_instance.login()  # logs you in 
```

#### From the Command Line

NOTE: Even better, configure a custom keyboard shortcut! I use control alt l.

run in a terminal: ```login```

If you need to reconfigure (run in a terminal) ```configure```

### Installation
* [lib\_work\_login](#lib\_work\_login)

Install the package with:
```pip3 install lib_work_login```

To install from source and develop:
```
git clone https://github.com/jfuruness/lib_work_login.git
cd lib_work_login
pip3 install wheel --upgrade
pip3 install -r requirements.txt --upgrade
python3 setup.py sdist bdist_wheel
python3 setup.py develop
```

### System Requirements
* [lib\_work\_login](#lib\_work\_login)

Must have linux. You can prob change easily to support other OSes, but not currently supported

## Testing
* [lib\_work\_login](#lib\_work\_login)

Run tests on install by doing:
```pip3 install lib_off_campus_housing_parser --force --install-option test```
This will install the package, force the command line arguments to be installed, and run the tests
NOTE: You might need sudo to install command line arguments when doing this

You can test the package if in development by moving/cd into the directory where setup.py is located and running:
```python3 setup.py test```

To test a specific submodule, cd into that submodule and run:
```pytest```

Note: I currently have not written any tests, since I have tried the program and checked it's output by hand so I know that it works. I know that this is not sufficient, but no one is going to use this thing but me so whatevs.

## Development/Contributing
* [lib\_work\_login](#lib\_work\_login)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
6. Email me at jfuruness@gmail.com because I do not check those messages often

## History
* [lib\_work\_login](#lib\_work\_login)
   * 0.1.1 - Forgot to recreate egg stuff, pushing to pypi again
   * 0.1.0 - Initial commit

## Credits
* [lib\_work\_login](#lib\_work\_login)

https://stackoverflow.com/a/38493278/8903959

## License
* [lib\_work\_login](#lib\_work\_login)

BSD License

## TODO/Possible Future Improvements
* [lib\_work\_login](#lib\_work\_login)
    * Actual testing
    * Cross platform compatibility

## FAQ
* [lib\_work\_login](#lib\_work\_login)

Q: Did you just write this to procrastinate logging into work?

A: Yes
