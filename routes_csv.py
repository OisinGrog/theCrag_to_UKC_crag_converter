import csv

def write_to_csv(routes_data, filename):
    """Writes the routes data to a CSV file."""

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        field = ['Climb Name', 'Grade', 'Stars', 'Description', 'FA', 'Height', 'Pitches', 'Climb Type']

        # Removed bolts from header
        writer.writerow(field)  # Write the header
        for route in routes_data:
            writer.writerow([
                route.name,
                route.grade,
                route.stars,
                route.description,
                route.fa.what + ' ' + route.fa.who + ', ' + route.fa.when if route.fa else 'N/A',
                route.height,
                route.pitches,
                route.climb_type
            ])
    