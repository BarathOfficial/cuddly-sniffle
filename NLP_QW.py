import sqlite3
from openai import OpenAI

#Deepseek AI R1 API
client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key="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")




def fetchData(query):
    try:
        #connection to local SQL
        sqliteConnection = sqlite3.connect('Medical.db')
        #initiated DB
        cursor = sqliteConnection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        return error

    finally:
        if sqliteConnection:
            sqliteConnection.close()


    return result



#Get Response from Deepseek
def getQuery(content):
    completion = client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-r1-zero:free",
        messages=[
            {
            "role": "user",
            "content": content
            }
        ]
    )
    return completion


def runLogic(content):
    query = getQuery(content)
    table = fetchData(query)
    final_query = "Explain this table "+table

    finalResult = getQuery(final_query)
    return finalResult


fetchData("select * from medicalData;")