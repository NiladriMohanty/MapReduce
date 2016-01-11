import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name 
    # value: friend
    key = record[0]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_friends):
    # key: person name
    # value: list of ones for each friend 
    mr.emit((key, sum(list_of_friends)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
