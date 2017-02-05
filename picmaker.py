f = open('img.ppm', 'w+')
f.write('P3 500 500 255\n')
f.close

f = open('img.ppm', 'a+')
for i in range(0,500):
    for j in range(0,500):
        r = j % 256
        g = j % 256
        b = i % 256
        f.write('%d %d %d\n' % (r, g, b))
f.close
