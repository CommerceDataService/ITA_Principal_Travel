from model_mommy.recipe import Recipe, foreign_key
from model_mommy import mommy
from travel.models import Event, Trip, Region
from cities_light.models import Country
from itertools import cycle
from datetime import date

REGION_NAMES = ['EMEA', 'Asia', 'Americas', 'China', None]
region = Recipe(Region, name=cycle(REGION_NAMES))

COUNTRY_NAMES = ['India', 'United States', 'Belgium', 'Madagascar', 'Canada', 'Zambia']

country = Recipe(Country,
    name = cycle(COUNTRY_NAMES),
    #agency_region = foreign_key(region.prepare_recipe()),
)

event = Recipe(Event)

MONTHS = [ date(2015, x, 1) for x in range(1,13) ]
trip = Recipe(Trip, start_date=cycle(MONTHS))
