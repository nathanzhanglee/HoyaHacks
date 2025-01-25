def restaurant_update_fn(building, time, city):
    if time >= 10 or time <= 20:
        i = 0
        while i < building.size:
            person = building.occupants[i]
            if time < 20:
                if not (person in building.employees):
                    building.remove_occupant(person)
                    person.home.add_occupant(person)
                    i -= 1
            else:
                building.remove_occupant(person)
                person.home.add_occupant(person)
                i -= 1
            i += 1