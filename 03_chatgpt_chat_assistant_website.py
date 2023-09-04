#
# ・Clearしても質問履歴は保持された解答を得られる．
#
# 
#Gradioは一時的な公開URLを生成
#01 動作OK
#demo.launch(share=True) 
#02
#demo.launch(server_name="0.0.0.0", server_port=8000, share=True)      
#03　サーバ側で実行したが動作NG（Local&Publicサーバは割り当てられるが表示不可）
#demo.launch(server_name="xs815357.xsrv.jp", server_port=8000, share=True)
#


import openai
import gradio
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

#Gradioｲﾝｽﾀﾝｽ生成
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "ono-piano.com")

#Gradioは一時的な公開URLを生成
#01 動作OK
#demo.launch(share=True) 
#02
demo.launch(server_name="0.0.0.0", server_port=8000, share=True)      
#03　サーバ側で実行したが動作NG（Local&Publicサーバは割り当てられるが表示不可）
#demo.launch(server_name="xs815357.xsrv.jp", server_port=8000, share=True)