from conan import ConanFile
from conan.tools.meson import Meson

class videoConan(ConanFile):
    name = "timer"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "pkg_config"
    requires = "ffmpeg/4.0@bincrafters/stable"
    exports_sources = "src/*"

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()
