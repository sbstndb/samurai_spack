
from spack import * 

class Samurai(CMakePackage):

    homepage = "https://initiative-hpc-maths.gitlab.labos.polytechnique.fr/site/pages/samurai.html"
    url = "https://github.com/hpc-maths/samurai"

    version('main', git=url)

    def cmake_args(self):
        spec = self.spec
        options = []
        return options
    


