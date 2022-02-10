cities = [
    {
        "name": "lusaka",
        "population": 3000000
    },{
        "name": "kitwe",
        "population": 1000000
    },{
        "name": "kafue",
        "population": 500000
    },{
        "name": "livingstone",
        "population": 300000
    }
]

for city in cities:
    print("{} has population of {}".format(city["name"], city["population"]))