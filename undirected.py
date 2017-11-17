"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

"""


class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid:
            return 0
        self.N, self.M = len(grid), len(grid[0])
        res = 0
        for i in range(self.N):
            for j in range(self.M):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        if i < 0 or i > self.N - 1 or j < 0 or j > self.M - 1 or grid[i][j] != '1':
            return
        grid[i][j] = 'x'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)


"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""


class Solution:
    def exist(self, board, word):
        self.M, self.N = map(len, [board, board[0]])
        for i in range(self.M):
            for j in range(self.N):
                if board[i][j] == word[0] and self.isWord(board, i, j, 0, word):
                    return True
        return False

    def isWord(self, board, i, j, index, word):
        if index == len(word):
            return True
        if i < 0 or i >= self.M or j < 0 or j >= self.N or board[i][j] != word[index]:
            return False

        board[i][j] = '#'
        for k in [-1, 1]:
            if self.isWord(board, i + k, j, index + 1, word) or self.isWord(board, i, j + k, index + 1, word):
                return True

        board[i][j] = word[index]

        return False


"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""


class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0:  # This is sooooo keng
            return board
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                    self.bfs(board, i, j)
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, board, row, col):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != 'O':
            return
        board[row][col] = 'V'
        self.dfs(board, row + 1, col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)


Directed
graph
"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you
 should also have finished course 1. So it is impossible.
click to show more hints.
Hints:
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological
ordering exists and therefore it will be impossible to take all courses.
There are several ways to represent a graph. For example, the input prerequisites is a graph represented
by a list of edges. Is this graph representation appropriate?
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        for i in xrange(numCourses):
            if not self.dfs(graph, i, visit):
                return False
        return True

    def dfs(self, graph, i, visit):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, j, visit):
                return False
        visit[i] = 1
        return True


# How to represent a graph
"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.
For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3]
"""


class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.res = []
        if self.canFinish(numCourses, prerequisites):
            return self.res
        return []

    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        for i in xrange(numCourses):
            if not self.dfs(graph, i, visit):
                return False
        return True

    def dfs(self, graph, i, visit):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, j, visit):
                return False
        self.res.append(i)
        visit[i] = 1
        return True


# three statuses for the visisted table


"""
If there is no directed cycle, there will be a simple solution.
This version will exhaust all stacks once with directed cycle.
"""


class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.res = []
        graph = [[] for _ in xrange(numCourses)]
        visit = [False for _ in xrange(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        for i in xrange(numCourses):
            self.dfs(graph, i, visit)
        return self.res

    def dfs(self, graph, i, visit):
        if visit[i] == True:
            return
        for j in graph[i]:
            self.dfs(graph, j, visit)
        self.res.append(i)
        visit[i] = True