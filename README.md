# mplstyle
A collection of customized matplotlib styles sheets. 

For my own usage, but  might be of interest of someone else.

## Usage
At the begining of your `python`🐍 script add the following lines:

`import matplotlib.pyplot as plt`

`path = '~/Documents/FolderWhereYourStyleSheetIsLocated/`

`plt.style.use(path + 'timesnromanstyle.mplstyle')'`

That's all.

## Example
See `usage_example.py` file for a minimal example.

The example below show: (a) the default Matplotlib 2.1.0 plotting style and 
(b) using timesnromanstyle.mplstyle.

## References
More details [here](https://matplotlib.org/users/customizing.html).
