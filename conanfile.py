import os
import sys
from conans import ConanFile, tools, CMake, errors, python_requires, RunEnvironment
import re


#https://docs.conan.io/en/1.4/howtos/capture_version.html
def parse_version_from_cmake():
    try:
        content = tools.load("CMakeLists.txt")
        version = re.search("project\((.*) VERSION (.*)\)", content).group(2)
        #print("Parsed version from CMakeLists.txt: %s"%(version.strip()) )
        return version.strip()
    except Exception as e:
        print("Failed to parsed version from CMakeLists.txt")
        return None


class DemoConan(ConanFile):
    name = 'demo'
    branch = 'develop'
    version = parse_version_from_cmake()
    license = ''
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake', 'virtualrunenv'
    keep_imports=True
    no_copy_source=True
    exports = "CMakeLists.txt", "deps.cmake"


    def requirements(self):
        versions = tools.load('deps.cmake')

        deps1_v = '0.0.1' # will be replaced by parsed values from deps.cmake
        deps2_v = '0.0.1' # will be replaced by parsed values from deps.cmake
        self.requires('deps1/{}@me/testing'.format(deps1_v))
        self.requires('deps2/{}@me/testing'.format(deps2_v))

    def build(self):
        print("build")

    def package(self):
        print("package")