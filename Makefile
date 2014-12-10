build:
	python geocities.py suchnoms.yml > suchnoms.geojson

# If you don't have inotify-tools, install it first: `apt-get install inotify-tools`
watch:
	@while true; do \
	inotifywait  -e modify -e move -e create -e delete \
	suchnoms.yml && $(MAKE) --silent build; \
	done
