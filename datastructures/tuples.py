def tuple_demo():
    """
    Usage: immutable heterogeneous sequence of elements that are accessed via 
    unpacking or indexing
    """
    
    fields = ('emp_id', 'name', 'email')
    record = (1, 'Vik', 'vik.geerawor@gmail.com')

    print(f"Fields: {fields}")
    print(f"Record: {record}")

    emp_id, name, email = record
    print(f"Tuple unpacking: {emp_id} - {name} - {email}")

    data = dict(zip(fields, record))
    print(f"data: {data}")


def main():
    tuple_demo()
