import csv

def timings(newtime,oldtime):
    if newtime < oldtime:
        return True
    else:
        return False


def highscores(diff, y):
    r,placeholder = [],'99:99:99'
    f = open ('./Data/highscores.csv', 'r', newline = '')
    reader = csv.reader(f)
    for i in reader:
        if i[0] == diff:
            placeholder = i[1]
            if timings(y,i[1]):
                r.append([diff,y])
            else:
                r.append(i)
        else:
            r.append(i)
    w = open('./Data/highscores.csv', 'w', newline = '')
    writer = csv.writer(w)
    for i in r:
        writer.writerow(i)
    w.close()
    f.close()
    if timings(y,placeholder):
        return True
    else:
        return False


def displayhighscore():
    r = []
    f = open ('./Data/highscores.csv', 'r', newline = '')
    reader = csv.reader(f)
    for i in reader:
        r.append(i)
    f.close()
    return r
