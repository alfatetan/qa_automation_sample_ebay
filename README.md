# :snake: Simple QA automate framework for eBay website

![eBay logo](/readme_makeup/images/ebay-icon-logo.png)

This project is an illustrative one and does not claim that the code is correct and optimal. The main purpose is to demonstrate my mastery of this or that technology.

This framework consists of 4 main parts:

- Header navigation testing
- Flyout main menu testing
- Search results testing
- Filter results testing

QA framework has been implemented using Selenium and Behave (BDD)

Preparing to run tests (Linux/Unix/Mac).
Execute the following command in your terminal (you can copy and paste commands below). Depending on the distribution, some commands may require you to add "sudo" at the beginning of the command and enter an administrator password.

Create a directory for this project e.g. in your home directory "/home/<user>/ebay_automation_tests"

```bash
$ mkdir ~/ebay_automation_tests && cd ~/ebay_automation_tests
```

Check if you have Python installed and which version you have:

```bash
$ which python3 && python3 --version
```

If you do not see the Python version (should be 3.x.x) and the message (python3 not found), install the python:

```bash
# for Linux Debian/Ubuntu family
$ sudo apt update && apt upgrade
$ sudo apt install python3.9.12
$ python3 --version

# for Linux CentOS/RedHat family
$ sudo yum update && apt upgrade
$ sudo yum install python3.9.12
$ python3 --version

# for Mac OS X
# install homebrew installer
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# update and upgrade installer
$ brew update && brew upgrade
# install python 3
$ brew install python3.9.12
```

Install and launch the Python virtual environment

```bash
$ python -m venv ./venv
$ source ./venv/bin/activate
```

Clone this repository:

```bash
$ git clone https://github.com/alfatetan/qa_automation_sample_ebay.git
```

Install all needed requirements:

```bash
$ pip install -r requirements.txt
```

Launch tests
All tests scenarios contained in "features" folder.

```bash
# Go to the features folder
$ cd features
```

Then you have different options to launch the tests

```bash
# Start specific test set
# behave <test_set>.feature
# e.g. start test set "search"
$ behave search.feature

# To create a report you can use "tee" command
$ behave search.feature || tee ../reports/search_report.txt

# use all test sets
$ behave
# or (if you want to save all test results)
$ behave | tee ../reports/all_test_results.txt
```

### Thank you for taking the time and attention to my work.
