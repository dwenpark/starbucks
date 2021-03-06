from django.db import models


class Menu(models.Model):
	name = models.CharField(max_length=45)

	class Meta:
		db_table = "menus"


class Category(models.Model):
	menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, db_column='menu_id')
	name = models.CharField(max_length=45)

	class Meta:
		db_table = "categories"


class Nutrition(models.Model):
	one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
	sodium_mg = models.DecimalField(max_digits=6, decimal_places=2)
	saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2)
	sugars_g = models.DecimalField(max_digits=6, decimal_places=2)
	protein_g = models.DecimalField(max_digits=6, decimal_places=2)
	caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2)
	size_ml = models.CharField(max_length=45)
	size_fluid_ounce = models.CharField(max_length=45)
	#size_ml, size_fluid_ounce는 int로 사용?

	class Meta:
		db_table = "nutritions"


class Product(models.Model):
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id')
	korean_name = models.CharField(max_length=45)
	english_name = models.CharField(max_length=45)
	description = models.TextField()
	nutrition_id = models.ForeignKey(Nutrition, on_delete=models.CASCADE, db_column='nutrition_id')

	class Meta:
		db_table = "products"


class Image(models.Model):
	image_url = models.CharField(max_length=2000)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')

	class Meta:
		db_table = "images"


class Allergy(models.Model):
	name = models.CharField(max_length=45)

	class Meta:
		db_table = "allergies"


class Allergy_product(models.Model):
	allergy_id = models.ForeignKey(Allergy, on_delete=models.CASCADE, db_column='allergy_id')
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')

	class Meta:
		db_table = "allergy_products"