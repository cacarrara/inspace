from inspace.models import Galaxy


class Provider(object):
    def __init__(self, ):
        self.galaxies = []

    def create_galaxy(self, name):
        galaxy = self.get_galaxy(name)
        if galaxy is not None:
            return galaxy
        galaxy = Galaxy({'name': name}, validate=True)
        self.galaxies.append(galaxy)
        return galaxy

    def get_galaxy(self, name):
        for galaxy in self.galaxies:
            if galaxy.name == name:
                return galaxy
        return None
