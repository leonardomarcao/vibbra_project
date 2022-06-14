"""Utils File."""
import simplejson


class JsonDecimalDumper:
    """A class to json decimal loader."""

    @staticmethod
    def dumps(data):
        """Dump json function with simplejson library."""
        return simplejson.dumps(data, use_decimal=True, indent=4, sort_keys=True)
