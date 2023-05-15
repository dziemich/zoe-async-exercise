run-server:
	poetry run python src/server

run-client:
	poetry run python src/client

generate-proto:
	poetry run python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. src/proto/inference.proto

.PHONY: run-server run-client generate-proto