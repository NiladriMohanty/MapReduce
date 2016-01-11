import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    doc_id = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, doc_id)

def reducer(word, list_of_doc_ids):
    # key: word
    # value: list of doc_ids 
    # remove duplicate doc_ids
    list_of_doc_ids = list(set(list_of_doc_ids))
    mr.emit((word, list_of_doc_ids))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
