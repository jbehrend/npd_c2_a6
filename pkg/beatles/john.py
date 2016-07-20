from ..countries.us import locations as us
from ..countries.uk import locations as uk

from ..general.expressions import impolite

# DO NOT EDIT BELOW THIS LINE
phrase = impolite("{} is ok in the US, but for the UK, I dislike {}".format(
    us.best,
    uk.worst,
))
