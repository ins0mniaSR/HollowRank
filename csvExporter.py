import csv

def csvExport(runScoreOrdered, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Player', 'Score']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for key, value in runScoreOrdered.items():
            writer.writerow([key, value])

