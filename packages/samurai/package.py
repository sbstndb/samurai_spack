
from spack import * 

class Samurai(CMakePackage):

    """Description Samurai"""

    homepage = "https://github.com/hpc-maths/samurai"
    url = "https://github.com/hpc-maths/samurai.git"

    version('master', git=url)


    depends_on('xtl')
    dpeends_on('xsimd')
    depends_on('xtensor')
    depends_on('highfive')
    depends_on('highfive')
    dpeends_on('pugixml')
    dpeends_on('fmt')
    depends_on('nlohmann-json')
    depends_on('hdf5')
    depends_on('boost')


    variant('mpi',      default=False, description="Enable MPI support")
    variant('openmp',   default=False, description="Enable OpenMP support")
    variant('demos',    default=False, description="Build Demos")
    variant('benchmarks',default=False,description="Build benchmarks")
    variant("tests",    default=False, description="Build tests")
    variant("check_nan",default=False, description="Check for Nan in computations")


    def cmake_args(self):
        spec = self.spec
        options = [
#            "-DBUILD_DEMOS=ON"

                ]
        return options
    

'
