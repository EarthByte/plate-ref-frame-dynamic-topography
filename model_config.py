M1R = './reconstructions/M1_reconstruction/'
M2013= './reconstructions/Global_Model_WD_Internal_Release_2013.2-r213/'
M2015_v2 = './reconstructions/Global_Model_WD_Internal_Release_2015_v2/'
Mterra = './reconstructions/terra/'
M2014_1_401 = './reconstructions/2014_1_401/'
Mdynto_smean = './reconstructions/Caltech_Global_20101129/'
M2014_1_380 = './reconstructions/Global_Model_WD_Internal_Release_2014.1-r380/'
M2015_v2_873 = './reconstructions/Global_Model_WD_Internal_Release_2015_v2-r873'
M2014_1_399 = './reconstructions/Global_Model_WD_Internal_Release_2014.1-r399'
M2013_1_183 = './reconstructions/Global_Model_WD_Internal_Release_2013.1-r183'
M2013_2_252 = './reconstructions/Global_Model_WD_Internal_Release_2013.2-r252'
M2015_2_702 = './reconstructions/Global_Model_WD_Internal_Release_2015_v2-r702'
M2013_1_206 = './reconstructions/Global_Model_WD_Internal_Release_2013.1-r206'
M2015_1_618 = './reconstructions/Global_Model_WD_Internal_Release_2015_v1-r618'
M2014_1_409 = './reconstructions/Global_Model_WD_Internal_Release_2014.1-r409'
M2016_6_1009 = './reconstructions/Global_Model_WD_Internal_Release_2016_v6-r1009'
M2016_5_1018 = './reconstructions/Global_Model_WD_Internal_Release_2016_v5-r1018'
#gld428_recon_dir = './reconstructions/gld428'
M21NNR = './reconstructions/M21NNR'
gld428_recon_dir = M21NNR

model_defs = {
    'M1':{
        'multipoint'        :   M1R+'lat_lon_velocity_domain_180_360.gpmlz',
        'rotations'         :   [
                                    M1R+'Caltech_Global_20101129.rot'
                                ],
        'coastlines'        :   M1R+'Global_EarthByte_GPlates_Coastlines_20111013.gpmlz',
        'static_polygons'   :   M1R+'Global_EarthByte_GPlates_PresentDay_StaticPlatePolygons_20111012.gpmlz',
    },
    
    'M2':{
        'multipoint'        :   M2013 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'rotations'         :   [
                                    M2013 + 'Andes_Flat_Slabs_2013.2.rot',
                                    M2013 + 'Andes_Rotations_2013.2.rot',
                                    M2013 + 'AUSANT_DeformingModel_2013.2.rot',
                                    M2013 + 'AUSLHR_DeformingModel_2013.2.rot',
                                    M2013 + 'Global_EarthByte_TPW_CK95G94_2013.2.rot',
                                    M2013 + 'NAM_displacements_as_poles_2013.2.rot',
                                    M2013 + 'NAM_Flat_Slab_2013.2.rot',
                                    M2013 + 'SATL_HeineModel_Rotations_2013.2.rot'
                                ],
        'coastlines'        :   M2013 + '/StaticGeometries/Global_EarthByte_CK95G94_Coastlines_2013.2_20130828.gpmlz',
        'topology_dir'      :   M2013
    },
    
    'M7':{
        'multipoint'        :   M2015_v2+'/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'rotations'         :   [
                                    M2015_v2+'Andes_Flat_Slabs_2015_v2.rot',
                                    M2015_v2+'AUSLHR_DeformingModel_2015_v2.rot',
                                    M2015_v2+'Global_EB_410-250Ma_GK07_2015_v2.rot',
                                    M2015_v2+'NAM_Flat_Slab_2015_v2.rot',
                                    M2015_v2+'Andes_Rotations_2015_v2.rot',
                                    M2015_v2+'Eurasia_Arabia_DeformingModel_Rotations_2015_v2.rot',
                                    M2015_v2+'GoM_displacements_as_poles_2015_v2.rot',
                                    M2015_v2+'SATL_HeineModel_Rotations_2015_v2.rot',
                                    M2015_v2+'AUSANT_DeformingModel_2015_v2.rot',
                                    M2015_v2+'Global_EB_250-0Ma_GK07_2015_v2.rot',
                                    M2015_v2+'NAM_displacements_as_poles_2015_v2.rot',
                                ],
        'coastlines'        :   M2015_v2+'StaticGeometries/Coastlines/Global_coastlines_2015_v2_low_res.shp' ,
        'topology_dir'      :   M2015_v2 
    },
    'terra':{
        'rotations'         :   [
                                    Mterra + 'Rotation/Shephard_etal_ESR2013_Global_EarthByte_2013.rot'
                                ],
        'coastlines'        :   Mterra + 'Coastlines/Shephard_etal_ESR2013_Global_Coastlines_cookiecuttostatic.shp',
        'multipoint'        :   Mterra + 'MultipointGrid/lat_lon_velocity_domain_360.shp',
        'topology_dir'      :   Mterra + 'COB'
    },
    'M4':{
        'multipoint'        :   M2014_1_401+'/domain_points/lat_lon_velocity_domain_720_1440.gpml',
        'rotations'         :   [
                                    M2014_1_401+'Andes_Flat_Slabs_2014.1.rot',
                                    M2014_1_401+'AUSANT_DeformingModel_2014.1.rot',
                                    M2014_1_401+'Global_EarthByte_TPW_GeeK07_2014.1_VanDerMeer_CrossoverFix.rot',
                                    M2014_1_401+'NAM_Flat_Slab_2014.1.rot',
                                    M2014_1_401+'WesternTethys_DeformingModel_2014.1.rot',
                                    M2014_1_401+'SATL_HeineModel_Rotations_2014.1.rot',
                                    M2014_1_401+'NAM_displacements_as_poles_2014.1.rot',
                                    M2014_1_401+'AUSLHR_DeformingModel_2014.1.rot',
                                    M2014_1_401+'Andes_Rotations_2014.1.rot',
                                ],
        'coastlines'        :   M2014_1_401+'/StaticGeometries/Global_EarthByte_GeeK07_Coastlines_2014.1.gpmlz' ,
        'topology_dir'      :   M2014_1_401 
    },
    'gld98':{
        'multipoint'        :   M2014_1_380+'/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2014_1_380+'/StaticGeometries/Global_EarthByte_GeeK07_Coastlines_2014.1.gpmlz' ,
        'topology_dir'      :   M2014_1_380,
        'rotation_dir'      :   M2014_1_380,
    },
    'gld107':{
        'multipoint'        :   M2014_1_399+'/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2014_1_399+'/StaticGeometries/Global_EarthByte_GeeK07_Coastlines_2014.1.gpmlz' ,
        'topology_dir'      :   M2014_1_399,
        'rotation_dir'      :   M2014_1_399,
    },
    'gld241':{
        'multipoint'        :   M2015_v2_873+'/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2015_v2_873+'/StaticGeometries/Global_Coastlines_2015_v2_low_res.gpml' ,
        'topology_dir'      :   M2015_v2_873,
        'rotation_dir'      :   M2015_v2_873,
    },
    'gld24':{
        'multipoint'        :   M2013_1_183 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2013_1_183 + '/StaticGeometries/Global_EarthByte_CK95G94_Coastlines_2013.1_20130521.gpml' ,
        'topology_dir'      :   M2013_1_183,
        'rotation_dir'      :   M2013_1_183,
    },
    'gld95':{
        'multipoint'        :   M2013_2_252 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2013_2_252 + '/StaticGeometries/Global_EarthByte_CK95G94_Coastlines_2013.2_20130828.gpmlz' ,
        'topology_dir'      :   M2013_2_252,
        'rotation_dir'      :   M2013_2_252,
    },
    'gld189':{
        'multipoint'        :   M2015_2_702 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2015_2_702 + '/StaticGeometries/Coastlines/Global_coastlines_2015_v2_low_res.shp' ,
        'topology_dir'      :   M2015_2_702,
        'rotation_dir'      :   M2015_2_702,
    },
    'gld31':{
        'multipoint'        :   M2013_1_206 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2013_1_206 + '/StaticGeometries/Global_EarthByte_CK95G94_Coastlines_2013.1_20130521.gpml' ,
        'topology_dir'      :   M2013_1_206,
        'rotation_dir'      :   M2013_1_206,
    },
    'gld216':{
        'multipoint'        :   M2015_1_618 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2015_1_618 + '/StaticGeometries/Global_Coastlines_2015_v1_low_res.gpml' ,
        'topology_dir'      :   M2015_1_618,
        'rotation_dir'      :   M2015_1_618,
    },
    'gld162':{
        'multipoint'        :   M2014_1_409 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2014_1_409 + '/StaticGeometries/Global_EarthByte_GeeK07_Coastlines_2014.1.gpmlz' ,
        'topology_dir'      :   M2014_1_409,
        'rotation_dir'      :   M2014_1_409,
    },
    'gld321':{
        'multipoint'        :   M2016_6_1009 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2016_6_1009 + '/StaticGeometries/Global_Coastlines_2016_v6_low_res.gpml' ,
        'topology_dir'      :   M2016_6_1009,
        'rotation_dir'      :   M2016_6_1009,
        'static_polygons'   :   M2016_6_1009 + '/StaticGeometries/StaticPolygons/Global_EarthByte_GPlates_PresentDay_StaticPlatePolygons_2016_v6.shp'
    },
    'gld324':{
        'multipoint'        :   M2016_5_1018 + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M2016_5_1018 + '/StaticGeometries/Coastlines/Global_coastlines_2016_v5_low_res.shp' ,
        'topology_dir'      :   M2016_5_1018,
        'rotation_dir'      :   M2016_5_1018,
        'static_polygons'   :   M2016_5_1018 + '/StaticGeometries/StaticPolygons/Global_EarthByte_GPlates_PresentDay_StaticPlatePolygons_2016_v5.shp'
    },
    'gld428':{
        'multipoint'        :   gld428_recon_dir + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   gld428_recon_dir + '/static_geometries/GSHHS_l_coastlines.gpmlz',
        'topology_dir'      :   gld428_recon_dir,
        'rotation_dir'      :   gld428_recon_dir,
        'static_polygons'   :   gld428_recon_dir + '/shapes_static_polygons_Merdith_et_al.gpml'
    },
    'gld428_m21':{
        'multipoint'        :   M21NNR + '/domain_points/lat_lon_velocity_domain_720_1440.shp',
        'coastlines'        :   M21NNR + '/static_geometries/GSHHS_l_coastlines.gpmlz',
        'topology_dir'      :   M21NNR,
        'rotation_dir'      :   M21NNR,
        'static_polygons'   :   M21NNR + '/shapes_static_polygons_Merdith_et_al.gpml'
    },
}


model_defs['gld108'] = model_defs['M4'] 
model_defs['gld115n'] = model_defs['gld115'] = model_defs['gld98'] 
model_defs['gld134'] = model_defs['gld112'] = model_defs['gld119'] = model_defs['gld136'] = model_defs['gld118'] = model_defs['gld91'] = model_defs['gld89'] = model_defs['gld95']
model_defs['gld226'] = model_defs['gld225'] = model_defs['gld130'] = model_defs['gld224'] = model_defs['gld123'] = model_defs['gld95']
model_defs['gld37'] = model_defs['gld34'] = model_defs['gld31']
model_defs['gld230'] = model_defs['gld214'] = model_defs['gld215'] = model_defs['gld217'] = model_defs['gld216']
model_defs['M3'] = model_defs['M7'] 
model_defs['M5'] = model_defs['M2'] 
model_defs['M6'] = model_defs['M7'] 
model_defs['dynto_smean'] = model_defs['M1']
model_defs['dynto_ngrand'] = model_defs['M1']
model_defs['dynto_s20rts'] = model_defs['M1']
model_defs['C1'] = model_defs['M7']
model_defs['C1s'] = model_defs['M7']
model_defs['C2'] = model_defs['M7']
model_defs['C3'] = model_defs['M7']
model_defs['C6'] = model_defs['M7']
model_defs['C4'] = model_defs['M2']
model_defs['C5'] = model_defs['M2']
model_defs['gld106'] = model_defs['M4']
model_defs['gld179'] = model_defs['gmcm9'] = model_defs['gld205'] = model_defs['gld200'] = model_defs['gld178'] = model_defs['gld189']
