

pattern = input('replace the changing number by *: ')
limit = int(input('upper limit: '))
links = ''

for i in range(1, limit+1):
    link = pattern.replace('*', str(i))
    links += link + '\n'

print(links)
