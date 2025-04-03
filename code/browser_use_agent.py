# https://github.com/browser-use/browser-use
# https://docs.browser-use.com/introduction
# https://youtu.be/zGkVKix_CRU?si=Thb-84St-zwYHasn

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from browser_use import Agent, Browser, BrowserConfig, Controller
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
import asyncio

load_dotenv()

import asyncio

class Post(BaseModel):
    caption: str
    url: str

class Posts(BaseModel):
    posts: List[Post]

controller = Controller(output_model=Posts)

browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

# Initialize the model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.0,
    timeout=100,  # Increase for complex tasks    
)
# llm = ChatAnthropic(
#     model_name="claude-3-5-sonnet-20240620",
#     temperature=0.0,
#     timeout=100,  # Increase for complex tasks
# )


async def main():
    initial_actions=[
        {'open_tab': {'url' : 'https://www.instagram.com/tech_with_tim'}}
    ]
    agent = Agent(
        task="go to tech with tim's instagram and grab the 5 most recent posts",
        llm=llm,
        browser=browser,
        controller=controller,
        initial_actions=initial_actions
    )

    result = await agent.run()
    print(result.final_result())

    data = result.final_result()
    parsed: Posts = Posts.model_validate_json(data)

    await browser.close()

asyncio.run(main())