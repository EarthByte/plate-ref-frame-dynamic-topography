import pygplates
import glob, re
import numpy as np
#import xarray as xr
import sys, os
sys.path.append('/Users/Simon/GIT/gplates-web/django/GWS/utils/')
from sphere_tools import sampleOnSphere


def create_model_file_list_by_time(ModelPath,modelnum,Frame='Plate',Res='Hi'):

    # if Res is none, there is no subfolders with Hi and Lo Resolution grids (e.g. Rakib's models)
    if Res is None:
        file_list = glob.glob(f'{ModelPath}/{modelnum}/Dynamic_topography/{Frame}Frame/*.nc')
        file_list.extend(glob.glob(f'{ModelPath}/{modelnum}/Dynamic_topography/{Frame}Frame/*.grd'))
    # For Nico's models, there will be Hi and Lo Resolution versions - and, for Mantle Frame we force the -180/180 version
    else:
        if Frame is 'Mantle':
            file_list = glob.glob(f'{ModelPath}/{modelnum}/Dynamic_topography/{Res}Res/{Frame}Frame_180/*.nc')
            file_list.extend(glob.glob(f'{ModelPath}/{modelnum}/Dynamic_topography/{Res}Res/{Frame}Frame_180/*.grd'))
        else:
            file_list = glob.glob(f'{ModelPath}/{modelnum}/Dynamic_topography/{Res}Res/{Frame}Frame/*.nc')
            file_list.extend(glob.glob(f'{ModelPath}/{modelnum}/Dynamic_topography/{Res}Res/{Frame}Frame/*.grd'))

    model_time_list = []
    # Note this method to extract times from filenames will not detect decimal places in age
    for filename in file_list:
        f = os.path.basename(filename)
        f = re.sub(modelnum, '', f)
        if f.startswith('.'):
            f = f[1:]
            print(f)
        time = float(re.findall(r'\d*\.\d+|\d+',f)[-1])
        model_time_list.append((time,filename))

    model_time_list = sorted(model_time_list, key=lambda model: model[0])

    return model_time_list


def plate_frame_profile(model_time_list,PtLon,PtLat):

    profile = []

    # iterate over reconstruction times
    for TIME,FNAME in model_time_list:

        #result = sample_grid_using_kdtree(PtLon,PtLat,InputGridFile)
        result = sample_grid_using_kdtree(PtLon,PtLat,FNAME)
        profile.append(result)

    return np.asarray(profile)


def sample_grid_using_kdtree(PtLon,PtLat,FNAME):

    ds_disk = xr.open_dataset(FNAME)
    keys = list(ds_disk.keys())
    data_array = ds_disk[keys[2]]
    lon_array = data_array.coords[keys[0]]
    lat_array = data_array.coords[keys[1]]

    inputLons,inputLats = np.meshgrid(lon_array,lat_array)

    d,l = sampleOnSphere(inputLats,inputLons,data_array, PtLat, PtLon, tree=None, n=16)


#################################################
def sample_grid_using_scipy(x,y,grdfile):

    data=Dataset(grdfile,'r')
    try:
        lon = np.copy(data.variables['x'][:])
        lat = np.copy(data.variables['y'][:])
    except:
        lon = np.copy(data.variables['lon'][:])
        lat = np.copy(data.variables['lat'][:])

    Zg = data.variables['z'][:]

    #test = inpaint.fill_ndimage(Zg)
    mask = np.isnan(Tm)
    Tmm = np.ma.masked_array(Tm)
    Tmmf = np.ma.fix_invalid(Tmmf,fill_value=-9999999)

    lut=spi.RectBivariateSpline(lon,lat,Tmmf.T)
    result = []
    if len(np.asarray((x,y)).shape)==1:
        result.append(lut(x,y)[0][0])
    else:
        for xi,yi in zip(x,y):
            result.append(lut(xi, yi)[0][0])
    
    result[np.where(result<-999999)] = np.nan
    
    return result

