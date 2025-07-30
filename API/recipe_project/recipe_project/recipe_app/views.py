from rest_framework import viewsets
from .models import Recipe, Ingredient, Tag
from .serializers import RecipeSerializer, IngredientSerializer, TagSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-created_at')
    serializer_class = RecipeSerializer

    @action(detail=True, methods=['get'])
    def nutrition_summary(self, request, pk=None):
        recipe = self.get_object()
        total = {'calories': 0, 'protein': 0, 'fat': 0, 'carbs': 0}
        for ing in recipe.ingredients.all():
            if hasattr(ing, 'nutritioninfo'):
                n = ing.nutritioninfo
                total['calories'] += n.calories
                total['protein'] += n.protein
                total['fat'] += n.fat
                total['carbs'] += n.carbs
        return Response(total)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer