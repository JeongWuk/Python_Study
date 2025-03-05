# 요구사항
# 1. 사용자로부터 난파선 이름을 입력 받는다.
# 2. 난파선 csv파일을 읽어서 해당 난파선 데이터를 추출한다.
# 3. 다양한 visualization 도구를 활용하여 데이터를 보여준다.

# 학습내용
# 1. 파이썬으로 csv파일을 읽을 수 있다.
# 2. 사용자로부터 입력을 받을 수 있다.
# 3. csv파일로부터 필요한 데이터를 추출할 수 있다.


import turtle, worldmap

file = open("famous_shipwrecks.csv","r")

header = file.readline().strip().split(',')

try:
  ship_name_index = header.index('Ship Name')
  date_sank_index = header.index('Date Sank')
  date_discovered_index = header.index('Year Discovered')
  location_index = header.index('Sea/Ocean')
  longitude_index = header.index('Longitude')
  latitude_index = header.index('Latitude')
  depth_index = header.index('Depth (meters)')
  vessel_type_index = header.index('Type of Vessel')
except ValueError:
  print("One or more columns are missing in the CSV file.")
  exit()

user_input = input("Enter the name of a famous shipwreck: ")

found = False

for line in file:
   row = line.strip().split(',')

   if row[ship_name_index].strip() == user_input:
      ship_name = row[ship_name_index].strip()
      date_sank = row[date_sank_index].strip()
      date_discovered = row[date_discovered_index].strip() if date_discovered_index < len(row) else "Not Available"
      location = row[location_index].strip()
      longitude = row[longitude_index].strip()
      latitude = row[latitude_index].strip()
      depth = row[depth_index].strip()
      vessel_type = row[vessel_type_index].strip()
      found = True
      break
  
if not found:
   print(f"No shipwreck found with the name '{user_input}'")

file.close()

#Output informationon screen
print(f"Ship Name: {ship_name}")
print(f"Date Sank: {date_sank}")
print(f"Date Discovered: {date_discovered}")
print(f"Location: {location}")
print(f"Longitude: {longitude}")
print(f"Latitude: {latitude}")
print(f"Depth: {depth}m")
print(f"Type of Vessel: {vessel_type}")

#Plot the shipwreck on the map  
worldmap.plot(longitude, latitude)


