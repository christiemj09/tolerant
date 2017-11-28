"""
Wrap functions in error-tolerant response objects.
"""


class Response(object):
    """A response from a function."""
    
    def __init__(self, val, func, error=None):
        self.val = val
        self.func = func
        self.error = error
    
    def __call__(self):
        return self.val


def response(func):
    """Wrap the evaluation of a function in a Response object."""
	
	def decorator(*args, **kwargs):
		try:
		    resp = Response(func(*args, **kwargs), func)
		except Exception as e:
		    resp = Response(None, func, error=e)
		return resp
	
	return decorator


class LazyResponse(object):
    """A lazily evaluated response from a function."""
    
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.error = None
    
    def __call__(self):
        try:
            return self.func(*self.args, **self.kwargs)
        except Exception as e:
            self.error = e
    

def lazy_response(func):
    """Wrap the evaluation of a function in a LazyResponse object."""

	def decorator(*args, **kwargs):
		return LazyResponse(func, *args, **kwargs)
	
	return decorator

