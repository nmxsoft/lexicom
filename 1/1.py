from dataclasses import dataclass

from global_var import COST_DIVISION
from qsort import quick_sort


@dataclass(frozen=True)
class Technic:
    name: str
    cost: float
    avail: bool


if __name__ == '__main__':
    """ Задание 1."""
    tech = [
        Technic('denn', 1.0, True),
        Technic('pin', 501.0, True),
        Technic('cisco', 300.2, False)
        # Add more technic
    ]

    # def set_category(product_cost: float) -> str:
    #     return '"budget"' if product_cost < COST_DIVISION else '"costly"'
    #
    #
    # for t in tech:
    #     print(
    #         ' '.join(['Product name:', t.name]),
    #         ' '.join(['Category:', set_category(t.cost)]),
    #         ' '.join(['In stock:', 'exist' if t.avail else 'not exist'])
    #     )

    """ Задание 2."""
    # Magic method 1
    product_names = [tech[i].name for i in range(len(tech))]
    product_names.sort(key=len)
    print(product_names)

    # Magic method 2
    print(sorted(tech, key=lambda tech: len(tech.name)))

    # My function quick sort
    quick_sort(tech, 0, len(tech) - 1)
    print(tech)
