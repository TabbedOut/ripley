ripley
======
![The Stomach Burster](http://img.gawkerassets.com/img/193wi15clx5irjpg/ku-xlarge.jpg)

"The stomach burster." All of the best places to eat near the office.

Resources
---------

- Good for copying x,y coords and plain text searching of location: http://mygeoposition.com/
- Google Maps : will provide walking/driving distance estimates and parsing URL will also give lat/long coords

Instructions
------------

1. Add stuff to suchnoms.yml (in alphabetical order so we don't accidentally
   add the same place twice please).
2. Update the geojson file:

        make build

FAQ
---

What's your favorite place to eat?

> I really enjoy a 7-11 pizza. It's only $5, so it's really a good shame/$
> value.


Requirements
------------

See `make install` for more details.

- Ruby -- Seems to be the best at handing YAML and maintains ordering of YAML to JSON
- jsonpp -- Command line json pretty printer
- node -- If you want to run `make dev`
