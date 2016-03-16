#!/usr/bin/python
#
# Mohr_circle_D-P_2D.py
#
# This script plots Mohr circles using principal stress values for cases with
# and without pore fluid pressure. The script also plots the 2D Drucker-Prager
# failure envelope for a given cohesion and friction angle.
#
# dwhipp 05.13

#--- User-defined input values ------------------------------------------------#
sigma_1=500                                                                     # The largest principal stress [MPa]
sigma_3=350                                                                     # The smallest principal stress [MPa]
zmax=50                                                                         # zmax, tThickness of crust [km]
gravity=9.81                                                                    # Acceleration due to gravity [m/s2]
rho_c=2750                                                                      # Rock density [kg/m3]
coh_c=10                                                                        # Rock coehsion [MPa]
phi_c=30                                                                         # Rock friction angle [degrees]
pore_p=250                                                                       # Pore fluid pressure [MPa]

#--- End user-defined input ---------------------------------------------------#

#--- DO NOT MODIFY ANYTHING BELOW THIS LINE -----------------------------------#

# Import libraries
import pylab

# Scale input values
#sigma_1=sigma_1*1e6                                                             # MPa -> Pa
#sigma_3=sigma_3*1e6                                                             # MPa -> Pa
zmax=zmax*1000                                                                  # km -> m
#coh_c=coh_c*1e6                                                                 # MPa -> Pa
phi_c=phi_c*pylab.pi/180                                                              # deg -> rad
#pore_p=pore_p*1e6                                                               # MPa -> Pa

#origin
xorigin=0
yorigin=0

# Parameter ranges
theta=pylab.linspace(0,pylab.pi,100);
z=pylab.linspace(1,zmax,100);

# Mohr circle equations
sigma_n=(sigma_1+sigma_3)/2 + ((sigma_1-sigma_3)/2)*pylab.cos(2*theta);
sigma_n_fluid=(sigma_1+sigma_3)/2 + ((sigma_1-sigma_3)/2)*pylab.cos(2*theta) - pore_p;
sigma_s=((sigma_1-sigma_3)/2)*pylab.sin(2*theta);

# Frictional strength equations
str_c=((rho_c*gravity*z)*pylab.sin(phi_c) + coh_c*pylab.cos(phi_c)) / 1e6

# Convert stresses to MPa for plots
#sigma_1=sigma_1/1e6
#sigma_3=sigma_3/1e6
#sigma_n=sigma_n/1e6
#sigma_n_fluid=sigma_n_fluid/1e6
#sigma_s=sigma_s/1e6
#pore_p=pore_p/1e6
#str_c=str_c/1e6

# Calculate lithostatic pressure
p_lith=rho_c*gravity*z / 1e6
#p_lith=p_lith/1e6

# Calculate mean stress
sigma_m=(sigma_1+sigma_3)/2
sigma_m_fluid=sigma_m-pore_p

# Plot Mohr circle
pylab.plot(sigma_n,sigma_s,'k--')
pylab.text(sigma_m-150,max(sigma_s)+10,'Mohr circle, dry',color='k')
pylab.plot(sigma_n_fluid,sigma_s,'b')
pylab.text(sigma_m_fluid-275,min(sigma_s)-50,'Mohr circle, fluid pressured',color='b')
pylab.plot(p_lith,str_c,'r')
pylab.plot(p_lith,-str_c,'r')
pylab.text(p_lith[45],str_c[99]+40,'Drucker-Prager, phi='+str(phi_c*180/pylab.pi),rotation=(pylab.sin(phi_c))*180/pylab.pi,color='r')
pylab.axis('equal')
pylab.xlabel('Normal stress [MPa]')
pylab.ylabel('Shear stress [MPa]')
pylab.axhline(y=0, xmin=0, xmax=1, color='k')
pylab.axvline(x=0, ymin=0, ymax=1, color='k')
pylab.scatter(xorigin,yorigin)
pylab.scatter(sigma_m,0,color='k')
pylab.scatter(sigma_m_fluid,0,color='b')

pylab.show()