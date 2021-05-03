## standart libraries
import os,sys
import numpy as np

from scipy.signal import argrelmax
from scipy.stats import linregress

# xarray
import xarray as xr

# plot
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.cm as cm
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.colors import from_levels_and_colors
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#import cmocean


# custom tools
import lib_eurosea

def plotmapMEDWEST(fig1,ax,ehonan,nav_lon,nav_lat,cmap,norm,plto='tmp_plot',typlo='pcolormesh',coastL=False,coastC=False,coastLand=False,xlim=(0,10), ylim=(0,10),su='b',so='k',loncentr=0.,latcentr=0.,labelplt="",incrgridlon=5,incrgridlat=5,edgcol1='#585858',edgcol2='w',mk="o",mks=0.1,scattcmap=True,scattco='k',alpha=1):

        # Projection
        trdata  = ccrs.PlateCarree() 
        
        ax = plt.axes(projection= ccrs.PlateCarree())
        ax.outline_patch.set_edgecolor(edgcol2)

        gridl=True
        if gridl:
            # gridlines
            gl = ax.gridlines(draw_labels=True,linewidth=1, color='#585858', alpha=0.2, linestyle='--')
            # grid labels
            #label_style = {'size': 12, 'color': 'black', 'weight': 'bold'}
            label_style = {'size': 12, 'color': '#BDBDBD', 'weight': 'normal'}
            
            gl.xlabel_style = label_style
            gl.xlabels_bottom = False
            gl.xlocator = mticker.FixedLocator(np.arange(-180,180,incrgridlon,dtype=float))
            gl.ylabel_style = label_style
            gl.ylabels_right = False
            gl.ylocator = mticker.FixedLocator(np.arange(-90,90,incrgridlat,dtype=float))

        # Add Coastlines and or plain continents
        if coastC:
            ax.add_feature(ccf.COASTLINE, facecolor='w', edgecolor='none')
        if coastLand:
            ax.add_feature(ccf.LAND, facecolor='w', edgecolor='none')
        if coastL:
            #ax.coastlines(color='#585858',linewidth=1)
             ax.coastlines(color='w',linewidth=1)
        
        ### PLOTS: 
        if typlo=='pcolormesh':
            cs  = plt.pcolormesh(nav_lon, nav_lat, ehonan,cmap=cmap,transform=trdata,norm=norm,alpha=alpha,shading='nearest')
            
        if typlo=='contourf':
            cs  = plt.contourf(nav_lon, nav_lat, ehonan,transform=trdata,levels=levels,norm=norm,cmap=cmap,alpha=alpha, extend='both')

        # geographical limits
        plt.xlim(xlim)
        plt.ylim(ylim)   
        return cs,ax
        
        
def saveplt(fig,diro,namo,dpifig=300):
    fig.savefig(diro+namo, facecolor=fig.get_facecolor(), edgecolor='none',dpi=dpifig,bbox_inches='tight', pad_inches=0)
    plt.close(fig) 

def mycolormap(levbounds,cm_base='Spectral_r',cu='w',co='k',istart=0):
    lmin = levbounds[0]
    lmax = levbounds[1]
    incr = levbounds[2]
    levels = np.arange(lmin,lmax,incr)
    if ( (cm_base=='NCL') | (cm_base=='MJO') | (cm_base=='NCL_NOWI') ):
        nice_cmap = slx.make_SLXcolormap(whichco=cm_base)
    else:
        nice_cmap = plt.get_cmap(cm_base)
    colors = nice_cmap(np.linspace(istart/len(levels),1,len(levels)))[:]
    cmap, norm = from_levels_and_colors(levels, colors, extend='max')
    cmap.set_under(cu)
    cmap.set_over(co)
    return cmap,norm
    
def addcolorbar(fig,cs,ax,levbounds,levincr=1,tformat="%.2f",tlabel='',shrink=0.45,facmul=1.,orientation='vertical',tc='k',loc='lower right',wth="15%",bbta=(0.08, -0.1,0.9,0.2)):
    lmin = levbounds[0]
    lmax = levbounds[1]
    incr = levbounds[2]
    levels = np.arange(lmin,lmax,incr)
    cblev = levels[::levincr]
    
    if orientation =='horizontal':
        axins1 = inset_axes(ax,
                        height=wth,  # height : 5%
                            width="50%",
                        bbox_to_anchor=bbta,
                        bbox_transform=ax.transAxes,
                        borderpad=0)

    if orientation =='vertical':
        axins1 = inset_axes(ax,
                        height="50%",  # height : 5%
                            width="2%",
                        loc='center left',
                       borderpad=2)

    cb = fig.colorbar(cs,cax=axins1,
                                    extend='both',                   
                                    ticks=cblev,
                                    spacing='uniform',
                                    orientation=orientation,
                                    )
    
    new_tickslabels = [tformat % i for i in cblev*facmul]
    cb.set_ticklabels(new_tickslabels)
    cb.ax.set_xticklabels(new_tickslabels, rotation=70,size=10,color=tc)
    cb.ax.tick_params(labelsize=10,color=tc) 
    cb.set_label(tlabel,size=14,color=tc)
    
