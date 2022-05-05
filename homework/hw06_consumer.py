from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

import pyspark.sql.functions as f
import pandas as pd
import plotly.express as px
import time

stream_df = (spark.readStream.format('socket')
                             .option('host', '127.0.0.1')
                             .option('port', 22260)
                             .load())
json_df = stream_df.selectExpr("CAST(value AS STRING) AS payload")
writer = (
    json_df.writeStream
           .queryName('issloc')
           .format('memory')
           .outputMode('append')
)
streamer = writer.start()

for _ in range(5):
    df = spark.sql("""
    SELECT get_json_object(payload, '$.timestamp') AS time,
           CAST(get_json_object(payload, '$.iss_position') AS string) AS position
    FROM issloc
    """)

    df.show(10)
    time.sleep(5)

streamer.awaitTermination(timeout=180)

df_temp = df.withColumn('time', df['time']) \
       .withColumn('latitude', f.split(df['position'], '"').getItem(3)) \
       .withColumn('longitude', f.split(df['position'], '"').getItem(7))
df_final = df_temp.toPandas()
df_final['time'] = pd.to_datetime(df_final['time'],unit='s')

fig = px.scatter_geo(df_final,lat='latitude',lon='longitude',hover_name='time', projection="natural earth")
fig.update_layout(title = 'ISS location 2022-04-12 21:38:25 to  23:11:40 UTC ', title_x=0.5)
fig.show()