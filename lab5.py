
events_list = [(2008, "Iron Man"),
               (2011, "Thor"),
               (2012, "The Avengers"),
               (2017, "Spider-Man: Homecoming")]

time_dict = dict(events_list)

years_to_visit = {2008, 2011, 2012, 2017}  

for year in years_to_visit:
    try:
        event = time_dict[year]
        print(f"У році {year} відбулася подія: {event}")
    except KeyError:
        print(f"У році {year} немає виходу фільмів  .")
