from Enviroment import Enviroment
from astar import *
env = Enviroment(10,10,20)
env.print_enviroment()
astar = AStar(env.startPos,env.endPos,env)
astar.Search()