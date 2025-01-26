from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, dense_rank, col, sum as f_sum, lead, min as f_min, datediff
from pyspark.sql.types import IntegerType, BooleanType
from pyspark.sql import SparkSession
import os

os.environ["PYSPARK_PYTHON"] = "path_to_python_executable"  # e.g., C:\Python39\python.exe
os.environ["PYSPARK_DRIVER_PYTHON"] = "path_to_python_executable"

spark = SparkSession.builder \
    .appName("YourAppName") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .getOrCreate()


spark = SparkSession.builder.appName('Badminton_code').getOrCreate()

badminton_court_data = [
    (1, 2, "2016-03-01", 5),
    (1, 2, "2016-03-02", 6),
    (2, 3, "2017-06-25", 1),
    (3, 1, "2016-03-02", 2),
    (3, 4, "2016-03-02", 3),
    (3, 2, "2018-07-03", 5)
]

columns = ['user_id', 'kit_id', 'login_date', 'session_court']

court_input_df = spark.createDataFrame(badminton_court_data, columns)

court_input_df.show()
court_input_df.printSchema()
