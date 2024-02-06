from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/hello")
def hello(request, name):
    return f"Hello {name}"