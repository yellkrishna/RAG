from dependencies import *

nest_asyncio.apply()

def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b

def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b

def divide(a: int, b: int) -> float:
    """Divide two integers and return the result as a float"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b



add_tool = FunctionTool.from_defaults(fn=add)
multiply_tool = FunctionTool.from_defaults(fn=multiply)
divide_tool = FunctionTool.from_defaults(fn=divide)

llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)

agent = OpenAIAgent.from_tools(
    [multiply_tool, add_tool, divide_tool], llm=llm, verbose=True
)
response = agent.chat("What is (121 / 3) + 42?")
print(str(response))

