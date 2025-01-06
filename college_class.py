class CollegeClass:
    """A class representing a UNC lecture, lab, recitation, or other."""

    def __init__(self, building, room, days, time):
        self.building = building
        self.room = room
        self.days = days
        self.time = time

    def __str__(self):
        return f"Building: {self.building}\nRoom: {self.room}\nDays: {self.days}\nTime: {self.time}"
