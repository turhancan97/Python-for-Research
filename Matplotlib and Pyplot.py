#  Introduction to Matplotlib and Pyplot

import matplotlib.pyplot as plt
import numpy as np
plt.plot([0,1,4,9,16])
x = np.linspace(0,10,20)
y=x**2
plt.plot(x,y)
y1=x**2.0
y2=x**1.5
plt.plot(x,y1,"bo-")
plt.plot(x,y2,"gs-",linewidth=2,markersize=5)

#Customizing Your Plot
x = np.linspace(0,10,20)
y1=x**2.0
y2=x**1.5
plt.plot(x,y1,"bo-",label="First")
plt.plot(x,y2,"gs-",linewidth=2,markersize=5,label="Second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
xmin=-0.5
xmax=10.5
ymin=-5
ymax=105
plt.axis([xmin,xmax,ymin,ymax])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")

# =============================================================================
# Plotting Using Logarithmic Axes
# =============================================================================
x = np.logspace(-1,1,40)
y1=x**2.0
y2=x**1.5
plt.loglog(x,y1,"bo-",label="First")
plt.loglog(x,y2,"gs-",linewidth=2,markersize=5,label="Second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
xmin=-0.5
xmax=10.5
ymin=-5
ymax=105
plt.axis([xmin,xmax,ymin,ymax])
plt.legend(loc="upper left")

# =============================================================================
# Generating Histograms
# =============================================================================
x = np.random.normal(size=1000)
plt.hist(x)
plt.hist(x,normed=True)
plt.hist(x,normed=True,bins=np.linspace(-5,5,21));
#--------------------------------------------
x = np.random.gamma(2,3,1000)
plt.hist(x,bins=30)
plt.hist(x,bins=30,normed=True)
plt.figure()
plt.subplot(221)
plt.hist(x,bins=30)
plt.subplot(222)
plt.hist(x,bins=30,normed=True)
