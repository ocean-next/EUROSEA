#!/usr/bin/env  python
#=======================================================================
"""
StepHANIE Leroux
Collection of customed  tools related to  IMHOTEP project
"""
#=======================================================================

## standart libraries
import os,sys
import numpy as np

# xarray
import xarray as xr

#scipy
import scipy.signal as sps
import scipy.linalg as spl


# plot
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.cm as cm
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.colors import from_levels_and_colors
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def saveplt(fig,diro,namo,dpifig=300):
    fig.savefig(diro+namo, facecolor=fig.get_facecolor(),
                edgecolor='none',dpi=dpifig,bbox_inches='tight', pad_inches=0)
    plt.close(fig) 
    
    
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

def make_cmap(colors, position=None, bit=False):
    '''
    make_cmap takes a list of tuples which contain RGB values. The RGB
    values may either be in 8-bit [0 to 255] (in which bit must be set to
    True when called) or arithmetic [0 to 1] (default). make_cmap returns
    a cmap with equally spaced colors.
    Arrange your tuples so that the first color is the lowest value for the
    colorbar and the last is the highest.
    position contains values from 0 to 1 to dictate the location of each color.
    '''
    
    import matplotlib as mpl
    import numpy as np
    bit_rgb = np.linspace(0,1,256)
    if position == None:
        position = np.linspace(0,1,len(colors))
    else:
        if len(position) != len(colors):
            sys.exit("position length must be the same as colors")
        elif position[0] != 0 or position[-1] != 1:
            sys.exit("position must start with 0 and end with 1")
    if bit:
        for i in range(len(colors)):
            colors[i] = (bit_rgb[colors[i][0]],
                         bit_rgb[colors[i][1]],
                         bit_rgb[colors[i][2]])
    cdict = {'red':[], 'green':[], 'blue':[]}
    for pos, color in zip(position, colors):
        cdict['red'].append((pos, color[0], color[0]))
        cdict['green'].append((pos, color[1], color[1]))
        cdict['blue'].append((pos, color[2], color[2]))

    cmap = mpl.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    return cmap



def make_SLXcolormap(reverse=False,whichco='MJO',r=0,g=0,b=0):
    ''' Define a custom cmap .
    Parameters: 
    * Reverse (default=False). If true, will  create the reverse colormap
    * whichco (default='MJO': which colors to use. For now: only 'MJO', 'NCL', 'NCL_NOWI' available.
    ''' 

    ### colors to include in my custom colormap
    if whichco=='MJO':
        colors_NCLbipo=[(176,17,3,1),(255,56,8,1),(255,196,1,1),(255,255,255,1),(255,255,255,1),(13,176,255,1),(2,88,255,1),(0,10,174,1)]

    if whichco=='NCL':
        colors_NCLbipo=[(11,76,95),(0,97,128),(0,161,191),(0,191,224),(0,250,250),(102,252,252),(153,250,250),(255,255,255),(255,255,255),(252,224,0),(252,191,0),(252,128,0),(252,64,0),(252,33,0),(128,0,0),(0,0,0)]

    if whichco=='NCL_NOWI':
        colors_NCLbipo=[(11,76,95),(0,97,128),(0,161,191),(0,191,224),(0,250,250),(102,252,252),(153,250,250),(255,255,255),(252,224,0),(252,191,0),(252,128,0),(252,64,0),(252,33,0),(128,0,0),(0,0,0)]
        
    if whichco=='bluyello':
        colors_NCLbipo=[(11,76,95),(0,97,128),(0,161,191),(0,191,224),(0,250,250),(102,252,252),(153,250,250),(255,255,255),(252,224,0),(252,191,0),(252,128,0),(252,64,0),(252,33,0),(128,0,0),(0,0,0)]
        
    if whichco=='oneco':
        colors_NCLbipo=[(r,g,b),(0,0,0)]

    ### Call the function make_cmap which returns my colormap
    my_cmap_NCLbipo = make_cmap(colors_NCLbipo[:], bit=True)
    my_cmap_NCLbipo_r = make_cmap(colors_NCLbipo[::-1], bit=True)
    
    if reverse==True:
        my_cmap_NCLbipo = my_cmap_NCLbipo_r

    return(my_cmap_NCLbipo)



def printdatestringF(time,it,opt="hour"):
        '''
        Read time in xarray (datetime64 format) and return date in a set format (string)
        Parameters:
        time is the time coordinnate of an xarray, converted to index. For example time as input can be time = air.time.to_index() where air is the xarray of the temperature.
        it is the time index of the date to read and print
        '''    
        
        ## imports
        # xarray
        import xarray as xr
        
        if (time.hour[it]<12):
            adh=str("0")
        else:
            adh=str()
        if (time.month[it]<10):
            adm=str("0")
        else:
            adm=str()
        if (time.day[it]<10):
            add=str("0")
        else:
            add=str()    
            
        if (opt=="day"):
            retstring=str(time.year[it])+"-"+adm+str(time.month[it])+"-"+add+str(time.day[it])
        if (opt=="hour"):
            retstring=str(time.year[it])+"-"+adm+str(time.month[it])+"-"+add+str(time.day[it])+" "+adh+str(time.hour[it])+":00" 
        if (opt=="month"):
            retstring=str(time.year[it])+"-"+adm+str(time.month[it])
        if (opt=="year"):
            retstring=str(time.year[it])

        return(retstring)





def trpolyfit(xrar,fty='yr'):
    # Based on  http://atedstone.github.io/rate-of-change-maps/
    # convert to np array before applying polifit function
    # fty will be the parameter to indicate the frequency of. the input data. For now only works with 'yr' for yearly data.
    
    vals = xrar.values 
    years = xrar.time_counter.to_index().year.values

    # Reshape to an array with as many rows as years and as many columns as there are pixels
    vals2 = vals.reshape(len(years), -1)

    # Do a first-degree polyfit
    regressions = np.polyfit(years, vals2, 1)

    # Get the coefficients back
    trends = regressions[0,:].reshape(vals.shape[1], vals.shape[2])
    origins    = regressions[1,:].reshape(vals.shape[1], vals.shape[2])

    # make it back to xarray format
    xrtrends = xr.DataArray(
        data=trends,
        dims=["y", "x"],
        attrs=dict(
            description="trend coeff",
            units="(g/kg)/year"
        ),
    )

    xrorigins = xr.DataArray(
        data=origins,
        dims=["y", "x"],
        attrs=dict(
            description="b value",
            units="(g/kg)"
        ),
    )
    return xrtrends,xrorigins,years


def trseries(xrtrends,xrorigins,ty,tc):
    # Based on http://atedstone.github.io/rate-of-change-maps/
    ic=-1
    for iy in ty:
        ic = ic+1
        lintr  = iy*xrtrends
        lintro = xrorigins
        tmp = lintro.expand_dims(dim='time_counter',axis=0) + lintr.expand_dims(dim='time_counter',axis=0)
        if (ic!= 0):
            tr = xr.concat([tr, tmp], dim="time_counter")
        else:
            tr = tmp
    tr = tr.assign_coords({"time_counter": tc})
    return tr


def pltgridparam(reg='GLO',gridl=False,incrgridlon=45,incrgridlat=30,sath=35785831,minlat=-70.0,maxlat=84.0,minlon= -180,maxlon=179,loncentr=0,latcentr=10):
    # default gridlines parameters
    gridl=False
    incrgridlon=45
    incrgridlat=30
    #
    if reg=='gro':
        loncentr=-35
        latcentr=75
        sath=2085831
    if reg=='atl':
        loncentr=-35
        latcentr=10
        sath=35785831
    if reg=='ind':
        loncentr=90
        latcentr=0
        sath=35785831
    if reg=='GLO':
        minlat=-70.0
        maxlat=84.0
        minlon= -180
        maxlon=179
        loncentr=0
        incrgridlon=60
        incrgridlat=30 
    return gridl,incrgridlon,incrgridlat,sath,minlat,maxlat,minlon,maxlon,loncentr,latcentr

def pltaddfeatures(ax,incrgridlon,incrgridlat,onecohrml='#2E2E2E',reg='GLO',landedgeco='none'):
    
    rivers = cartopy.feature.NaturalEarthFeature(
        category='physical', name='rivers_lake_centerlines',
        scale='50m',facecolor='none',edgecolor='b')

    #lands = cartopy.feature.NaturalEarthFeature(
    #    category='physical', name='coastline',
    #    scale='50m',facecolor='none',edgecolor='k')

    cl2 = ax.add_feature(cfeature.LAND.with_scale('50m'),facecolor=onecohrml,edgecolor=landedgeco ,linewidth=0.2,alpha=1,zorder=5)
    clr = ax.add_feature(cartopy.feature.RIVERS,alpha=0.4,facecolor='none',edgecolor='#A9E2F3',zorder=6)
    clr2 = ax.add_feature(rivers,alpha=0.4,facecolor='none',edgecolor='#A9E2F3',zorder=6)  ##CEE3F6

    #========= GRIDLINES
    gl =ax.gridlines(xlocs=range(-180,181,incrgridlon), ylocs=range(-90,91,incrgridlat),draw_labels=True,linewidth=1, color='#585858', alpha=0.3, linestyle='--',zorder=8)
    label_style = {'size': 12, 'color': '#BDBDBD', 'weight': 'normal'}
    gl.xlabel_style = label_style
    #gl.xlabels_bottom = False
    gl.ylabel_style = label_style
    #gl.ylabels_right = False


    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axis('off')
    return ax,gl
