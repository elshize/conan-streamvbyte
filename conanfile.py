from conans import ConanFile, CMake, tools


class StreamvbyteConan(ConanFile):
    name = "streamvbyte"
    version = "master"
    license = "Apache 2.0"
    url = "https://github.com/elshize/conan-streamvbyte"
    code_url = "https://github.com/lemire/streamvbyte"
    description = "Fast integer compression in C using the StreamVByte codec"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/lemire/streamvbyte.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="streamvbyte")
        cmake.build()

    def package(self):
        with tools.chdir("streamvbyte"):
            cmake = CMake(self)
            cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["streamvbyte"]

    def configure(self):
        del self.settings.compiler.libcxx
