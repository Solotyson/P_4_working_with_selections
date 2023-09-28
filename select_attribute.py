# Commonly used terms when working with selections

# Feature class: A table containing an attribute field that stores geometery that defines shape of a feature.
# Feature layer: An in-memory representation of the data in the feature class

# Table: A storage container for rows that coontain fields to store data
# TableView: an in-memory representation of the data in a table

import arcpy
import os

gdb_path = r"D:\Sem 3\Prog_3\P_4\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)

# Converting a feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")

# getting count of all the festures before applying selection
pre_count = arcpy.GetCount_management("restaurant_lyr")
print("Count of total number of restaurant before applying selection is {}".format(pre_count[0]))

# Applying Select by Attribute to get the restaurants serving alcohol
arcpy.management.SelectLayerByAttribute("restaurant_lyr", "NEW_SELECTION", "ALCOHOL = 1")

# Getting count of selection
post_count = arcpy.GetCount_management("restaurant_lyr")
print("The count of restaurant containing alcohol after applying the selection is {}".format(post_count[0]))

# output_alcohol_restaurants = "Wilson_Restaurants_Alcohol"
# output_alcohol_restaurants_path = os.path.join(gdb_path, output_alcohol_restaurants)
#
# # Converting the feature layer to feature class (only selected feature will be saved)
# arcpy.management.CopyFeatures("restaurant_lyr", output_alcohol_restaurants_path)

print("process completed")