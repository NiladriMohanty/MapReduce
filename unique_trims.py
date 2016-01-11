import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: seq_id
    # value: nucleotides
    seq_id = record[0]
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[:-10], seq_id)

def reducer(nucleotides, list_of_seq_id):
    #Trim the nucleotides, and emit
    mr.emit(nucleotides)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
