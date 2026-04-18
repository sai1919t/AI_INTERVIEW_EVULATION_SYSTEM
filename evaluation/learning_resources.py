RESOURCE_DATABASE = {
    "binary search": [
        "https://www.geeksforgeeks.org/binary-search/",
        "https://www.youtube.com/results?search_query=binary+search+tutorial"
    ],
    "dynamic programming": [
        "https://www.geeksforgeeks.org/dynamic-programming/",
        "https://www.youtube.com/results?search_query=dynamic+programming+tutorial"
    ],
    "inheritance": [
        "https://www.geeksforgeeks.org/inheritance-in-java/",
        "https://www.youtube.com/results?search_query=inheritance+oops+tutorial"
    ],
    "dbms": [
        "https://www.geeksforgeeks.org/dbms/",
        "https://www.youtube.com/results?search_query=dbms+tutorial"
    ],
    "acid": [
        "https://www.geeksforgeeks.org/acid-properties-in-dbms/",
        "https://www.youtube.com/results?search_query=acid+properties+dbms"
    ]
}


def suggest_resources(department, weak_topics):

    resources = []

    # Department level
    if department == "CSE":
        resources.append("https://leetcode.com/")
        resources.append("https://www.geeksforgeeks.org/data-structures/")
        resources.append("https://www.javatpoint.com/")
        resources.append("https://www.javatpoint.com/")
        

    if department == "ECE":
        resources.append("https://www.geeksforgeeks.org/digital-electronics-logic-design-tutorials/")
        resources.append("https://www.javatpoint.com/")
        resources.append("https://www.w3schools.com/")


    if department == "EEE":
        resources.append("https://www.geeksforgeeks.org/electrical-engineering/")
        resources.append("https://www.electrical4u.com/")
        resources.append("https://www.allaboutcircuits.com/")

    if department == "MECH":
        resources.append("https://www.geeksforgeeks.org/mechanical-engineering/")
        resources.append("https://www.mechanicaltutorial.com/")
        resources.append("https://www.youtube.com/results?search_query=mechanical+engineering+tutorial")
        resources.append("https://www.engineeringtoolbox.com/")
    
    if department == "CIVIL":
        resources.append("https://www.geeksforgeeks.org/civil-engineering/")
        resources.append("https://www.aboutcivil.org/")
        resources.append("https://www.youtube.com/results?search_query=civil+engineering+tutorial")
        resources.append("https://www.engineeringcivil.com/")
    
    
    # Topic based links
    for topic in weak_topics:
        topic_lower = topic.lower()

        for key in RESOURCE_DATABASE:
            if key in topic_lower:
                resources.extend(RESOURCE_DATABASE[key])

    # Remove duplicates
    resources = list(set(resources))

    return resources