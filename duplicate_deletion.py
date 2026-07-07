records= [
    {"id":1,"name":"A"},
    {"id":2,"name":"B"},
    {"id":1,"name":"A"}
]
def remove_duplicates(records):
    seen=set()
    unique_records=[]
    for record in records:
        record_tuple=tuple(record.items())
        if record_tuple not in seen:
            seen.add(record_tuple)
            unique_records.append(record)
    return unique_records

print(remove_duplicates(records))