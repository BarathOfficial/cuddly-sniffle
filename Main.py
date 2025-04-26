from NLP_QW import Get_query

query = ''

while query != "Bye":
    query = str(input("Query: "))

    ans = Get_query(content=query)

    print(f"Deepseek"+': ',ans.choices[0].message.content)


print('Signing off')
exit()


