# mplstyle
A collection of customized [Matplotlib](http://matplotlib.org) styles sheets. 

For my own usage, but  might be of interest for someone else.

## Usage
At the begining of your `python`🐍 script add the following lines:

`import matplotlib.pyplot as plt`

`path = '~/Documents/FolderWhereYourStyleSheetIsLocated/`

`plt.style.use(path + 'timesnromanstyle.mplstyle')'`

That's all.

## Example
See `usage_example.py` file for a minimal example.

The examples below show: (a) the default Matplotlib 2.1.0 plotting style and 
(b) using timesnromanstyle.mplstyle.

![example_default](https://user-images.githubusercontent.com/21266453/31866944-e4e05380-b743-11e7-82b9-b8fa722f2fa0.png)
![example_tmnroman](https://user-images.githubusercontent.com/21266453/31866973-8da6c1b6-b744-11e7-8a8d-f720532db044.png)

## References
More details [here](https://matplotlib.org/users/customizing.html).
