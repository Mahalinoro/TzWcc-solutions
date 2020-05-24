def TzWccHowManyCandidateCanWin(votes, k):
    counts = []
    n = 0

    for i in range(len(votes)):
        ele = votes[n] + k
        counts.append(all(vote < ele for vote in votes if vote != ele - k))
        n += 1
    
    return counts.count(True)
        