# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
     "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    expanded_nodes = util.Counter()
    priority_queue = util.PriorityQueue()
    priority_queue.push([problem.getStartState(), []], 0)
    while priority_queue.isEmpty() False:
        current_node, current_path = priority_queue.pop()
        if problem.isGoalState(current_node);
            break
        expanded_nodes[current_node] = problem.getCostOfActions(current_path)
        for expanded_node in problem.getSuccessors(current_node):
            successor_node, action, _ = expanded_node
            if successor_node in expanded_nodes:
                cost = problem.getCostOfActions(current_path)
                if expanded_nodes[successor_node] > cost:
                    expanded_nodes[successor_node] = cost
                    path = current_path + [action]
                    f = problem.getCostOfActions(path)
                    priority_queue.push([successor_node, path], f)
                else:
                    path = current_path + [action]
                    f = problem.getCostOfActions(path)
                    priority_queue.push([successor_node,path], f)
    return current_path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    expanded_nodes = util.Counter()
    priority_queue = util.PriorityQueue()
    priority_queue.push([problem.getStartState(), []], 0)

    while priority_queue.isEmpty() is False:
        current_node, current_path = priority_queue.pop()
        if problem.isGoalState(current_node):
            break
        expanded_nodes[current_node] = problem.getCostOfActions(current_path)
        for expanded_node in problem.getSuccessors(current_node):
            successor_node, action, _ = expanded_node
            if successor_node in expanded_nodes:
                cost = problem.getCostOfActions(current_path)
                if expanded_nodes[successor_node] > cost:
                    expanded_nodes[successor_node] = cost
                    path = current_path + [action]
                    f = problem.getCostOfActions(path)
                    h = heuristic(successor_node, problem)
                    priority_queue.push([successor_node, path], f + h)
            else:
                path = current_path + [action]
                f = problem.getCostOfActions(path)
                h = heuristic(successor_node, problem)
                priority_queue.push([successor_node, path], f + h)
    return current_path

def hillClimbing(problem, heuristic):
    priority_queue = util.PriorityQueue()
    current_cost = heuristic(problem.getStartState(), problem)
    priority_queue.push([problem.getStartState(), []], current_cost)
    current_node, actions = priority_queue.pop()
    while True:
        for expanded_node in problem.getSuccessors(current_node):
            successor, action, _ = expanded_node
            node_cost = problem.getCostOfActions(actions + [action]) + heuristic(successor, problem)
            priority_queue.push([successor, actions + [action]], node_cost)

        current_node, actions = priority_queue.pop()
        current_node_cost = heuristic(current_node, problem)
        if problem.isGoalState(current_node) or current_node_cost > current_cost:
            break
        priority_queue = util.PriorityQueue()
        current_cost = current_node_cost
    return actions


def simulatedAnnealing(problem):
    pass


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
hcl = hillClimbing
san = simulatedAnnealing