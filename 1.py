def min_points(segments):
    if not segments:
        return 0
    segments.sort(key=lambda x: x[1])  
    points = []
    current_point = segments[0][1]  
    points.append(current_point)
    
    for seg in segments:
        if seg[0] > current_point:
            current_point = seg[1]  
            points.append(current_point)
    
    return len(points)

with open("data_prog_contest_problem_1.txt", "r") as f:
    segments = []
    for line in f:
        line = line.strip()
        if line:
            parts = list(map(int, line.split()))
            if len(parts) == 2:
                segments.append((parts[0], parts[1]))
            elif len(parts) == 1:
                segments.append((parts[0], parts[0]))

result = min_points(segments)
print(result)