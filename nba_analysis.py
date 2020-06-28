import basketball_crawler as bc
import line_of_best_fit as lobf
import matplotlib.pyplot as plt
import main

# - first step -
# build player dictionary by scratching and store it in players.json
# players = bc.buildPlayerDictionary()
#
# bc.savePlayerDictionary(players, '/Users/zzc/PycharmProjects/nba/venv/players.json')


# - second step -
# load player dictionary (players.json)
players = bc.loadPlayerDictionary('players.json')
# print (players)



# getting the heights requires parsing of strings, e.g. "6-3" -> 75 (inches)
def parse_height_value(height_string):
    ft, inches = [int(val) for val in height_string.split('-')]
    return ft * 12 + inches


def draw_weight_height_C_and_PG():
    plt.figure(figsize=(12.8, 8))
    plt.scatter(pg_weights, pg_heights, c="red", label="PG")
    plt.scatter(c_weights, c_heights, c="blue", label="C")
    plt.xlabel("Weight")
    plt.ylabel("Height")
    plt.legend(loc=4)
    plt.show()



season_list = ["2018-19", "2017-18", "2016-17", "2015-16", "2014-15", "2013-14", "2012-13", "2011-12", "2010-11",
                "2009-10", "2008-09", "2007-18", "2006-07", "2005-06", "2004-05", "2003-04", "2002-03", "2001-02"]

color_list = ["red", "blue", "green", "black", "cyan", "brown", "gray", "goldenrod", "hotpink", "indigo", "ivory",
                "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral"]


def draw_player_pts_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_pts = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_pts[j] = [int(pts) for pts in games[j].get("PTS").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_pts[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("pts")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_pts[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_pts[z])
    plt.show()


def draw_player_fg_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_fg = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_fg[j] = [int(pts) for pts in games[j].get("FG").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_fg[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("field goals")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_fg[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_fg[z])
    plt.show()


def draw_player_fga_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_fga = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_fga[j] = [int(pts) for pts in games[j].get("FGA").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_fga[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("field goals attemps")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_fga[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_fga[z])
    plt.show()


def draw_player_fgp_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_fgp = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_fgp[j] = [int(pts) for pts in games[j].get("FG%").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_fgp[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("field goals %")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_fgp[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_fgp[z])
    plt.show()


def draw_player_3p_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_3p = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_3p[j] = [int(pts) for pts in games[j].get("3P").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_3p[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("3 pints made")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_3p[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_3p[z])
    plt.show()


def draw_player_3pa_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_3pa = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_3pa[j] = [int(pts) for pts in games[j].get("3PA").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_3pa[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("3 pints attemps")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_3pa[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_3pa[z])
    plt.show()


def draw_player_3pp_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_3pp = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_3pp[j] = [int(pts) for pts in games[j].get("3P%").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_3pp[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("3 pints %")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_3pp[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_3pp[z])
    plt.show()


def draw_player_ft_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_ft = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_ft[j] = [int(pts) for pts in games[j].get("FT").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_ft[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("free throw")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_ft[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_ft[z])
    plt.show()


def draw_player_fta_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_fta = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_fta[j] = [int(pts) for pts in games[j].get("FTA").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_fta[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("free throws attemps")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_fta[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_fta[z])
    plt.show()


def draw_player_ftp_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_ftp = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_ftp[j] = [int(pts) for pts in games[j].get("FT%").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_ftp[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("free throw %")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_ftp[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_ftp[z])
    plt.show()


def draw_player_orb_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_orb = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_orb[j] = [int(pts) for pts in games[j].get("ORB").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_orb[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("offensive rebounds")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_orb[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_orb[z])
    plt.show()


def draw_player_drb_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_drb = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_drb[j] = [int(pts) for pts in games[j].get("DRB").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_drb[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("defensive rebounds")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_drb[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_drb[z])
    plt.show()


def draw_player_trb_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_trb = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_trb[j] = [int(pts) for pts in games[j].get("TRB").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_trb[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("total rebounds")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_trb[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_trb[z])
    plt.show()


def draw_player_ast_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_ast = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_ast[j] = [int(pts) for pts in games[j].get("AST").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_ast[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("assists")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_ast[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_ast[z])
    plt.show()


def draw_player_stl_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_stl = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_stl[j] = [int(pts) for pts in games[j].get("STL").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_stl[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("steals")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_stl[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_stl[z])
    plt.show()


def draw_player_blk_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_blk = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_blk[j] = [int(pts) for pts in games[j].get("BLK").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_blk[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("blocks")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_blk[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_blk[z])
    plt.show()


def draw_player_tov_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_tov = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_tov[j] = [int(pts) for pts in games[j].get("TOV").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_tov[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("turnover")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_tov[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_tov[z])
    plt.show()


def draw_player_pf_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_pf = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_pf[j] = [int(pts) for pts in games[j].get("PF").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_pf[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("personal fouls")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_pf[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_pf[z])
    plt.show()


def draw_player_GmSc_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_GmSc = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_GmSc[j] = [int(pts) for pts in games[j].get("GmSc").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_GmSc[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("game score")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_GmSc[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_GmSc[z])
    plt.show()


def draw_player_pm_trend(name, noy=6):
    # noy: number of years
    games = [1] * 20
    game_pm = [1] * 20

    for i in range(0, noy):
        games[i] = bc.regularSeasonGameLogs(players, name, season_list[i])

    for j in range(0,noy):
        game_pm[j] = [int(pts) for pts in games[j].get("+/-").tolist()]

    # drawing pts trends through years
    plt.figure(figsize=(12.8, 8))
    for x in range(0,noy):
        plt.plot(games[x].get("G"), game_pm[x], c=color_list[x], label=season_list[x])
    plt.legend(loc=4)
    plt.ylabel("plus minus")
    plt.show()

    # draw linear regression
    plt.figure(figsize=(12.8, 8))
    for y in range(0, noy):
        lobf.draw_linear_regression([int(g) for g in games[y].get("G").tolist()], game_pm[y])
    plt.show()

    # draw polynomials features
    plt.figure(figsize=(12.8, 8))
    for z in range(0, noy):
        lobf.draw_poly_feature([int(g) for g in games[z].get("G").tolist()], game_pm[z])
    plt.show()


def draw_player_year_ave_pm(name):
    pbp = bc.play_by_playLogs(players, name)
    PM = [float(pm) for pm in pbp.get("OnCourt").tolist()]
    NPM = [float(pm) for pm in pbp.get("On-Off").tolist()]
    plt.figure(figsize=(12.8, 8))
    # plt.plot(games[x].get("G"), game_pts[x], c=color_list[x], label=season_list[x])
    plt.plot(PM, c="red", label="PM")
    plt.plot(NPM, c="blue", label="NPM")
    plt.show()


# define data set array by positions
point_guards = [players[name] for name in players
                if "Point Guard" in players[name].positions]
shooting_guard = [players[name] for name in players
                  if "Shooting Guard" in players[name].positions]
small_forward = [players[name] for name in players
                  if "Small Forward" in players[name].positions]
power_forward = [players[name] for name in players
                  if "Power Forward" in players[name].positions]
centers = [players[name] for name in players
           if "Center" in players[name].positions]


# get height and weight
pg_weights = [int(pg.weight) for pg in point_guards]
pg_heights = [parse_height_value(pg.height) for pg in point_guards]
sg_weights = [int(sg.weight) for sg in shooting_guard]
sg_heights = [parse_height_value(sg.height) for sg in shooting_guard]
sf_weights = [int(sf.weight) for sf in small_forward]
sf_heights = [parse_height_value(sf.height) for sf in small_forward]
pf_weights = [int(pf.weight) for pf in power_forward]
pf_heights = [parse_height_value(pf.height) for pf in power_forward]
c_weights = [int(c.weight) for c in centers]
c_heights = [parse_height_value(c.height) for c in centers]

