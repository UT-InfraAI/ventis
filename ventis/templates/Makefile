# Ventis Project Makefile
# Convenience targets for common operations.
# You can also use `ventis build` and `ventis deploy` directly.

build:
	ventis build

deploy:
	ventis deploy

clean:
	rm -f ./stubs/*_stub.py
	rm -f ./grpc_stubs/*_pb2.py
	rm -f ./grpc_stubs/*_pb2_grpc.py
	rm -rf ./docker_container/

.PHONY: build deploy clean
