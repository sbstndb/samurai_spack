
from spack import *


class HelloWorld(Package):
    """Hello, package example ! """

    homepage = "https://initiative-hpc-maths.gitlab.labos.polytechnique.fr/site/pages/samurai.html"

    version('1.0')

    depends_on('gcc')
    depends_on('cmake@3.30', type='build')

  def cmake_args(self):
      return []


