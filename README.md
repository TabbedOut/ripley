ripley
======
![The Stomach Burster](http://img.gawkerassets.com/img/193wi15clx5irjpg/ku-xlarge.jpg)

"The stomach burster." All of the best places to eat near the TabbedOut office. 

Resources
=======

- Good for copying x,y coords and plain text searching of location: http://mygeoposition.com/
- Google Maps : will provide walking/driving distance estimates and parsing URL will also give lat/long coords

Instructions
=======

Pretty simple stuff, mostly fill in the blank. 

1) Add a new feature to the collection with this template:
	
	{ "type": "Feature", 
      "properties": {
        "Name": "Winflo Osteria",
        "Address": "1315 W 6th St. ",
        "Walkable": "5 min.",
        "marker-symbol": "restaurant"
      }, 
      "geometry": { 
        "type": "Point", 
        "coordinates": [ -97.7599382, 30.2736973 ]
      } 
    }

2) Make sure you add a comma to the preceeding '}' to continue the array and prevent breakage. 

3) Profit?