#list -variable holds multiple variables , mutable
#tuple- immutable lists
#dictionary- hold values in key:value pairs
from typing import List, Union

person: List[Union[str, int, float, bool]] = ["John", "Doe", 30, 65.54, "Mombasa", True]
person[2] = 39
print(person[0])
print(person[-4:-2])

person_t = ("John", "Doe", 30, 65.54, "Mombasa", True)
print(person_t)
print(person[0:5])
#person_t[2] = 31 a tuple cannot change.

person.append("New York")
print(person)

person.pop(1)
print(person)

#person.sort()
print(len(person))

person_dict = {"firstName" : "John", "surName" : "Doe", "weight" : 65.54, "location" : "Mombasa", "activeUser" : True}
print(person_dict["location"], person_dict["surName"])
