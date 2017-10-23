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

That's all.

## Description of style sheets

1. `timesnromanstyle.mplstyle`: 
  * Font: uses the Times New Roman for both text and math; 
  * Color palette: uses the Matplotlib 2.1.0 defauls; 
  * Figure size: modified; (TODO: make width / heigth = golden ratio)
  * Ticks: changes length and width of both major and minor ticks; minor ticks 
  are always visibl; ticks point inward the frame
  * Legend: changes default font size and removed frame. 
  
More to come soon.
 
## Example
See `usage_example.py` file for a minimal example.

The examples below show: (a) the default Matplotlib 2.1.0 plotting style and 
(b) using timesnromanstyle.mplstyle.

(`Default`)
![example_default](https://user-images.githubusercontent.com/21266453/31866944-e4e05380-b743-11e7-82b9-b8fa722f2fa0.png)

(`timesnromanstyle.mplstyle`)
![example_tmnroman](https://user-images.githubusercontent.com/21266453/31866973-8da6c1b6-b744-11e7-8a8d-f720532db044.png)

## References
More details [here](https://matplotlib.org/users/customizing.html).
