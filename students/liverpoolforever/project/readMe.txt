Modified Project : 

1. Builds a simple web form (was hoping for a dashboard) using Flask
2. Takes a single input from the form which is location - ex : Manhattan , Brooklyn , Queens
3. Uses that input to query a MongoDB instance to count no of restaurants in that location

Resources:

1. The Flask implementon references this tutorial - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-now-with-python-3-support
2. MongoDB dataset - https://docs.mongodb.com/getting-started/shell/query/

Directory Stucture:

Nachikets-MacBook-Pro:project nachiketgalande$ ls -lrt

total 40
-rw-r--r--   1 nachiketgalande  staff   114B Dec  3 22:27 pyvenv.cfg
drwxr-xr-x   3 nachiketgalande  staff   102B Dec  3 22:27 lib/
drwxr-xr-x   2 nachiketgalande  staff    68B Dec  3 22:27 include/
-rw-r--r--   1 nachiketgalande  staff    60B Dec  3 22:30 pip-selfcheck.json
drwxr-xr-x  14 nachiketgalande  staff   476B Dec  3 22:30 bin/
drwxr-xr-x   2 nachiketgalande  staff    68B Dec  3 22:35 tmp/
-rwxr-xr-x   1 nachiketgalande  staff   146B Dec  3 23:08 run.py*
-rw-r--r--   1 nachiketgalande  staff    60B Dec  6 00:29 config.py
drwxr-xr-x   3 nachiketgalande  staff   102B Dec  6 00:31 __pycache__/
drwxr-xr-x  13 nachiketgalande  staff   442B Dec 11 21:41 app/
-rw-r--r--   1 nachiketgalande  staff   141B Dec 11 21:44 readMe.txt

Main Scripts:

1. run.py runs the Flask instance in a virtualenv(in the bin folder)
2. /app/forms.py has the Form class which captures input from the web form
3. /app/templates has the html pages - http://localhost:5000/dashboard is the one which I am using
4. /app/views.py has the webservice along with links of the tutorial I followed too
5. /app/publisher.py has the class which queries the data from MongoDB
6. /app/formatter.py has a Formatter class which I was meaning to use to format the output but did not get time


Sample from the MongoDB:

db.restaurants.findOne()
{
    "_id" : ObjectId("583a2cdeb4de7ef7cf61cfb9"),
    "address" : {
        "building" : "469",
        "coord" : [
            -73.961704,
            40.662942
        ],
        "street" : "Flatbush Avenue",
        "zipcode" : "11225"
    },
    "borough" : "Brooklyn",
    "cuisine" : "Hamburgers",
    "grades" : [
        {
            "date" : ISODate("2014-12-30T00:00:00Z"),
            "grade" : "A",
            "score" : 8
        },
        {
            "date" : ISODate("2014-07-01T00:00:00Z"),
            "grade" : "B",
            "score" : 23
        },
        {
            "date" : ISODate("2013-04-30T00:00:00Z"),
            "grade" : "A",
            "score" : 12
        },
        {
            "date" : ISODate("2012-05-08T00:00:00Z"),
            "grade" : "A",
            "score" : 12
        }
    ],
    "name" : "Wendy'S",
    "restaurant_id" : "30112340"
}
