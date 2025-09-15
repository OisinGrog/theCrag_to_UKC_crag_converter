import csv

def write_to_csv(routes_data, filename):
    """Writes the routes data to a CSV file."""

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        field = ['Route Name', 'Climb Type', 'Grade', 'Height', 'Description', 'Bolts']

        writer.writerow(field)  # Write the header
        
        for route in routes_data:
            writer.writerow([
                route.name,
                route.climb_type,
                route.grade,
                route.height,
                route.description,
                route.bolts if route.bolts is not None else 'N/A'
            ])
    