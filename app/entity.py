class Team:
    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__gf = 0
        self.__ga = 0
        self.__pos = 0

    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self, pos):
        self.__pos = pos

    @property
    def name(self):
        return self.__name
    
    @property
    def points(self):
        return self.__points
    
    @property
    def goals_for(self):
        return self.__gf
    
    @property
    def goals_against(self):
        return self.__ga
    
    @points.setter
    def points(self, points):
        self.__points = points
    
    @goals_for.setter
    def goals_for(self, goals_for):
        self.__gf = goals_for
    
    @goals_against.setter
    def goals_against(self, goals_against):
        self.__ga = goals_against
    
    def __repr__(self):
        return "<Team Object %s>" % self.__name