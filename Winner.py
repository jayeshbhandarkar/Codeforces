n = int(input())
rounds = []
total_scores = {}
 
for _ in range(n):
    name, score = input().split()
    score = int(score)
    rounds.append((name, score))
    if name in total_scores:
        total_scores[name] += score
    else:
        total_scores[name] = score
 
max_score = max(total_scores.values())
 
running_scores = {}
for name, score in rounds:
    if name in running_scores:
        running_scores[name] += score
    else:
        running_scores[name] = score
    
    if running_scores[name] >= max_score and total_scores[name] == max_score:
        print(name)
        break
  
