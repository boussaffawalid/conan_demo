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
    scm = {
        'type': 'git',
        'url': 'https://github.com/boussaffawalid/conan_demo.git',
        'revision': 'auto'
    }
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

        # just a dummy parser
        zlib_v = versions.split(' ')[2]
        print('parsed zlib version: {}'.format(zlib_v) )

        self.requires('zlib/{}@conan/stable'.format(zlib_v))

    def build(self):
        print("build")

    def package(self):
        print("package")