# Spack Recipe for Samurai 

This repository contains spack recipes for installing [`Samurai`](https://github.com/hpc-maths/samurai), a High-Performance Computation mesh library. 

# Prequisities
Before guietting started, ensure that Spack is intalled on your system. Follow the [official Spack documentation](https://spack.io/) for detailed installation instructions. 


# Installation steps

1. Clone this repository
Clone the repository to a directory of your choice:
```bash
git clone git@github.com:hpc-maths/spack_samurai.git
cd spack_samurai
```

2. Add the repository to Spack
Add the repository to your local Spack setup : 
```bash
spack repo add . 
```

3. Explore available options
Display information about the Samurai recipe and its configuration options:
```bash
spack info samurai
```

4. Install `Samurai`
To install with default options (recommanded), run:
```bash
spack install samurai
```

For advanced users, you can specify build options or dependencies. For example:
For example: 
```bash
spack install samurai +openmp +demos %gcc@14.2
```

# Usage

5. Load Samurai
After installation, load the Samurai module into your environment:
```bash
spack load samurai
```

6. Unload Samurai:
To unload Samurai module from your environment, use:
```bash
spack unload samurai
```


