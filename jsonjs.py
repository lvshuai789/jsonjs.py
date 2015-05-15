#!/usr/bin/python
#####################################
#                                   #
#   Helper to write JSON into a JS  #
#   Written by radj                 #
#                                   #
#####################################

import json, re

def sanitize(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '_', s)
    return s

def writeDictToJS(jsonDict, jsPath):
    fh_jsfile = open(jsPath, 'w')
    for outerKey in jsonDict:
        fh_jsfile.write("var %s = \n" % sanitize(outerKey)) 
        fh_jsfile.write(json.dumps(jsonDict[outerKey], sort_keys=True, indent=4))
        fh_jsfile.write(";\n")
        fh_jsfile.flush()
    fh_jsfile.close()

# This assumes the JS follows the output of writeDictToJS.
def loadDictFromJS(jsPath):
    jsonDict = {}

    fh_jsfile = open(jsPath, 'r')
    jsString = fh_jsfile.read()
    outerStrings = jsString.split(";\n")

    # Split the lines into var grouping
    for outerString in outerStrings[:-1]:
        # Derive outer key
        # 3 is just enough to cut out "var name = "
        dictStrings = outerString.split(' ', 3) 
        outerKey = dictStrings[1]
        jsonDict[outerKey] = json.loads(dictStrings[3])

    fh_jsfile.close()

    return jsonDict

if __name__ == "__main__":
    import logging as log
    log.basicConfig(level=log.DEBUG, format='%(asctime)s %(message)s')
    
    data = {
        "firstRoot" : {
            "_id": "5555b4a058ebe952cc8b1cb1",
            "index": 0,
            "guid": "6f767542-0f21-41cb-a45a-016e982a645f",
            "isActive": False,
            "balance": "$2,828.55",
            "picture": "http://placehold.it/32x32",
            "age": 32,
            "eyeColor": "green",
            "name": "Case Chase",
            "gender": "male",
            "company": "ANOCHA",
            "email": "casechase@anocha.com",
            "phone": "+1 (894) 479-3854",
            "registered": "2014-01-02T06:19:36 -08:00",
            "latitude": 26.837759,
            "longitude": -122.830029,
            "tags": [
                "eiusmod",
                "duis",
                "veniam",
                "aute",
                "mollit",
                "culpa",
                "nostrud"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Tiffany Parsons"
                },
                {
                    "id": 1,
                    "name": "Lilia Morales"
                },
                {
                    "id": 2,
                    "name": "Jerry Rojas"
                }
            ],
            "greeting": "Hello, Case Chase! You have 8 unread messages.",
            "favoriteFruit": "banana"
        },
        "secondRoot" : {
            "_id": "5555b4a00755b76c69d96574",
            "index": 1,
            "guid": "ea45dc3d-a43a-4232-a2e5-c7d55bbcf28e",
            "isActive": True,
            "balance": "$1,029.51",
            "picture": "http://placehold.it/32x32",
            "age": 25,
            "eyeColor": "green",
            "name": "Robbie Lott",
            "gender": "female",
            "company": "PERKLE",
            "email": "robbielott@perkle.com",
            "phone": "+1 (963) 492-2158",
            "registered": "2015-01-24T05:25:16 -08:00",
            "latitude": 9.215018,
            "longitude": -97.992207,
            "tags": [
                "esse",
                "culpa",
                "nostrud",
                "proident",
                "sit",
                "voluptate",
                "adipisicing"
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Hanson Sellers"
                },
                {
                    "id": 1,
                    "name": "Wolfe Rodgers"
                },
                {
                    "id": 2,
                    "name": "Phillips Norman"
                }
            ],
            "greeting": "Hello, Robbie Lott! You have 8 unread messages.",
            "favoriteFruit": "apple"
        }
    };

    writeDictToJS(data, "test.js")

    newData = loadDictFromJS("test.js")
    
    if newData == data:
        log.debug("Test OK.")
    else:
        log.error("Test failed.")