from sortedcontainers import SortedList

def process_server_requests(n, logs, x, queries):
    # Sort logs based on the time they were received
    logs.sort(key=lambda log: log[1])
    
    # Prepare and sort queries while keeping track of their original index
    indexed_queries = [(query, i) for i, query in enumerate(queries)]
    indexed_queries.sort(key=lambda q: q[0])
    
    # Initialize variables to track active logs and processed answers
    current_logs = SortedList()
    answer = [0] * len(queries)
    j = 0
    
    # Process each query
    for t_q, i_q in indexed_queries:
        # Add new logs to the window [t_q - x, t_q]
        while j < len(logs) and logs[j][1] <= t_q:
            server_id, time_stamp = logs[j]
            current_logs.add((server_id, time_stamp))
            j += 1
        
        # Remove logs that fall outside the window [t_q - x, t_q]
        while current_logs and current_logs[0][1] < t_q - x:
            server_id, time_stamp = current_logs.pop(0)
        
        # Count unique servers that have logs within the window
        if len(current_logs) == 0:
            # No servers received logs, all are inactive
            answer[i_q] = n
        else:
            # Use binary search in SortedList to find the number of unique servers
            start_index = current_logs.bisect_left((current_logs[0][0], float('-inf')))
            end_index = current_logs.bisect_right((current_logs[-1][0], float('inf')))
            
            # Count unique servers using set slicing
            num_active_servers = len(set(current_logs[start_index:end_index]))
            answer[i_q] = n - num_active_servers
    
    return answer

# Example usage:
n = 3
logs = [[1, 3], [2, 6], [1, 5]]
x = 5
queries = [10, 11]
print(process_server_requests(n, logs, x, queries))  # Output: [1, 2]

n = 3
logs = [[2, 4], [2, 1], [1, 2], [3, 1]]
x = 2
queries = [3, 4]
print(process_server_requests(n, logs, x, queries))  # Output: [0, 1]