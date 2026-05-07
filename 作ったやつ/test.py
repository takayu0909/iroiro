import streamlit as st
import random

st.title("試作１号")



num = st.text_input("ここに整数を入力")

if num:
    num = int(num)

if "target" not in st.session_state:
    st.session_state.target=random.randint(0,100)

if "mistakes" not in st.session_state:
    st.session_state.mistakes = 0

if num:

    if (st.session_state.target==num) == True:
        print("正解！")
        st.write("正解！")
    else:
        print("残念！")
        st.write("残念！")
        st.session_state.mistakes +=1
        print(st.session_state.mistakes)

        if st.session_state.mistakes>=3:
            print(st.session_state.target)
            st.write("ヒントを表示しますか？")
            hint = st.button("ヒント")
            
            if "hint" not in st.session_state:
                st.session_state.hint=0

            

            if (st.session_state.hint==1) or (hint ==True) :
                st.session_state.hint=1
                
                per=st.session_state.target*0.05
                
                if per<5:
                    per+=5
                under=st.session_state.target-per

                if under<0:
                    under=0

                up=st.session_state.target+per
                if up>100:
                    up=100
                st.write(f"{int(under)}から{int(up)}の範囲です")

                ###ユーザーに範囲を指定させてやるのもやってみたい。ifの条件判定の<0と>100は変数にしないといけない。ヒントを邪魔だったら隠せるようにする。またヒントのボタン押すとかそれ用のボックスみたいなのを新しく
                ##つくるか
