# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------------
#   script taumonplot.py
#--------------------------------------------------------------------------
#
#
subdirectory = './example/'
name_prefix = 'fluid.solution' # name of monitor file, without the ending '.monitor.tmp.dat', '.monitor.pval.dat', '.monitor.tmp.unsteady.dat', '.monitor.pval.unsteady.dat'
#
x_variable_list = ['Inner-iter']
#~ x_variable_list = ['thistime']
y_variable_list = [ 'Residual',
                    'C-lift',
                    'C-drag' ]
#
#--------------------------------------------------------------------------
# Copyright (c) 2012, Institute of Aircraft Design and Lightweight Structures (IFL),
# TU Braunschweig, Hermann-Blenk-Str. 35, 38108 Braunschweig.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the IFL, TU Braunschweig nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL IFL, TU Braunschweig BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#
#--------------------------------------------------------------------------
# Description: Python module using matplotlib to plot TAU monitoring data
#--------------------------------------------------------------------------
#
# This program is written in Python <= 2.7 under Linux-Ubuntu 10.04, it has been tested under MS Windows 7
# This program was updated to support Python 3.X
#
# Author: Kay Sommerwerk
# e-mail: k.sommerwerk@tu-braunschweig.de
# Date: see version history
# Revision: see version history
#
# Modified by: Ian Krukow (Version 1.96)
# e-mail: i.krukow@tu-braunschweig.de
#
# This software is provided under the assumption that major improvements of this software 
# will be made available to the IFL
#
#--------------------------------------------------------------------------
# Version history:
#--------------------------------------------------------------------------
# plot_monitoring.py,   version 1.00, 08.03.2012       # first implementation
#                       version 1.05, 15.03.2012       # monitor file name change when run completed
#                       version 1.10, 15.03.2012       # integration in Tkinter, interactive reload
#                       version 1.15, 15.03.2012       # interactive choice of x and y-values
#                       version 1.20, 16.03.2012       # clean GUI
#                       version 1.25, 16.03.2012       # toggle logarithmic scales
#                       version 1.30, 20.03.2012       # added unsteady monitoring
#                                                        # removed dependency on read_ascii_module
#                       version 1.35, 07.04.2012       # fixed reset of start values when updating or toggling buttons
#                                                        # added title_line variable
#                       version 1.40, 12.04.2012       # added major grid lines
#                       version 1.45, 14.04.2012       # toggle major, minor grid lines
#                                                        # bugfix save .png
#                       version 1.50, 04.05.2012       # legend location changed to best
#                                                        # added choice of iteration range to display
#                       version 1.55, 06.05.2012       # added choice to display a data table of all selected y-variables. 
#                                                        # values represent the mean of selected last number of iterations
#                                                        # added manual in header 
#                                                        # added popup before Quit
#                       version 1.60, 06.05.2012       # added dialog to ask for file if file not available 
#                                                        # added Load button to load other files
#                       version 1.65, 15.05.2012       # bugfix table data with no values
#                                                        # fix update of table range values
#                       version 1.70, 21.05.2012       # bugfix data range entries
#                       version 1.75, 12.06.2012       # tick formater for offset
#                       version 1.80, 24.08.2012       # x-Variable drop down menu
#                       version 1.85, 27.08.2012       # adjustment to data table: displays mean range, maximum of mean range is 
#                                                        # now tied to maximum value to display, thus allowing mean of desired ranges
#                       version 1.90, 28.09.2012       # renamed plot_monitoring to taumonplot
#                                                        # integrated code into Plotcreator, speed up reload data
#                                                        # terminal startup support with filename
#                       version 1.91, 10.10.2012       # fixed Update button not requiring two clicks for update
#                                                        # fixed programm exit on clicking 'cancel' in the load file dialogue
#                       version 1.92, 17.10.2012       # pop-up when file not available
#                       version 1.93, 02.12.2012       # auto update switch and time
#                                                        # remodeled GUI buttons
#                                                        # added Tooltips
#                       version 1.94, 07.12.2012       # circumvent error with no y-variables selected
#                       version 1.95, 15.12.2012       # debug load error
#                                                        # auto update: Tau run finished: load appropriate file and end auto update
#                       version 1.96, 10.01.2013       # modified by Ian Krukow 
#                                                        # numbers of inner iterations modified
#                                                        # for the case that the iterations are counted seperately for each timestep
#                       version 1.97, 16.03.2013       # load file path set identical to inital subdirectory 
#                       version 1.98, 22.03.2013       # keeps lower interval during updates, only adjusts the upper interval
#                       version 2.00, 22.03.2013       # added Sphinx compatible documentation to source code
#                                                      # created Sphinx dokumentation html, pdf
#                                                      # adapted model name for Sphinx from 'taumonplot_vX-YZ.py to 'taumonplot_vX_YZ.py 
#                       version 2.01, 13.02.2014        # added switch to plot only last value of an inner iteration, when plotting x-value 'thistime'
#                       version 2.02, 13.02.2014        # added interval control for thistime
#                       version 2.03, 14.02.2014        # changed title, subgrid, lin/log buttons to checkbuttons
#                       version 2.04, 17.02.2014        # major: added plot options via a plot options menu. allows direct manipulation of plot lines, axis and legend
#                       version 2.05, 17.02.2014        # subplot border distance adjustment in plot options
#--------------------------------------------------------------------------
# ToDo 
#--------------------------------------------------------------------------
#                      
#                       - when loading another file remap the X- and Y-Variable entries
#                       - add additional (2nd) y-axis, Y-variable-choice for axis, additional lin/log-toggle
#
#--------------------------------------------------------------------------
# Necessary files in the working directory:
#           TAU monitoring file:   steady:             'prefix.monitor.tmp.dat' or 'prefix.monitor.pval.dat'
#                                            or unsteady:     'prefix.monitor.tmp.unsteady.dat' or 'prefix.monitor.pval.unsteady.dat'
#
#---------------------------------------------------------------------------
# ouput:
#       plot with indicated variables 
#       and/or
#       image files with indicated variables 
# 
#---------------------------------------------------------------------------
#
# variables to be declared
#   
#   necessary - if file not found, search dialog will open.
#       subdirectory = path to monitoring file and where output/logifle is writen
#       name_prefix = Output files prefix as indicated in the TAU parameter file
#
#   adjustable for convenience.
#       data_line = line where data values start in monitoring file
#       title_line = line where the column names are located
#       x_variable_list = list of x axis variables as indicated in monitoring file (without "",defaults to ['Inner-iter'])
#       y_variable_list = list of y axis variables as indicated in monitoring file (without "")
#       check_iter_numbers = check whether iteration numbers are ascending, adjust e.g. if numbered seperately for each timestep
#
#   obsolete.
#       save_to_file = toggle to save files or show plot
#       formats =   list of image format strings to ouput
#   
#---------------------------------------------------------------------------
#   function can directly be called after import through 
#       >>>create_plot(subdirectory,name_prefix,data_line,x_variable_list,y_variable_list,save_to_file)
#---------------------------------------------------------------------------
#   script can directly be executed from terminal with or without filepath
#       >>>python tauplot.py ./sol_2.monitor.pval.dat
#---------------------------------------------------------------------------
#   Additional configuration and layout:
#       layout for axes, legend, labels and title can be changed in method 'plot_monitor_file' for interactive output and for images to save respectively
#---------------------------------------------------------------------------
#   2. PROGRAM MANUAL
#---------------------------------------------------------------------------
#   1. declare subdirectory and name_prefix of tau monitoring file (without the ending '.monitor.tmp.dat', 
#                                       '.monitor.pval.dat', '.monitor.tmp.unsteady.dat', '.monitor.pval.unsteady.dat')
#       1.1 not necessarily needed as monitoring file can be choosen through file browser if file not found
#   2. verify that data_line and title_line are correct
#   3. run program: variables to display can be choosen in the gui
#       (3.1) variables to display automatically at startup may be changed with the variables x_variable_list and y_variable_list
#   4. Button explanation
#       row 1: Basic display functions
#           Quit : closes the program
#           Help : open license and manual
#           (Save .png:)  creates a png image of the set up plot (takes some time to replot data)
#                   can be saved using the tkinter gui
#           Load : opens another Tau monitoring file
#           Title : toggles title display of monitoring file
#           Subgrid : toggles the display of subgrid lines
#           LIN/LOG x/y : toggles the logarithmic or linear axis 
#           Offset : toggles number offset of axis ticks (documentation:http://matplotlib.org/1.2.0/api/ticker_api.html)
#           Update : updates the data from the monitoring file (new data is displayed if monitoring file has received 
#                                       an update from TAU)
#       row 2: Auto Update 
#           Set: sets the desired update interval in seconds
#           auto update on/off switch
#   
#       row 3: Iteration interval display options
#           reset : resets the minimum and maximum values to display to the complete range
#           set min : sets the minimum Iteration number to display (entered in the left box)
#           set max : sets the maximum Iteration number to display (entered in the right box)
#       row 4: Data table display options
#           toggle data table (on/off) : toggle the display of a data table on the plot with mean values of the last iterations 
#                                       set by 'set interval' (standard values is 1/50th of Iteration range)
#           set interval : sets the range of last iterations to include in the mean value
#           Tick (offset,no offset, math): sets the axis ticks offset type
#       row 5: Variable choice options
#           X-Variable : one choice of variable for the abcissa
#           Y-Variables : multiple choice of variables for the ordinate
#      
#---------------------------------------------------------------------------
############################### USER INPUT
data_line = 24                       # line where data values start in monitoring file, typically line 25 for TAU monitoring file , sometimes 24 after restarts
title_line = 23                         # line with variable names
#
# startup values to display

check_iter_numbers = True	# Enable to check ascending order of iteration numbers
#
## unnecessary because TK gui allows saving directly, only makes sense for function calls
save_to_file = False        # toggle save files or show plot - can be interactively used in gui
formats = ['png']           # emf, eps, jpeg, jpg, pdf, png, ps, raw, rgba, svg, svgz, tif, tiff
############################### INPUT END
#
############################### MODULES
# system
import os
import sys
import time
from typing import Literal
from pathlib import Path
# numpy > 1.6.1
import numpy as np
def is_string_like(obj):
    """Return True if obj is string-like (filename/path)."""
    return isinstance(obj, (str, bytes, Path, np.str_, np.bytes_))
# matplotlib > 0.99.1
import pylab
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
# TKinter gui
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog
############################### MODULES END
#
############################### TERMINAL or DIRECT startup
if len(sys.argv) > 1:
    # terminal input with path/filename    
    filepath = sys.argv[1]
    print(filepath)
    if '/' in filepath:
        #~ path in filename
        split_path = filepath.split('/')
        split_name = split_path[-1]
        subdirectory = '/'.join(split_path[:-1])+'/'
        split_name = split_name.split('.')        
        name_prefix = '.'.join(split_name[:-3])        
    else:
        #~ only filname
        split_name = filepath.split('.')        
        name_prefix = '.'.join(split_name[:-3])        
        #
    #
else:
    # direct startup
    pass
    #
###############################
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#

class PlotCreator:
    """
    Class to create a matplotlib figure plot
    """
    #
    def __init__(self,
                 subplot,
                 subdirectory,
                 name_prefix,
                 data_line,
                 title_line,
                 x_variable_list,
                 y_variable_list,
                 check_iter_numbers,
                 save_to_file=False,
                 ):
        """
        Create a matplotlib figure plot

        :Parameters:
            subplot : matplotlib subplot instance
                the figure subplot
            subdirectory : string
                directory containing monitoring data, absolute or relative
            name_prefix : string
                name prefix of monitoring file
            data_line : integer
                line number where data starts
            title_line : integer
                line number of variable names
            x_variable_list :
                list of strings for x-variable
            y_variable_list : list of strings
                list of strings for y-variable
            check_iter_numbers : bool
                check ascending order of iteration numbers
            save_to_file : bool
                switch to save file (deprecated)
        """
        #
        self.data_line = data_line
        self.title_line = title_line
        self.x_variable_list = x_variable_list
        self.y_variable_list = y_variable_list
        self.check_iter_numbers = check_iter_numbers
        #
        self.header = None
        self.value_dict = None
        self.available_variables = None
        self.min_entry_val = None
        self.max_entry_val = None
        #
        self.set_title = True
        self.x_scale_log = False
        self.y_scale_log = True
        self.subgrid = False       
        self.plt_table_data = False
        self.ticker_type = 'no_offset'  #  'no_offset'  ,  'with_offset' ,  'math_offset' 
        #
        self.unsteady = False
        if self.x_variable_list[0] == 'thistime':
            self.plot_last_InnerIter = True        
        else:
            self.plot_last_InnerIter = False
        #
        self.name_prefix = name_prefix
        self.get_log_name(subdirectory, name_prefix)
        #        
        self.get_variables()
        self.min_entry_val_disp = self.min_entry_val
        self.max_entry_val_disp = self.max_entry_val
        #~ self.min_entry_val = 50
        #~ self.max_entry_val = 100
        #
        self.auto_update = False        # auto update deactivated at start
        self.auto_update_time = 15  #in seconds
        #
        self.table_entry_val = int( ( self.max_entry_val - self.min_entry_val ) / 50 )
        #
        #
        #
        self.suplot_left = .125
        self.suplot_right = .95
        self.suplot_top = .9
        self.suplot_bottom = .125
        #        
        self.plot_options_dict = {"X-Var": x_variable_list[0],
                                  "ticker_size": 'medium',
                                  "legend_size": 'large',
                                  "xaxis_size": 'large',
                                  "yaxis_size": 'large',
                                  }
        #

        # COLORING
        # http://scipy-lectures.github.io/intro/matplotlib/matplotlib.html#line-properties
        #
        self.plot_line_color_color = ['b','g','r','c','m','y']     # gray scale colors, hexmap colors, RGB tuples possible
        self.plot_alpha = list(np.linspace(0.,1.,21)[::-1])
        self.plot_line_color_grey = list(map(str,np.linspace(0.,1.,21)[::-1]))
        self.plot_line_color = iter(self.plot_line_color_color+self.plot_line_color_grey)
        self.plot_line_styles = ['-','--','..','-.','.',',','o','^','v','<','>','s','+','x','d','1','2','3','4','h','p','|','S','H']
        self.plot_line_widths = np.arange(1,13)
        self.plot_marker_styles = ['o','h','^','v','<','>','_','1','2','3','4','8','p','|','d',',','+','s','*','l','x','D','H','.','']
        self.plot_marker_styles_iterator = iter(self.plot_marker_styles)
        self.plot_marker_size = np.arange(1,13)
        self.plot_marker_every = [1,10,100,1000]
        #
        # plot
        self.plot_monitor_file( subplot, data_line, title_line, x_variable_list, y_variable_list, save_to_file)
        #
        return
    #
    def get_log_name(self,
                     subdirectory: str,
                     name_prefix: str,
                     ):
        """
        Returns the logfile name or error when file not found

        :Parameters:
            subdirectory : string
                directory containing monitoring data, absolute or relative
            name_prefix : string
                name prefix of monitoring file

        """
        #
        log_name = None
        if os.path.isfile(subdirectory + name_prefix+'.monitor.tmp.dat'):
            self.subdirectory = subdirectory
            self.unsteady = False
            log_name = name_prefix + '.monitor.tmp.dat'
            self.filename = log_name
            #
        #
        if os.path.isfile(subdirectory+name_prefix+'.monitor.pval.dat'):
            self.subdirectory = subdirectory
            self.unsteady = False
            log_name = name_prefix + '.monitor.pval.dat'
            self.filename = log_name
            #
        #
        if os.path.isfile(subdirectory+name_prefix+'.monitor.tmp.unsteady.dat'):
            self.subdirectory = subdirectory
            self.unsteady = True
            log_name = name_prefix + '.monitor.tmp.unsteady.dat'
            self.filename = log_name
            #
        #
        if os.path.isfile(subdirectory+name_prefix+'.monitor.pval.unsteady.dat'):
            self.subdirectory = subdirectory
            self.unsteady = True
            log_name = name_prefix + '.monitor.pval.unsteady.dat'
            self.filename = log_name
            #
        #
        if log_name is None:
            print("File with prefix '",subdirectory+name_prefix,"' not available. Please choose a file...")
            file_path = tkFileDialog.askopenfilename(initialdir=subdirectory,defaultextension=".dat",filetypes=[("data files", ".dat"),("all files", ".*")])            
            self.filename = file_path.split('/')[-1]
            self.subdirectory = '/'.join(file_path.split('/')[:-1])+'/'
            #
            #~ sys.exit("WARNING : File '"+subdirectory+name +".monitor.tmp.dat' or '"+subdirectory+name +".monitor.pval.dat'"+" not found. Process interrupted.")
        #
        return
    #
    def get_variables(self):
        """
        Returns a list of available variables and the min and max value of the x variable from the TAU monitoring file

        :Parameters:
            none
        """
        if os.path.isfile(self.subdirectory+self.filename):
            self.header, self.value_dict = ascii_read(self.subdirectory+self.filename ,
                                                        self.data_line,
                                                        self.title_line,
                                                        title_line_junk='#',
                                                        column_titles=True,
                                                        return_header=True,
                                                        check_iter_numbers=self.check_iter_numbers)
            #            
            self.available_variables = list(self.value_dict.keys())
            #
            self.min_entry_val = min(self.value_dict['"'+self.x_variable_list[0]+'"'])
            self.max_entry_val = max(self.value_dict['"'+self.x_variable_list[0]+'"'])
            
            #~ print "self.min_entry_val",self.min_entry_val
            #~ print "self.max_entry_val",self.max_entry_val
            return 0
        else:
            # return because file nonexistent anymore
            return -1                  
        
    #
    def plot_monitor_file(self,
                          subplot,
                          data_line: int = 1,
                          title_line: int = data_line-1,
                          x_variable_list: list = ('Inner-iter',),
                          y_variable_list: list = ('Residual',),
                          save_to_file = False):
        """
        Uses read data and adds it to the subplot.

        It additionally creates image files when save_to_file is set to True (obsolete) .

        :Parameters:

            subplot : matplotlib subplot instance
                the figure subplot
            data_line : integer
                line number where data starts
            title_line : integer
                line number of variable names
            x_variable_list :
                list of strings for x-variable
            y_variable_list : list of strings
                list of strings for y-variable
            save_to_file : bool
                switch to save file (deprecated)


        """
        self.plot_options_dict["X-Var"] = x_variable_list[0]
        #
        # ######################################
        #
        subdirectory = self.subdirectory
        name = self.filename
        y_variable_list.sort()
        #
        #~ look for file
        #~ log_name = self.get_log_name(subdirectory, name)
        #
        #~ get dictionary of all monitoring values
        #~ print 'plot_monitor_file'
        header = self.header
        value_dict = self.value_dict
        #~ header, value_dict = ascii_read(self.subdirectory+self.filename, \
                                                                        #~ data_line, \
                                                                        #~ title_line, \
                                                                        #~ title_line_junk='#', \
                                                                        #~ column_titles=True, \
                                                                        #~ return_header=True)
        #
        col_labels = []
        row_labels = []
        table_vals = []
        #
        #~ prepare variable list    
        y_variable_list_plot = list(y_variable_list)    
        x_variable_list_plot = list(x_variable_list)    
        for variable in range(len(y_variable_list_plot)):
            y_variable_list_plot[variable] = '"'+y_variable_list_plot[variable]+'"'
            #
        #
        for variable in range(len(x_variable_list_plot)):
            x_variable_list_plot[variable] = '"'+x_variable_list_plot[variable]+'"'
            #
        #
        if value_dict is not None and x_variable_list_plot[0] in value_dict:
            try:
                min_plot_index = np.where(value_dict[x_variable_list_plot[0]]==self.min_entry_val_disp)[0][0]
            except:
                min_plot_index=0
            try:
                max_plot_index = np.where(value_dict[x_variable_list_plot[0]]==self.max_entry_val_disp)[0][-1]
            except:
                max_plot_index = len(value_dict[x_variable_list_plot[0]])-1
            
            if min_plot_index>max_plot_index:
                min_plot_index=0
                max_plot_index = len(value_dict[x_variable_list_plot[0]])-1

            #~ raise  "find out where min and max entry value start and stop"
            #~ x = value_dict[x_variable_list_plot[0]][self.min_entry_val_disp-value_dict[x_variable_list_plot[0]][0]:self.max_entry_val_disp-value_dict[x_variable_list_plot[0]][0]]
            
            x = value_dict[x_variable_list_plot[0]][min_plot_index:max_plot_index]
            
            if self.plot_last_InnerIter: 
                
                            
                #get the last data values of each thistime (y)
                thistimes = list(set(x))
                thistimes.sort()
                x_indices = []
                for time in thistimes:          
                    indices = np.where(time==x)[0]
                    x_indices.append(indices[-1]) # use last entry
        else:
            sys.exit("WARNING : X-Variable "+x_variable_list_plot[0]+" not found in TAU monitoring file. Process interrupted. \n Check 'data_line' and 'title_line'")
        #
        # remove plot_options from dict if variable not available anymore
        #
        used_colors = []
        used_markers = []
        #
        
   
        
        for key in self.plot_options_dict.keys():
            
            if key not in y_variable_list_plot and key not in ["X-Var","ticker_size","legend_size","xaxis_size","yaxis_size"]:
                self.plot_options_dict.pop(key, None)
            if key in y_variable_list_plot:
                used_colors.append(self.plot_options_dict[key]['c'])
                used_markers.append(self.plot_options_dict[key]['m'])
                
        
        
        for variable in y_variable_list_plot:        
            if variable in value_dict:
                
                    
                    #~ alpha
                    #~ color
                    #~ linestyle
                    #~ linewidth 
                    #~ marker
                    #~ markeredgecolor
                    #~ markeredgewidth
                    #~ markerfacecolor
                    #~ markerfacecoloralt 
                    #~ markersize 
                    #~ markevery
                
                    if variable not in self.plot_options_dict:
                        self.plot_options_dict[variable] = {}
                        color = next(self.plot_line_color)
                        while color in used_colors:
                            color = next(self.plot_line_color)
                        alpha = self.plot_alpha[0]
                        ls = self.plot_line_styles[0]
                        lw = self.plot_line_widths[0]
                        #~ marker = next(self.plot_marker_styles)      #
                        
                        #~ while marker in used_markers:
                            #~ marker = next(self.plot_marker_styles)
                        marker = self.plot_marker_styles[-1]            # no marker as default
                        
                        ms = self.plot_marker_size[5]
                        me = self.plot_marker_every[0]
                        
                        label = variable.strip('"')
                        axislabel = variable.strip('"')
                        self.plot_options_dict[variable]['label'] = label
                        self.plot_options_dict[variable]['axis'] = axislabel
                        
                        self.plot_options_dict[variable]['c'] = color
                        used_colors.append(color)
                        
                        self.plot_options_dict[variable]['m'] = marker
                        used_markers.append(marker)
                        
                        self.plot_options_dict[variable]['alpha'] = alpha
                        self.plot_options_dict[variable]['ls'] = ls
                        self.plot_options_dict[variable]['lw'] = lw
                        self.plot_options_dict[variable]['ms'] = ms
                        self.plot_options_dict[variable]['me'] = me
                        
                        
                        
                    else:
                        if self.plot_options_dict[variable]['label'] == "":
                            color = next(self.plot_line_color)
                            while color in used_colors:
                                color = next(self.plot_line_color)
                            alpha = self.plot_alpha[0]
                            ls = self.plot_line_styles[0]
                            lw = self.plot_line_widths[0]
                            marker = self.plot_marker_styles[-1]            # no marker as default
                            #~ marker = next(self.plot_marker_styles)
                            #~ while marker in used_markers:
                                #~ marker = next(self.plot_marker_styles)
                            ms = self.plot_marker_size[5]
                            me = self.plot_marker_every[0]
                            
                            label = variable.strip('"')
                            axislabel = variable.strip('"')
                            self.plot_options_dict[variable]['label'] = label
                            self.plot_options_dict[variable]['axis'] = axislabel
                            
                            self.plot_options_dict[variable]['c'] = color
                            used_colors.append(color)
                            
                            self.plot_options_dict[variable]['m'] = marker
                            used_markers.append(marker)
                            
                            self.plot_options_dict[variable]['alpha'] = alpha
                            self.plot_options_dict[variable]['ls'] = ls
                            self.plot_options_dict[variable]['lw'] = lw
                            self.plot_options_dict[variable]['ms'] = ms
                            self.plot_options_dict[variable]['me'] = me
                        else:                            
                            label = self.plot_options_dict[variable]['label']
                            axislabel = self.plot_options_dict[variable]['axis']
                            
                            color = self.plot_options_dict[variable]['c']
                            marker = self.plot_options_dict[variable]['m']
                            
                            
                            alpha = float(self.plot_options_dict[variable]['alpha'])
                            ls = self.plot_options_dict[variable]['ls']
                            lw = float(self.plot_options_dict[variable]['lw'])
                            ms = float(self.plot_options_dict[variable]['ms'])
                            me = float(self.plot_options_dict[variable]['me'])
                        
                    if variable not in self.plot_options_dict:
                        self.plot_options_dict[variable] = {}
                    
                    
                    #~ y = value_dict[variable][self.min_entry_val_disp-value_dict[x_variable_list_plot[0]][0]:self.max_entry_val_disp-value_dict[x_variable_list_plot[0]][0]]
                    y = value_dict[variable][min_plot_index:max_plot_index]
                    
                    if self.plot_last_InnerIter:    # only plot last innerIteration
                        
                        plot_entity = subplot.plot(x[x_indices], y[x_indices], 
                                                    label=label,
                                                    c=color,
                                                    ls=ls,
                                                    lw=lw,
                                                    marker=marker,
                                                    ms=ms,
                                                    alpha=alpha,
                                                    markevery=me)
                                              
                        
                        
                    else:   # standard plot
                        subplot.plot(x, y, 
                                        label=label,
                                        c=color,
                                        ls=ls,
                                        lw=lw,
                                        marker=marker,
                                        ms=ms,
                                        alpha=alpha,
                                        markevery=me)
                    #
                    #~ row_labels.append(variable.strip('"'))       #working
                    row_labels.append(label) 
                    
                    if self.table_entry_val!=0:
                        if self.plt_table_data:
                            
                            #
                            val_list = []
                            #
                            for val in value_dict[variable][self.max_entry_val_disp-value_dict[x_variable_list_plot[0]][0]-self.table_entry_val:self.max_entry_val_disp-value_dict[x_variable_list_plot[0]][0]]:
                                val_list.append(val)
                            #
                            value = (sum(val_list)/self.table_entry_val)   
                            #~ max(val_list)
                            #~ min_valmin(val_list)
                            val_list = []
                            val_list.append(value)                        
                            #
                            table_vals.append(val_list)  
                            #
                    #
               
                    #
                #
            else:
                sys.exit("WARNING : Y-Variable %s not found in TAU monitoring file. Process interrupted. \n Check 'data_line' and 'title_line'" % variable)                
                #
            #
        col_labels.append('mean of last '+str(int(self.table_entry_val))+' iter: '+str(int(self.max_entry_val_disp-value_dict[x_variable_list_plot[0]][0]-self.table_entry_val))+'-'+str(int(self.max_entry_val_disp-value_dict[x_variable_list_plot[0]][0])) )
        #
        #~ legend font properties
        fontP = FontProperties()
        #~ fontP.set_size('medium')
        fontP.set_size(11)
        #
        #~ setup plot for file saving
        
        if save_to_file:
            pylab.grid(True)
            if self.subgrid:
                pylab.grid(True, which='minor',color='gray')                
                pylab.grid(True, which='major')    
            if self.x_scale_log:
                pylab.semilogx()
            if self.y_scale_log:
                pylab.semilogy()
            pylab.xlabel(x_variable_list[0].strip('"'), size = 'large' )
            pylab.ylabel(', '.join(y_variable_list).replace('"',''), size = 'large' )
            pylab.title(header[0].split(':')[1])                                     
            pylab.legend(y_variable_list,
                                loc = 'best',
                                #loc = 'lower left',
                                #~ bbox_to_anchor=(1,1),
                                prop = fontP,
                                numpoints = 4,
                                scatterpoints = 4,
                                markerscale = None,
                                fancybox= False,
                                shadow = False,
                                ncol = 1,
                                mode = None,
                                title = None
                                )
            #
            #~ subplot.gca().xaxis.set_major_formatter(pylab.ScalarFormatter(useMathText=True))   #useOffset=False, useMathText=True
            #~ subplot.gca().yaxis.set_major_formatter(pylab.ScalarFormatter(useMathText=True))
            #
        else:
            #
            # --- logarithmic scaling
            if self.x_scale_log:
                subplot.semilogx()
                if self.y_scale_log:
                    subplot.loglog()           
                    #
                #
            else:
                if self.y_scale_log:
                    subplot.semilogy()                          
                    #
                #
            #
            #~ subplot.set_xlabel(x_variable_list[0].strip('"'), size = 'large' )
            #~ subplot.set_ylabel(', '.join(y_variable_list).replace('"',''), size = 'large' )       
            # ##########################
            # Variable labels
            # ##########################
            
            xsize = self.plot_options_dict["xaxis_size"]
            
            subplot.set_xlabel(self.plot_options_dict["X-Var"], size = 'large' )
            
            
            y_axis_plot_list = []
            
            
            ysize = self.plot_options_dict["yaxis_size"]
            for variable in y_variable_list_plot:
                y_axis_plot_list.append(self.plot_options_dict[variable]["axis"])
           
            subplot.set_ylabel(', '.join(y_axis_plot_list).replace("'",""), size = 'large' )       
            
            #~ subplot.set_title(header[0].split(':')[1])                                    # TITLE
            if self.set_title:
                subplot.set_title(self.filename)                                    # TITLE
            
            #
            # --- grid lines            
            subplot.grid(True)
            if self.subgrid:
                subplot.grid(True, which='minor',color='gray')                
                subplot.grid(True, which='major')                        
                #
            #
            # --- plot table of selected values            
            if self.plt_table_data and len(table_vals)>0:    
                y_lim = subplot.get_ylim()
                if self.y_scale_log:                    
                    subplot.set_ylim(y_lim[0],y_lim[1]*10**np.ceil(1+(len(row_labels)/3)))
                else:                    
                    pass                    
                the_table = subplot.table(cellText = table_vals,
                                                          colWidths = [0.5],
                                                          rowLabels = row_labels,
                                                          colLabels = col_labels,
                                                          #loc='center right')                                                          
                                                            loc='upper center')
                                                            
                #~ the_table.auto_set_column_width(1)
                the_table.auto_set_font_size(True)
                
                #
            #
            
            label_plot_list = []
            for variable in y_variable_list_plot:
                label_plot_list.append(self.plot_options_dict[variable]["label"])
                
            
            
            
            leg = subplot.legend(label_plot_list,
                                    loc = 'best',
                                    prop = fontP,
                                    numpoints = 4,
                                    scatterpoints = 4,
                                    markerscale = None,
                                    fancybox = False,
                                    shadow = False,
                                    ncol = int(np.ceil((len(row_labels)/4.0))),
                                    mode = None,
                                    title = None
                                    )
            #
            legend_text_list = leg.get_texts()
            for iter1,variable in enumerate(y_variable_list_plot):
                legend_text_list[iter1].set_fontsize(self.plot_options_dict["legend_size"])
            #
            legend_line_list = leg.get_lines()
            for iter1,variable in enumerate(y_variable_list_plot):        
                legend_line_list[iter1].set_linewidth(self.plot_options_dict[variable]['lw'])  # the legend line width
            #
            # ################
            # set ticker type (documentation:http://matplotlib.org/1.2.0/api/ticker_api.html)
            #
            if self.ticker_type == 'no_offset':
                if self.x_scale_log:
                    #~ subplot.xaxis.set_major_formatter(pylab.LogFormatter(useOffset=False))   #useOffset=False, useMathText=True
                    pass
                else:
                    subplot.xaxis.set_major_formatter(pylab.ScalarFormatter(useOffset=False))   #useOffset=False, useMathText=True
                    #
                #
                if self.y_scale_log:
                    #~ subplot.yaxis.set_major_formatter(pylab.LogFormatter(useOffset=False))
                    pass
                else:
                    subplot.yaxis.set_major_formatter(pylab.ScalarFormatter(useOffset=False))
                    #
                #
            #
            elif self.ticker_type == 'with_offset':
                if self.x_scale_log:
                    #~ subplot.xaxis.set_major_formatter(pylab.LogFormatter(useOffset=True))   #useOffset=False, useMathText=True
                    pass
                else:
                    subplot.xaxis.set_major_formatter(pylab.ScalarFormatter(useOffset=True))   #useOffset=False, useMathText=True
                    #
                #
                if self.y_scale_log:
                    #~ subplot.yaxis.set_major_formatter(pylab.LogFormatter(useOffset=True))
                    pass
                else:
                    subplot.yaxis.set_major_formatter(pylab.ScalarFormatter(useOffset=True))
                    #
                #
            #
            elif self.ticker_type == 'math_offset':
                if self.x_scale_log:
                    #~ subplot.xaxis.set_major_formatter(pylab.LogFormatter(useMathText=True))   #useOffset=False, useMathText=True
                    pass
                    #
                #
                else:
                    subplot.xaxis.set_major_formatter(pylab.ScalarFormatter(useMathText=True))   #useOffset=False, useMathText=True
                    #
                #
                if self.y_scale_log:
                    #~ subplot.yaxis.set_major_formatter(pylab.LogFormatter(useMathText=True))
                    pass
                else:
                    subplot.yaxis.set_major_formatter(pylab.ScalarFormatter(useMathText=True))
                    #
                #
            else:
                sys.exit("TICKER TYPE NOT SUPPORTED: "+self.ticker_type+"use one of 'no_offset'  ,  'with_offset' ,  'math_offset' ")
            #         
            subplot.tick_params(axis='both', which='major', labelsize = self.plot_options_dict["ticker_size"])
            subplot.tick_params(axis='both', which='minor', labelsize = self.plot_options_dict["ticker_size"])
            #
        #
        #~ save to file
        """
        if save_to_file:
            for format in formats:
                #
                #~ check if file exists - increase numbering              
                fig_name = header[0].split(':')[1].rstrip('\n').lstrip(' ./')
                #
                file_numbering = 1
                for file in os.listdir("./") :
                    if file.startswith(fig_name):                                                
                        if  int( file.split('_')[-1].split('.')[0] ) >= file_numbering:                          
                            file_numbering = int( file.split('_')[-1].split('.')[0] ) + 1
                        #
                    #
                #        
                #~ number incease
                fig_name = fig_name+'_'+str(file_numbering)+'.'+format
                pylab.savefig(fig_name,
                                        dpi = 600,  
                                        facecolor='w', 
                                        edgecolor='w',  
                                        format=format,
                                        bbox_inches='tight', 
                                        pad_inches=0.1)        
                #
            pylab.close()
            #
        """
        #
        #~ print ' - Function plot_monitor_file exited successfully --------------------- '
        #
    #
    def replot(self, subplot, data_line, title_line, x_variable_list, y_variable_list, save_to_file):
        """
        Executes plot_monitor_file method

        :Parameters:
            subplot : matplotlib subplot instance
                the figure subplot
            data_line : integer
                line number where data starts
            title_line : integer
                line number of variable names
            x_variable_list :
                list of strings for x-variable
            y_variable_list : list of strings
                list of strings for y-variable
            save_to_file : bool
                switch to save file (deprecated)

        """
        #
        self.plot_monitor_file(subplot, data_line, title_line, x_variable_list, y_variable_list,save_to_file)
        #
    #
    def add_TAU_status(self,fig):
        """
        Adds the current TAU solver status to the canvas.

        :Parameters:
            fig - matplotlib figure instance
                the figure
        """
        #
        if self.filename.split('.')[-2] == 'pval':
            status_text = 'status: run completed'            
        elif self.filename.split('.')[-2] == 'tmp':
            status_text = 'status: run active'
        elif self.filename.split('.')[-3] == 'pval':
            status_text = 'status: run completed'
        elif self.filename.split('.')[-3] == 'tmp':
            status_text = 'status: run active'
        else:
            status_text = 'status: unknown'
            #
        #
        #~ TAU run status text
        fig.text(0.8, 0.015, status_text,
                        fontsize='small', color='black',
                        alpha=0.4)
            #~ ha='right', va='bottom',
            #
        #
        #~ IFL text
        fig.text(0.01, 0.015, "IFL-TU Braunschweig",
                        fontsize='small', color='black',
                        alpha=0.3)
        #
    #
#
# ##########################################################################################################
# ##########################################################################################################
#
#
def create_plot(subdirectory,
                name_prefix,
                data_line,
                title_line,
                x_variable_list,
                y_variable_list,
                check_iter_numbers,
                save_to_file = False
                ):
    """
    Creates a Tkinter GUI for TAU monitoring file data

    :Parameters:
            subdirectory : string
                directory containing monitoring data, absolute or relative
            name_prefix : string
                name prefix of monitoring file
            data_line : integer
                line number where data starts
            title_line : integer
                line number of variable names
            x_variable_list :
                list of strings for x-variable
            y_variable_list : list of strings
                list of strings for y-variable
            check_iter_numbers : bool
                check ascending order of iteration numbers
            save_to_file : bool
                switch to save file (deprecated)


    """
    #
    #~ create tk instance
    root = tk.Tk()
    root.option_add("*font", ("Arial", 8, "normal"))
    #~ root.configure(background='white')
    #~ root.minsize(width=1000,height=800)
    root.wm_title("TAU plot monitoring file data - TAUmonplot")
    
    
    #
    #~ create figure instance    
    fig = Figure(facecolor='white')
    #~ fig.set_size_inches(7,5)
    subplot = fig.add_subplot(111)  
      
    #
    #~ create plot   
    plot_creator = PlotCreator(subplot,
                               subdirectory,
                               name_prefix,
                               data_line,
                               title_line,
                               x_variable_list,
                               y_variable_list,
                               check_iter_numbers,
                               save_to_file)
    plot_creator.add_TAU_status(fig)
    plot_creator.fig = fig
    plot_creator.fig.subplots_adjust(bottom=float(plot_creator.suplot_bottom),
                                     left=float(plot_creator.suplot_left),
                                     right=float(plot_creator.suplot_right),
                                     top=float(plot_creator.suplot_top) )
    
    #~ available_variables, plot_creator.min_entry_val, plot_creator.max_entry_val = get_variables(plot_creator,plot_creator.subdirectory, plot_creator.filename, data_line, title_line, x_variable_list)
    available_variables = plot_creator.available_variables
    #
    #~ create canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #
    #~ create toolbar
    toolbar = NavigationToolbar2Tk( canvas, root )
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #
       
    #
    #
    #~ toolbar functions and buttons
    def _quit():
        """ 
        Button command to close TK gui
        """
        #
        if tkMessageBox.askokcancel('Quit?' , 'Do you want to quit TAU monitoring plot script?' ):
            root.quit()                # stops mainloop
            root.destroy()          # this is necessary on Windows to prevent
                                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        else:
            pass
            #
        #
    #
    def _help():
        """ 
        Button command to open help window
        """
        #
        help_window.deiconify()
        #
    #
    def _save_help():
        help_window.withdraw()
    #
    help_window = tk.Toplevel(root)
    myLabel = tk.Label(help_window, text='TAU plot monitoring file data (taumonplot) - Help')
    myLabel.pack()
    #
    help_text = tk.Text(help_window)
    #
    help_file_text = """ 
    #--------------------------------------------------------------------------
    #   script taumonplot.py
    #--------------------------------------------------------------------------
    # Contents:
    #   1. LICENSE INFORMATION
    #   2. PROGRAM MANUAL
    #
    #--------------------------------------------------------------------------
    # 1. LICENSE INFORMATION
    #--------------------------------------------------------------------------
    # Copyright (c) 2012, Institute of Aircraft Design and Lightweight Structures (IFL),
    # TU Braunschweig, Hermann-Blenk-Str. 35, 38108 Braunschweig.
    # All rights reserved.
    #
    # Redistribution and use in source and binary forms, with or without
    # modification, are permitted provided that the following conditions are met:
    #    * Redistributions of source code must retain the above copyright
    #      notice, this list of conditions and the following disclaimer.
    #    * Redistributions in binary form must reproduce the above copyright
    #      notice, this list of conditions and the following disclaimer in the
    #      documentation and/or other materials provided with the distribution.
    #    * Neither the name of the IFL, TU Braunschweig nor the
    #      names of its contributors may be used to endorse or promote products
    #      derived from this software without specific prior written permission.
    #
    # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    # ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    # WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    # DISCLAIMED. IN NO EVENT SHALL IFL, TU Braunschweig BE LIABLE FOR ANY
    # DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    # (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    # LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
    # ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    # SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    #
    #
    #--------------------------------------------------------------------------
    # Description: Python module using matplotlib to plot TAU monitoring data
    #--------------------------------------------------------------------------
    #
    # This program is written in Python <= 2.7 under Linux-Ubuntu 10.04, it has been tested under MS Windows 7
    #
    # Author: Kay Sommerwerk
    # e-mail: k.sommerwerk@tu-braunschweig.de
    # Date: see version history
    # Revision: see version history
    #
    # This software is provided under the assumption that major improvements of this software 
    # will be made available to the IFL
    #
    #--------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #   2. PROGRAM MANUAL
    #---------------------------------------------------------------------------
    #   1. declare subdirectory and name_prefix of tau monitoring file (without the ending '.monitor.tmp.dat', 
    #                                       '.monitor.pval.dat', '.monitor.tmp.unsteady.dat', '.monitor.pval.unsteady.dat')
    #       1.1 not necessarily needed as monitoring file can be choosen through file browser if file not found
    #   2. verify that data_line and title_line are correct
    #   3. run program: variables to display can be choosen in the gui
    #       (3.1) variables to display automatically at startup may be changed with the variables x_variable_list and y_variable_list
    #   4. Button explanation
    #       row 1: Basic display functions
    #           Quit : closes the program
    #           Help : open license and manual
    #           (Save .png:)  creates a png image of the set up plot (takes some time to replot data)
    #                   can be saved using the tkinter gui
    #           Load : opens another Tau monitoring file
    #           Title : toggles title display of monitoring file
    #           Subgrid : toggles the display of subgrid lines
    #           LIN/LOG x/y : toggles the logarithmic or linear axis 
    #           Offset : toggles number offset of axis ticks (documentation:http://matplotlib.org/1.2.0/api/ticker_api.html)
    #           Update : updates the data from the monitoring file (new data is displayed if monitoring file has received 
    #                                       an update from TAU)
    #       row 2: Auto Update 
    #           Set: sets the desired update interval in seconds
    #           auto update on/off switch
    #   
    #       row 3: Iteration interval display options
    #           reset : resets the minimum and maximum values to display to the complete range
    #           set min : sets the minimum Iteration number to display (entered in the left box)
    #           set max : sets the maximum Iteration number to display (entered in the right box)
    #       row 4: Data table display options
    #           toggle data table (on/off) : toggle the display of a data table on the plot with mean values of the last iterations 
    #                                       set by 'set interval' (standard values is 1/50th of Iteration range)
    #           set interval : sets the range of last iterations to include in the mean value
    #           Tick (offset,no offset, math): sets the axis ticks offset type
    #       row 5: Variable choice options
    #           X-Variable : one choice of variable for the abcissa
    #           Y-Variables : multiple choice of variables for the ordinate
    #      
    #---------------------------------------------------------------------------
    """
    #
    help_text.insert(tk.INSERT, help_file_text)
    help_text.config(width=100)
    help_text.configure( state= "disabled" )
    scrollbar1 = tk.Scrollbar(help_window)
    #~ scrollbar2 = Tk.Scrollbar(help_window)
    scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
    #~ scrollbar2.pack(side=Tk.BOTTOM, fill=Tk.X)
    help_text.pack(side=tk.LEFT, fill=tk.Y)
    #~ help_text.pack(side=Tk.BOTTOM, fill=Tk.X)
    scrollbar1.config(command=help_text.yview)
    #~ scrollbar2.config(command=help_text.xview)
    help_text.config(yscrollcommand=scrollbar1.set)    
    #~ help_text.config(xscrollcommand=scrollbar2.set)    
    #
    help_window.protocol("WM_DELETE_WINDOW", _save_help)
    #
    help_window.withdraw()
    ##############################################
    #
    #file not available pop up window
    #
    def _fileAvail():
        """ 
        Command to open file not available window
        """
        #
        fileAvail_window.deiconify()
        #
    #
    def _save_fileAvail():
        fileAvail_window.withdraw()
    #
    #
    fileAvail_window = tk.Toplevel(root)
    fileAvail_window.config(width=80)   #,height=50)
    top_frame_fileAvail_window = tk.Frame(fileAvail_window, bd=1, relief=tk.SUNKEN)
    fileAvail_text = '  File not found:\n  '+ plot_creator.subdirectory + plot_creator.filename +'\n  Probably TAU finished and renamed the file to pval.dat\n  Press "Load" to load another file. Press "Cancel" to return without change.'
    #~ myLabel = Tk.Label(top_frame_fileAvail_window, text='File not available')
    myLabel = tk.Label(top_frame_fileAvail_window, text=fileAvail_text)
    myLabel.pack()
    #
    #~ fileAvail_text_widget = Tk.Text(top_frame_fileAvail_window)
    #    
    #
    #~ fileAvail_text_widget.insert(Tk.INSERT,fileAvail_text)
    #~ fileAvail_text_widget.config(height=5)
    #~ fileAvail_text_widget.configure( state= "disabled" )    
    #~ fileAvail_text_widget.pack() #side=Tk.LEFT, fill=Tk.Y)
    # add load and cancel button
    bot_frame_fileAvail_window = tk.Frame(fileAvail_window, bd=1, relief=tk.SUNKEN)
    #    
    top_frame_fileAvail_window.pack(side=tk.TOP)
    top_frame_fileAvail_window.config(height=0)
    bot_frame_fileAvail_window.pack(side=tk.BOTTOM)
    bot_frame_fileAvail_window.config(height=0)
    #    
    fileAvail_window.protocol("WM_DELETE_WINDOW", _save_fileAvail)
    #
    fileAvail_window.withdraw()
    #
    ##############################################
    def _replot():
        """ 
        Button command to replot figure
        """      
        #        
        
        plot_creator.fig.subplots_adjust(bottom=float(plot_creator.suplot_bottom),
                                         left=float(plot_creator.suplot_left),
                                         right=float(plot_creator.suplot_right),
                                         top=float(plot_creator.suplot_top) )
        #
        y_variable_list = []
        for ix, item in enumerate(cb):
            if cb_v[ix].get():
                y_variable_list.append(item['text'].strip('"'))
        x_variable_list[0] = v.get().strip('"')
        fig.clear()
        subplot = fig.add_subplot(111)
        if len(y_variable_list) > 0:            
            #
            #~ print "plot_creator.replot"
            plot_creator.replot(subplot,data_line, title_line,x_variable_list,y_variable_list,save_to_file)
            plot_creator.add_TAU_status(fig)
        canvas.draw()
        
        #
    #
    def _reload():
        """ 
        Button command to reload and replot figure
        """
        #
        
        return_val = plot_creator.get_variables()
        if return_val!=0:
            # file not available - open pop up dialogue to ask for open file or cancel
            #~ print 'File not available'
            if plot_creator.auto_update:
                plot_creator.auto_update=False
                auto_switch.set(0)        
                # reset filename to *.monitot.pval.dat
                plot_creator.get_log_name(plot_creator.subdirectory, plot_creator.name_prefix)
                _reload()        
                #pop up run finished?
                
            else:
                plot_creator.get_log_name(plot_creator.subdirectory, plot_creator.name_prefix)
                _reload()        
            #
            #_fileAvail()
            return        
        #
        _update_range()
        #
        fig.clear()
        y_variable_list = []
        for ix, item in enumerate(cb):
            if cb_v[ix].get():
                y_variable_list.append(item['text'].strip('"'))
        x_variable_list[0] = v.get().strip('"')            
        #
        subplot = fig.add_subplot(111)
        #
        if len(y_variable_list) > 0:            
            plot_creator.replot(subplot,data_line, title_line,x_variable_list,y_variable_list,save_to_file)
            plot_creator.add_TAU_status(fig)
            #
        canvas.draw()
        #
    #    
    def _replot_with_last_InnerIter():
        """
        Button command to switch the values to plot only the last InnerIter
        """
        #~ print "_replot_with_last_InnerIter"
        
        if plot_creator.plot_last_InnerIter:
            plot_creator.plot_last_InnerIter = False
        else:
            plot_creator.plot_last_InnerIter = True
        _replot()
        #
    #    
    def _update():
        """
        Button command to reload the figure
        """
        #
        update_button.configure(text="..Updating..", width=8)
        _reload()  
        update_button.configure(text="   Update   ", width=8)
        #
    #
    def _update_range():
        """
        Button command to update data range
        """
        #        
        min_entry_var.set(float(plot_creator.min_entry_val))
        max_entry_var.set(float(plot_creator.max_entry_val))
        #
        #plot_creator.min_entry_val_disp = plot_creator.min_entry_val
        plot_creator.min_entry_val_disp =  float(entry_widget_min.get())
        #
        plot_creator.max_entry_val_disp = plot_creator.max_entry_val
        entry_widget_min.delete(0, tk.END)
        #
        #~ entry_widget_min.insert(0, str(min_entry_var.get()))
        
        entry_widget_min.insert(0, str(plot_creator.min_entry_val_disp))
        #
        entry_widget_max.delete(0, tk.END)
        entry_widget_max.insert(0, str(max_entry_var.get()))
        #
        if x_variable_list[0] == 'Inner-iter':
            Var_text = "Iter"
            entry_widget_min_label.config(text = Var_text+" (min "+str(min_entry_var.get())+")")
            entry_widget_max_label.config(text = Var_text+" (max "+str(max_entry_var.get())+")")
        elif x_variable_list[0] == 'thistime':
            Var_text = "Time"
            entry_widget_min_label.config(text = Var_text+" (min "+str(min_entry_var.get())+")")
            entry_widget_max_label.config(text = Var_text+" (max "+str(max_entry_var.get())+")")
        #~ else:
            #~ var_text = "Val"
        
        
        #
        #        
    #
    def _save_png():
        """
        Button command to save a png file
        """
        #
        y_variable_list = []
        for ix, item in enumerate(cb):
            if cb_v[ix].get():
                y_variable_list.append(item['text'].strip('"'))
        x_variable_list[0] = v.get().strip('"')   
        
        fig.clear()
        subplot = fig.add_subplot(111)
        if len(y_variable_list) > 0:            
            #
            plot_creator.replot(subplot,data_line, title_line,x_variable_list,y_variable_list,True)
        
        fig.clear()
        subplot = fig.add_subplot(111)
        if len(y_variable_list) > 0:            
            #
            plot_creator.replot(subplot,data_line, title_line,x_variable_list,y_variable_list,False)
        
        plot_creator.add_TAU_status(fig)
        print('---- THIS TK WARNING MAY BE IGNORED:')
        tk.mainloop()
    #   
    def _log_y():
        """
        Button command to toggle logarithmic scaling of x-axis
        """
        #
        if plot_creator.y_scale_log:
            plot_creator.y_scale_log = False
        else:
            plot_creator.y_scale_log = True
            #
        #
        _replot()
        #
    #
    def _log_x():
        """
        Button command to toggle logarithmic scaling of y axis
        """
        #
        if plot_creator.x_scale_log:
            plot_creator.x_scale_log = False
        else:
            plot_creator.x_scale_log = True
        #
        _replot()
        #
    #
    def _toggle_sub_grid():
        """
        Button command to toggle subgrid of plots
        """
        #
        if plot_creator.subgrid:
            plot_creator.subgrid = False
        else:
            plot_creator.subgrid = True
        #
        _replot()
        #
    #
    def _load_file():
        """
        Button command to load another file
        """
        #        
        file_path = tkFileDialog.askopenfilename(initialdir=subdirectory,defaultextension=".dat",filetypes=[("data files", ".dat"),("all files", ".*")])          
        #
        if not file_path == '' and  not file_path == ():         
            plot_creator.filename = file_path.split('/')[-1]
            plot_creator.subdirectory = '/'.join(file_path.split('/')[:-1])+'/'
            fileAvail_window.withdraw()
            _reload()          
        #
        
    #
    def _title():
        """
        Button command to toggle filename in title
        """
        #
        if plot_creator.set_title:
            plot_creator.set_title = False
        else:
            plot_creator.set_title = True
        #
        _replot()
        #
    #
    #~ -------------------------- TICKER BUTTONS    
    def _switch_ticker():
        """
        Button command to switch tickers on axes

        Switch between:
        - with numerical offset
        - no numerical offset
        - with mathtext
        """
        #
        if plot_creator.ticker_type == 'no_offset':
            plot_creator.ticker_type = 'with_offset'
            button_ticker.configure( text = 'Offset on')
        elif plot_creator.ticker_type == 'with_offset':
            plot_creator.ticker_type = 'math_offset'
            button_ticker.configure( text = 'Offset math')
        else:
            plot_creator.ticker_type = 'no_offset'
            button_ticker.configure( text = 'Offset none')
            #
        #
        _replot()
        #
    #
    # file not available buttons
    #~ place buttons
    load_button_file_avail = tk.Button(master=bot_frame_fileAvail_window, text='Load', command=_load_file)
    load_button_file_avail.pack(side=tk.LEFT)
    cancel_button = tk.Button(master=bot_frame_fileAvail_window, text='Cancel', command=_save_fileAvail)
    cancel_button.pack(side=tk.LEFT)
    
    #
    button_frame = tk.Frame(root, width=50, height=100)
    button_frame.pack()
    
    canvas_button_frame = tk.Canvas(button_frame)
    canvas_button_frame.pack()
    # ######################################
    #~ # TOP FRAME SCROLLBAR
    #~ scrollbar0y = Tk.Scrollbar(canvas_button_frame,orient="vertical",command=canvas_button_frame.yview)
    #~ canvas_button_frame.configure(yscrollcommand=scrollbar0y.set) 
   
    #~ scrollbar0y.pack(side="right",fill="y")        
        
    # ######################################
    top_frame = tk.Frame(canvas_button_frame, bd=1, relief=tk.SUNKEN)
    
    #
    # ######################################
    #~ PLACE BUTTONS
    quit_button = tk.Button(master=top_frame, text='Quit', command=_quit)
    quit_button.pack(side=tk.LEFT)
    # createToolTip(quit_button,"Quit taumonplot")
    #
    help_button = tk.Button(master=top_frame, text='Help', command=_help)
    help_button.pack(side=tk.LEFT)
    # createToolTip(quit_button,"Quit taumonplot")
    #
    #~ button = Tk.Button(master=top_frame, text='Save .png', command=_save_png)
    #~ button.pack(side=Tk.LEFT) 
    #
    load_button = tk.Button(master=top_frame, text='Load', command=_load_file)
    load_button.pack(side=tk.LEFT)
    create_tool_tip(load_button, "Load new TAU monitoring file")
    #    
    button_ticker = tk.Button(master = top_frame, text ='Offset none', command = _switch_ticker)
    button_ticker.pack(side = tk.LEFT)
    create_tool_tip(button_ticker, "Ticker offset (on/off/math)")
    #
    update_button = tk.Button(master=top_frame, text='   Update   ', width=8, command=_update)
    update_button.pack(side=tk.RIGHT)
    create_tool_tip(update_button, "Manual update of monitoring file data")
    #
    
    #
    #  BUTTONS changed to Checkbuttons
    """
    scalex_button = Tk.Button(master=top_frame, text='LIN/LOG x', command=_log_x)
    scalex_button.pack(side=Tk.RIGHT)
    createToolTip(scalex_button,"Switch between linear and logarithmic scaling on X-Axis")
    #
    scaley_button = Tk.Button(master=top_frame, text='LIN/LOG y', command=_log_y)
    scaley_button.pack(side=Tk.RIGHT)        
    createToolTip(scaley_button,"Switch between linear and logarithmic scaling on Y-Axis")
    #
    grid_button = Tk.Button(master=top_frame, text='Subgrid', command=_toggle_sub_grid)
    grid_button.pack(side=Tk.RIGHT)
    createToolTip(grid_button,"Toggle subgrid on/off")
    #
    title_button = Tk.Button(master=top_frame, text='Title', command=_title)
    title_button.pack(side=Tk.RIGHT)      
    createToolTip(title_button,"Toggles title on off taumonplot")
    #
    """
    #
    scalex_button = tk.Checkbutton(master=top_frame, text='LIN/LOG x', command=_log_x)
    scalex_button.pack(side=tk.RIGHT)
    create_tool_tip(scalex_button, "Switch between linear and logarithmic scaling on X-Axis")
    #
    if plot_creator.x_scale_log == False:
        scalex_button.deselect()
    else:
        scalex_button.select()
    #
    scaley_button = tk.Checkbutton(master=top_frame, text='LIN/LOG y', command=_log_y)
    scaley_button.pack(side=tk.RIGHT)
    create_tool_tip(scaley_button, "Switch between linear and logarithmic scaling on Y-Axis")
    if plot_creator.y_scale_log == False:
        scaley_button.deselect()
    else:
        scaley_button.select()
    #
    grid_button = tk.Checkbutton(master=top_frame, text='Subgrid', command=_toggle_sub_grid)
    grid_button.pack(side=tk.RIGHT)
    create_tool_tip(grid_button, "Toggle subgrid on/off")
    #
    if plot_creator.subgrid == False:
        grid_button.deselect()
    else:
        grid_button.select()
    title_button = tk.Checkbutton(master=top_frame, text='Title', command=_title)
    title_button.pack(side=tk.RIGHT)
    create_tool_tip(title_button, "Toggles title on off taumonplot")
    #
    
    if plot_creator.set_title == False:
        title_button.deselect()
    else:
        title_button.select()
    
    
    #
    # ######################################
    #side=Tk.RIGHT)
    top_frame.pack(side=tk.TOP)
    #~ top_frame.config(height=0)
    
    
    
    
    #
    # ######################################
    # #
    #~ -------------------------- AUTO UPDATE
    #
    auto_frame = tk.Frame(canvas_button_frame, bd=1, relief=tk.SUNKEN)
    auto_frame.pack()
    #
    #
    def _set_auto_time():
        """
        Button command to set time of auto update
        """
        #                      
        plot_creator.auto_update_time_disp = int(entry_widget_auto_update.get())
        auto_update_time.set(int(plot_creator.auto_update_time_disp))
        plot_creator.auto_update_time = plot_creator.auto_update_time_disp
        entry_widget_auto_update.delete(0, tk.END)
        entry_widget_auto_update.insert(0, str(auto_update_time.get()))       
        # print plot_creator.auto_update_time
        #
    #
    #
    auto_update_time = tk.IntVar(value = int(plot_creator.auto_update_time))
    auto_update_time_label = tk.Label(auto_frame, text="AUTO UPDATE:")
    auto_update_time_label.pack(side=tk.LEFT)
    entry_widget_auto_update = tk.Entry(master=auto_frame, width=5)
    entry_widget_auto_update.pack(side=tk.LEFT)
    create_tool_tip(entry_widget_auto_update, "Automatic update interval in seconds. \nNeeds to be set with 'Set'.")
    #
    auto_update_time_label_S = tk.Label(auto_frame, text="(s)")
    auto_update_time_label_S.pack(side=tk.LEFT)
    entry_widget_auto_update.delete(0, tk.END)
    entry_widget_auto_update.insert(0, str(int(plot_creator.auto_update_time)))
    #
    button_auto_update = tk.Button(master=auto_frame, text='Set', command=_set_auto_time)
    button_auto_update.pack(side=tk.LEFT)
    create_tool_tip(button_auto_update, "Set update interval")
    #    
    def _auto_updater():
        """
        Function that executes the update command and waits for set number of seconds
        """
        while plot_creator.auto_update:
            time.sleep(plot_creator.auto_update_time)
            print('auto updating...')
            _update()                        
        return
    #
    def _auto_update():
        """
        Auto update command. Switches between manual and auto update. Starts new thread to autoupdate
        """
        import threading
        if  plot_creator.auto_update:
            plot_creator.auto_update = False
        else:
            plot_creator.auto_update = True
            thread = threading.Thread(target=_auto_updater, daemon=True)  # auto terminate with main program
            thread.start()
        return
        #
    #
    auto_switch = tk.IntVar()
    auto_button = tk.Checkbutton(auto_frame, text="Auto", variable=auto_switch, command=_auto_update)
    auto_button.pack()
    auto_switch.set(0)   
    create_tool_tip(auto_button, "Toggles automatic update")
    #
    #~ -------------------------- ENTRY WIDGETS
    #
    def _set_min():
        """
        Button command to set minimum x value to plot
        """
        #
        #~ plot_creator.min_entry_val_disp = int(entry_widget_min.get())
        plot_creator.min_entry_val_disp = float(entry_widget_min.get())
        #~ entry_widget_min.insert(0, str(plot_creator.min_entry_val))
        #
        _replot()
        #
    #
    def _set_max():
        """
        Button command to set maximum x value to plot
        """
        #   
        #~ plot_creator.max_entry_val_disp = int(entry_widget_max.get() )
        plot_creator.max_entry_val_disp = float(entry_widget_max.get() )
        #~ entry_widget_min.insert(0, str(plot_creator.max_entry_val))
        #
        _replot()
        #
        #~ available_variables, min_entry_val, max_entry_val = get_variables(plot_creator,plot_creator.subdirectory, plot_creator.filename, data_line, title_line, x_variable_list)
    #
    def _reset():
        """
        Button command to reset values to plot
        """
        #
        
        #~ available_variables, plot_creator.min_entry_val, plot_creator.max_entry_val = get_variables(plot_creator,plot_creator.subdirectory, plot_creator.filename, data_line, title_line, x_variable_list)
        #~ plot_creator.get_variables()
        
        min_entry_var.set(float(plot_creator.min_entry_val))
        max_entry_var.set(float(plot_creator.max_entry_val))
        plot_creator.min_entry_val_disp = plot_creator.min_entry_val
        plot_creator.max_entry_val_disp = plot_creator.max_entry_val
        entry_widget_min.delete(0, tk.END)
        entry_widget_min.insert(0, str(min_entry_var.get()))
        entry_widget_max.delete(0, tk.END)
        entry_widget_max.insert(0, str(max_entry_var.get()))
        #
        var_text = ""
        if x_variable_list[0] == 'Inner-iter':
            var_text = "Iter"
            entry_widget_min_label.config(text = var_text+" (min "+str(min_entry_var.get())+")")
            entry_widget_max_label.config(text = var_text+" (max "+str(max_entry_var.get())+")")
        elif x_variable_list[0] == 'thistime':
            var_text = "Time"
            entry_widget_min_label.config(text = var_text+" (min "+str(min_entry_var.get())+")")
            entry_widget_max_label.config(text = var_text+" (max "+str(max_entry_var.get())+")")
        #~ else:
            #~ var_text = "Val"
        
        entry_widget_min_label.config(text = var_text+" (min "+str(min_entry_var.get())+")")
        entry_widget_max_label.config(text = var_text+" (max "+str(max_entry_var.get())+")")
        #
        _replot()
        #
    #
    entry_widget_frame = tk.Frame(canvas_button_frame, bd=1, relief=tk.SUNKEN)
    entry_widget_frame.pack()
    #
    WidgetState = Literal["normal", "active", "disabled"]
    #
    if x_variable_list[0] == 'Inner-iter':
       widget_state: WidgetState = "normal"
    else:
       widget_state: WidgetState  = "disabled"
       #
    if x_variable_list[0] == 'thistime':
       widget_state_last_iter: WidgetState  = "normal"
    else:
       widget_state_last_iter: WidgetState  = "disabled"
       #
    #
    #    
    interval_label = tk.Label(entry_widget_frame, text="INTERVAL:")
    interval_label.pack(side=tk.LEFT)
    #
    button_reset = tk.Button(master=entry_widget_frame, text='Reset', command=_reset)
    button_reset.pack(side=tk.LEFT)
    create_tool_tip(button_reset, "Resets iteration interval on display \nto all available iterations steps")
    #
    #~ min_entry_var = Tk.IntVar(value = int(plot_creator.min_entry_val))
    min_entry_var = tk.DoubleVar(value = float(plot_creator.min_entry_val))
    entry_widget_min_label = tk.Label(entry_widget_frame, text="Iter (min " + str(min_entry_var.get()) + ")")
    entry_widget_min_label.pack(side=tk.LEFT)
    entry_widget_min = tk.Entry(master=entry_widget_frame, state=widget_state, width=10)
    entry_widget_min.pack(side=tk.LEFT)
    create_tool_tip(entry_widget_min, "MINIMUM iteration number to display")
    #
    button_min = tk.Button(master=entry_widget_frame, text='Set', command=_set_min)
    button_min.pack(side=tk.LEFT)
    create_tool_tip(button_min, "Set MINIMUM iteration number")
    #
    #~ max_entry_var = Tk.IntVar(value = int(plot_creator.max_entry_val))
    max_entry_var = tk.DoubleVar(value = float(plot_creator.max_entry_val))
    entry_widget_max_label = tk.Label(entry_widget_frame, text="Iter (max " + str(max_entry_var.get()) + ")")
    entry_widget_max_label.pack(side=tk.LEFT)
    entry_widget_max = tk.Entry(master=entry_widget_frame, state=widget_state, width=10)
    entry_widget_max.pack(side=tk.LEFT)
    create_tool_tip(entry_widget_min, "MAXIMUM iteration number to display")
    #
    button_max = tk.Button(master=entry_widget_frame, text='Set', command=_set_max)
    button_max.pack(side=tk.LEFT)
    create_tool_tip(button_min, "Set MAXIMUM iteration number")
    #
    button_min.configure(state=widget_state)
    button_min.update()
    button_max.configure(state=widget_state)
    button_max.update()   
    button_reset.configure(state=widget_state)
    button_reset.update()   
    #
    #
    #~ --------------------------  DATA TABLE
    #    
    table_data_frame = tk.Frame(canvas_button_frame, bd=1) #, relief=Tk.SUNKEN)
    table_data_frame.pack()
    
    table_data_frame1 = tk.Frame(table_data_frame, bd=1, relief=tk.SUNKEN)
    table_data_frame1.pack(side=tk.LEFT)
    #
    
    table_data_frame2 = tk.Frame(table_data_frame, bd=1, relief=tk.SUNKEN)
    table_data_frame2.pack(side=tk.RIGHT)
    #
    table_data_label = tk.Label(table_data_frame1, text="DATA TABLE:")
    table_data_label.pack(side=tk.LEFT)
    #
    def _data_table():
        """
        Button command to enable or disable plot of data table
        """
        #
        if plot_creator.plt_table_data:
            plot_creator.plt_table_data = False
            # button_data_table.configure( text = '(on)')            
        else:
            plot_creator.plt_table_data = True
            # button_data_table.configure( text = '(off)')
        #        
        #~ print plot_creator.plt_table_data
        _replot()
        #
    #        
    def _set_table_interval():
        """
        Button command to set range of Iterations to use for mean data table
        """
        #                   
        plot_creator.table_entry_val = float(entry_widget_table.get() )
        #        
        _replot()
        #
    #    
    #~ if plot_creator.plt_table_data:
        #~ button_data_table_text = '(off)'
    #~ else:
        #~ button_data_table_text = '(on)'
        #
    #
    # button_data_table = Tk.Button(master = table_data_frame, text = button_data_table_text, command = _data_table)
    # button_data_table.pack(side = Tk.LEFT) 
    #   
    #
    entry_widget_table_label = tk.Label(table_data_frame1, text ="mean of IterNb:").pack(side = tk.LEFT)
    entry_widget_table = tk.Entry(master=table_data_frame1, state=widget_state, width = 10)
    entry_widget_table.pack(side=tk.LEFT)
    create_tool_tip(entry_widget_table, "Number of last iterations from INTERVAL used \nto calculate mean value")
    #
    button_table_interval = tk.Button(master = table_data_frame1, text ='Set interval', command = _set_table_interval)
    button_table_interval.pack(side = tk.LEFT)
    create_tool_tip(button_table_interval, "Set number of last iterations")
    #   
    #
    button_data_table = tk.Checkbutton(master=table_data_frame1, text="Table", variable=plot_creator.plt_table_data, command=_data_table)
    button_data_table.pack(side = tk.LEFT)
    create_tool_tip(button_data_table, "Toggles data table")
    #
    button_data_table.configure(state = widget_state)
    button_min.update()
    button_table_interval.configure(state = widget_state)
    button_max.update()
    #
    # ##### Last Inner Iter Switch
    #
    switch_last_iter = tk.Checkbutton(master=table_data_frame2, text="Last InnerIter", variable=plot_creator.plot_last_InnerIter, command = _replot_with_last_InnerIter)
    switch_last_iter.pack(side = tk.LEFT)
    create_tool_tip(switch_last_iter, "Toggle to plot last inner iteration values")
    #
    switch_last_iter.configure(state = widget_state_last_iter)
    switch_last_iter.update()

    #
    #
    # #############################
    #
    def _enable_entries():
        """
        Enables Iteration range buttons
        """
        #
        entry_widget_min.configure(state="normal")
        entry_widget_min.update()
        entry_widget_min.delete(0, tk.END)
        entry_widget_min.insert(0, str(float(plot_creator.min_entry_val)))
        entry_widget_min.xview(0)
        entry_widget_max.configure(state="normal")
        entry_widget_max.update()
        entry_widget_max.delete(0, tk.END)
        entry_widget_max.insert(0, str(float(plot_creator.max_entry_val)))
        entry_widget_max.xview(0)
        #
        button_min.configure(state="normal")
        button_min.update()
        button_max.configure(state="normal")
        button_max.update()   
        button_reset.configure(state="normal")
        button_reset.update()  
        #
        entry_widget_table.configure(state="normal")
        entry_widget_table.update()
        entry_widget_table.delete(0, tk.END)
        entry_widget_table.insert(0, str(plot_creator.table_entry_val))
        entry_widget_table.xview(0)
        button_data_table.configure(state="normal")
        button_min.update()
        button_table_interval.configure(state="normal")
        button_max.update()   
        #
    #
    def _disable_entries():
        """
        Disable Iteration range buttons
        """
        #
        entry_widget_min.configure(state="disabled")
        entry_widget_min.update()
        entry_widget_max.configure(state="disabled")
        entry_widget_max.update()
        button_min.configure(state="disabled")
        button_min.update()
        button_max.configure(state="disabled")
        button_max.update()
        button_reset.configure(state="disabled")
        button_reset.update()
        #
        entry_widget_table.configure(state="disabled")
        entry_widget_table.update()
        button_data_table.configure(state="disabled")
        #~ button_data_table.deselect()
        button_min.update()
       
        button_table_interval.configure(state="disabled")
        button_max.update()   
        #
    #
    def _enable_entries_thistime():
        """
        Enables Last InnerIter buttons
        """
        switch_last_iter.configure(state="normal")
        switch_last_iter.update()
        
    def _disable_entries_thistime():
        """
        Disable Last InnerIter buttons
        """
        plot_creator.plot_last_InnerIter = False
        switch_last_iter.deselect() 
        switch_last_iter.configure(state="disabled")
        switch_last_iter.update()
    #
    # #############################
    #
    
    #    
    #~ -------------------------- Y-VARIABLES
    #
    y_frame = tk.Frame(canvas_button_frame, bd=1, relief=tk.SUNKEN)
    y_var_label = tk.Label(y_frame, text="Y-Variables").grid(column=0, row=0, sticky=tk.N)
    create_tool_tip(y_frame, "Variables on Y-Axis.")
    #
    def _change_variables():
        """ 
        Button command to change variables on plot. also de-/activates Iteration range buttons
        """        
        #~ ENTRY WIDGETS
        
        _replot()
        _update_plot_options()
        #
    #        
    def _change_variablesX(xvar):
        """ 
        Button command to change variables on plot. also de-/activates Iteration range buttons
        """        
        x_variable_list[0]=xvar
        
        #~ print ' x_variable_list[0]',x_variable_list[0]
        plot_creator.get_variables()
        min_entry_var.set(float(plot_creator.min_entry_val))
        max_entry_var.set(float(plot_creator.max_entry_val))
        plot_creator.min_entry_val_disp = plot_creator.min_entry_val
        plot_creator.max_entry_val_disp = plot_creator.max_entry_val
        #~ ENTRY WIDGETS
        #~ raise "recover data from xvariable"
        
        #
        
        #
        if x_variable_list[0] == 'Inner-iter':
            Var_text = "Iter"
            _enable_entries()
            _disable_entries_thistime()
            entry_widget_min_label.config(text = Var_text+" (min "+str(min_entry_var.get())+")")
            entry_widget_max_label.config(text = Var_text+" (max "+str(max_entry_var.get())+")")
        elif x_variable_list[0] == 'thistime':
            Var_text = "Time"
            _enable_entries_thistime()
            entry_widget_min.configure(state="normal")
            entry_widget_min.update()
            entry_widget_min.delete(0, tk.END)
            entry_widget_min.insert(0, str(float(plot_creator.min_entry_val)))
            entry_widget_min.xview(0)
            entry_widget_max.configure(state="normal")
            entry_widget_max.update()
            entry_widget_max.delete(0, tk.END)
            entry_widget_max.insert(0, str(float(plot_creator.max_entry_val)))
            entry_widget_max.xview(0)
            #
            button_min.configure(state="normal")
            button_min.update()
            button_max.configure(state="normal")
            button_max.update()   
            button_reset.configure(state="normal")
            button_reset.update()  
            entry_widget_min_label.config(text = Var_text+" (min "+str(min_entry_var.get())+")")
            entry_widget_max_label.config(text = Var_text+" (max "+str(max_entry_var.get())+")")
        else:
            Var_text = "Val"
            _disable_entries()
            _disable_entries_thistime()
        
        #
        #
            
            
        _replot()
        _update_plot_options()
        #
    #
    mylist = list(available_variables)
    mylist.sort()    
    #
    cb:list = list(range(len(mylist)))
    cb_v:list = list(range(len(mylist)))
    column_nb=0
    #
    for ix, text in enumerate(mylist):
        # IntVar() tracks checkbox status (1=checked, 0=unchecked)
        cb_v[ix] = tk.IntVar()
        # command is optional and responds to any cb changes
        cb[ix] = tk.Checkbutton(y_frame,
                                text=text.strip('"'),
                                variable=cb_v[ix],
                                command=_change_variables)
        # cb[ix].pack(side=Tk.LEFT)
        #
        if ((ix+1)-column_nb*4)%4 == 0:
            row = 4
            cb[ix].grid(column=column_nb,row=row)
            column_nb +=1
        elif ((ix+1)-column_nb*4)%3 == 0:
            row = 3
            cb[ix].grid(column=column_nb,row=row)
        elif ((ix+1)-column_nb*4)%2 == 0:
            row = 2
            cb[ix].grid(column=column_nb,row=row)
        else:
            row = 1
            cb[ix].grid(column=column_nb,row=row)
            #
        #
    #
    #
    selected_variables = [0]*len(mylist)
    available_variables.sort()
    for i,variable_name in enumerate(available_variables):
        if variable_name.strip('"') in y_variable_list:
            selected_variables[i] = 1
            #
        #
    #    
    #    
    # you can preset check buttons (1=checked, 0=unchecked)
    for variable in range(len(selected_variables)):
        cb_v[variable].set(selected_variables[variable])
        #
    #    
    #
    y_frame.pack(side=tk.RIGHT, padx=5, pady=5)
    #
    #    
    #~ -------------------------- X-VARIABLE drop down menu
    #
    x_frame = tk.Frame(canvas_button_frame, bd=1, relief=tk.SUNKEN)
    label_x = tk.Label(x_frame, text="X-Variable") #.grid(column=0, row=0, sticky=Tk.N)
    label_x.pack()
    create_tool_tip(x_frame, "Variable on X-Axis.")
    #    
    mylist2 = list(available_variables)
    v = tk.StringVar()
    v.set(x_variable_list[0])
    column_nb=0
    #
    menu_vars = []
    for var in available_variables:
        menu_vars.append(var.strip('"'))
        #
    #
    #~ print menu_vars
    b = tk.OptionMenu(x_frame, v, *menu_vars, command=_change_variablesX)
    #~ b.config(bg = "white")
    b.pack(side=tk.RIGHT)
    #
    """ old x variable choice
    #~ for ix,text in enumerate(mylist2):
        # command is optional and responds to any cb changes        
        b = Tk.Radiobutton(x_frame, text=text.strip('"'), variable=v, value=text, command=_change_variables, indicatoron=0)
        if text.strip('"') == x_variable_list[0]:
            b.select()
        b.pack(side=Tk.RIGHT)

        if ((ix+1)-column_nb*4)%4 == 0:
            row = 4
            b.grid(column=column_nb,row=row)
            column_nb +=1
        elif ((ix+1)-column_nb*4)%3 == 0:
            row = 3
            b.grid(column=column_nb,row=row)
        elif ((ix+1)-column_nb*4)%2 == 0:
            row = 2
            b.grid(column=column_nb,row=row)
        else:
            row = 1
            b.grid(column=column_nb,row=row)
    """
    #
    x_frame.pack(side=tk.LEFT, padx=5, pady=5)
    #
    
    y_frame.pack(side=tk.RIGHT, padx=5, pady=5)
    #
    # ########################################### PLOT options
    #
    def _plot_options():
        """ 
        Button command to open plot_options window
        """
        #
        #~ for entry in dir(plot_options_window):
            #~ print entry
        #~ print help(plot_options_window.deiconify)
        #~ print help(plot_options_window.iconify)
        
        if plot_options_window.state() == "withdrawn":
            plot_options_window.deiconify()
        else:
            _save_plot_options()
        #
    #
    def _save_plot_options():
        plot_options_window.withdraw()
    #
     # ############ ####################################
    # change canvas_button_frame to plot_options_window         !!!!!!!!!!!!!!!!!!!
    # ############ ####################################
    
    plot_options_window = tk.Toplevel(root)
    plot_options_window_canvas = tk.Canvas(plot_options_window)
    plot_options_window_canvas.pack()
    plot_options_window.protocol("WM_DELETE_WINDOW", _save_plot_options)
    #~ plot_options_window_label = Tk.Label(plot_options_window, text='TAU plot options')
    #~ plot_options_window_label.pack()
    plot_options_window.withdraw()
    #~ plot_options_window = Tk.Frame(canvas_button_frame,bd=1, relief=Tk.SUNKEN)  
    #~ plot_options_window.pack()
    #
    #
    plot_options_button = tk.Button(master=canvas_button_frame, text='plot_creator\nOptions', command=_plot_options)
    plot_options_button.pack(side=tk.LEFT, padx=5, pady=5)
    create_tool_tip(plot_options_button, "Opens/Closes plot options window")
    #
    
   
    # - extra window: color, linestyle, marker size, markershape, marker every=5 etc
    #
    # ############ plot_creator Option buttons in grid
    #
    #~ entry_widget_PLOT_OPTIONS_Corner_label = Tk.Label(plot_options_window, text="Line Opts:  ")
    #~ entry_widget_PLOT_OPTIONS_Corner_label.grid(column=0,row=0)
    #
    label_list = ["label","axis","c","m","ls","lw","ms","me","alpha"]
    label_tool_tip_dict = { "label":"Label to plot in the figure.\nLatex formatting possbile by using $$.",
                            "axis":"Label to plot on the axis.\nLatex formatting possbile by using $$.",
                            "c":"""Color of the curve\n('b','g','r','c','m','y', '0.1','0.2' etc.)\nb: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black\
Gray shades : 0.5, 0.6 etc.
html hex string: #eeefff
html names for colors: 'red', 'burlywood', 'chartreuse'
""",
                            "m":"Marker of the curve\nEmptyfor none\n('o','h','^','v','<','>','_','1','2','3','4','8','p','|','d',',','+','s','*','l','x','D','H','.')",
                            "ls":"Line style\nEmptyfor none\n('-','--','..','-.','.',',','o','^','v','<','>','s','+','x','d','1','2','3','4','h','p','|','S','H')",
                            "lw":"Line width",
                            "ms":"Marker size",
                            "me":"Marker every n-th value",
                            "alpha":"Alpha blending value\n(0.0 transparent through 1.0 opaque)",                            
                            }
                            
        
    for ix,lab in enumerate(label_list):
        entry_widget_PLOT_OPTIONS_Corner_label = tk.Label(plot_options_window_canvas, text=lab)
        #~ entry_widget_PLOT_OPTIONS_Corner_label.pack()
        entry_widget_PLOT_OPTIONS_Corner_label.grid(column=ix+1,row=0,padx=5, pady=1)
        text = label_tool_tip_dict[lab]
        #~ print text 
        create_tool_tip(entry_widget_PLOT_OPTIONS_Corner_label, text)
        #
    #
    
    
    def _set_plot_options():
        """ 
        Button command to set plot options
        
        read all options from the entry widgets
        """
        
        # Y - Axis        
        for iter1,y_var in enumerate(mylist):
            if y_var in plot_creator.plot_options_dict:
                for iter2,lab in enumerate(label_list):
                    option = option_list_widgets[iter1][iter2].get()
                    plot_creator.plot_options_dict[y_var][lab] = option
                
        # X - Axis
        #
        plot_creator.plot_options_dict["X-Var"] = entry_widget_x_Var_plot.get()
        #
        #
        # Label sizes        
        plot_creator.plot_options_dict["ticker_size"] = entry_widget_plot_size_ticker.get()
        plot_creator.plot_options_dict["legend_size"] = entry_widget_plot_size_legend.get()
        plot_creator.plot_options_dict["xaxis_size"] = entry_widget_plot_size_axis_x.get()
        plot_creator.plot_options_dict["yaxis_size"] = entry_widget_plot_size_axis_y.get()
        #
        #
        plot_creator.suplot_left = entry_widget_subplot_size_left.get()
        plot_creator.suplot_right = entry_widget_subplot_size_right.get()
        plot_creator.suplot_top = entry_widget_subplot_size_top.get()
        plot_creator.suplot_bottom = entry_widget_subplot_size_bottom.get()
        #
        _replot()
        #
        return
        #
    #
    def _update_plot_options():
        """ 
        Command to update plot options, when toggling X-Variable or Y-variables
        
        """
        
        for iter1,y_var in enumerate(mylist):
            for iter2,lab in enumerate(label_list):
                #
                # label
                #
                #~ print lab 
                if lab == "label" or lab == "axis":
                    width = 15                   
                elif lab == "c" :
                    width = 8
                elif lab == "alpha" :
                    width = 3
                else:
                    width = 2
                
                option_list_widgets[iter1][iter2].delete(0, tk.END)
                
                if y_var not in plot_creator.plot_options_dict:
                    
                    option_list_widgets[iter1][iter2].insert(0, "")
                else:
                    option_list_widgets[iter1][iter2].insert(0, str(plot_creator.plot_options_dict[y_var][lab]))
                
        
        entry_widget_x_Var_plot_label.config(text="X-Ax: "+x_variable_list[0])
        entry_widget_x_Var_plot.delete(0, tk.END)
        entry_widget_x_Var_plot.insert(0, plot_creator.plot_options_dict["X-Var"])
        
        entry_widget_subplot_size_left.delete(0, tk.END)
        entry_widget_subplot_size_right.delete(0, tk.END)
        entry_widget_subplot_size_top.delete(0, tk.END)
        entry_widget_subplot_size_bottom.delete(0, tk.END)
        entry_widget_subplot_size_left.insert(0, plot_creator.suplot_left)
        entry_widget_subplot_size_right.insert(0, plot_creator.suplot_right)
        entry_widget_subplot_size_top.insert(0, plot_creator.suplot_top)
        entry_widget_subplot_size_bottom.insert(0, plot_creator.suplot_bottom)
        
    
        return
        #
    #
    #    
    option_list_variable_labels = []
    option_list_set_buttons = []
    
    option_list_widgets = []
        
    ########################### Size of tickers, plot labels, axis labels
    option_list_TAU_label = tk.Label(plot_options_window_canvas, text="TAU var")
    option_list_TAU_label.grid(column=0,row=0)

    for iter1,y_var in enumerate(mylist):        

        option_list_variable_labels.append(tk.Label(plot_options_window_canvas, text=y_var))
        option_list_variable_labels[-1].grid(column=0,row=iter1+2)
        #~ 
        # #####################
        # widgets
        # #####################
        option_list_widgets_options = []
        
        if y_var not in plot_creator.plot_options_dict:
            plot_creator.plot_options_dict[y_var] = {}
            for iter2 in label_list:                    
                plot_creator.plot_options_dict[y_var][iter2] = ""
        
        for iter2,lab in enumerate(label_list):
            #
            # label
            #            
            if lab == "label" or lab == "axis":
                width = 15                
            elif lab == "c" :
                width = 8
            elif lab == "alpha" :
                width = 4
            else:
                width = 3
            
            if y_var not in plot_creator.plot_options_dict:
                plot_creator.plot_options_dict[y_var] = {}
                for label2 in label_list:                    
                    plot_creator.plot_options_dict[y_var][label2] = ""
                    #
                #   
            #
            entry_widget_Option = tk.Entry(master=plot_options_window_canvas, state="normal", width=width)
            entry_widget_Option.grid(column=iter2+1,row=iter1+2)
            entry_widget_Option.update()
            entry_widget_Option.delete(0, tk.END)
            entry_widget_Option.insert(0, str(plot_creator.plot_options_dict[y_var][lab]))
            option_list_widgets_options.append(entry_widget_Option)
            #
        #
        option_list_widgets.append(option_list_widgets_options)
        #
    #
    
    # ######################## 
    # ADD FOR X-AXIS LABEL
    # ######################## 
    #    
    entry_widget_x_Var_plot_label = tk.Label(plot_options_window_canvas, text="X-Ax: " + x_variable_list[0])
    entry_widget_x_Var_plot_label.grid(column=0,row=iter1+3,padx=5, pady=20)
    entry_widget_x_Var_plot = tk.Entry(master=plot_options_window_canvas, state="normal", width=15)
    entry_widget_x_Var_plot.grid(column=2,row=iter1+3)
    entry_widget_x_Var_plot.update()
    entry_widget_x_Var_plot.delete(0, tk.END)
    entry_widget_x_Var_plot.insert(0, plot_creator.plot_options_dict["X-Var"])
    #    
    option_list_set_button = tk.Button(master=plot_options_window_canvas, text='Set', command=_set_plot_options)
    option_list_set_button.grid(column=iter2+2,row=iter1+4)
    create_tool_tip(option_list_set_button, "Set all plot style options and replot")
    #    
    # ######################## 
    # ADD FOR Ticker Size, Axis Label Size, plot_creator Label size
    # ######################## 
    #    
    size_labels = tk.Label(plot_options_window_canvas, text="Label sizes")
    size_labels.grid(column=0,row=iter1+4,padx=5, pady=10)
    #
    entry_widget_plot_size_ticker_label = tk.Label(plot_options_window_canvas, text="ticker:")
    entry_widget_plot_size_ticker_label.grid(column=1,row=iter1+4)
    entry_widget_plot_size_ticker = tk.Entry(master=plot_options_window_canvas, state="normal", width=6)
    entry_widget_plot_size_ticker.grid(column=2,row=iter1+4)
    entry_widget_plot_size_ticker.update()
    entry_widget_plot_size_ticker.delete(0, tk.END)
    entry_widget_plot_size_ticker.insert(0, plot_creator.plot_options_dict["ticker_size"])
    create_tool_tip(entry_widget_plot_size_ticker, "Set the ticker font size\nEither a relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' or an absolute font size, e.g., 12")
    #
    entry_widget_plot_size_legend_label = tk.Label(plot_options_window_canvas, text="legend:")
    entry_widget_plot_size_legend_label.grid(column=3,row=iter1+4)
    entry_widget_plot_size_legend =  tk.Entry(master=plot_options_window_canvas, state="normal", width=6)
    entry_widget_plot_size_legend.grid(column=4,row=iter1+4)
    entry_widget_plot_size_legend.update()
    entry_widget_plot_size_legend.delete(0, tk.END)
    entry_widget_plot_size_legend.insert(0, plot_creator.plot_options_dict["legend_size"])
    create_tool_tip(entry_widget_plot_size_legend, "Set the legend font size\nEither a relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' or an absolute font size, e.g., 12")
    #    
    entry_widget_plot_size_axis_label_x_label = tk.Label(plot_options_window_canvas, text="x-axis:")
    entry_widget_plot_size_axis_label_x_label.grid(column=5,row=iter1+4)
    entry_widget_plot_size_axis_x =  tk.Entry(master=plot_options_window_canvas, state="normal", width=6)
    entry_widget_plot_size_axis_x.grid(column=6,row=iter1+4)
    entry_widget_plot_size_axis_x.update()
    entry_widget_plot_size_axis_x.delete(0, tk.END)
    entry_widget_plot_size_axis_x.insert(0, plot_creator.plot_options_dict["xaxis_size"])
    create_tool_tip(entry_widget_plot_size_axis_x, "Set the x-axis font size\nEither a relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' or an absolute font size, e.g., 12")
    #
    entry_widget_plot_size_axis_label_y_label = tk.Label(plot_options_window_canvas, text="y-axis:")
    entry_widget_plot_size_axis_label_y_label.grid(column=7,row=iter1+4)
    entry_widget_plot_size_axis_y =  tk.Entry(master=plot_options_window_canvas, state="normal", width=6)
    entry_widget_plot_size_axis_y.grid(column=8,row=iter1+4)
    entry_widget_plot_size_axis_y.update()
    entry_widget_plot_size_axis_y.delete(0, tk.END)
    entry_widget_plot_size_axis_y.insert(0, plot_creator.plot_options_dict["yaxis_size"])
    create_tool_tip(entry_widget_plot_size_axis_y, "Set the y-axis font size\nEither a relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' or an absolute font size, e.g., 12")
    #    
    # ################################
    # SUBPLOT SIZE ADJUSTMENT
    # ################################
    #
    
    #
    entry_widget_subplot_size_label = tk.Label(plot_options_window_canvas, text="Subplot size:")
    entry_widget_subplot_size_label.grid(column=0,row=iter1+5)
    entry_widget_subplot_size_left = tk.Entry(master=plot_options_window_canvas, state="normal", width=6)
    entry_widget_subplot_size_left.grid(column=1,row=iter1+5)
    entry_widget_subplot_size_left.update()
    entry_widget_subplot_size_left.delete(0, tk.END)
    entry_widget_subplot_size_left.insert(0, plot_creator.suplot_left)
    create_tool_tip(entry_widget_subplot_size_left, "Distance from left border in figure coordinates")
    entry_widget_subplot_size_right = tk.Entry(master=plot_options_window_canvas, state="normal", width=6)
    entry_widget_subplot_size_right.grid(column=2,row=iter1+5)
    entry_widget_subplot_size_right.update()
    entry_widget_subplot_size_right.delete(0, tk.END)
    entry_widget_subplot_size_right.insert(0, plot_creator.suplot_right)
    create_tool_tip(entry_widget_subplot_size_right, "Distance from right border in figure coordinates")
    entry_widget_subplot_size_top = tk.Entry(master=plot_options_window_canvas, state="normal", width=6)
    entry_widget_subplot_size_top.grid(column=3,row=iter1+5)
    entry_widget_subplot_size_top.update()
    entry_widget_subplot_size_top.delete(0, tk.END)
    entry_widget_subplot_size_top.insert(0, plot_creator.suplot_top)
    create_tool_tip(entry_widget_subplot_size_top, "Distance from top border in figure coordinates")
    entry_widget_subplot_size_bottom = tk.Entry(master=plot_options_window_canvas, state="normal", width=6)
    entry_widget_subplot_size_bottom.grid(column=4,row=iter1+5)
    entry_widget_subplot_size_bottom.update()
    entry_widget_subplot_size_bottom.delete(0, tk.END)
    entry_widget_subplot_size_bottom.insert(0, plot_creator.suplot_bottom)
    create_tool_tip(entry_widget_subplot_size_bottom, "Distance from bottom border in figure coordinates")
    print("done..")
    #
    # ###########################################
    #
    if x_variable_list[0] == 'Inner-iter':        
        _enable_entries()
    else:
        _disable_entries()
        #
    if x_variable_list[0] == 'thistime':
        switch_last_iter.select()
        
        _enable_entries_thistime()
        #~ _change_variablesX(x_variable_list[0])
        entry_widget_min_label.config(text = "Time (min "+str(min_entry_var.get())+")")
        entry_widget_max_label.config(text = "Time (max "+str(max_entry_var.get())+")")
        entry_widget_min.configure(state="normal")
        entry_widget_min.update()
        entry_widget_min.delete(0, tk.END)
        entry_widget_min.insert(0, str(float(plot_creator.min_entry_val)))
        entry_widget_min.xview(0)
        entry_widget_max.configure(state="normal")
        entry_widget_max.update()
        entry_widget_max.delete(0, tk.END)
        entry_widget_max.insert(0, str(float(plot_creator.max_entry_val)))
        entry_widget_max.xview(0)
        #
        button_min.configure(state="normal")
        button_min.update()
        button_max.configure(state="normal")
        button_max.update()   
        button_reset.configure(state="normal")
        button_reset.update()  
    else:
        _disable_entries_thistime()
        #
    #       
    #
    #~ run in loop for input
    tk.mainloop()
    #
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#
class ToolTip(object):
    """
    ToolTip classs from Michael Foord
    http://www.voidspace.org.uk/python/weblog/arch_d7_2006_07_01.shtml#e387
    """
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        #
        self.follow = False
        self.delay = 1
        return
    #
    def showtip(self, text):
        """
        Display text in tooltip window
        """
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27  +10
        y = y + cy + self.widget.winfo_rooty() +27 +10
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        # try:
            # For Mac OS
            # tw.tk.call("::tk::unsupported::MacWindowStyle",
                       # "style", tw._w,
                       # "help", "noActivates")
        # except TclError:
            # pass
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
        return
    #
    def hidetip(self):
        """
        Remove text in tooltip window
        """
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

        return
    #
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#
def create_tool_tip(widget, text):
    """
    Function to create ToolTips given a widget and a TooltipText
    """
    tool_tip = ToolTip(widget)
    #
    def enter(event):
        # if time() - self.lastMotion > self.delay
        tool_tip.showtip(text)
    def leave(event):
        tool_tip.hidetip()
    #
    def move( event ):
        """
        Processes motion within the widget.
        
        Arguments:
          event: The event that called this function
        """
        tool_tip.lastMotion = time.time()
        if tool_tip.follow == False:                                                # If the follow flag is not set, motion within the widget will make the ToolTip dissapear
            tool_tip.tipwindow.withdraw()
            tool_tip.visible = 1
        # tool_tip.geometry( '+%i+%i' % ( event.x_root+10, event.y_root+10 ) )        # Offset the ToolTip 10x10 pixes southwest of the pointer
        try:
            tool_tip.msgVar.set( tool_tip.msgFunc() )                                   # Try to call the message function.  Will not change the message if the message function is None or the message function fails
        except:
            pass
        tool_tip.tipwindow.after( int( tool_tip.delay * 1000 ), tool_tip.showtip(text) )
    #
    # bind to widget
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
    # widget.bind('<Motion>', move )
    return
    #
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#
def ascii_read(filename,
               data_line,
               title_line=None,
               title_line_junk='#',
               column_titles=True,
               return_header=False,
               string_cols: list = None,
               usecols=None,
               loadtxt_args=None,
               check_iter_numbers=False):
    """A wrapper around numpy loadtxt to load acsii data files, allowing for 
    headers, string columns and returning the output as a dictionary using a
    line in the header as keys.
    
    :Paremters:
        filename : str
            full filename of file e.g. "swicsdata.txt", or file object
        data_line : int
            line number for the first line of data
        title_line : int, optional
            line in the file where the list of coloum titles are
            (default 2 above data_line)
        title_line_junk : str, optional
            A string at the begging of the title line which should be removed
            also passed to loadtxt as comments kwarg
        column_titles : bool, optional
            If false will not return dict it returns ndarray.
        return_header : bool, optional
            Returns header lines as list if True
        string_cols : list, optional
            A sequence of column numbers eg, [1,2] which are strings, and will
            be extracted from the file seperatly from the main loadtxt call.
        usecols : list, optional
            same as loadtxt_args{"usecols",[]}, selects specific columns from
            the data file. If using string_cols as well, usecols should include
            the columns that are in string_cols.
        loadtxt_args: dict, optional
            Keyword Arguments to pass to numpy loadtxt
    
    
    Created on Thu Feb 10 15:19:13 2011

    @author: Stuart Mumford

    This ascii_read a wrapper for loadtxt
    
    DEV:
            TO-DO
                - Add mutiple Title pulls, for many columns
                - Allow only string cols
                - Improve logical flow of program (reduce if statements, esp if string_cols:)
                -Include support for open file object
    
    .. Note:        
        Modified on 2012.03.14 for TAU monitoring files
        Kay Sommerwerk
        Institute of Aircraft Design and Lightweight Structures (IFL), TU Braunschweig
        Collaborative Research Center 880
    """
    if not(loadtxt_args):
        loadtxt_args = {}
    #Set title header line to be 2 above data line is blank
    if not(title_line):
        title_line = data_line -2
    #Pass usecols argument to loadtxt
    if usecols:
        loadtxt_args.update({"usecols":usecols})
    #Pass title_line_junk to numpy
    loadtxt_args.update({"comments":title_line_junk})
    
    #f = open(filename)    
        
    
    #Open file
    if is_string_like(filename):
        try:            
            f = open(filename)
            #~ print "Opening file '",filename,"' ..."
        except IOError as e:
            print(e,'Could not open file.')
            exit()
    elif hasattr(filename, 'readline'):
        try:      
            f = filename
        except:
            print('Could not open file "',filename,'". File not found. ')
            exit()
    else:
        raise ValueError('fname must be a string or file handle') 
    
    ## # Read in Header and initial processing
    #Read in the header to a list, in the process skipping it
    header = []
    for i in range(data_line-1):
        header.append(f.readline())
    #Store position in file where header ends
    data_start = f.tell()
   
    #Find width of file (from numpy.loadtxt)
    first_line = f.readline()
    first_vals = first_line.split()
    N = len(first_vals)
    
    #Do not read in string_cols, set usecols to be all columns that arn't string
    if string_cols:
        #List of columns
        columns: list = list(range(N))
        #remove string_cols from columns
        for i in string_cols:
            columns.remove(i)
        #if columns is specified as well as string_cols remove them as well
        if "usecols" in loadtxt_args.keys():
            for i in loadtxt_args["usecols"]:
                columns.remove(i)
        #put columns into loadtxt
        loadtxt_args.update({"usecols":columns}) #TODO: Catch no columns!
    else:
        if "usecols" in loadtxt_args:
            columns = loadtxt_args["usecols"]
        else:
            columns = list(range(N))
    
    #Read file
    f.seek(data_start)
    #Read in numeric data
    try:
        ndata = np.loadtxt(f, **loadtxt_args)
    except ValueError as Err:
        raise ValueError(
        "Conversion Error in loadtxt:[%s], have you specified string_cols?"
        %Err)
    
    #Read in string data
    if string_cols:
        loadtxt_args.update({"usecols":string_cols, "dtype":str})
        f.seek(data_start)
        sdata = np.loadtxt(f, **loadtxt_args)    
    
    #If no column titles then return array
    if not column_titles:
        #Sort array so that the array is in the same order as the file
        fdata = np.zeros([len(columns)])
        if string_cols:
            for i, T in enumerate(string_cols):
                fdata[T] = sdata[i]
        for i, T in columns:
            fdata[T] = ndata[i]
        #Return the data
        if return_header:
            return header, fdata
        else:
            return fdata
   
    
    def dict_maker(header,
                   columns,
                   data):
        """
        Creates a dictionary from a list of columns and the data array
        """
        #Create a list of all the coloumn names
        keys = header[title_line-1].split(title_line_junk)[-1].strip().split()
               
        #Pick out keys for which ever data columns have been used
        fkeys = []
        if len(keys) == len(columns):
            #~ same length
            for col_id in columns:
                fkeys.append(keys[col_id])
        else:
            #~ remove first variable (Tau Monitor first value == '"VARIABLES="')
            keys.pop(0)            
            for col_id in columns:
                fkeys.append(keys[col_id])
            
        #Zip fails if only one column selected
        if len(fkeys) == 1:
            data = {fkeys[0]:data}
        else:
            data = dict(zip(fkeys,np.transpose(data)))
        return data
    
    
    #Make dict out of numeric data
    outdict = dict_maker(header, columns, ndata)
    if string_cols:
        sdict = dict_maker(header, string_cols, sdata)  
        outdict.update(sdict)

    """# added by Ian Krukow #"""
    if check_iter_numbers and '"Inner-iter"' in outdict:
        for ii in range(1, len(outdict['"Inner-iter"'])):
            inc = outdict['"Inner-iter"'][ii] - outdict['"Inner-iter"'][ii-1]
            if inc < 0:
                outdict['"Inner-iter"'][ii:] += 1 - inc
    """# /added by Ian Krukow #"""

    f.close()
    #~ print '...done'
    if return_header:
        return header, outdict
    else:
        return outdict
        #
    #
#
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#
if __name__ == "__main__": 
    print("-"*40)
    print(" taumonplot.py, version info in file header")
    print("-"*40)
    #   
    create_plot(subdirectory,
                name_prefix,
                data_line,
                title_line,
                x_variable_list,
                y_variable_list,
                check_iter_numbers,
                save_to_file)
    #
#
    
