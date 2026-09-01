from itertools import count

departments = [
    ["Alice", "Bob"],
    ["Charlie", "David"]
]
for department in departments:
    for employee in department:
        print(employee)


batches = [
    ["record-101", "record-102"],
    ["record-103", "record-104"],
    ["record-105"]
]

for batch in batches:
    for record in batch:
        print(record)


batches = [
    ["A", "B", "C"],
    ["D", "E"],
    ["F", "G", "H", "I"]
]

count = 0
for batch in batches:
    for record in batch:
        count +=1


print("Total Count:",count)

print("Example 3")

pipelines = [
    {
        "name": "sales_etl",
        "jobs": ["extract", "transform", "load"]
    },
    {
        "name": "inventory_etl",
        "jobs": ["extract", "load"]
    }
]

for pipeline in pipelines:
    for job in pipeline['jobs']:
        print(f"{pipeline['name']} -> {job}")

