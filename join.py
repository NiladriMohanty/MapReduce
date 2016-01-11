import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: rest of the data record
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_records):
    # key: order_id
    # value: list of  records
    
    # For this key, seperate the orders and list_items
    orders = filter(lambda record: record[0] == "order", list_of_records)
    line_items = filter(lambda record: record[0] == "line_item", list_of_records)

    # Now for each order type record, emit a combination of order and line_item
    # The result should be a single list of length 27 
    # that contains the fields from the order record followed by 
    # the fields from the line item record. Each list element should be a string.
    # Behold the sexy list comprehensions!
    results  = [ order + line_item for order in orders for line_item in line_items ]
    # Now emit for each entry in results
    for result in results:
        mr.emit(result)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
