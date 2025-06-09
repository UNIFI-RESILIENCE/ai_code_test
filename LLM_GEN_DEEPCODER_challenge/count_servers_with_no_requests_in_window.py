def count_servers(n, logs, x, queries):
    # Create a dictionary to map each server to its list of request times
    from collections import defaultdict
    server_logs = defaultdict(list)
    
    for server_id, time in logs:
        server_logs[server_id].append(time)
    
    # Sort each server's request times for binary search
    for server_id in server_logs:
        server_logs[server_id].sort()
    
    # Prepare the result array
    result = []
    
    for query in queries:
        start = query - x
        end = query
        inactive_count = 0
        
        # Iterate over all possible servers (1..n)
        # Since n can be large, but server_logs only contains servers with logs,
        # we can optimize by checking servers present in server_logs and assume others are inactive if their logs are missing
        
        # The inactive servers are:
        # 1. Servers not present in server_logs (never logged any requests)
        # 2. Servers present in server_logs but have no logs in [start, end]
        
        # Total servers is n, so inactive_count = (n - len(server_logs)) + servers with no logs in [start, end]
        inactive_count = n - len(server_logs)
        
        for server_id in server_logs:
            times = server_logs[server_id]
            # Find the first time >= start
            left = bisect.bisect_left(times, start)
            # Find the first time > end
            right = bisect.bisect_right(times, end)
            
            if right - left == 0:
                inactive_count += 1
        
        result.append(inactive_count)
    
    return result

import bisect

# Example usage:
# n = 3
# logs = [[1,3],[2,6],[1,5]]
# x = 5
# queries = [10,11]
# print(count_servers(n, logs, x, queries))  # Output: [1, 2]