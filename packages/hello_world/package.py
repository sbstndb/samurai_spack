from spack import *
import os



class HelloWorld(CMakePackage):
    """Hello, package example ! """

    homepage = "https://initiative-hpc-maths.gitlab.labos.polytechnique.fr/site/pages/samurai.html"

    version('1.0')  # expand=False prevents any extraction attempt


    # Define path to local source directory
    resource(
        name="hello_world",
        destination=".",
        when="@1.0",
        placement="source",
        path="/home/sbstndbs/samurai_spack/package/hello_world/source"  # Change this to your actual local path
    )

    def cmake_args(self):
        source_path = "/home/sbstndbs/samurai_spack/package/hello_world/source"
        return ["-DCMAKE_SOURCE_DIR=" + source_path]

    def build(self, spec, prefix):
        with working_dir(self.build_directory, create=True):
            cmake(self.stage.source_path, *self.cmake_args())
            make()


    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            make("install")
