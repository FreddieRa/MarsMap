import sys, os
from pathlib import Path
from PIL import Image, ImageDraw
import vectormath as vmath

import argparse

import settings as s

import heightmap
import projection
import colormap
import normalmap
import lightmap

import topng

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Command-line tool for generating acurately rendered displacement maps of mars",
        epilog="Created by PietPtr, adapted by FreddieRa",
    )

    parser.add_argument(
        "--dir",
        action="store",
        type=Path,
        default="./",
        help="Folder of the output files",
        dest="directory",
    )

    parser.add_argument(
        "--name",
        action="store",
        type=str,
        default="map.png",
        help="File name of the end map",
        dest="name",
    )

    parser.add_argument(
        "--scale",
        action="store",
        type=int,
        default=-1,
        help="Scale of the map (smaller is higher res, 1=8k)",
        dest="scale",
    )

    return parser.parse_args(args)

def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)

    directory = args.directory
    name = (args.name).replace('.png', '') + '.png'
    scale = args.scale

    if scale == -1:
        scale = s.SCALE


    hm = Image.open('heightmap.tif')

    probableTime = int( 1105 * ((10 / scale) ** 2) )
    print("Projected time to complete: ", probableTime // 60, "minutes, ", probableTime % 60, "seconds")

    scaled = heightmap.heightmap(hm, scale)
    scaled.save(directory / "hm.tif")

    projected = projection.projectmap(scaled, scale)
    projected.save(directory / "pm.tif")

    colors = colormap.colormap(projected, s.gradient, s.smoothness)
    colors.save(directory / "cm.png")

    normals = normalmap.normalmap(projected, s.sobelScale)
    normals.save(directory / "nm.png")

    shaded = lightmap.lightmap(normals, colors, s.light, s.ambientPercentage)
    shaded.save(directory / name)

    scaledpng = topng.to_png(scaled)
    scaledpng.save(directory / "hm.png")

    projectedpng = topng.to_png(projected)
    projectedpng.save(directory / "pm.png")

def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()