import googlemaps
from datetime import datetime
import re
import time
import gpxpy
import gpxpy.gpx
import math


"""Initiates the gmap client by booting api key from a text file

Returns:
    GMap Client -- Portal to accessing the Google Maps API
"""


def initiate_gmap_client():
    # reads the api key from a file for security purposes
    api_key = open("api_key.txt", "r").readline()
    gmaps = googlemaps.Client(key=api_key)

    return gmaps


def read_destination_address(file_path):
    return open(file_path, 'r').readline()

def confirm_address(destination_address):
    return "Just to confirm, you want to go to {}".format(destination_address)


"""Geocodes both the start and destination addresses using Geocoding API

Returns:
    String -- Geocoded start and destination addresses
"""
def geocode_addresses(gmaps_client, start_address, dest_address):
    # geocoding the starting and ending address
    geocode_start = gmaps_client.geocode(start_address)
    geocode_dest = gmaps_client.geocode(dest_address)

    return geocode_start, geocode_dest


"""Gets latitude and longitude

Returns:
    String -- latitude and longitude of the start position
"""
def get_start_coords(geocode_start_address):
    # finds the start coordinates (latitude, longitude)
    lat_start = geocode_start_address[0]["geometry"]["location"]["lat"]
    lng_start = geocode_start_address[0]["geometry"]["location"]["lng"]

    return lat_start, lng_start


"""Gets the latitude and longitude 

Returns:
    String -- latitude and longitude of the destination
"""
def get_dest_coords(geocode_dest_address):
    # finds the end coordinates (latitude, longitude)
    lat_dest = geocode_dest_address[0]["geometry"]["location"]["lat"]
    lng_dest = geocode_dest_address[0]["geometry"]["location"]["lng"]

    return lat_dest, lng_dest


"""Gets the directions from start to destination using Google Maps API

Returns:
    list -- each element in the list contains a 
"""


def get_directions(gmaps_client, lat_start, lng_start, lat_dest, lng_dest):
    current_time = datetime.now()

    directions_result = gmaps_client.directions(
        (lat_start, lng_start), (lat_dest, lng_dest), mode="walking", departure_time=current_time)

    directions = directions_result[0]["legs"][0]["steps"]

    return directions


"""Uses a regex functions it to remove HTML tags present in the directions

Returns:
    String -- a string without HTML tags
"""


def remove_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


"""Parses directions in the format {Start Latitude, Start Longitude, Instructions}

Returns:
    List -- each element is a dictionary in the specified format listed above
"""


def parse_directions(directions):
    parsed_directions = []
    for direction in directions:
        parsed_directions.append({
            "start_lat": direction["start_location"]["lat"],
            "start_lng": direction["start_location"]["lng"],
            "step": remove_tags(direction["html_instructions"])
        })

    return parsed_directions


def parse_gpx_temp_method():
    # some how get current gps location
    gpx_file = open("mapstogpx20190921_175809.gpx", 'r')
    gpx = gpxpy.parse(gpx_file)

    latitude = []
    longitude = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # print('Point at ({},{})'.format(point.latitude, point.longitude))
                latitude.append(point.latitude)
                longitude.append(point.longitude)

    return list(set(latitude)), list(set(longitude))

def generate_map_instructions(instructions):
    
    directions = [instructions[i]["step"] for i in range(len(instructions))]
    
    waypoints_coord = []
    with open("waypoints.txt", 'r') as f:
        for line in f.readlines():
            waypoints_coord.append(line[:-1])

    combined_coord_directions = [[waypoints_coord[i], directions[i]] for i in range(len(directions))]

    

    f = open("directions.txt", 'w')
    with f:
        for i in range(len(combined_coord_directions)):
            if waypoints_coord[i] == str(combined_coord_directions[i][0]):
                f.write(combined_coord_directions[i][1])
                f.write("\n")
    


def write_waypoints_to_file(instructions):
    waypoints_coord = [(instructions[i]["start_lat"], instructions[i]["start_lng"])
                 for i in range(len(instructions))]
    with open("waypoints.txt", 'w+') as f:
        for waypoint in waypoints_coord:
            f.write(str(waypoint))
            f.write("\n")
    
    f.close()




        
    