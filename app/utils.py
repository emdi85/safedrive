from geopy.distance import geodesic

def is_nearby(current_location, alert_location, threshold=1.0):
    # Returns True if the alert location is within the threshold distance (km)
    return geodesic(current_location, alert_location).km < threshold

def calculate_distance(loc1, loc2):
    # Calculate distance between two coordinates
    return geodesic(loc1, loc2).km
