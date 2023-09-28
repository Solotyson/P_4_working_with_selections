import arcpy
import os

gdb_path = r"D:\Sem 3\Prog_3\P_4\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
hist_fc_name = "Wilson_Histdist"
crime_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
hist_fc_path = os.path.join(gdb_path, hist_fc_name)
crime_fc_path = os.path.join(gdb_path, crime_fc_name)

# Converting a feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")
arcpy.management.MakeFeatureLayer(hist_fc_path, "hist_dist_lyr")
arcpy.management.MakeFeatureLayer(crime_fc_path, "crime_lyr")


arcpy.management.SelectLayerByAttribute("restaurant_lyr", "NEW_SELECTION", "ALCOHOL = 1")
arcpy.management.SelectLayerByLocation("restaurant_lyr", "WITHIN_A_DISTANCE", "hist_dist_lyr", "1000 feet","SUBSET_SELECTION")
arcpy.management.SelectLayerByLocation("crime_lyr", "WITHIN_A_DISTANCE", "restaurant_lyr", "500 feet","SUBSET_SELECTION")
arcpy.management.SelectLayerByAttribute("crime_lyr", "SUBSET_SELECTION", "ALCOHOL > 0")


post_count = arcpy.GetCount_management("crime_lyr")
print("The count of crime near restaurantS are {}".format(post_count[0]))


print("process completed")