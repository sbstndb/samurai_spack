
from spack import * 

class Samurai(CMakePackage):

    """Intervals coupled with algebra of set to handle adaptive mesh refinement and operators on it"""

    homepage = "https://github.com/hpc-maths/samurai"
    url = "https://github.com/hpc-maths/samurai.git"

    version('master', git=url)

    depends_on('xtl@0.7.5')
    depends_on('xsimd@11.0.0')
    depends_on('xtensor@0.25.0 +xsimd ~tbb')
    depends_on('highfive')
    depends_on('pugixml')
    depends_on('fmt')
    depends_on('nlohmann-json')
    depends_on('hdf5~mpi', when='~mpi')
    depends_on('hdf5+mpi', when='+mpi')    
    depends_on('boost~mpi', when='~mpi')
    depends_on('boost+mpi', when='+mpi')


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

        options.append(self.define_from_variant("BUILD_DEMOS", "demos"))
        options.append(self.define_from_variant("BUILD_BENCHMARKS", "benchmarks"))
        options.append(self.define_from_variant("BUILD_TESTS","tests"))
        options.append(self.define_from_variant("SAMURAI_CHECK_NAN", "check_nan"))

    # MPI support
        if '+mpi' in spec : 
            options.append(self.define_from_variant("WITH_MPI", "mpi"))
            options.append(self.define("HDF5_IS_PARALLEL", True)) ## !!! reflechir sur la dependance HDF5 --> hdf mpi obligatoire ? 

    # OpenMP support
        if '+openmp' in spec :
            options.append(self.define_from_variant("WITH_OPENMP", "openmp"))

#        options.append("-DFLUX_CONTAINER=xtensor") 


        return options
    
