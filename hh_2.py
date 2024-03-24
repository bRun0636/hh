from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Создаем Spark сессию
spark = SparkSession.builder.appName("product_category_pairs").getOrCreate()

# Тестовые данные
products_data = [("product1", "category1"), ("product2", "category2"), ("product3", None)]
categories_data = [("category1", "product1"), ("category3", "product3")]

# Создаем DataFrame для продуктов и категорий
products_df = spark.createDataFrame(products_data, ["product", "category"])
categories_df = spark.createDataFrame(categories_data, ["category", "product"])

# Выполняем объединение (join) DataFrame'ов
final_df = products_df.join(categories_df, "product", "left")

# Фильтруем продукты без категорий
products_without_category = final_df.filter(col("category").isNull()).select("product")

# Выводим все пары "Имя продукта - Имя категории"
final_df.show()

# Выводим имена продуктов, у которых нет категорий
products_without_category.show()

# Останавливаем Spark сессию
spark.stop()