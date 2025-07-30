from rest_framework import serializers
from .models import Recipe, Ingredient, NutritionInfo, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class NutritionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionInfo
        fields = ['calories', 'protein', 'fat', 'carbs']

class IngredientSerializer(serializers.ModelSerializer):
    nutrition = NutritionInfoSerializer(source='nutritioninfo', read_only=True)

    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'nutrition']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'tags', 'ingredients', 'created_at']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)

        for tag in tags_data:
            tag_obj, _ = Tag.objects.get_or_create(name=tag['name'])
            recipe.tags.add(tag_obj)

        for ingredient in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient)

        return recipe

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        ingredients_data = validated_data.pop('ingredients', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.tags.clear()
        for tag in tags_data:
            tag_obj, _ = Tag.objects.get_or_create(name=tag['name'])
            instance.tags.add(tag_obj)

        instance.ingredients.all().delete()
        for ingredient in ingredients_data:
            Ingredient.objects.create(recipe=instance, **ingredient)

        return instance