"""
// Time Complexity : O(N)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
Idea is to place the task with highest frequency first and consider 
the remaining tasks after that, 
Since we need only the number of intervals irrespective of where
the tasks are placed, we can take a mathematically driven approach
where in we esentially derive the number of intervals using 3 components
pending tasks,empty tasks, idle tasks 
Return Result - idle + len(tasks)
"""
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_count = 0
        max_freq = 0
        cnt = Counter(tasks)
        most_common = cnt.most_common()
        max_freq = most_common[0][1]
        print(max_freq,most_common)
        for v in most_common:
            if v[1] == max_freq:
                max_count+=1
        print(max_count)
        #max_freq-1 -> number of partitions for which tasks can be placed matching the condition of cooling period
        #since we can have multiple tasks haing same freq, we take into account max count to compute the empty slots which less frequent tasks can take.
        empty_tasks = (n - (max_count - 1)) * (max_freq - 1)
        #pending tasks is remainder of the tasks that need to be scheduled
        pending = len(tasks) - (max_freq * max_count)
        #time required to essentially match the cooling period conditoin, so no tasks need to be scheduled here
        idle = max(0,empty_tasks - pending)
        return idle + len(tasks)