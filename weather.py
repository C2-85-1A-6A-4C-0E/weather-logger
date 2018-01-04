import json, os, csv
def main():
    os.system("wget https://api.weather.gov/points/43.13,-71.92/forecast/hourly")

    data = json.load(open('hourly'))

    temps = [['Time'],['Wind'],['Temperature']]

    for i in data['properties']['periods']:
        temps[0].append(i['startTime'])
        temps[1].append(parse_windspeed(i['windSpeed']))
        temps[2].append(i['temperature'])

    with open('data.csv', "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(temps)

def parse_windspeed(data):

    numbers = ['']

    for i in data:
        if i in '0123456789':
            numbers[-1] += i
        elif numbers[-1] != '':
            numbers.append('')
    for i in range(len(numbers)):
        try:numbers[i] = int(numbers[i])
        except:numbers.pop(i)

    return int( sum(numbers) / len(numbers) )
main()
