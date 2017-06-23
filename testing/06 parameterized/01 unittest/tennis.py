score_names = ["Love", "Fifteen", "Thirty", "Forty"]


def tennis_score(p_player1_points, p_player2_points):
    player1_points = p_player1_points % len(score_names)
    player2_points = p_player2_points % len(score_names)

    if player1_points == player2_points:
        return "{0}-All".format(score_names[player1_points])
    else:
        return "{0}-{1}".format(score_names[player1_points], score_names[player2_points])
