from conans import ConanFile

class Recipe(ConanFile):
    name = "consumer_flac"

    python_requires = "pyreq/0.1"
    python_requires_extend = "pyreq.BaseMixin"

    def requirements(self):
        self.requires("flac/[>=0.0]")

    def build_requirements(self):
        self.build_requires("cmake/[>=0.0]")
