
CSS Unminifier
==============

A simple utility written in javascript for node.js to unminify CSS. The script is converted from the [MrColes.com browser-based css unminifier](http://mrcoles.com/blog/css-unminify/).

Install the script with npm:

    npm install cssunminifier

Run this to print out an unminified version of a CSS file named style.min.css:

    cssunminifier style.min.css


### Additional examples

Save the output to a file:

    cssunminifier style.min.css style.css

Change the default tab width from 4 spaces to 8:

    cssunminifier -w=8 style.min.css

Save the output to a file, reading from stdin:

    cat style.mins.css | cssunminifier - style.css


### Notes

You must have node installed to run this script. You can install it with something like [homebrew](http://mxcl.github.com/homebrew/) `brew install node` or [manually](http://nodejs.org/#download).

The code for this project [lives on github](https://github.com/mrcoles/cssunminifier).
