def seg_end(segment):
    return segment[1]

def min_points(segments):
    if not segments:
        return 0
    segments.sort(key=seg_end)  
    points = []
    cur_point = segments[0][1]  
    points.append(cur_point)   
    for seg in segments:
        if seg[0] > cur_point:
            cur_point = seg[1]  
            points.append(cur_point)  
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

res = min_points(segments)
print(res)
