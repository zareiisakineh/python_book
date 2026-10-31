# file: ex_05_11_high_score_board_start.py

scores = [420, 380, 510, 295, 620, 380]

# TODO: 1. Print how many players played today (len)
print(len(scores))
# TODO: 2. Print the total (sum), and the highest (max) and lowest (min) score
print(sum(scores))
print(max(scores))
print(min(scores))
# TODO: 3. Print the average, rounded to one decimal
#          Hint: sum(scores) / len(scores), then round(..., 1)
print(round(sum(scores) / len(scores), 1))
# TODO: 4. A late player scored 450 - add it to the end (append)
scores.append(450)
print(scores)
# TODO: 5. The score at index 0 was wrong - it should be 440
scores[0] = 440
print(scores)
# TODO: 6. A player was disqualified - remove the score 295 (remove)
scores.remove(295)
print(scores)
# TODO: 7. Print the three best scores
#          Hint: sorted(scores, reverse=True) then take the first three with slicing
sortert = sorted(scores, reverse=True)
print(sortert[:3])
# TODO: 8. Print how many players scored exactly 380 (count)
print(scores.count(380))
# TODO: 9. Print the position of the score 620 (index)
print(scores.index(620))
# TODO: 10. Print whether anyone reached 620 (in)
if 620 in scores:
    print("someone reached 620")
# TODO: 11. Print all scores from best to worst (sorted with reverse=True)
print(sorted(scores, reverse=True))