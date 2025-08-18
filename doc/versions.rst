Version information
===================


Version table
---------------------------

==============  ==================  ============================================================================
version         date                changes
==============  ==================  ============================================================================
2.05            17.02.2014          subplot border distance adjustment in plot options
2.04            17.02.2014          major: added plot options, direct manipulation of plot lines, axis, legend
2.03            14.02.2014          changed title, subgrid, lin/log buttons to checkbuttons
2.02            13.02.2014          added interval control for thistime
2.01            13.02.2014          added switch to plot only last value of an inner iteration, when plotting x-value 'thistime'
2.00            22.03.2013          adapted model name for Sphinx from 'taumonplot_vX-YZ.py to 'taumonplot_vX_YZ.py
2.00            22.03.2013          added Sphinx compatible documentation to source code
2.00            22.03.2013          created Sphinx documentation: html, pdf
1.98            22.03.2013          keeps lower interval during updates, only adjusts the upper interval
1.97            16.03.2013          load file path set identical to inital subdirectory 
1.96            10.01.2013          modified by Ian Krukow 
1.96            10.01.2013          numbers of inner iterations modified
1.96            10.01.2013          for the case that the iterations are counted seperately for each timestep
1.95            15.12.2012          debug load error
1.95            15.12.2012          auto update: Tau run finished: load appropriate file and end auto update
1.94            07.12.2012          circumvent error with no y-variables selected
1.93            02.12.2012          auto update switch and time
1.93            02.12.2012          remodeled GUI buttons
1.93            02.12.2012          added Tooltips
1.92            17.10.2012          pop-up when file not available
1.91            10.10.2012          fixed Update button not requiring two clicks for update
1.91            10.10.2012          fixed programm exit on clicking 'cancel' in the load file dialogue
1.90            28.09.2012          renamed plot_monitoring to taumonplot
1.90            28.09.2012          integrated code into Plotcreator, speed up reload data
1.90            28.09.2012          terminal startup support with filename
1.85            27.08.2012          adjustment to data table: displays mean range, maximum of mean range is 
1.85            27.08.2012          now tied to maximum value to display, thus allowing mean of desired ranges
1.80            24.08.2012          x-Variable drop down menu
1.75            12.06.2012          tick formater for offset
1.70            21.05.2012          bugfix data range entries
1.65            15.05.2012          bugfix table data with no values
1.65            15.05.2012          fix update of table range values
1.60            06.05.2012          added dialog to ask for file if file not available 
1.60            06.05.2012          added Load button to load other files
1.55            06.05.2012          added choice to display a data table of all selected y-variables
1.55            06.05.2012          values represent the mean of selected last number of iterations
1.55            06.05.2012          added manual in header 
1.55            06.05.2012          added popup before quit
1.50            04.05.2012          legend location changed to best
1.50            04.05.2012          added choice of iteration range to display
1.45            14.04.2012          toggle major, minor grid lines
1.45            14.04.2012          bugfix save .png
1.40            12.04.2012          added major grid lines
1.35            07.04.2012          fixed reset of start values when updating or toggling buttons
1.35            07.04.2012          added title_line variable
1.30            20.03.2012          added unsteady monitoring
1.30            20.03.2012          removed dependency on read_ascii_module
1.25            16.03.2012          toggle logarithmic scales
1.20            16.03.2012          cleaned GUI
1.15            15.03.2012          interactive choice of x and y-values
1.10            15.03.2012          integration in Tkinter, interactive reload
1.05            15.03.2012          monitor file name change when run completed
1.00            08.03.2012          first implementation
==============  ==================  ============================================================================