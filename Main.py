from NLP_QW import runLogic

query = ''

while query != "Bye":
    query = str(input("Query: "))

    ans = runLogic(content=query)

    print(f"Deepseek"+': ',ans.choices[0].message.content)


print('Signing off')
exit()


