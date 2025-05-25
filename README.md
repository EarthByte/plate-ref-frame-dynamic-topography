### Generate plate reference frame dynamic topography grids

🟢 Step 1:

In this dynamic_topography folder, start the docker container

`` docker run -p 8888:8888 --rm -it -v `pwd`:/workspace/ gplates/pygplates-dt ``

🟢 Step 2:

Check the following list and copy the reconstruction model into the "reconstructions" folder

https://drive.google.com/file/d/1zKTMStjwI9DlS4pSDwJWNfa06Ok1PswQ/view?usp=sharing

Edit model_config.py to add the new model

🟢 Step 3.

Copy the mantle frame grids into folder `./models/{*MODEL_NAME*}`

🟢 Step 4.

Open and run `generate_plate_ref_frame_grids.ipynb` and this will generate plate frame grids in folder `./models/{*MODEL_NAME*}/Dynamic_topography/dist/PlateFrame`

Open and run `generate_images.ipynb` and the images will be in folder `./models/{*MODEL_NAME*}/Dynamic_topography/dist`

🟢 Step 5.

Update portal (optional, only if you need add the model to GPlates Portal website)

Copy files to `portal_home/DynamicTopography/Models`

Change file `portal/dynamic_topography_models.py` and `portal/dynamic_topography.py`

On Dev server: <http://localhost:8888/portal/dynamic_topography_reset_db/>

On Prod server: <https://portal.gplates.org/portal/dynamic_topography_reset_db>

**Note:** Important! Please read!!

You need to have the "models" and "reconstructions" folders in the current working directory.
The two folders can be found at EarthByte NAS `/Public/EarthByteData/PlateRefFrameDynamicTopography`.

See [How to access the EarthByte NAS](https://www.earthbyte.org/ebytecentral/)

You also need to make a "tmp" directory in the current working directory.

### Generate dynamic topography profile

🟢 Generate a profile PNG plot

`python3 DynamicTopographyProfile.py 10 0 test.png ./ gld98`

🟢 Generate a CSV file containing the profile data

`python3 DynamicTopographyProfile.py 10 0 test.csv ./ gld98`

- 10 is the longitude
- 0 is the latitude
- test.png and test.csv is the output file name
- ./ means the current working directory
- gld98 is the model name

**Note:** Important! Please read!!

You need to copy the **data** folder into your current working directory from EarthByte NAS `/Public/EarthByteData/PlateRefFrameDynamicTopography`.

See [How to access the EarthByte NAS](https://www.earthbyte.org/ebytecentral/)
