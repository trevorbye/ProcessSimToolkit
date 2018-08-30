# ProcessSimToolkit

This is a simplified tool for running stochastic discrete-event process simulations that follow a Server/Queue model. Models are easily built in a building-block format, with easy access to the classes and functions to create custom logic for more-complicated scenarios. Plotting output is included for a histogram output of total system time, as well as live plotting for output mean stabilization used for determining optimal simulation runs. 

<br><br><br>
## Lemonade Stand Tutorial

Full code for this tutorial can be accessed [here.](https://github.com/trevorbye/ProcessSimToolkit/blob/master/LemonadeStandTutorial/LemonadeStandSim.py)

### Getting Started

This is a tutorial for simulating the flow of customers through a lemonade stand. Although a simple example, it serves to illustrate the design pattern for this toolkit, and simply adding more Servers/Queues will allow for significantly more complex simulations. To get started, fork this entire project.

After you have access to all classes, begin by importing the necesary libraries and classes:

```python
from UtilityClasses.ServerEntity import Server
from UtilityClasses.QueueEntity import PriorityQueue
from UtilityClasses.TimeRandomizerEntity import TimeRandomizer
from UtilityClasses.ServerAndQueueWrapperEntity import ServerAndQueueWrapper
from SimulationClasses.SimulationApplication import SimApplication

import datetime
```
<br>
The `UtilityClasses` are various classes used as the building blocks for building a simulation. The `Server` class represents a capacity-constrained resource in your system that processes customers and holds them for a certain period of time. This time is stochastically generated by the `TimeRandomizer` class, which allows you to define different distributions to draw samples from. After customers are processed by a Server, they are typically transitioned into a `PriorityQueue` where wait time is accumulated while waiting for the next Server to be available (in this tutorial there is only one Server for brevity). 

`ServerAndQueueWrapper` is simply a wrapper object for either a `Server` or a `PriorityQueue`, and allows all system resources to be added to one list in sequence. `SimApplication` is the main configuration class, and accepts parameters for the start and end time of each run, total simulation runs, and switches for turning on/off chart output. Importing `datetime` is necesary to define these time parameters.
<br><br>
### Building the System
