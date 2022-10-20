n = int(input("Введите целое число: "))

# основные вычисления
years = n // (24 * 3600 * 30 * 12)
mounts = n // (24 * 3600 * 30) % 12
days = n // (24 * 3600) % 30
hours = n // 3600 % 24
minutes = n % 3600 // 60
seconds = n % 3600 % 60

print(f"{years} лет, {mounts} месяцев, {days} дней, {hours:02}:{minutes:02}:{seconds:02}")
