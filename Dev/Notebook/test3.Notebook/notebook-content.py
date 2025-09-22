# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "aa8e1acb-4ac6-4599-a161-fb26b20cd886",
# META       "default_lakehouse_name": "TEST_KM_Bronze_LH",
# META       "default_lakehouse_workspace_id": "62f10259-ac2d-461a-bda1-ef452bc0d836",
# META       "known_lakehouses": [
# META         {
# META           "id": "aa8e1acb-4ac6-4599-a161-fb26b20cd886"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.sql("SELECT * FROM TEST_KM_Bronze_LH.Offices LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
