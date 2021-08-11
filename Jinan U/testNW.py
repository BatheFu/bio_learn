"""
Test File for NW alignment algorithm.
"""
from needleman import GlobalAssign
s1='atcta'
s2='atcgt'
test = GlobalAssign(s1,s2)

score_mat, trace_mat = test.score_matrix()

test.print_matrix(m=score_mat)

test.pretty_print_align()