import logging
import time


def test_decorator(calls=3):
    def decorator(f):
        chache = {}

        def wrap(*args, **kwargs):
            params = (args, frozenset(kwargs))
            if params in chache:
                logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                )
                logging.info("Кешированный результат")
                chache[params]['calls'] += 1
                return chache.pop(params)['result'] if chache[params]['calls'] == calls else chache[params]['result']
            else:
                logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                )
                start_time = time.time()
                result = f(*args, **kwargs)
                end_time = time.time()
                logging.info("Время выполнения %.2f с", end_time - start_time)
                chache[params] = {'result': result, 'calls': 1}
                return result

        return wrap

    return decorator
