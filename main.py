from fastapi import FastAPI
from fastapi.responses import FileResponse




app = FastAPI()


@app.get("/", response_class=FileResponse)
def serve_index():
    return FileResponse("index.html")

@app.get("/quote/{search_param}")
def get_quote(search_param: str):
    import quote
    import random
    quote_list = quote.quote(search_param)
    print(quote_list)
    if quote_list is None:
        return{"nothing generated"}
    else: 
        random_idx = random.randint(0, len(quote_list))
        quote = quote_list[random_idx]["quote"]
    print(type(quote))
    return {"quote": quote}

@app.get("/square/{number}")
def get_square(number: int):
    square = number ** 2
    return {"number": number, "square": square, "message": "hello"}

@app.get("/ana")
def get_ana():
    return {"my name is ana :)"}

@app.get("/parity/{num}")
def get_parity(num: int):
    if num % 2 == 0:
        return {"number": num, "parity": "even"}
    else: 
        return {"number": num, "parity": "odd"}
    




    

