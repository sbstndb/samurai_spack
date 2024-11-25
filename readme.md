# Spack Recipe for Samurai 


# Repository content
    This repository contains spack recipes for the installation of [`Samurai`](https://github.com/hpc-maths/samurai). 

# Installation
1. Install Spack if you have not already. Follow the [official documentation](https://spack.io/) for detailed instructions. 
2. Clone this repository into a directory of your choice:
```bash
git clone git@github.com:hpc-maths/spack_samurai.git
cd spack_samurai
```
3. Add the repository to your local Spack:
```bash
spack repo add . 
```
4. Explore the available options of the Samurai recipe:
```bash
spack info samurai
```
5. Installing the `Samurai` stack:
```bash
spack install samurai
```
5b. For advanced users, you can specify options or dependencing with:
```bash
spack install samurai +<option1> +<option2> %<compiler>
```
For example: 
```bash
spack install samurai +openmp +demos %gcc@14
```
6. Load your Spack recipe:
```bash
spack load samurai
```




