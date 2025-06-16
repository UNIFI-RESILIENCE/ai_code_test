from collections import defaultdict
import bisect

def count_servers(n, logs, x, queries):
    # Create a mapping from server_id to a sorted list of request times
    server_logs = defaultdict(list)
    for server_id, time in logs:
        server_logs[server_id].append(time)
    
    for server_id in server_logs:
        server_logs[server_id].sort()
    
    result = []
    
    # Process each query to find number of servers with no activity in [q - x, q]
    for q in queries:
        inactive_servers = 0
        time_start = q - x
        time_end = q
        
        # Check each server to see whether it has any request in [time_start, time_end]
        for server_id in range(1, n + 1):
            times = server_logs.get(server_id, [])
            
            # Use binary search to find the first log >= time_start
            idx = bisect.bisect_left(times, time_start)
            
            # Check if there's a time within the interval [time_start, time_end]
            if idx == len(times) or times[idx] > time_end:
                inactive_servers += 1
        
        result.append(inactive_servers)
    
    return result