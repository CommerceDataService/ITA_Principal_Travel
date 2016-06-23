from itertools import cycle
from datetime import date

from model_mommy.recipe import Recipe
from travel.models import Event, Trip, Region
from cities_light.models import Country

REGION_NAMES = ['Asia', 'Americas', 'Europe', 'Africa']
region = Recipe(Region, name=cycle(REGION_NAMES))

COUNTRY_NAMES = ['India', 'Thailand', 'United States', 'Canada', 'Belgium', 'Germany', 'Madagascar', 'Zambia', 'Australia']

country = Recipe(Country, name=cycle(COUNTRY_NAMES))

event = Recipe(Event)

MONTHS = [date(2015, x, 1) for x in range(1, 13)]
trip = Recipe(Trip, start_date=cycle(MONTHS))
