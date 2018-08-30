# ProcessSimToolkit

This is a simplified tool for running stochastic discrete-event process simulations that follow a Server/Queue model. Models are easily built in a building-block format, with easy access to the classes and functions to create custom logic for more-complicated scenarios. Plotting output is included for a histogram output of total system time, as well as live plotting for output mean stabilization used for determining optimal simulation runs. 

<br><br>
## Lemonade Stand Tutorial

Full code for this tutorial can be accessed [here.](https://github.com/trevorbye/ProcessSimToolkit/blob/master/LemonadeStandTutorial/LemonadeStandSim.py)

### Getting Started

This is a tutorial for simulating the flow of customers through a lemonade stand. Although a simple example, it serves to illustrate the design pattern for this toolkit, and simply adding more Servers/Queues will allow for significantly more complex simulations. To get started, fork this entire project.

After you have access to all classes, begin by importing the necesary libraries and classes:

