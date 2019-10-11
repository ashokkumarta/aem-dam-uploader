import logging, logging.handlers

def get_logger(track):
    'Returns a logger for the track'
    _format_ = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    _handler_ = logging.handlers.RotatingFileHandler(track);
    _handler_.setFormatter(_format_)

    _logger_ = logging.getLogger(track)
    _logger_.addHandler(_handler_)
    _logger_.addHandler(logging.StreamHandler())
    _logger_.setLevel(logging.DEBUG)

    return _logger_

def get_output_handler(handle):
    'Returns a logger for the track'

    _handler_ = logging.handlers.RotatingFileHandler(handle);
    _logger_ = logging.getLogger(handle)
    _logger_.addHandler(_handler_)
    _logger_.setLevel(logging.INFO)
    return _logger_
