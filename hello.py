from openai import OpenAI # これはどうゆう意味？
# pip install openaiで公式ライブラリを入れた時に使えるようになった。
# openaiライブラリの中からOpenAIクラスを取り出して使えるようにしているってこと。

client = OpenAI()  # これはクラスなの？ → はい、OpenAIクラスのインスタンスを作っている。
 
response = client.responses.create(
    model="gpt-6-astra",
    input="名古屋のおすすめランチを3つ教えてください。",
)

print(response.output_text)
print(response.usage)
