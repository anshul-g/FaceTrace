import os
import pandas as pd
image_dir = os.path.join("database")
data = []

for index, filename in enumerate(os.listdir(image_dir), start=1):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        new_name = filename.replace(" ", "_")
        os.rename(str(image_dir) + os.path.sep + filename, str(image_dir)+os.path.sep + new_name)
        print(new_name)
        record_name = new_name[:-4].replace("_"," ")
        data.append([record_name, new_name, index])
        

df = pd.DataFrame(data, columns=['name', 'image', 'roll_no'])
df.to_excel("database/people_db.xlsx")
