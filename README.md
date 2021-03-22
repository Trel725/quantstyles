# Quantstyles

A set of slightly customized colormaps and styles, developed for internal use by Quantum Technology research group in the University of Rostock.

List of available colormaps can be found in the file quant_cmaps.png

This project depends on
- [Beautiful package for generating perceptually uniform colormaps](https://github.com/peterkovesi/PerceptualColourMaps.jl) by Peter Kovesi. The heart of this small project is just a small modification of original Julia code.
- get-cpt script that allows efficient export of generated colormaps to Python.

If you'd like to manually go through all the steps:
1. Generate colormaps by executing Julia code in colormaps folder
```
cd colormaps
julia colormaps.jl
```
PerceptualColourMaps.jl and PyPlot.jl need to be installed. See that code for more details, or just use pre-generated colormaps in the colormaps directory.
2. Generate Python representation of the colormaps by running `python generate_quantcmaps.py`. This will produce actual file containing colormaps, quantcmaps.py
3. Run quantcmaps in your script. All the listed colormaps will be available as usual, e.g. `plt.imshow(data, cmap="quantjet")`