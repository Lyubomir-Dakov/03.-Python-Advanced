def start_spring(**kwargs):
    collection = {}

    for spring_object, value_type in kwargs.items():
        if value_type not in collection:
            collection[value_type] = []
        collection[value_type].append(spring_object)
        collection[value_type] = sorted(collection[value_type])

    sorted_collection = sorted(collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''
    for spring_object, value_type in sorted_collection:
        result += f"{spring_object}:\n"
        for el in value_type:
            result += f"-{el}\n"

    return result


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))


# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))


# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))

