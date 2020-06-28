import basketball_crawler as bc
from nba_analysis import *



# - third step -
# height and weight plot for pg & c
draw_weight_height_C_and_PG()

# then we find a special point guard: Giannis -> print it out
print [pg.name for pg in point_guards if int(pg.weight) > 240]


# analysis Giannis' PTS trends
draw_player_pts_trend(u'Giannis Antetokounmpo', 6)


# draw plus minus of players
draw_player_year_ave_pm(u'Giannis Antetokounmpo')