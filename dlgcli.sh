 #!/bin/bash 

# color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
BASIC='\033[0m'
BOLD=$(tput bold)
NORMAL=$(tput sgr0)

# variables
_msg_test="running function tests with python3's unittest module"
_end_msg="deployment completed successfully"

_manual="
DLG CLI Manual
=======================

usage: $(basename "$0") deploy

where:
  serve			this command will startup the API server
  test			this command will run a functional test against 6 test assertions
  call			this command will call the API with from 1,2,...,10000001
  shutdown		this command will shutdown the server
  -h [--help]	used to access this manual

more info:
  To read more information about how this command line interface works, check out the git link on https://github.com/pukonu/Raw-Python3-API
"

exit_on_failure() {
	echo ""
	echo -e "${RED}========================================================="
	echo -e "Failed to complete this task, check that you have "
	echo -e "the server running on port :5000"
	echo -e "Just run ${BOLD}./dlg.sh serve${NORMAL}${RED} now and we will run it in"
	echo -e "the background, then you can repeat your command"
	echo -e "=========================================================${BASIC}"
	echo ""
	exit 1
}

print_completed() {
	echo ""
	echo -e "${GREEN}========================================================="
	echo -e "Completed API call successfully"
	echo -e "=========================================================${BASIC}"
	echo ""
	exit 0
}

command=$1

func_test() {
	# run python test using pytest module (exit on failure to pass test)
	echo ""
	echo -e "${GREEN}$_msg_test${BASIC}"
	python3 -m unittest -v tests.py || exit_on_failure
	echo "$_msg_test"
}

func_serve() {
	# serve the HTTP server on 5000
	python3 api.py &
}

func_call() {
	# request the API via :5000 with numbers=1,2,.....,10000001
	time python3 call.py || exit_on_failure
	print_completed
}

func_shutdown() {
	sudo kill -9 $(lsof -i :5000 | grep -v PID | awk '{print $2}')
}

if [ "$command" = 'test' ] ; then
	func_test

elif [ "$command" = 'serve' ] ; then
	func_serve

elif [ "$command" = 'call' ] ; then
	func_call

elif [ "$command" = 'shutdown' ] ; then
	func_shutdown

else
	echo "$_manual"
	
fi
