# Получаем базу из внешнего модуля
from .customer_base import technic


def service() -> dict:
    base_to_print = {}
    for tech in technic:
        name = ' '.join([tech[2], tech[3]])
        gadget = tech[0]
        cost = tech[1]
        if name not in base_to_print:
            base_to_print[name] = gadget + ' - ' + str(cost)
        else:
            base_to_print[name] += '; ' + gadget + ' - ' + str(cost)

    return base_to_print
