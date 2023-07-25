class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass


class Midea_AC(AC):
    def cool_wind(self):
       print("midea cool")

    def hot_wind(self):
        print("midea hot")

    def swing_l_r(self):
        print("midea swing")

class GREE_AC(AC):
    def cool_wind(self):
       print("gree cool")

    def hot_wind(self):
        print("gree hot")

    def swing_l_r(self):
        print("gree swing")

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)


"""
midea cool
gree cool
"""