"""
Log errors, choose to ignore them.
"""

# Probably want to use the built-in logging module somehow. Research.

import os


def log_errors(func, log_dir=os.getcwd(), silent=False):
    """Log errors to a file."""
    
    log_path = os.path.join(log_dir, '%s.log' % func.__name__)
    
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs):
        except Exception as e:
            with open(log_path, 'a') as log_file:
                log_file.write('%s\n' % str(e))
                # ^^ Better representation of error?
                #    Could probably use logging module here instead of this.
            if not silent:
                raise
