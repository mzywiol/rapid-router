# Rapid Router (codename: ocargo)

[![Build Status](https://travis-ci.org/ocadotechnology/rapid-router.svg?branch=master)](https://travis-ci.org/ocadotechnology/rapid-router)
[![Coverage Status](https://coveralls.io/repos/ocadotechnology/rapid-router/badge.svg?branch=master&service=github)](https://coveralls.io/github/ocadotechnology/rapid-router?branch=master)
[![Code Climate](https://codeclimate.com/github/ocadotechnology/rapid-router/badges/gpa.svg)](https://codeclimate.com/github/ocadotechnology/rapid-router)

Rapid Router is a 'Coding For Life' project, aimed at teaching children programming concepts through a vehicle routing
game.

## To use the app
Go to the official [Code For Life website][c4l].

## To run the app locally
* Clone the repo
* Make and activate a virtualenv (We recommend [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html) - [this blog post](http://mkelsey.com/2013/04/30/how-i-setup-virtualenv-and-virtualenvwrapper-on-my-mac/) may also be
 useful if you're using a Mac)
    * e.g. the first time, `mkvirtualenv -a path/to/rapid-router rapid-router`
    * and thereafter `workon rapid-router`
* `./run` in your rapid-router dir - This will:
    * install all of the dependencies using pip
    * sync the database
    * collect the static files
    * run the server

## Run the app locally from scratch (instructions for Linux Mint)
These step by step instructions were tested on vanilla Linux Mint. Will probably work on other Linuxes as well, maybe with minor tweaks.

* Prerequisites:
    * `sudo apt-get install git`
    * `sudo apt-get install virtualenvwrapper`
    * `sudo apt-get install python-dev`
    * `sudo apt-get install ruby2.0` - although for some reason it's still Ruby 1.9 that's hiding under `ruby` command...
    * `sudo gem install sass -v 3.3.4` - because newest version (3.5) is incompatible with Ruby 1.9 (see above).
* Now start a brand new terminal.
    * `cd` to whatever path you want to clone to.
    * `git clone https://github.com/ocadotechnology/rapid-router.git`
    * `cd rapid-router`
    * The first time: `mkvirtualenv -a . rapid-router`, on subsequent times you'll only need `workon rapid-router`.
    * `./run` - this will download and setup a lot of stuff, so go grab a coffee.
* Once you see `Quit the server with CONTROL-C`, you can open the Code For Life portal in your browser, by going to `localhost:8000`.
* If you have problems seeing the portal on machines with different locale (e.g. Polish), check the terminal for errors mentioning `ValueError: unknown locale: UTF-8`. If you see them, you need to have environment variables `LANG` and `LC_ALL` both set to `en_US.UTF-8`.
    * Either export them in your `.bashrc` or `.bash_profile`
    * or restart the portal with command `LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 ./run`.

## To contribute
__Found a problem? Please check whether it has already been reported in our [issue tracker][issues] first!__ If not,
[add it][add-issue]. Please make sure that you give us a suitable level of detail about the symptoms and how to
reproduce it. Please label it as a "bug".

__Want to suggest a feature? Please check whether it has already been added to our [issue tracker][issues] first!__ if
not, [add it][add-issue]. Please make sure that you give us a suitable level of detail about the feature. Please label
it as a "suggestion". Please note that we may not act upon all suggestions, if they are not in line with the direction
we want to take the project, or if we don't have the development resources to get it done.

__Want to help develop?__ Check out the [issue tracker][issues] for the tasks we'd like to implement. The
[issues with the 'ready for pickup' label][ready-for-pickup] are tasks we think are ready to be picked up. Once you have
chosen an issue, make sure you assign it to yourself so others don't also pick it up. Develop it on your fork of the
project. Please ensure all files have the license at the top (see another source file for an example). Once you are
happy that it works, and have written tests for it, submit a pull request. We'll then look to review the changes. If it
looks good, we'll merge it. If we find issues with it, we'll let you know and hopefully we can work with you to improve
it and get it re-submitted. If it is a change that we just don't want, we'll reject it.

[c4l]: https://www.codeforlife.education/
[c4l-portal]: http://github.com/ocadotechnology/codeforlife-portal/
[issues]: https://github.com/ocadotechnology/rapid-router/issues
[add-issue]: https://github.com/ocadotechnology/rapid-router/issues/new
[ready-for-pickup]: https://github.com/ocadotechnology/rapid-router/labels/ready%20for%20pickup
