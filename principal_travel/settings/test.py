from .base import *

def auto_slug_gen():
    # this is just a placeholder so tests don't fail with
    # this field type while using model_mommy
    return 'auto-slug'

MOMMY_CUSTOM_FIELDS_GEN = {
    'autoslug.fields.AutoSlugField': auto_slug_gen,
}
