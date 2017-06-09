from inspace.models import Galaxy


class Provider(object):
    def __init__(self, ):
        self.galaxies = {}

    def get_galaxy(self, name):
        galaxy = self.galaxies.get(name)
        if galaxy is not None:
            return galaxy
        self.galaxies[name] = Galaxy({'name': name}, validate=True)
        return self.galaxies[name]
