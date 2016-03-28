help: ## Shows this help
	@echo "$$(grep -h '#\{2\}' $(MAKEFILE_LIST) | sed 's/: #\{2\} /	/' | column -t -s '	')"

install: ## Install requirements
	brew install jq
	npm install -g nodemon

build:
	ruby ripley.rb | jq --raw-output "." > suchnoms.geojson

watch:
	nodemon --ext yml --exec "$(MAKE) --silent build"

dev: build watch
