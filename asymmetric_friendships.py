import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(friend, person) # One for expected relationship.
    mr.emit_intermediate(person, friend) # One for existing relationship.

def reducer(person, lst_o_rel):
    # key: person
    # value: list of existing and expected relationships

    # If the relation is symmetric, then each entry in list of relations will
    # be *2, each singular entry in list is an asymmetric relation.
    asym_relations = filter(lambda friend: lst_o_rel.count(friend) == 1, lst_o_rel)
    for rel in asym_relations:
        mr.emit((person, rel))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
