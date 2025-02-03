def get_grade(score1, score2, score3):
    avg_score = (score1 + score2 + score3) / 3
    
    if 90 <= avg_score <= 100:
        return 'A'
    elif 80 <= avg_score < 90:
        return 'B'
    elif 70 <= avg_score < 80:
        return 'C'
    elif 60 <= avg_score < 70:
        return 'D'
    elif 0 <= avg_score < 60:
        return 'F'