## So you want to **clone** the project and figure out **what** to do...
* The good practice is to: 
    * Fork the project on your account
    * Clone your repo using HTTPS
    * Work on a new git branch.
    * Need help with [git](https://git-scm.com/docs/gittutorial)?
    Anyway you can't use Ocado Technology's master.
* The [issues are listed on ocadotechnology/rapid-router](https://github.com/ocadotechnology/rapid-router/issues). 
It's even better if you're using [ZenHub](https://www.zenhub.com/) because it will allow you to look at a [Kanban-ish board](https://github.com/ocadotechnology/rapid-router/issues#boards) for the project.<br>
One word of caution: please do not add any issues related to security. Evil hackers are everywhere nowadays... If you do find a security issue, let us know using our [contact form][c4l-contact-form].

## Now you want to **test** your changes and **run** the project locally... (UNIX)
* To work on the project, you can use whichever editor you like. Lots here like [IntelliJ or PyCharm](https://www.jetbrains.com/), for instance.
* There are some more [guidelines here](https://github.com/ocadotechnology/rapid-router#to-contribute)
* As said in the [readme](https://github.com/ocadotechnology/rapid-router), you should set up a virtual environment. 
    * e.g. the first time, `mkvirtualenv -a path/to/rapid-router rapid-router`
    * and thereafter: `workon rapid-router`
* You can test your change by running the test suite - you can go to the root of the project and type: `python example_project/manage.py test` ; but Travis uses `python setup.py test` (will also install stuff in your virtualenv needed for the tests)
* To manually test things and run the project, `./run` in the root.

## Great, you can **commit**, open a **Pull Request**, and we'll **review** it...
* Then you can commit! On a new branch for a new Pull Request please.
* If your commit resolves a GitHub issue, please include “fixes #123” in the commit message.
* Then you can push to your forked repo, and create a pull request from your branch to ocadotechnology's master branch.
* Some tests will run automatically: Travis will run the automated tests, coverage will test the test coverage and codeclimate will test the code quality. Please fix found issues, then repush on your branch - it will rerun the tests.
* Do not accept a PR yourself - at least one other person should review your code and approve it first.
* Some old PRs will need to see the branch rebased on the current master
* When a PR is accepted, **congrats!** It will be merged on master.

[c4l-contact-form]: https://www.codeforlife.education/help/#contact