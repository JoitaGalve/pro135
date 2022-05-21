import csv
import plotly.express as px
import pandas as pd
import plotly.express as px
rows = []

with open("stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
stars_data_rows = rows[1:]

print(headers)
print(stars_data_rows[0])

headers[0] = "row_num"
solar_system_stars_count = {}
for stars_data in stars_data_rows:
    if solar_system_stars_count.get(stars_data[2]):
        solar_system_stars_count[stars_data[2]] += 1

    else:
        solar_system_stars_count[stars_data[2]] = 1

max_solar_system = max(solar_system_stars_count, key = solar_system_stars_count.get)

print("Solar system {} has maximum stars {} out of the solar system we have discovered so far".format(max_solar_system, solar_system_stars_count[max_solar_system]))

sun_star = []

for stars_data in stars_data_rows:
    if max_solar_system == stars_data[2]:
        sun_star.append(stars_data)

#print(len(KOI_351_planet))
#print(KOI_351_planet)
sun_star_masses = []
sun_star_names = []

for planet_data in sun_star:
    sun_star_masses.append(stars_data[4])
    sun_star_names.append(stars_data[1])

sun_star_masses.append(1)
sun_star_names.append("Sun")

fig = px.bar(x = sun_star_names, y = sun_star_masses)
fig.show()

temp_data_rows = list(stars_data_rows)
print(temp_data_rows[0])

for planet_data in temp_data_rows:
    planet_mass = planet_data[3]
    
    if planet_mass.lower() == "unknown":
        stars_data_rows.remove(planet_data)
        
        continue
    else:
        planet_mass_value = planet_mass.split(' ')[0]
        planet_mass_ref = planet_mass.split(' ')[1]

        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8
            planet_data[3] = planet_mass_value
            planet_radius = planet_data[7]

            if planet_radius.lower() == "unknown":
                stars_data_rows.remove(planet_data)

                continue
            else:
                planet_radius_value = planet_radius.split()[0]
                planet_radius_ref = planet_radius.split()[2]

                if planet_radius_ref == "Jupiter":
                  planet_radius_value = float(planet_radius_value) * 11.2
                  planet_data[7] = planet_radius_value


KOI_351_planet = []

for planet_data in stars_data_rows:
    if max_solar_system == planet_data[11]:
        KOI_351_planet.append(planet_data)

print(len(KOI_351_planet))
print(KOI_351_planet)

KOI_351_planet_masses = []
KOI_351_planet_names = []

for planet_data in KOI_351_planet:
    KOI_351_planet_masses.append(planet_data[3])
    KOI_351_planet_names.append(planet_data[1])

KOI_351_planet_masses.append(1)
KOI_351_planet_names.append("Earth")

fig = px.bar(x = KOI_351_planet_names, y = KOI_351_planet_masses)
fig.show()


temp_planet_data_rows = list(stars_data_rows) 
for planet_data in temp_planet_data_rows: 
  if planet_data[1].lower() == "hd 100546 b": 
    stars_data_rows.remove(planet_data) 
planet_masses = [] 
planet_radiuses = [] 
planet_names = [] 

for planet_data in stars_data_rows: 
  planet_masses.append(planet_data[3]) 
  planet_radiuses.append(planet_data[7]) 
  planet_names.append(planet_data[1])

planet_gravity = [] 
print(planet_masses)
print(planet_radiuses)
print(planet_names)
for index, name in enumerate(planet_names): 
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11 
  planet_gravity.append(gravity) 

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names]) 
fig.show()

low_gravity_planets = []

for index, gravity in enumerate(planet_gravity):
  if gravity < 10:
    low_gravity_planets.append(stars_data_rows[index])

print(len(low_gravity_planets))

low_gravity_planets = []

for index, gravity in enumerate(planet_gravity):
  if gravity < 100:
    low_gravity_planets.append(stars_data_rows[index])

print(len(low_gravity_planets))

planet_type_values = []

for planet_data in stars_data_rows:
  planet_type_values.append(planet_data[6])

print(list(set(planet_type_values)))

planet_masses = []
planet_radiuses = []

for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])

fig = px.scatter(x = planet_radiuses, y = planet_masses)
fig.show()

from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt 
import seaborn as sns 

X = [] 
for index, planet_mass in enumerate(planet_masses): 
  temp_list = [ planet_radiuses[index], planet_mass ] 
  X.append(temp_list) 
wcss = [] 

for i in range(1, 11): 
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42) 
  kmeans.fit(X) 
  
  # inertia method returns wcss for that model 
  wcss.append(kmeans.inertia_) 
plt.figure(figsize=(10,5)) 
sns.lineplot(range(1, 11), wcss, marker='o', color='red') 
plt.title('The Elbow Method') 
plt.xlabel('Number of clusters') 
plt.ylabel('WCSS') 
plt.show()

planet_masses = [] 
planet_radiuses = [] 
planet_types = [] 

for planet_data in low_gravity_planets: 
  planet_masses.append(planet_data[3]) 
  planet_radiuses.append(planet_data[7]) 
  planet_types.append(planet_data[6]) 
  
fig = px.scatter(x=planet_radiuses, y=planet_masses, color=planet_types) 
fig.show()

suitable_planets = []

for planet_data in low_gravity_planets:
  if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth":
    suitable_planets.append(planet_data)

print(len(suitable_planets))

temp_suitable_planets = list(suitable_planets)
print(temp_suitable_planets)
for planet_data in temp_suitable_planets:
  if planet_data[8].lower() == "unknown":
    suitable_planets.remove(planet_data)

for planet_data in suitable_planets:
  if planet_data[9].split(' ')[1].lower() == "days":
    planet_data[9] = float(planet_data[9].split(" ")[0])

  else:
    planet_data[9] = float(planet_data[9].split(" ")[0]) * 365

  planet_data[8] = float(planet_data[8].split(" ")[0])

orbital_radiuses = []
orbital_planets = []

for planet_data in suitable_planets:
  orbital_radiuses.append(planet_data[8])
  orbital_planets.append(planet_data[9])

fig = px.scatter(x = orbital_radiuses, y = orbital_planets)
fig.show()

goldilocks_planets = list(suitable_planets)
temp_goldilock_planets = list(suitable_planets)

for planet_data in temp_goldilock_planets:
  if planet_data[8] < 0.38 or planet_data[8] > 2:
    goldilocks_planets.remove(planet_data)

print(len(suitable_planets))
print(len(goldilocks_planets))

planet_speeds = []

for planet_data in suitable_planets:
  distance = 2 * 3.14 * (planet_data[8] * 1.496e+9) 
  time = planet_data[9] * 86400
  speed = distance/time
  planet_speeds.append(speed)

speed_supporting_planets = list(suitable_planets)
temp_speed_supporting_planets = list(suitable_planets)

for index, planet_data in enumerate(temp_speed_supporting_planets):
  if planet_speeds[index] > 200:
    speed_supporting_planets.remove(planet_data)

print(len(speed_supporting_planets))

habitable_planets = []

for planet in speed_supporting_planets:
  if planet in goldilocks_planets:
    habitable_planets.append(planet)

print(len(habitable_planets))



final_dict = {}

for index, planet_data in enumerate(stars_data_rows):
  features_list = []
  gravity = (float(planet_data[3]) * 5.972e+24) / (float(planet_data[7]) * float(planet_data[7]) * 6371000 * 6371000) * 6.674e-11
  try:
    if gravity < 100:
      features_list.append("gravity")

  except:
    pass

  try:
    if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth":
      features_list.append("planet_type")

  except:
    pass

  try:
    if planet_data[8] > 0.38 or planet_data[8] > 2:
      features_list.append("goldilock")

  except:
    pass

  try:
    distance = 2 * 3.12 * (planet_data[8] * 1.496e+9)
    time = planet_data[9] * 86400
    speed = distance/time

    if speed < 200:
      features_list.append("speed")

  except:
    pass

  final_dict[index] = features_list

print(final_dict)

planet_count = 0

for key, value in final_dict.items():
  if "goldilock" in value:
    planet_count += 1

print(planet_count)

speed_planet_count = 0

for key, value in final_dict.items():
  if "speed" in value:
    speed_planet_count += 1

print(speed_planet_count)



df = pd.read_csv("stars.csv")
fig = px.bar(df, x = "star_mass", y = "host_name")
fig = px.bar(df, x = "star_radius", y = "host_name")
fig = px.bar(df, x = "star_distance", y = "host_name")
fig.show()


