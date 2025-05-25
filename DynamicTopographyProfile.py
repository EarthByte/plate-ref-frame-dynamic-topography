# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
import io, os, re
import numpy as np
#from scipy.io import netcdf_file as netcdf
from netCDF4 import Dataset
#from scipy.interpolate import RectBivariateSpline
from scipy.interpolate import RegularGridInterpolator 
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
#########
#%matplotlib inline
def get_profile(PtLon, PtLat, filename=None, home=None, model=None, co=False):
    if not model:
        model = 'gld21'
    if not home:
        home = './'

    file_list=[]
    for dirpath, dirs, files in os.walk(home + '/data/DynamicTopography/Models/'+model+'/PlateFrame/'):
        file_list=[f for f in files if f.endswith('.nc')]
        break

    time_list = []
    for f in file_list:
        numbers = re.findall(r"\d*\.\d+|\d+", f)

        if len(numbers) == 1:
            time_list.append(numbers[0])
        elif len(numbers) > 1:
            time_list.append(numbers[-1])
        else:
            continue
            
    time_list = list(set(time_list))
    time_list = sorted(time_list, key=lambda x: float(x))

    # Empty Min and Max vales - we will use these to store the min,max of the full range of grids
    GridMin = 999999 
    GridMax = -999999

    TopoProfile = np.zeros(len(time_list))

    index=0
    for reconstruction_time in time_list:
        if co:
            InputGridFile = home + '/data/DynamicTopography/Models/'+model+"/PlateFrame/Masked_"+reconstruction_time+'.nc'
            if not os.path.isfile(InputGridFile):
                InputGridFile = home + '/data/DynamicTopography/Models/'+model+"/PlateFrame/"+reconstruction_time+'.nc'    
        else:
            InputGridFile = home + '/data/DynamicTopography/Models/'+model+"/PlateFrame/"+reconstruction_time+'.nc'
        
        data = Dataset(InputGridFile,'r')
        Tm = data.variables['z'][:].T
        mask = np.isnan(Tm)
        x = np.ma.masked_array(Tm)
        y = np.ma.fix_invalid(x,fill_value=-999999)
        #f=RectBivariateSpline(data.variables['lon'][:],data.variables['lat'][:],y)

        gridX,gridY = np.meshgrid(data.variables['lon'][:],data.variables['lat'][:])
        coords = tuple([np.array(data.variables['lon'][:]),np.array(data.variables['lat'][:])])
        f=RegularGridInterpolator(coords,y,method='linear', bounds_error=True, fill_value=None)

        #TopoProfile[index] = (f(PtLon, PtLat)[0])
        TopoProfile[index] = f((PtLon, PtLat))

        # Get min,max for this grid, then see if it is bigger than the existing min,max for whole sequence
        GridMin = min(GridMin,y.min())
        GridMax = max(GridMax,y.max())
        #import sys
        #sys.stderr.write('{0}\n'.format(GridMin))        

        index=index+1     

    TopoProfile[np.where(TopoProfile<-3000)] = np.nan
    data_len = np.count_nonzero(~np.isnan(TopoProfile))
# <codecell>

#import numpy.ma as ma
#mask = np.isnan(Tm)
#x = ma.masked_array(Tm)
#y = ma.fix_invalid(x,fill_value=-9999)
    if os.path.splitext(filename)[1] == '.csv':
        with open(filename, 'w+') as f:
            f.write('#Lon: '+str(PtLon)+', Lat: '+str(PtLat)+'\n')
            f.write('#Time,Elevation \n')
            for i in zip(time_list,TopoProfile):
                f.write(str(i[0]) +','+ str(i[1])+'\n')
        return

    time_list_float = [float(i) for i in time_list]

    fig = plt.figure(figsize=(10,7),dpi=300)
    plt.plot(time_list_float,TopoProfile,'-o',linewidth=5,markersize=12)
    plt.gca().grid()
    plt.gca().invert_xaxis()
    plt.xlim([np.max(time_list_float)+10,np.min(time_list_float)-10])
    #plt.ylim([np.floor(GridMin/200)*200,np.ceil(GridMax/200)*200])
    #plt.yticks(np.arange(np.floor(GridMin/200)*200,1+np.ceil(GridMax/200)*200,200))    
    #import sys
    #sys.stderr.write(np.array_str(TopoProfile)+str(data_len) )
    if data_len != 0:
        plt.ylim([np.min(TopoProfile[:data_len])-100, np.max(TopoProfile[:data_len])+100]) 
    #else:
    #    plt.ylim([np.min(TopoProfile)-100, np.max(TopoProfile)+100])
    y_label = 'Elevation (m)'
    if model == 'M7Rate':
        y_label = 'Rate (m/Ma)'
    plt.ylabel(y_label, fontsize=14)
    plt.xlabel('Time (Ma)',fontsize=14)
    title_begin = 'Dynamic Topography'
    if model == 'M7Rate':
        title_begin = 'Dynamic Topography Change Rate'
    plt.title(title_begin + ' at Lon '+str(PtLon)+', Lat '+str(PtLat),fontsize=14)
    #plt.show()
    if filename:
        fig.savefig(filename)
        plt.close("all");
        return
    else:
        imgdata = io.StringIO()
        fig.savefig(imgdata, format='png', bbox_inches='tight')
        imgdata.seek(0)
        plt.close("all");
        return imgdata
# <codecell>

import sys
if __name__ == "__main__":
    if(len(sys.argv)) == 7:
        get_profile(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], True)
    else:
        get_profile(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
