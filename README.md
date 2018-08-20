# mplstyle
A collection of customized [Matplotlib](http://matplotlib.org) styles sheets. 

For my own usage, but  might be of interest for someone else.

## Usage
At the begining of your `python`🐍 script add the following lines:

~~~~
import matplotlib.pyplot as plt
path = '~/Documents/FolderWhereYourStyleSheetIsLocated/
plt.style.use(path + 'timesnromanstyle.mplstyle')
~~~~

That's all. 😎

## Description of style sheets

1. `timesnromanstyle.mplstyle`: 
  * Font: uses the Times New Roman for both text and math; 
  * Color palette: uses the Matplotlib 2.1.0 defauls; 
  * Figure size: modified; (TODO: make width / heigth = golden ratio)
  * Ticks: changes length and width of both major and minor ticks; minor ticks 
  are always visible; ticks point inward the frame
  * Legend: changes default font size and removed frame.
  
2. `computermodernstyle.mplstyle`: 
 * Font: uses the default LaTeX Computer Modern font for both text and math; 
 * Color palette: uses the Matplotlib 2.1.0 defauls; 
 * Figure size: modified; (TODO: make width / heigth = golden ratio)
 * Ticks: changes length and width of both major and minor ticks; minor ticks 
 are always visible; ticks point inward the frame
 * Legend: changes default font size and removed frame. 
  
More to come soon.
 
## Example
See `usage_example.py` file for a minimal example.

The examples below show: (a) the default Matplotlib 2.1.0 plotting style, 
(b) using timesnromanstyle.mplstyle and (b) using computermodernstyle.mplstyle.
Warning: computermodernstyle.mplstyle uses "text.usetex: True", hence it runs 
it might take longer than normal to generate the output.

(`Default`)
![example_default](example_default.png)

(`timesnromanstyle.mplstyle`)
![example_tmnroman](example_tmnroman.png)

(`computermodernstyle.mplstyle`)
![example_tmnroman](example_computermodern.png)


## References
More details [here](https://matplotlib.org/users/customizing.html).
