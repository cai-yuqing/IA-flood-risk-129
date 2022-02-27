import matplotlib.pyplot as plt
import numpy as np
# from.analysis import polyfit
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


#Task 2E
def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()
    return plt.show()


#Task 2F
def plot_water_level_with_fit(station, dates, levels, p):
  x = matplotlib.dates.date2num(dates)

     # Create set of 10 data points on interval (0, 2)
     #x = np.linspace(0, 2, 10)
  y = levels
  print(y)

     # Find coefficients of best-fit polynomial f(x) of degree 4
  p_coeff = np.polyfit(x - x[0], y, p)

     # Convert coefficient into a polynomial that can be evaluated,
     # e.g. poly(0.3)
  poly = np.poly1d(p_coeff)

     # Plot original data points
  plt.plot(x, y, '.')

     # Plot polynomial fit at 30 points along interval
  x1 = np.linspace(x[0], x[-1], 30)
  plt.plot(x1, poly(x1 - x[0]))

     # Display plot
  return plt.show()