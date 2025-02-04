def file_writer(year, month, day, elapsed_time):
    data = open("log.txt", "a")
    data.write(",\n{0}/{1}/{2} {3}".format(year, month, day, elapsed_time))
    data.close()
