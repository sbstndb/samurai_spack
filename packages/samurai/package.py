
from spack import * 

class Samurai(CMakePackage):

    """Description Samurai"""

    homepage = "https://github.com/hpc-maths/samurai"
    url = "https://github.com/hpc-maths/samurai.git"

    version('master', git=url)

    def cmake_args(self):
        spec = self.spec
        options = []
        return options
    


