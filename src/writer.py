import csv
import datetime;


def write_to_csv(solution, iterations, matrix_size):
    with open("output/" + str(datetime.datetime.now()) + '_output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Matrix Size = " + str(matrix_size), "Iterations = " + str(iterations)])
        writer.writerow(["Algorithm", "Number of Moves","Execution Time"])
        for algorithm in solution:
            for i in range(1,iterations+1):
                writer.writerow([algorithm[0],algorithm[i][0],algorithm[i][1]])
            writer.writerow(["Average " + str(algorithm[0]),round(sum([algorithm[i][0] for i in range(1,iterations+1)])/iterations,3),round(sum([algorithm[i][1] for i in range(1,iterations+1)])/iterations,3)])