# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, template='Hello, <name>!'):
    template_new = template.replace('<name>', name)
    greeting = template_new
    if name != ' ':
        return greeting
    else:
        return


greet('Doc')
greet('Bob', "What's up, <name>!")
greet(' ')


def force(mass, body='earth'):
    gravity_data = {
        "sun": 274.0,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6
    }
    calc_force = mass * gravity_data[body]
    return calc_force


force(1.0, 'sun')


def pull(m1, m2, d):
    gravitational_constant = 6.674 * (10 ** -11)
    gravitional_pull = gravitational_constant * ((m1 * m2) / d ** 2)
    return gravitional_pull


pull(0.1, (5.972 * (10 ** 24)), (6.371 * 10 ** 6))
