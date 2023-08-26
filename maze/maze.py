import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

#Last in, first out (DFS)
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(n.state == state for n in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1] #or just self.frontier.pop(-1) idk
            return node

#First in, first out (BFS)
class QueueFrontier(StackFrontier): #inherits from stack frontier
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:] #alt self.frontier.pop(0)
            return node

class Maze():
    def __init__(self, filename):
        