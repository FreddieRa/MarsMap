# Mars Relief Map Generator

## Installation

```bash
git clone https://github.com/FreddieRa/MarsMap.git
cd ./MarsMap/
sudo apt-get update
sudo apt-get install python3-pip
pip3 install -r requirements.txt
wget https://planetarymaps.usgs.gov/mosaic/Mars_MGS_MOLA_DEM_mosaic_global_463m.tif -O height map.tif
```

## Config

In `settings.py` you can adjust scale, color gradient, and lighting settings.

 - `SCALE` - Defines the resolution of the map. Smaller numbers (e.g. < 10) will give a lot mire detail but take longer to render.
 - `smoothness` - I don't really know.
 - `sobelScale` - Defines how "smooth" to draw the map (i.e. how much of an impact the heightmap has).

## Running

To generate the map, run the following command:
`python map.py --dir [output directory] --name [name of file] --scale [scale]`

All of the parameters are optional, and will default to:
`python map.py --dir ./ --name map.png`

where the scale used is whatever is defined in `settings.py`.

## Process

Rendering consists of a five step process. First the original heightmap is downscaled, since usually we don't need such a high resolution. Then the map is reprojected to the [Robinson projection](https://xkcd.com/977/). The third step is the generation of a color map. Based on the height data a color is picked from the gradient defined in the settings. After this a normal map is generated from the reprojected heightmap. Combining the normal map and the color map, lightmap will provide shading to generate the final product.

In the specified `$directory` the following files are generated:

* `hm.tif` and `hm.png`, the heightmap, both in TIF to preserve information for the next step and as a PNG to allow easy viewing.
* `pm.tif` and `pm.png`, the reprojected heightmap.
* `cm.png`, the color map.
* `nm.png`, the normalmap.
* `map.png`, the final shaded map.

To combine everything in a nice map, `annotations.svg` has the names of many different features and an overlay with lines showing latitudes and longitudes.

# License

All graphics files in this project are licensed under the CC-BY-SA 3.0.

All code in this project is licensed under the GPL version 3 or (at your option) any later version.
