import pygame

class ResourceManager:
    def __init__(self):
        self.resources = {
            "wood": 10,
            "stone": 10
        }

        self.costs = {
            "lumbermill": {
                "wood": 7,
                "stone": 3
            },
            "stonemasonry": {
                "wood": 3,
                "stone": 5
            }
        }

    def apply_cost(self, building):
        for resource, cost in self.costs[building].items():
            self.resources[resource] -= cost

    def affordable(self, building):
        affordable = True
        for resource, cost in self.costs[building].items():
            if self.resources[resource] < cost:
                affordable = False
        return affordable
