def test():
    bilgiler = {
        "is_login_success": "ok",
        "verification_code_is": "waiting"
    }
    yield bilgiler
    

sayi = test()

print(next(sayi))

