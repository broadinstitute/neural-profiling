import os
import pandas as pd
import config

plates = pd.read_csv('rem_plates.csv').iloc[:,1].tolist()
index = pd.read_csv('original_index.csv')
s3_location = config.LOC
wells = index.Metadata_Well.unique()
sites = index.Metadata_Site.unique()

for plate in plates:

    os.system('mkdir {}'.format(plate))
    big_csv = s3_location + 'full_csv/' + plate + '_loc.csv'
    os.system("aws s3 cp {} ./".format(big_csv))
    big_df = pd.read_csv(plate + '_loc.csv')

    for well in wells:
        for site in sites:
            sub_df = big_df.query("Image_Metadata_Well == @well & Image_Metadata_Site == @site")
            sub_df = sub_df[['Nuclei_Location_Center_X', 'Nuclei_Location_Center_Y']]

            try:
                sub_csv = index.query("Metadata_Plate == @plate & Metadata_Well == @well & Metadata_Site == @site").DNA.item()
                sub_csv_path = os.path.join(plate, sub_csv[11:-5] + '.csv')
                sub_df.to_csv(sub_csv_path, index=False)
            except:
                print('--------\nWARNING: On PLate {}, Well {} in site {}. There are no locations'.format(plate, well, site))
    upload_loc = s3_location + plate + '/'
    os.system("aws s3 mv --recursive {} {}".format(plate + '/', upload_loc))
    os.remove(plate + '_loc.csv')
    os.system("rm -rf {}".format(plate))

