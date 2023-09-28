import arcpy
import os

gdb_path = r"D:\Sem 3\Prog_3\P_4\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
hist_fc_name = "Wilson_Histdist"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
hist_fc_path = os.path.join(gdb_path, hist_fc_name)

# Converting a feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")
arcpy.management.MakeFeatureLayer(hist_fc_path, "hist_dist_lyr")

# getting count of all the features before applying selection
pre_count = arcpy.GetCount_management("restaurant_lyr")
print("Count of total number of restaurant before applying selection is {}".format(pre_count[0]))

arcpy.management.SelectLayerByLocation("restaurant_lyr", "WITHIN_A_DISTANCE", "hist_dist_lyr", "500 feet")

post_count = arcpy.GetCount_management("restaurant_lyr")
print("The count of restaurant within a distance of 500ft are {}".format(post_count[0]))

restaurants_500ft = "Wilson_Restaurants_within_500ft"
restaurants_500ft_path = os.path.join(gdb_path, restaurants_500ft)

arcpy.management.CopyFeatures("restaurant_lyr", restaurants_500ft_path)


print("Process Completed")
