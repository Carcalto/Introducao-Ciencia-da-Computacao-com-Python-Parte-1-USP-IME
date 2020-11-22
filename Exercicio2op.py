segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
a = segundos // 86400
b = (segundos % 86400) // 3600
c = ((segundos % 86400) % 3600) // 60 
d = ((segundos % 86400) % 3600) % 60
print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")
