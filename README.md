# charge-square-potential

## Overview

This Python script computes and visualizes the electrostatic equipotential lines of a finite square sheet of charge by discretizing the sheet into point charges and summing their contributions.

## Features

* Numerical evaluation of the electric potential using direct summation.
* Customizable sheet size, surface charge density, and grid resolutions.
* Visualization of equipotential lines with Matplotlib.

### Script Parameters

All parameters are defined at the top of the script:

| Variable | Description                               | Default |
| -------- | ----------------------------------------- | ------- |
| `L`      | Side length of the square sheet (m)       | 1.0     |
| `sigma`  | Surface charge density (C/m²)             | 1e-6    |
| `N`      | Number of point charges per side          | 100     |
| `M`      | Grid resolution for evaluation (per axis) | 100     |
| `levels` | Number of equipotential contour levels    | 25      |

## Output

* A contour plot displaying equipotential lines in the XY plane.
* Contour labels indicate potential values in volts (V).

![alt text](https://github.com/ajsteinmetz/charge-square-potential/blob/main/example_output.png "A contour plot displaying equipotential lines in the XY plane.")

## License

This project is licensed under the MIT License.
