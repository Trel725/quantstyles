# Quantstyles

A set of slightly customized colormaps and styles, developed for internal use by Quantum Technology research group in the University of Rostock.

<img src="https://raw.githubusercontent.com/Trel725/quantstyles/master/quantstyles/quant_cmaps.png" width="50%">

## Installation
The package is published on pypi, so it is enough to run:
```
pip install quantstyles
```

## Acknoledgements
This project depends on
- [Beautiful package for generating perceptually uniform colormaps](https://github.com/peterkovesi/PerceptualColourMaps.jl) by Peter Kovesi. The heart of this small project is just a small modification of original Julia code.  
- get-cpt script that allows efficient export of generated colormaps to Python.  

## Development
If you'd like to manually go through all the steps:  
0. Clone the repo by `git clone https://github.com/Trel725/quantstyles.git --recursive` Recursive is needed to sync get-cpt repo.
1. Generate colormaps by executing Julia code in colormaps folder  
```
cd colormaps
julia colormaps.jl
```
PerceptualColourMaps.jl and PyPlot.jl need to be installed. See that code for more details, or just use pre-generated colormaps in the colormaps directory.  
2. Generate Python representation of the colormaps by running `python generate_quantcmaps.py`. This will produce actual file containing colormaps, quantcmaps.py  The command requires numpy, os, glob and (probably) urllib (from get-cpt).
3. Run quantcmaps in your script. All the listed colormaps will be available as usual, e.g. `plt.imshow(data, cmap="quantjet")`  
4. Additionally you can try to build pip wheel by executing `python setup.py sdist bdist_wheel` in the project top directory.
