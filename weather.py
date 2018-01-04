import json, os, datetime


def main():
    os.system("wget https://api.weather.gov/points/43.13,-71.92/forecast/hourly")
    current_time = str( datetime.datetime.now() )
    data = json.load(open('hourly'))

    temps = [['Time'],['Wind'],['Temperature']]

    for i in data['properties']['periods']:

        timestamp = parse_timestamp(i['startTime'])
        info = [ current_time, parse_windspeed(i['windSpeed']), i['temperature'] ]
        save_data( timestamp, info )
        print('\n---------------------\n')        
    os.remove('hourly')
    os.system("rm hourly*")



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


def save_data(timestamp, data):
    with open(timestamp+'.csv', "a") as output:
        print(data)
        output.write(write_csv(data))

def write_csv(data):
    wr = ''
    for i in data:
        wr += str(i)
        wr += ','
    wr = wr[:-1] + '\n'
    return wr


def parse_timestamp(timestamp_raw):
    year = timestamp_raw.split('-')[0]
    month = timestamp_raw.split('-')[1]
    day = timestamp_raw.split('-')[2][:2]

    time = timestamp_raw.split('-')[2][3:].split(':')
    hour = time[0]
    minute = time[1]
    second = time[2]

    #print("Year: " + year + '\nMonth: ' + month + '\nDay: ' + day + '\nHour: ' + hour + '\nMinute: ' + minute + '\nSecond: ' + second)
    timestamp = year + '-' + month + '-' + day + 'T' + hour
    return timestamp
    
if __name__ == '__main__':
    main()
