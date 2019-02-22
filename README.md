# Raw Python3 API
![N|Solid](https://img.shields.io/badge/Raw--Python3--API-v.1.0-blue.svg)

This readme document goes through an instruction to setup a simple python 3 API with no external libraries or frameworks. In this caller test, we will be sum up all number between 0 and 10000001 and expect a json response with `{"total": 50000005000000}`

##
## Environmental Setup
You will need the following programs installed on your system to use this CLI script contained in the repository
- python3.6

> _it's important to note that python 3.6 is the library we've used to test this application, however, I am confident that any version of python 3 should work properly_
##
## Using the Utility
Just clone this repository, navigate into it and run the following commands on your terminal
_before proceeding, the CLI will only work on a UNIX machine, to run this on a window machine use the python run examples given_

#### Unix Instruction

```sh
# before running any commands lets startup the server (the utility will start 
# up the server in the background on port 5000 and verbosity set to null)
./dlg.sh serve

# next we will run the test utility to be sure everything is fine, you can 
# try running the test utility before the serve is up to see what the output 
# looks like
./dlg.sh test

# let now make a proper API call, we will pass in values from 1,2,...,10000001 
# to view the output. This is a lot of data, a 10 million and one item array. 
# The server will process the total of the numbers in the array and return a 
# response to look like `{"total": 50000005000000}`
./dlg.sh call

# we can finally shutdown the server, you wouldn't want a server running on 
# your systems' background forever especially when its just a demo
./dlg.sh shutdown
``` 
&nbsp;
#### Windows Instruction

```sh
# before running any commands lets startup the server (the utility will start 
# up the server in the background on port 5000 and verbosity set to null)
# Open a new terminal tab
python3 api.py

# next we will run the test utility to be sure everything is fine, you can 
# try running the test utility before the serve is up to see what the output 
# looks like
python3 -m unittest -v tests.py

# let now make a proper API call, we will pass in values from 1,2,...,10000001 
# to view the output. This is a lot of data, a 10 million and one item array. 
# The server will process the total of the numbers in the array and return a 
# response to look like `{"total": 50000005000000}. We added a unix test utility 
# to return the time for this call to execute`
python3 call.py

# we can finally shutdown the server, just Ctrl+C on the terminal window running
# python serve.py
``` 
&nbsp;
##
#### Understanding the Test Routine
The main test routine runs the following test
##### - Tests
- check that the API is reachable, a health check
- check that the API is receiving POST calls
- check that the API returns a JSON reponse in the header
- check that the API returns a JSON response that follows the structure `{"total": <number | NaN>}`
- check that when the API is called wrongly without a number in the params the API returns `{"total": "NaN">}`
&nbsp;
