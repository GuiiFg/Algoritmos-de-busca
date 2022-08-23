import sys
sys.setrecursionlimit(999999)

from NumberPuzzle.struct import SearchTree

arvoreBusca = SearchTree()

arvoreBusca.BuscarResultado([1,2,3,4,0,6,7,8,5], [1,2,3,4,5,6,7,8,0])