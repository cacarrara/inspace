from inspace.models import Galaxy


class Provider(object):
    def __init__(self, ):
        self.galaxies = {}

    def create_galaxy(self, name):
        galaxy = self.get_galaxy(name)
        if galaxy is not None:
            return galaxy
        self.galaxies[name] = Galaxy({'name': name}, validate=True)
        return self.galaxies[name]

    def get_galaxy(self, name):
        return self.galaxies.get(name)
