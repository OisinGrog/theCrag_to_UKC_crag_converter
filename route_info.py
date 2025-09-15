
class Route:
    def __init__(self, name, climb_type, grade, height, description, bolts=None, fa=None):
        self.name = name
        self.climb_type = climb_type
        self.grade = grade
        self.height = height
        self.description = description
        self.bolts = bolts
        self.fa = FAInfo(*fa) if fa else None

    def __str__(self):
        return f"Route(name={self.name}, type={self.climb_type}, grade={self.grade}, height={self.height}, description={self.description}, bolts={self.bolts})"
    
class FAInfo:
    def __init__(self, what, who, when, ):
        self.what = what
        self.who = who
        self.when = when
