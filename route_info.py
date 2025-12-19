
class Route:

    # Removed bolts parameter
    def __init__(self, name, climb_type, grade, stars, height=None, pitches=None, description=None, fa=None):
        self.name = name
        self.climb_type = climb_type
        self.grade = grade
        self.stars = stars
        self.height = height
        self.pitches = pitches
        self.description = description
        self.fa = fa

    def __str__(self):
        return f"Route(name={self.name}, type={self.climb_type}, grade={self.grade}, stars={self.stars})"
    
class FAInfo:
    def __init__(self, what, who, when, ):
        self.what = what
        self.who = who
        self.when = when
