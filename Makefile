init:
	pip3 install -r docs/requirements.txt
	python3 scripts/module_creator.py

dev-run:
	./scripts/dev-mode-launcher.sh

docker-build:
	cd scripts
	./docker-build.sh

docker-run:
	cd scripts
	./docker-run.sh
