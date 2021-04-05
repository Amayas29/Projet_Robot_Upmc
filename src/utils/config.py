import configparser
from pathlib import Path
from utils.tools import Point
from model.obstacles import Obstacle


class Config:

    def __init__(self):
        self.conf = configparser.ConfigParser()
        src_path = Path(__file__).parent.parent
        self.conf.read(f"{src_path}/config.cfg")

    def get_vers(self):
        return float(self.conf['Version']['config_version'])

    def get_dist_secu(self):
        return float(self.conf['Robot']['distance_securite'])

    def get_fps(self):
        return float(self.conf['Robot']['fps'])

    def get_mode(self):
        return self.conf['Robot'].getboolean('mode_simu')

    # def get_strat_list(self):
    #     res = []
    #     for x in self.conf['Strat']:
    #         res.append(x)
    #     return res

    # def get_strat(self, strat):
    #     try:
    #         txt = self.conf['Strat'][strat]
    #         return txt.split(",")
    #     except Exception as e:
    #         print("Erreur : Strategie ", e, ' inexistante')

    def get_obstacles(self):
        obstacles = []

        for obstacle in self.conf['Obstacles']:

            str_points = self.conf['Obstacles'][obstacle].split(";")

            try:
                points = []
                for str_pt in str_points:
                    x_y = str_pt.split(",")
                    points.append(Point(float(x_y[0]), float(x_y[1])))

                src = points[0]
                dest = points[1]
                obstacles.append(Obstacle(src, dest))
            except:
                pass

        return obstacles
