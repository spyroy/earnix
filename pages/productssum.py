from abc import ABC, abstractmethod


class ProductsSum(ABC):
    @abstractmethod
    def sum_all_products(self):
        pass
