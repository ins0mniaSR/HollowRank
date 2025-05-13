import csv

def csvExport(runScoreOrdered):
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['Player', 'Score']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for key, value in runScoreOrdered.items():
            writer.writerow([key, value])

