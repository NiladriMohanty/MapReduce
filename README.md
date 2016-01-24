# MapReduce

inverted_index.py => input is a list of document id with text and output is a word, document ID list

join.py => input record is a list of strings representing a tuple in the database and output is a joined record: a single list of length 27 that contains the attributes from the order record followed by the fields from the line item record.

friend_count.py => input record is a 2 element list personA, personB and output is a pair (person, friend_count) 

asymmetric_friendships.py => input record is a 2 element list personA, personB and output is all pairs (friend, person) such that (person, friend) appears in the dataset but (friend, person) does not.

unique_trims.py => input record is a 2 element list sequence id, nucleotides and output from the reduce function is the unique nucleotide strings.

multiply.py => input to the map function is a row of a matrix represented as a list. Each list is in the form [matrix, i, j, value] where matrix is a string and i, j, and value are integers and output from the reduce function is a tuple of multiplication of 2 rows from input.

MapReduce.py => implements the MapReduce programming model
