all:
	protoc bank.proto --python_out .
	python data_initializer.py account_holders
	python data_reader.py account_holders

clean:
	rm -rf account_holders
	rm -rf bank_pb2.py