# Bank Atm Machine
This repo contains command line `Atm machine` interface with `protobuf` data structure.


## Install

To install protoc respective installation commands are

	$ sudo apt-get install protobuf-compiler
	
	$ brew install protobuf

Kindly make you have setup the [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Install the python packages that we have mention in `requirements.txt`

Example:

	$ pip install protobuf

## Usage

If have done with the installation. By running this script that will create bank account with dummy data

	$ python data_initializer.py account_holders
	
This script will show up the account holder list

	$ python data_reader.py account_holders
	
Now everything is setup just run this script and enjoy the atm interface

	$ python atm_menu.py
	
## Regenerate Protoc

	$ protoc bank.proto --python_out .
	
## Reached Me	

I can be reached at `waqar.zahour@gmail.com`