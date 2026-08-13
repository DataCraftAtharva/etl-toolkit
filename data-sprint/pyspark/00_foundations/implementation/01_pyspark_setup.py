from pyspark.sql import SparkSession


def main():
    spark = (
        SparkSession.builder
        .appName("DataInterviewSprint")
        .master("local[*]")
        .getOrCreate()
    )

    print("Spark version:", spark.version)

    data = [
        (1, "Atharva", "Mumbai"),
        (2, "Rahul", "Pune"),
        (3, "Priya", "Mumbai"),
    ]

    df = spark.createDataFrame(
        data,
        ["id", "name", "city"]
    )

    df.show()

    print("Schema:")
    df.printSchema()

    print("Row count:", df.count())

    spark.stop()


if __name__ == "__main__":
    main()