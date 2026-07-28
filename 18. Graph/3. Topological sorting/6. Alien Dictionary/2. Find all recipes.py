from collections import deque, defaultdict
class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        graph = defaultdict(list)
        indegree = {}
        for recipe, ingredient in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient) # remaining items needed for recipe
            for item in ingredient:
                graph[item].append(recipe)
        
        q = deque(supplies)
        result = []
        while q:
            item = q.popleft()
            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    q.append(recipe)
                    result.append(recipe)
        return result
        
