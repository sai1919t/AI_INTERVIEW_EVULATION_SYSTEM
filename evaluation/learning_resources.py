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

    if department == "ECE":
        resources.append("https://www.geeksforgeeks.org/digital-electronics-logic-design-tutorials/")

    # Topic based links
    for topic in weak_topics:
        topic_lower = topic.lower()

        for key in RESOURCE_DATABASE:
            if key in topic_lower:
                resources.extend(RESOURCE_DATABASE[key])

    # Remove duplicates
    resources = list(set(resources))

    return resources