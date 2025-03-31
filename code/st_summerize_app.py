import openai
import streamlit as st

##### OpenAI API 요청 함수 #####
def llm_request(prompt,apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}])
    gptResponse = response.choices[0].message.content
    return gptResponse

##### Streamlit UI #####
def main():
    st.set_page_config(page_title="요약 프로그램")
    if "OPENAI_API_KEY" not in st.session_state:
        st.session_state["OPENAI_API_KEY"] = ""

    with st.sidebar:
        api_key = st.text_input(label='OPENAI API KEY', placeholder='OPENAI API KEY를 입력하세요.', value='',type='password')    
        if api_key:
            st.session_state["OPENAI_API_KEY"] = api_key
        st.markdown('---')

    st.header("📃 문서 요약 서비스")
    st.markdown('---')
    
    document = st.text_area("요약 할 내용을 입력하세요")
    if st.button("요약하기"):
        prompt = f'''
            [Instructions]
            당신은 [Document]를 한국어로 요약하는 전문가 어시스턴트입니다.
            [[Document]를 읽고, 한국어로 요약하되, 중복된 내용은 생략하고, 중복된 내용을 강조하여 요약하세요.
            요약 시, 사례 증거보다는 개념과 주장을 강조해 주세요.
            요약은 3줄로 간결하게 작성해 주세요.
            요약은 글머리 기호 형태로 제공하세요.
            [Document]
            {document}
            '''
               
        st.info(llm_request(prompt,st.session_state["OPENAI_API_KEY"]))

if __name__=="__main__":
    main()
