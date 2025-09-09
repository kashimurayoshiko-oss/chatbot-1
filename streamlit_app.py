# requirements:
#   pip install streamlit google-genai

import streamlit as st
from google import genai
from google.genai import types as genai_types

st.title("💬 Chatbot (Gemini 2.5 Flash)")
st.write(
    "このチャットボットは Google の **Gemini 2.5 Flash** を使って応答を生成します。"
    " 利用には Gemini API Key が必要です（Google AI Studio で発行）。"
)

# Gemini API キーの入力
gemini_api_key = st.text_input("Gemini API Key", type="password")
if not gemini_api_key:
    st.info("続行するには Gemini API Key を入力してください。", icon="🗝️")
else:
    # Gemini クライアントを作成
    client = genai.Client(api_key=gemini_api_key)

    # セッションにメッセージ履歴を保持
    if "messages" not in st.session_state:
        st.session_state.messages = []  # [{"role": "user"|"assistant", "content": "text"}...]

    # 既存メッセージを表示
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 入力欄
    if prompt := st.chat_input("なにを話しますか？"):
        # ユーザー入力を保存＆表示
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Gemini 形式（role/parts）に変換
        contents = []
        for m in st.session
