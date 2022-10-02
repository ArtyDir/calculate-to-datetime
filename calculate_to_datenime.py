n = int(input("Введите целое число: "))

years = n // (24 * 3600 * 30 * 12)
mounts = n // (24 * 3600 * 30) % 12
days = n // (24 * 3600) % 30
hours = n // 3600 % 24
minutes = n % 3600 // 60
seconds = n % 3600 % 60

print(f"Годы:    {years}\n"
      f"Месяцы:  {mounts}\n"
      f"Дни:     {days}\n"
      f"Часы:    {hours}\n" 
      f"Минуты:  {minutes}\n"
      f"Секунды: {seconds}")
