class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq = Counter(tasks)
        # mode = freq.most_common()[0][1]
        # found_most = sum([freq[key] == mode for key in freq])
        # return max(len(tasks), (mode - 1) * (n + 1) + found_most)
        
        if n == 0:
            return len(tasks)
        
        tasks_dict = Counter(tasks)
        
        max_freq = max(tasks_dict.values())
        
        num_tasks_max_freq = sum([tasks_dict[key] == max_freq for key in tasks_dict])
        
        interval = (max_freq-1) * (n+1) + num_tasks_max_freq
        
        return max(len(tasks), interval)