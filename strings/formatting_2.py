movies = ['Dhol','Bahubali','Jab tak hai jaan','PK']
stars = ['⭐⭐⭐⭐','⭐⭐⭐⭐⭐','⭐','⭐⭐⭐⭐⭐']

for movie, star in zip(movies, stars):
    print(f'{movie:<16}  {star}')