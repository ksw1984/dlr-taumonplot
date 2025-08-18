.. _manual_Manual:

Manual
======

Starting taumonplot
..........................

- run the python script directly in a Text editor (F5 in SciTE)
- run the python script from a terminal ``python  taumonplot_v2-04.py``
- run the function ``create_plot(...)`` of the module ``taumonplot_v2-04`` in another script
- `Monitoring data on a cluster`: 
    1. Place the script on the cluster. Run the script with a Text editor on your own machine. You can use all options like auto updating. The monitoring file is transfered to your own machine for reading and display.
    
    or
    
    2. Place the script on the cluster. Run the script from you local terminal.

GUI
.............

GUI overview
----------------------
   
.. figure:: ../images/v204/GUI.png    
    :scale: 75 %  
    :align: center   
    :alt: alternate text
    
    Complete taumonplot GUI. At hte top is the plot canvas, at the bottom the options
    
The GUI consists of two main parts. The first is a cavas that displays the figure with the monitoring data on top of the GUI. The second is a frame on the botom containing options for loading files, plotting etc.

Canvas
----------------------

.. figure:: ../images/v200/canvas.png    
    :scale: 75 %  
    :align: center   
    :alt: alternate text
    
    Matplotlib canvas

The canvas plots the monitoring data dependent on the choosen options.

Options
----------------------

.. figure:: ../images/v204/Options.png    
    :scale: 100 %  
    :align: center   
    :alt: alternate text
    
    option bar

Tool tips
----------------------
Hoovering over a widget (buttons, letter boxes etc.) will open a tool tip window next to the cursor, that shortly describes the functionality of the widget.

Programm options
----------------------

+-----------------------------------+--------------------------------------------------------------------------------+
+-----------------------------------+--------------------------------------------------------------------------------+
|``Quit`` button                    |closes the program                                                              |
+-----------------------------------+--------------------------------------------------------------------------------+
|``Help`` button                    |opens license information and manual                                            |
+-----------------------------------+--------------------------------------------------------------------------------+

File options
----------------------

+-----------------------------------+--------------------------------------------------------------------------------+
+-----------------------------------+--------------------------------------------------------------------------------+
| ``Load`` button                   | opens a file dialog to open a different Tau monitoring file                    |
+-----------------------------------+--------------------------------------------------------------------------------+

Plot options
----------------------

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
|``Title`` switch                   |toggles title display of monitoring file                                                                             |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
|``Subgrid`` switch                 |toggles the display of subgrid lines for the logarithmic axes                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
|``LIN/LOG x`` switch               |toggles the change between logarithmic or linear axis for the abcissa                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
|``LIN/LOG y`` switch               |toggles the change between logarithmic or linear axis for the ordinate                                               |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
|``Offset (none/on/math)`` button   | toggles number offset of axis ticks (documentation_)                                                                |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``Update`` button                 |updates the data from the monitoring file (new data is displayed if monitoring file has received an update from TAU) |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------+


.. _documentation: http://matplotlib.org/1.2.0/api/ticker_api.html
                
.. figure:: ../images/v200/linlin.png    
    :scale: 45 %  
    :align: center   
    :alt: alternate text
    
    Canvas with linear X, linear Y axes
    
.. figure:: ../images/v200/linlog.png    
    :scale: 45 %  
    :align: center   
    :alt: alternate text
    
    Canvas with linear X, logarithmic Y axes - with subgrid

.. figure:: ../images/v200/loglin.png    
    :scale: 45 %  
    :align: center   
    :alt: alternate text
    
    Canvas with logarithmic X, linear Y axes - with subgrid
          
.. figure:: ../images/v200/loglog.png    
    :scale: 45 %  
    :align: center   
    :alt: alternate text
    
    Canvas with logarithmic X, logarithmic Y axes - with subgrid

Autoupdate option
----------------------

.. figure:: ../images/v200/autoupdate.png    
    :scale: 100 %  
    :align: center   
    :alt: alternate text
    
    autoupdate option bar

+-----------------------------------+--------------------------------------------------------------------------------+
+-----------------------------------+--------------------------------------------------------------------------------+
|``AUTO UPDATE`` letter box         |interval can be set here (in seconds)                                           |
+-----------------------------------+--------------------------------------------------------------------------------+
|``Set`` button                     | sets the update interval from the letter box                                   |
+-----------------------------------+--------------------------------------------------------------------------------+
|``Auto`` toggle                    | auto update on/off switch                                                      |
+-----------------------------------+--------------------------------------------------------------------------------+

.. Note::
    The script will execute an update command every `interval seconds` as if the user presses the ``Update`` button. If the file is to large and the interval is too small, this can lead to stability problems
       
Iteration interval display options
-------------------------------------

.. figure:: ../images/v200/interval.png    
    :scale: 100 %  
    :align: center   
    :alt: alternate text
    
    plot interval option bar


+----------------------------------------+--------------------------------------------------------------------------------+
+----------------------------------------+--------------------------------------------------------------------------------+
|``Reset`` button                        | resets the minimum and maximum values to display to the complete range         |
+----------------------------------------+--------------------------------------------------------------------------------+
|``Iter/Time (min XXXXX)`` letter box    | number of start iteration/time to plot                                         |
+----------------------------------------+--------------------------------------------------------------------------------+
|``Set`` button                          |  sets the start iteration/time to plot                                         |
+----------------------------------------+--------------------------------------------------------------------------------+
|``Iter/Time (max XXXXX)`` letter box    | number of end iteration/time to plot                                           |
+----------------------------------------+--------------------------------------------------------------------------------+
|``Set`` button                          |  sets the end iteration/time to plot                                           |
+----------------------------------------+--------------------------------------------------------------------------------+

Data table display options
----------------------------

.. figure:: ../images/v200/datatable.png    
    :scale: 100 %  
    :align: center   
    :alt: alternate text
    
    data table option bar


+------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
|``DATA TABLE: mean of IterNb`` letter box |number of iterations to compute mean for data table                                                                     |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
|``Table`` toggle                          |toggle the display of a data table on the plot with mean values of the last iterations                                  |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
|``Set interval`` button                   |sets the range of last iterations to include in the mean value (standard values is 1/50th of iteration range at startup)|
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------+


.. figure:: ../images/v200/data_table_canvas.png    
    :scale: 75 %  
    :align: center   
    :alt: alternate text
    
    Overlayed data table, mean computation set to 200 iterations
    
Time: Plot last inner iteration value
--------------------------------------------------
.. figure:: ../images/v204/LastInnerIter.png    
    :scale: 100 %  
    :align: center
    :alt: alternate text
    
    Last InnerIter switch
    
When plotting transient data over the time variable, the value of the inner iterations is oftten not of interest. To plot only the last values of the inner iterations, which are the result of the time step, a switch has been implemented. The switch is only active when ``X-Variable`` is ``thistime``.

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
|``Last InnerIter`` switch          | toggles to plot all iterations or only the last value of the inner iterations (swicht active with X-Variable=thistime  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+

Example of effect:

.. figure:: ../images/v204/wo_last_innerIter.png    
    :scale: 45 %  
    :align: center
    :alt: alternate text
    
    Last inner Iter off
    
.. figure:: ../images/v204/w_last_innerIter.png    
    :scale: 45 %  
    :align: center
    :alt: alternate text
    
    Last inner Iter on


Variable choice options
-------------------------

The variable choices will be automatically adapted, depending on the variables in monitoring file.

+-----------------------------------+--------------------------------------------------------------------------------+
+-----------------------------------+--------------------------------------------------------------------------------+
|``X-Variable`` drop-down menu      |**one** choice of variable for the abcissa.                                     |
+-----------------------------------+--------------------------------------------------------------------------------+

Choosing a variable different from ``Inner-iter`` will deactivate the `Iteration interval display options`_ and `Data table display options`_. Another sensible varibale to choose for the abcissa is the `this-time` variable for transient monitoring files.

.. figure:: ../images/v200/x-variable.png
    :scale: 100 %  
    :align: center   
    :alt: alternate text
    
    x-variable drop down menu

+-----------------------------------+--------------------------------------------------------------------------------+
+-----------------------------------+--------------------------------------------------------------------------------+
|``Y-variables`` checkbuttons       |**multiple** choices of variables for the ordinate                              |
+-----------------------------------+--------------------------------------------------------------------------------+

.. figure:: ../images/v200/y-variables.png    
    :scale: 100 %  
    :align: center   
    :alt: alternate text
    
    y-variable checkbuttons

Plot options
-------------
.. figure:: ../images/v204/plot_options_button.png    
    :scale: 100 %  
    :align: center
    :alt: alternate text
    
    Plot options button

This button opens another windows which contains the plot options for the variables and axes. The tabl is generated at startup for the loaded variables.

.. figure:: ../images/v205/plot_options_grid.png    
    :scale: 100 %  
    :align: center
    :alt: alternate text
    
    Plot options
    
+-----------+----------------------------------------------------------------------------------------------------------------------+
|Column     |Option                                                                                                                |
+===========+======================================================================================================================+
|TAU var    |name of the loaded TAU variable (see :ref:`usage_Monitoring`)                                                         |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|label      |label name as it apears in the legend. Latex formatting possbile with $$                                              |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|axis       |label name as it apears on the y-axis. Latex formatting possbile with $$                                              |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|c          |Color of the curve: standard colors, grey shades, html hex strings and html names for colors possible                 |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|m          | Marker ('o','h','^','v','<','>','_','1','2','3','4','8','p','|','d',',','+','s','*','l','x','D','H','.')             |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|ls         |Line style      ('-','--','..','-.','.',',','o','^','v','<','>','s','+','x','d','1','2','3','4','h','p','|','S','H')  |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|lw         | Line width (float)                                                                                                   |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|ms         | Marker size (float)                                                                                                  |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|me         | Marker every n-th value                                                                                              |
+-----------+----------------------------------------------------------------------------------------------------------------------+
|alpha      |      Alpha blending value (0.0 transparent through 1.0 opaque)                                                       |
+-----------+----------------------------------------------------------------------------------------------------------------------+



+-----------------------------------+--------------------------------------------------------------------------------+
|X-Axis: `variable`                 |    label name as it apears on the x-axis. Latex formatting possbile with $$    |
+-----------------------------------+--------------------------------------------------------------------------------+


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Label sizes                        |Font size of the tickers, legend and axes Either a relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' or an absolute font size, e.g., 12                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------+--------------------------------------------------------------------------------+
|Subplot size                       |   Suplot distance from the respective borders - see hover tooltip              |
+-----------------------------------+--------------------------------------------------------------------------------+

Mataplotlib figure options
---------------------------

.. figure:: ../images/v200/figureOptions.png
    :scale: 100 %  
    :align: center   
    :alt: alternate text
    
    Matplotlib figure option bar
    
- (home button? : no functionality)
- (back button? : no functionality)
- (forward button? : no functionality)
- ``Pan/Zoom`` button : allows panning and zooming of the image
- ``Zoom rect`` button : allows zoom into a rectangle
- ``Options`` button : to adjust subplot params. See documentation for subplots_adjust_.
- ``Save figure`` button : allows saving of the canvas


.. _subplots_adjust: http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.subplots_adjust


       



File choice
.............

Autochoice
----------------------
1. Execute taumonplot
2. The programm will search in the current working directory for a file with the endings 
    - '.monitor.tmp.dat'
    - '.monitor.pval.dat'
    - '.monitor.tmp.unsteady.dat'
    - '.monitor.pval.unsteady.dat'
    
    and the ``name_prefix = 'fluid.solution'``.
    
    If a file is found, it is opened.

Choice by file dialog
-------------------------

1. Same behaviour as in `Autochoice`_   
2. If no file is found, a file dialog is opened, that allows the user to choose any file for input

Choice by filename and subdirectory
----------------------------------------

1. Open the taumonplot script file
2. Declare ``subdirectory`` and ``name_prefix`` of tau monitoring file (without the endings '.monitor.tmp.dat', '.monitor.pval.dat', '.monitor.tmp.unsteady.dat', '.monitor.pval.unsteady.dat')
3. Verify that data_line and title_line are correct
4. Run program


Choice by function call
----------------------------

.. code-block:: python

    from taumonplot import create_plot
    #
    subdirectory = './'
    name_prefix = 'fluid.solution' # name of solution file
    data_line = 25    # line where data values start in monitoring file
    title_line = 23   # line with variable names
    # start variables to plot
    x_variable_list = ['Inner-iter']    
    y_variable_list = ['Residual',
                        'C-lift',
                        'C-drag' ]
    check_iter_numbers = True   # Enable to check ascending order of iteration numbers
    #
    create_plot(subdirectory, 
                name_prefix, 
                data_line, 
                title_line, 
                x_variable_list, 
                y_variable_list, 
                check_iter_numbers)
    #

:Function:

    ``create_plot(subdirectory, name_prefix, data_line, title_line, x_variable_list, y_variable_list, check_iter_numbers, save_to_file=False)``

    :Parameters:
        subdirectory : string
                directory containing monitoring data, absolute or relative
        name_prefix : string
                name prefix of monitoring file    
        data_line : integer 
                line number where data starts
        title_line : integer 
                line number of variable names
        x_variable_list : list of string 
                for x (display automatically at startup),
                Example: ``x_variable_list = ['Inner-iter']``
        y_variable_list : list of strings 
                for y (display automatically at startup),
                Example: ``y_variable_list = ['Residual','C-lift','C-drag' ]``
        check_iter_numbers : boole
                Check ascending order of iteration numbers
        save_to_file : bool
                save to file (deprecated)


Information for using taumonplot
.......................................
- the user has to press the ``Update`` button to reload the monitoring file
- all changes to the plot via other buttons do **not** trigger a reaload of the monitoring file 
- the status of the TAU run is indicated in the buttom rigth corner. This status does not indicate the status of the TAU process itself but gets its information from the file ending, which is read. The running TAU solver creates a file with the endings '.monitor.tmp.dat' (steady state run) or  '.monitor.tmp.unsteady.dat' (dual time stepping - unsteady run). While a file with this file ending is loaded, `taumonplot` will indicate the run as not completed. TAU will change the filename on its own after it completed to '.monitor.pval.dat' or '.monitor.pval.unsteady.dat'. However, when the solver fails to complte its run, the file endings are not changed. An indication for a failed run is no change in monitoring data after several seconds (normal computations) or minutes (very large computations).


      
