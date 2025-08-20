Usage
=====

Requirements
------------

Programs:
##################
- DLR TAU solver - to generate monitoring files

DLR TAU solver
..................

The DLR TAU code is a fluid solver. See description_ for more info.

.. _description: http://tau.dlr.de/code-description/


Python packages:
##################
- numpy
- matplotlib
- Tkinter
    
.. Note:: 
    
    Linux: 
        All packages mentioned are available via the standard repositories and can be downloaded for example with a package manager
    
    Windows: 
        Recommended is the installation of a python distribution, that includes many ohter packages. An example is PythonXY_.
        
        To install the needed packages in your existing python distribution you can use the precombiled binaries (inofficial) on Christoph Gohlke's page_ at the University of California, Irvine.
    
    
.. _PythonXY: https://code.google.com/p/pythonxy/wiki/Downloads
.. _page: http://www.lfd.uci.edu/~gohlke/pythonlibs/

NumPy
.......

NumPy_ is an extension to the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays.

.. _NumPy: https://pypi.python.org/pypi/numpy

Matplotlib
.............
Matplotlib_ is a plotting library for the Python programming language and its NumPy numerical mathematics extension.

.. _Matplotlib: http://matplotlib.org/

Tkinter
.............

Tkinter_ is Python's de-facto standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of Tcl/Tk.
Tkinter is included in python.

.. _Tkinter: http://tcl.sourceforge.net/

Getting ready
##################

Enable TAU monitoring
..........................

.. Note:: valid for TAU version 2013.2


To generate a monitoring file during a TAU run the user has to enable the monitoring parameter in the TAU input file.

 ``Monitor history (0/1): integer, default 0``

 - Turns on/off the print out of the Monitoring values in Tecplot ASCII format in an extra file. Whenever a restart is done and the Output files prefix is not changed the output of the values will be continued in the previous monitoring file. The monitoring files are named as prefix.monitoring.pval.dat and prefix.unsteady.monitoring.pval.dat in a steady and unsteady computation. If a restart is made with the turned on monitoring history the monitoring values have to be fixed over the whole computation.
 
 :Example: ``Monitor history (0/1): 1``
 
 
The monitoring values are indicated with the following parameter:

 ``Monitoring values: character string, default (none)``
 
 - Character string containing the names of the quantities to be monitored during execution of the solver. The names are separated by underline, e.g. Residual Max-res C-lift C-drag. The available names with a short explanation are listed by the solver in the standard output and are listed in Table 4 in the subsection Output files. Some of the monitoring values can be used to check the convergence of the inner iterations (parameter Use Cauchy convergence control). Those variables are marked with an "X" in the second column.

 :Example: ``Monitoring values: Residual_C-lift_C-drag_C-my_Angle-a``

See `Table of monitoring values`_ for available monitoring values.



Starting taumonplot
####################################

Please see the section :ref:`manual_Manual` for information.


.. _usage_Monitoring:

Table of monitoring values
####################################

==================== =======================================================================
Implemented monitoring values (to be separated by '_')
--------------------------------------------------------------------------------------------
KEY                  COMMENT
==================== =======================================================================
Residual             norm of rho-increments
dvx/dt               norm of u-increments
dvy/dt               norm of v-increments
dvz/dt               norm of w-increments
dp/dt                norm of pressure-increments
drhoE/dt             norm of energy-increments
dnue/dt              norm of nue-increments
drk/dt               norm of rho_k-increments
drk2/dt              norm of rho_k2-increments
Max-res              maximum of rho-increments
X-max-res            grid x-coordinate of Max-res
Y-max-res            grid y-coordinate of Max-res
Z-max-res            grid z-coordinate of Max-res
Max-res-global       global maximum of rho-increments over all domains
C-lift               lift-coefficient 
C-lift-p             pressure part of C-lift
C-lift-v             viscous part of C-lift
C-drag               drag-coefficient
C-drag-p             pressure part of C-drag
C-drag-v             viscous part of C-drag
C-sidef              coeff of sideforce
C-sidef-p            pressure part of C-sidef
C-sidef-v            viscous part of C-sidef
C-mx                 rolling moment coefficient
C-mx-p               pressure part of rolling moment coefficient
C-mx-v               viscous part of rolling moment coefficient
C-my                 pitching moment coefficient
C-my-p               pressure part of pitching moment coefficient
C-my-v               viscous part of pitching moment coefficient
C-mz                 yawing moment coefficient
C-mz-p               pressure part of yawing moment coefficient
C-mz-v               viscous part of yawing moment coefficient
C-fx                 force-coefficient (x-component)
C-fx-p               pressure part of force-coefficient (x-component)
C-fx-v               viscous part of force-coefficient (x-component)
C-fy                 force-coefficient (y-component)
C-fy-p               pressure part of force-coefficient (y-component)
C-fy-v               viscous part of force-coefficient (y-component)
C-fz                 force-coefficient (z-component)
C-fz-p               pressure part of force-coefficient (z-component)
C-fz-v               viscous part of force-coefficient (z-component)
Fx                   x-component of force [N]
Fx-p                 pressure part of x-component of force [N]
Fx-v                 viscous part of x-component of force [N]
Fy                   y-component of force [N]
Fy-p                 pressure part of y-component of force [N]
Fy-v                 viscous part of y-component of force [N]
Fz                   z-component of force [N]
Fz-p                 pressure part of z-component of force [N]
Fz-v                 viscous part of z-component of force [N]
Mx                   x-component of moment [Nm]
Mx-p                 pressure part of x-component of moment [Nm]
Mx-v                 viscous part of x-component of moment [Nm]
My                   y-component of moment [Nm]
My-p                 pressure part of y-component of moment [Nm]
My-v                 viscous part of y-component of moment [Nm]
Mz                   z-component of moment [Nm]
Mz-p                 pressure part of z-component of moment [Nm]
Mz-v                 viscous part of z-component of moment [Nm]
Min-mach             minimum Machnumber in field
Max-mach             maximum Machnumber in field
Heatflow             total heatflow [W]
Res-heat             heatflux-increment
Min-y+               minimum value of y+
X-min-y+             grid x-coordinate of Min-y+
Y-min-y+             grid y-coordinate of Min-y+
Z-min-y+             grid z-coordinate of Min-y+
Max-y+               maximum value of y+
X-max-y+             grid x-coordinate of Max-y+
Y-max-y+             grid y-coordinate of Max-y+
Z-max-y+             grid z-coordinate of Max-y+
Min-kr               minimum value of kr
X-min-kr             grid x-coordinate of Min-kr
Y-min-kr             grid y-coordinate of Min-kr
Z-min-kr             grid z-coordinate of Min-kr
Max-kr               maximum value of kr
X-max-kr             grid x-coordinate of Max-kr
Y-max-kr             grid y-coordinate of Max-kr
Z-max-kr             grid z-coordinate of Max-kr
Min-kr+              minimum value of kr+
X-min-kr+            grid x-coordinate of Min-kr+
Y-min-kr+            grid y-coordinate of Min-kr+
Z-min-kr+            grid z-coordinate of Min-kr+
Max-kr+              maximum value of kr+
X-max-kr+            grid x-coordinate of Max-kr+
Y-max-kr+            grid y-coordinate of Max-kr+
Z-max-kr+            grid z-coordinate of Max-kr+
act-area             Area actuation bdry
act-targ-mf          Actuation target massflow
act-pres             Actuation bdry pressure
Min-eddyv            min dim-less eddy viscosity
Max-eddyv            max dim-less eddy viscosity
Min-k                min kinetic energy
Max-k                max kinetic energy
Min-k2               min 2nd turb. quantity
Max-k2               max 2nd turb. quantity
Max-mtm              max eddy-viscosity/laminar-viscosity
Angle-a              angle of attack alpha
Angle-b              yaw angle beta
Sideslip             sideslip angle beta
Farf-vx              farfield vx
Farf-vz              farfield vz
Mtm-2t               number of pseudo time steps (unsteady)
Alpha(t)             pitch amplitude
H(t)                 heave amplitude [grid unit]
dalpha-dt            pitch angular velocity
dh-dt                heave velocity [grid unit/s]
S-k-e                structural kinetic energy
T/tperiod            time normalized with period length
Phi                  rotation angle phi
Psi                  rotation angle psi
Xi                   rotation angle xi
Trans-x              translation in x direction [grid unit]
Trans-y              translation in y direction [grid unit]
Trans-z              translation in z direction [grid unit]
Farf-mach            effective farfield Mach number at origin
Farf-alpha           effective farfield angle of attack alpha at origin [deg]
Farf-beta            effective farfield angle of attack beta at origin [deg]
les-dt               timescale resolution of des
les-percent          % of des points
hybcentpercent       % of fluxes computed with pure central
vort-center-x        center of vorticity (x)
vort-center-y        center of vorticity (y)
vort-center-z        center of vorticity (z)
vort-total           total vorticity
dudx                 dudx
dvdy                 dvdy
dwdz                 dwdz
total-ke             total ke
mean-dissip1         molecular dissipation
rmsu                 rms u
rmsv                 rms v
rmsw                 rms w
rmsp                 rms pressure
skew                 velocity derivative skewness
kurt                 normalized velocity derivative kurtosis
Taylor-f             Longitudinal Taylor length scale
Taylor-g             Transverse Taylor length scale
Taylor-Re            Re based on Taylor scale
L2n-vc               L2 norm of vortical correction
Max-vc               Max value of vortical correction
Min-vc               Min value of vortical correction
Res-lift             cl-increment
Res-drag             cd-increment
R-time               Total CPU time (real)
U-time               Total CPU time (user)
Rhs-time             CPU time for one compute_residual() call.
Norm-time            Normalized CPU time (real)
dJ/da-1              Adjoint & Primal: Partial dJ/da
dJ/da-2              Adjoint: psi * partial dR/da, Primal: Partial dJ/dW * dW/da
dJ/da                Adjoint & Primal: derivative of cost fn wrt design var.
Sens                 Functional sensitivity
Freqdom-Cl-Amp       Freqdom: Amplitude of CL
Freqdom-Cl-Phase     Freqdom: Phase shift of CL
Freqdom-Cd-Amp       Freqdom: Amplitude of CD
Freqdom-Cd-Phase     Freqdom: Phase shift of CD
Freqdom-Cmx-Amp      Freqdom: Amplitude shift of CM_X
Freqdom-Cmx-Phase    Freqdom: Phase shift of CM_X
Freqdom-Cmy-Amp      Freqdom: Amplitude shift of CM_Y
Freqdom-Cmy-Phase    Freqdom: Phase shift of CM_Y
Freqdom-Cmz-Amp      Freqdom: Amplitude shift of CM_Z
Freqdom-Cmz-Phase    Freqdom: Phase shift of CM_Z
RPM-Res-P            RPM residual on Newton subspace
RPM-Res-Q            RPM residual on complementary subspace.
RPM-Dim-P            RPM Newton subspace dimension
==================== =======================================================================










